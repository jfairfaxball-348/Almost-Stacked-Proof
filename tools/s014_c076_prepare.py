import hashlib,json
from pathlib import Path
B=Path('evidence/S014/neighbor_ascent');B.mkdir(exist_ok=True);assert not (B/'preflight.json').exists();old=Path('evidence/S014/leaf_ascent');cfg=json.loads((old/'inputs.json').read_bytes());assert len(cfg['cases'])==142
(B/'inputs.json').write_text(json.dumps(cfg,indent=2)+'\n',encoding='utf-8',newline='\n');plan=Path('sessions/S014/PLAN_AMENDMENT_76.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files=[B/'inputs.json',plan,plan.with_suffix('.sha256'),old/'inputs.json',old/'preflight.json',old/'verification.json',Path('research/S014_UNIQUE_MARKERS_AND_LEAF_ESCAPE.md'),Path('research/S014_TRIVALENT_BOUNDARY_AND_BIPARTITE_PARITY.md'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_c076_*.py')]
for c in cfg['cases']:files.extend([Path(c['certificate']),Path(c['summary'])])
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM76 frozen, exactly one child at a time')
