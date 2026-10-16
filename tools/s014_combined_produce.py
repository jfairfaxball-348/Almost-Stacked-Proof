import itertools,json,lzma,struct,sys,time
from pathlib import Path
B=Path('evidence/S014/combined_bound');shard=int(sys.argv[1]);D=B/f'shard{shard}';D.mkdir(exist_ok=True);start=time.monotonic();out=[];treecount=indcount=0
def distances(V,E):
    adj={u:[] for u in V}
    for u,v in E:adj[u].append(v);adj[v].append(u)
    result={}
    for s in V:
        ds={s:0};todo=[s]
        for u in todo:
            for v in adj[u]:
                if v not in ds:ds[v]=ds[u]+1;todo.append(v)
        result[s]=ds
    return adj,result
for c in json.loads((B/'inputs.json').read_bytes())['cases']:
    if c['index']%2!=shard:continue
    n=c['n'];adj,ds=distances(range(n),c['edges']);alpha=0;maxsets=[];trees=[]
    for mask in range(1<<n):
        assert time.monotonic()-start<540
        V=[v for v in range(n) if mask>>v&1];E=[e for e in c['edges'] if all(mask>>v&1 for v in e)]
        if not E:
            if len(V)>alpha:alpha=len(V);maxsets=[]
            if len(V)==alpha:maxsets.append(mask)
        if len(V)<2 or len(E)!=len(V)-1:continue
        ta,td=distances(V,E)
        if len(td[V[0]])<len(V) or any(td[u][v]!=ds[u][v] for u,v in itertools.product(V,repeat=2)):continue
        scores={r:1+sum(len(ta[v])*2**td[r][v] for v in V if v==r or len(ta[v])>1)+sum(len(ta[v])==1 and v!=r for v in V) for r in V};trees.append(dict(mask=mask,scores=scores,threshold=max(scores.values())))
    R=max(r['threshold'] for r in trees);bound=max(n+1,3*alpha+1 if alpha>=2 else 0,R);assert bound<=c['threshold'];row=dict(index=c['index'],source=c['id'],alpha=alpha,maximum_independent_sets=maxsets,trees=trees,R=R,bound=bound,threshold=c['threshold'],strict_gap=c['threshold']>bound)
    if row['strict_gap']:
        witness=None;Q=-1
        with lzma.open(c['certificate'],'rb') as f:
            while head:=f.read(12):
                mass,count=struct.unpack('<IQ',head)
                for _ in range(count):
                    x=f.read(16);assert len(x)==16
                    if mass!=c['threshold']-1:continue
                    config=list(x[:n])
                    if sum(z>1 for z in config)<=1 and sum(z*z for z in config)>Q:Q=sum(z*z for z in config);witness=config
        row['critical_AS_witness']=witness
    out.append(row);treecount+=len(trees);indcount+=len(maxsets);assert treecount<=1000000 and indcount<=1000000
(D/'results.json').write_text(json.dumps(out,separators=(',',':'))+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(shard=shard,cases=len(out),trees=treecount,strict_gaps=[dict(index=r['index'],threshold=r['threshold'],bound=r['bound']) for r in out if r['strict_gap']],seconds=time.monotonic()-start)))
