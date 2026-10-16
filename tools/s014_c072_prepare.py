import hashlib,json
from pathlib import Path
B=Path('evidence/S014/bip_parity');B.mkdir(exist_ok=True);assert not (B/'preflight.json').exists();old=Path('evidence/S014/critical_even');cfg=json.loads((old/'inputs.json').read_bytes());assert len(cfg['cases'])==638
(B/'inputs.json').write_text(json.dumps(cfg,indent=2)+'\n',encoding='utf-8',newline='\n');plan=Path('sessions/S014/PLAN_AMENDMENT_72.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files=[plan,plan.with_suffix('.sha256'),B/'inputs.json',old/'inputs.json',old/'preflight.json',old/'verification.json',Path('research/S014_PARITY_AND_TRUE_HEAD_FRONTIER.md'),Path('research/S014_BIPARTITE_NEUTRAL_CATALYSIS.md'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_c072_*.py')]
for c in cfg['cases']:files.extend([Path(c['certificate']),Path(c['summary'])])
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM72 complete existing critical matrix frozen')
