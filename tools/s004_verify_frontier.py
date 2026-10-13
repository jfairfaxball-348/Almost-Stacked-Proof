"""Independent certificate replay: packed states, canonical first-move parents.

No import of the frontier producer. Completeness follows because each nonterminal
loser has its canonical successor in the previous certified losing layer.
"""
import itertools,json,lzma,sys,time
from pathlib import Path

def verify(path):
    data=json.loads(lzma.decompress(Path(path).read_bytes()));n=data['n'];mode=data['mode']
    # 16-bit fields: inputs max mass 140, no carries/borrows across fields.
    units=[1<<(16*i) for i in range(n)];mask=65535
    adj=[[] for _ in range(n)]
    for u,v in data['edges']:adj[u].append(v);adj[v].append(u)
    for a in adj:a.sort()
    def encode(c):return sum(x*units[i] for i,x in enumerate(c))
    def fields(x):return [(x>>(16*i))&mask for i in range(n)]
    prev=set();checked=0;start=time.monotonic()
    for t,layer in enumerate(data['layers']):
        current={encode(c) for c in layer};assert len(current)==len(layer)
        assert all(len(c)==n and all(isinstance(v,int) and 0<=v<65536 for v in c) and sum(c)==t for c in layer)
        if t==0:assert not current;continue
        # Enumerate only inverses that undo the deterministic smallest heavy
        # vertex -> smallest neighbour move. This differs from all-parent union.
        pool=set()
        if t<=n:
            for chosen in itertools.combinations(range(n),t):pool.add(sum(units[i] for i in chosen))
        for d in prev:
            f=fields(d)
            for u in range(n):
                v=adj[u][0]
                if f[v]==0:continue
                x=d+2*units[u]-units[v];g=fields(x)
                if next((i for i in range(n) if g[i]>=2),None)==u:pool.add(x)
        expected=set()
        for x in pool:
            f=fields(x)
            if (sum(v!=0 for v in f)==1 if mode=='stack' else t==1):continue
            okay=True
            for u in range(n):
                if f[u]<2:continue
                for v in adj[u]:
                    if x-2*units[u]+units[v] not in prev:okay=False;break
                if not okay:break
            if okay:expected.add(x)
        assert expected==current,(str(path),t,len(expected),len(current))
        prev=current;checked+=len(current)
    threshold=len(data['layers'])-1 if not prev and len(data['layers'])-1>n else None
    if threshold:
        crit=data['layers'][-2];assert crit
        assert any(sum(x>1 for x in c)<=1 for c in crit)
    result={'file':str(path),'layers':len(data['layers'])-1,'certified_loser_states':checked,
            'threshold':threshold,'critical_as':True if threshold else None,'seconds':time.monotonic()-start}
    print(json.dumps(result),flush=True);return result

if __name__=='__main__':
    paths=[p for p in sys.argv[1:] if p!='--check-only'] or sorted(map(str,Path('evidence/S004').glob('*.json.xz')))
    out=[verify(p) for p in paths]
    if '--check-only' not in sys.argv:
        Path('evidence/S004/frontier_verification.json').write_text(json.dumps(out,indent=2)+'\n')
