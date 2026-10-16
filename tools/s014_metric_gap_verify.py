import hashlib,json,lzma
from pathlib import Path
B=Path('evidence/S014/metric_gap')
for pre in [B/'preflight.json',B/'negative_derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes());g=cfg['cases'][0]['graph'];n=g['n'];E={frozenset(e) for e in g['edges']};c=tuple(cfg['c']);seen={c};todo=[c];dependencies=0
for x in todo:
    assert len(seen)<=300000 and sum(z>0 for z in x)>1
    for u in range(n):
        if x[u]<2:continue
        for v in range(n):
            if frozenset([u,v]) not in E:continue
            y=list(x);y[u]-=2;y[v]+=1;y=tuple(y);dependencies+=1
            if y not in seen:seen.add(y);todo.append(y)
raw=lzma.decompress((B/'negative.bin.xz').read_bytes());assert len(raw)%16==0;stored=[tuple(raw[p:p+n]) for p in range(0,len(raw),16)];assert all(not any(raw[p+n:p+16]) for p in range(0,len(raw),16));assert len(stored)==len(set(stored))==len(seen)==json.loads((B/'negative.json').read_bytes())['states'] and set(stored)==seen
assert sum(c)==41 and sum(z>1 for z in c)==1;out=dict(states=len(seen),complete_legal_dependencies=dependencies,input=list(c),mass=41,negative_closures_equal=True,scope='Actual AS loser above proposed combined upper40; not ASH* counterexample')
(B/'negative_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
