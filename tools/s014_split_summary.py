"""Inventory completeness and complete-proof flags only; no native imports."""
import hashlib,itertools,json
from pathlib import Path
B=Path('evidence/S014/split_cegis');V=Path('evidence/S014/split_lrat')
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cases=[c for c in json.loads((B/'inputs.json').read_bytes())['cases'] if not c['control']];dp={(0,0):{()}}
for a in range(1,11):
    nxt={key:set(v) for key,v in dp.items()}
    for (m,l),tuples in dp.items():
        for k in range(1,min(8-l,(10-m)//a)+1):nxt.setdefault((m+k*a,l+k),set()).update(t+(a,)*k for t in tuples)
    dp=nxt
wanted={tuple(reversed(t))+(0,)*(8-l) for (m,l),ts in dp.items() if m==10 for t in ts if sum(x>=2 for x in t)>=2};assert len(wanted)==len(cases)==32 and {tuple(c['c']) for c in cases}==wanted
rows=[]
for c in cases:
    p=V/c['id']/'verification.json';valid=p.exists() and json.loads(p.read_bytes())['fixed_input_class_exclusion_certified'];D=B/c['id'];status=json.loads((D/'result.json').read_bytes())['status'] if (D/'result.json').exists() else 'NOT_EXECUTED';rows.append(dict(case=c['id'],c=c['c'],status=status,independently_excluded=valid))
out=dict(patterns=32,complete_inventory_equal=True,certified=sum(r['independently_excluded'] for r in rows),complete_mass10_order8_exclusion=all(r['independently_excluded'] for r in rows),cases=rows,scope='Finite fixed(n8,M10) only; universal ASH* OPEN')
(B/'summary.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k!='cases'}))
