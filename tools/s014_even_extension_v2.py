import json
from pathlib import Path
B=Path('evidence/S014/even_extension_v2');a=json.loads((B/'inputs.json').read_bytes());n=a['n'];unit=[1<<(8*i) for i in range(n)];arcs=[e for u,v in a['edges'] for e in [(u,v),(v,u)]];root=sum(z*unit[i] for i,z in enumerate(a['c']));seen=set();stack=[root]
while stack:
    x=stack.pop()
    if x in seen:continue
    seen.add(x);assert len(seen)<=300 and sum(bool((x>>(8*i))&255) for i in range(n))>1
    stack.extend(x-2*unit[u]+unit[v] for u,v in arcs if ((x>>(8*u))&255)>=2)
rows=[]
for t in a['targets']:
    x=sum(z*unit[i] for i,z in enumerate(t['c']));assert len(t['moves'])<=100
    for u,v in t['moves']:assert (u,v) in arcs and ((x>>(8*u))&255)>=2;x=x-2*unit[u]+unit[v]
    final=[(x>>(8*i))&255 for i in range(n)];assert sum(z>0 for z in final)==1;rows.append(dict(v=t['v'],moves=len(t['moves']),final=final))
out=dict(negative_states=sorted(seen),targets=rows);(B/'results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(negative_states=len(seen),positive_targets=len(rows))),flush=True)
