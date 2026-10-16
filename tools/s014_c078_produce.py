import hashlib,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/full_leaf_ascent');start=time.monotonic()
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
out=[];states=records=0
for case in json.loads((B/'inputs.json').read_bytes())['cases']:
    n=case['n'];adj=[[] for _ in range(n)]
    for u,v in case['edges']:adj[u].append(v);adj[v].append(u)
    color={0:0};queue=[0];bip=True
    for u in queue:
        for v in adj[u]:
            if v not in color:color[v]=1-color[u];queue.append(v)
            elif color[v]==color[u]:bip=False
    assert len(color)==n
    sign=[1 if color[u]==0 else -1 for u in range(n)];S=set()
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);assert count<=1000000
            for _ in range(count):raw=f.read(16);assert len(raw)==16;S.add(int.from_bytes(raw,'little'))
    states+=len(S);assert states<=2000000;rows=[]
    for x in sorted(S):
        c=list(x.to_bytes(16,'little')[:n])
        for v,a in enumerate(c):
            if a<1:continue
            for w in adj[v]:
                if len(adj[w])!=1:continue
                d=c.copy();d[v]-=1;d[w]+=2;y=int.from_bytes(bytes(d),'little');exception=sum(c)==2 and c[v]==c[w]==1;rows.append(dict(c=c,v=v,w=w,exception=exception,loses=y in S));records+=1;assert records<=2000000 and time.monotonic()-start<540
    out.append(dict(case=case['id'],bipartite=bip,states=len(S),rows=rows))
(B/'result.json.xz').write_bytes(lzma.compress(json.dumps(out,separators=(',',':')).encode()));print(json.dumps(dict(cases=len(out),bipartite_cases=sum(r['bipartite'] for r in out),states=states,extensions=records,failures=sum(not x['loses'] and not x['exception'] for r in out for x in r.get('rows',[])))))
