import json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/critical_even')
out=[]
for case in json.loads((B/'inputs.json').read_bytes())['cases']:
    n=case['n'];adj=[[] for _ in range(n)]
    for u,v in case['edges']:adj[u].append(v);adj[v].append(u)
    colors={0:0};queue=[0];bip=True
    for u in queue:
        for v in adj[u]:
            if v not in colors:colors[v]=1-colors[u];queue.append(v)
            elif colors[v]==colors[u]:bip=False
    assert len(colors)==n;critical=[]
    with lzma.open(case['certificate'],'rb') as f:
        while h:=f.read(12):
            mass,count=struct.unpack('<IQ',h)
            if mass==case['threshold']-1:
                assert count<=1000000
                critical=[int.from_bytes(f.read(16),'little') for _ in range(count)];break
            remain=count*16
            while remain:part=f.read(min(remain,65536));assert part;remain-=len(part)
    assert critical;selected=[];nonAS=twos=0
    for x in critical:
        c=[(x>>(8*i))&255 for i in range(n)];assert sum(c)==case['threshold']-1
        if sum(z>=2 for z in c)<2:continue
        nonAS+=1
        if 2 in c:twos+=1
        if any(z>=2 and z%2==0 for z in c):selected.append(c)
    out.append(dict(case=case['id'],bipartite=bip,critical=len(critical),nonAS=nonAS,nonAS_with2=twos,even_heavy_inputs=sorted(selected)))
assert sum(len(r['even_heavy_inputs']) for r in out)<=300000
(B/'results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(cases=len(out),critical=sum(r['critical'] for r in out),nonAS=sum(r['nonAS'] for r in out),nonAS_with2=sum(r['nonAS_with2'] for r in out),even_heavy_inputs=sum(len(r['even_heavy_inputs']) for r in out))),flush=True)
