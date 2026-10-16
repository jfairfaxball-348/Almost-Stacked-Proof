import hashlib,json
from pathlib import Path
B=Path('evidence/S014/coordinate_maximal');B.mkdir(exist_ok=True);cases=[]
for name,extra in [('P4',[]),('P4plus02',[[0,2]]),('P4plus03',[[0,3]]),('P4plus13',[[1,3]])]:cases.append(dict(graph=dict(graph=name,n=4,edges=[[0,1],[1,2],[2,3]]+extra),goal='stack',max_mass=15,candidate_cap=10000,loser_cap=10000))
(B/'inputs.json').write_text(json.dumps(dict(cases=cases),indent=2)+'\n',encoding='utf-8',newline='\n');plan=Path('sessions/S014/PLAN_AMENDMENT_50.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files=[B/'inputs.json',plan,plan.with_suffix('.sha256'),Path('research/S014_ACTUAL_NEUTRAL_EXTREMIZER_OBSTRUCTION.md'),Path('research/S014_COORDINATE_MAXIMAL_OBSTRUCTION.md'),Path('tools/s014_circulant_engine.py'),Path('tools/s014_circulant_engine_verify.py'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_coordinate*.py')]
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM50 exact inputs/code frozen before execution')
