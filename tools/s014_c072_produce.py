import hashlib,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/bip_parity');start=time.monotonic()
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
out=[];states=tests=0
for case in json.loads((B/'inputs.json').read_bytes())['cases']:
    n=case['n'];adj=[[] for _ in range(n)]
    for u,v in case['edges']:adj[u].append(v);adj[v].append(u)
    colors={0:0};queue=[0];bip=True
    for u in queue:
        for v in adj[u]:
            if v not in colors:colors[v]=1-colors[u];queue.append(v)
            elif colors[v]==colors[u]:bip=False
    assert len(colors)==n
    if not bip:out.append(dict(case=case['id'],bipartite=False));continue
    S=set()
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw)
            if mass==case['threshold']-1:
                assert count<=1000000
                for _ in range(count):raw=f.read(16);assert len(raw)==16;S.add(int.from_bytes(raw,'little'))
                break
            remain=count*16
            while remain:part=f.read(min(remain,65536));assert part;remain-=len(part)
    states+=len(S);assert states<=3000000;rows=[]
    for z in sorted(S):
        c=list(z.to_bytes(16,'little')[:n])
        if sum(a>=2 for a in c)<2:continue
        parity=[a%2 for a in c];sources=[]
        for q in range(n):
            d=parity.copy();d[q]+=sum(c)-sum(parity);y=int.from_bytes(bytes(d),'little');sources.append(y in S);tests+=1;assert tests<=1000000 and time.monotonic()-start<540
        rows.append(dict(c=c,losing_sources=[q for q,yes in enumerate(sources) if yes],all_source_failure=not any(sources),heavy_source_failure=not any(yes and c[q]>=2 for q,yes in enumerate(sources))))
    out.append(dict(case=case['id'],bipartite=True,critical=len(S),rows=rows))
(B/'result.json.xz').write_bytes(lzma.compress(json.dumps(out,separators=(',',':')).encode()));print(json.dumps(dict(cases=len(out),bipartite_cases=sum(r['bipartite'] for r in out),nonAS=sum(len(r.get('rows',[])) for r in out),all_source_failures=sum(x['all_source_failure'] for r in out for x in r.get('rows',[])),heavy_source_failures=sum(x['heavy_source_failure'] for r in out for x in r.get('rows',[])),critical_states=states,candidates=tests)))
