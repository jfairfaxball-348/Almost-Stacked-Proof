import hashlib,json
from pathlib import Path
B=Path('evidence/S014/mass_slack');B.mkdir(exist_ok=True);assert not (B/'preflight.json').exists()
old=Path('evidence/S014/eliminate_residual');cfg=json.loads((old/'inputs.json').read_bytes());cases=[c for c in cfg['cases'] if c['n']<=5];assert len(cases)==30
(B/'inputs.json').write_text(json.dumps(dict(cases=cases),indent=2)+'\n',encoding='utf-8',newline='\n');plan=Path('sessions/S014/PLAN_AMENDMENT_69.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files=[plan,plan.with_suffix('.sha256'),B/'inputs.json',old/'inputs.json',old/'preflight.json',old/'verification.json',Path('research/S014_NONDECREASING_MASS_ELIMINATION.md'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_c069_*.py')]
for c in cases:files.extend([Path(c['certificate']),Path(c['summary'])])
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(cases=len(cases))))
