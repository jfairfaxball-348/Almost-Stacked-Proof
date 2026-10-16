import hashlib,json
from pathlib import Path
B=Path('evidence/S014/cube_layers_full');B.mkdir(exist_ok=True);old=Path('evidence/S014/cube_layers');cfg=json.loads((old/'inputs.json').read_bytes());cfg['specified_group']='XOR translations and all coordinate permutations';(B/'inputs.json').write_text(json.dumps(cfg,indent=2)+'\n',encoding='utf-8',newline='\n');plan=Path('sessions/S014/PLAN_AMENDMENT_64.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files=[B/'inputs.json',plan,plan.with_suffix('.sha256'),Path('research/S014_COMPLETE_ORBIT_LAYERS.md'),Path('evidence/S014/cube_lower/verification.json'),Path('evidence/S014/cube_dag/choices.json'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_c064_*')]
for d,top in [(1,3),(3,15),(4,13)]:
    for m in range(1,top+1):files.extend([old/f'd{d}'/f'mass{m}.bin.gz',old/f'd{d}'/f'mass{m}_verification.json'])
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM64 graph/group/source and old complete prefixes frozen before build')
