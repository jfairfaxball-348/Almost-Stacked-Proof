import json,lzma,time
from pathlib import Path
B=Path('evidence/S014/metric_gap');cfg=json.loads((B/'inputs.json').read_bytes());g=cfg['cases'][0]['graph'];n=g['n'];units=[1<<(8*v) for v in range(n)];arcs=sorted((u,v) for e in g['edges'] for u,v in [e,e[::-1]]);start=time.monotonic();c=sum(z*units[v] for v,z in enumerate(cfg['c']));todo=[c];seen={c}
for x in todo:
    assert len(seen)<=300000 and time.monotonic()-start<540 and sum(bool((x>>(8*v))&255) for v in range(n))>1
    for u,v in arcs:
        if ((x>>(8*u))&255)<2:continue
        y=x-2*units[u]+units[v]
        if y not in seen:seen.add(y);todo.append(y)
with lzma.open(B/'negative.bin.xz','wb') as f:
    for x in sorted(seen):f.write(x.to_bytes(16,'little'))
(B/'negative.json').write_text(json.dumps(dict(states=len(seen),c=cfg['c']))+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(complete_negative_states=len(seen))))
