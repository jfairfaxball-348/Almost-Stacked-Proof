import hashlib,json
from pathlib import Path
B=Path('evidence/S014/sector_exchange');B.mkdir(exist_ok=True);assert not (B/'preflight.json').exists();old=Path('evidence/S014/odd_leaf_contraction');cfg=json.loads((old/'inputs.json').read_bytes());cfg['cases']=[c for c in cfg['cases'] if c['n']<=5];assert len(cfg['cases'])==30
(B/'inputs.json').write_text(json.dumps(cfg,indent=2)+'\n',encoding='utf-8',newline='\n');plan=Path('sessions/S014/PLAN_AMENDMENT_81.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files=[B/'inputs.json',plan,plan.with_suffix('.sha256'),old/'inputs.json',old/'preflight.json',old/'verification.json',Path('research/S014_THREE_LANGUAGE_EXCHANGE_OBSTRUCTION.md'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_c081_*.py')]
for c in cfg['cases']:files.extend([Path(c['certificate']),Path(c['summary'])])
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM81 frozen, rescaled mod3-sector exchange challenge')
