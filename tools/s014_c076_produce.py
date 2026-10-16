import hashlib,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/neighbor_ascent');start=time.monotonic()
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
out=[];states=records=extensions=0
for case in json.loads((B/'inputs.json').read_bytes())['cases']:
    n=case['n'];adj=[[] for _ in range(n)]
    for u,v in case['edges']:adj[u].append(v);adj[v].append(u)
    color={0:0};queue=[0];bip=True
    for u in queue:
        for v in adj[u]:
            if v not in color:color[v]=1-color[u];queue.append(v)
            elif color[v]==color[u]:bip=False
    assert len(color)==n
    if not bip:out.append(dict(case=case['id'],bipartite=False));continue
    sign=[1 if color[u]==0 else -1 for u in range(n)];S=set()
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);assert count<=1000000
            for _ in range(count):raw=f.read(16);assert len(raw)==16;S.add(int.from_bytes(raw,'little'))
    states+=len(S);assert states<=2000000;rows=[]
    for x in sorted(S):
        c=list(x.to_bytes(16,'little')[:n])
        if sum(a*e for a,e in zip(c,sign))%3:continue
        for v,a in enumerate(c):
            if a<2 or a%2:continue
            wins=[]
            for w in sorted(adj[v]):
                d=c.copy();d[v]-=1;d[w]+=2;wins.append([w,int.from_bytes(bytes(d),'little') in S]);extensions+=1
            rows.append(dict(c=c,v=v,neighbors=wins));records+=1
            assert records<=1000000 and extensions<=5000000 and time.monotonic()-start<540
    out.append(dict(case=case['id'],bipartite=True,states=len(S),rows=rows))
(B/'result.json.xz').write_bytes(lzma.compress(json.dumps(out,separators=(',',':')).encode()))
print(json.dumps(dict(cases=len(out),states=states,records=records,extensions=extensions,failures=sum(not any(b for w,b in r['neighbors']) for row in out for r in row.get('rows',[])))))
