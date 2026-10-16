import hashlib,json
from pathlib import Path
B=Path('evidence/S014/retract_trees');B.mkdir(exist_ok=True);old=Path('evidence/S014/onebit/inputs.json');graphs=json.loads(old.read_bytes())['graphs'];graphs=[dict(g,name='atlas'+str(g['id'])) for g in graphs]
graphs.append(dict(id=len(graphs),name='cube3',n=8,edges=[[u,v] for u in range(8) for v in range(u+1,8) if (u^v).bit_count()==1]))
for k in [5,6,7]:graphs.append(dict(id=len(graphs),name='crown'+str(k),n=2*k,k=k,edges=[[i,k+j] for i in range(k) for j in range(k) if i!=j]))
assert len(graphs)==31
(B/'inputs.json').write_text(json.dumps(dict(graphs=graphs,cases=[dict(graph=dict(graph='crown5',n=10,edges=graphs[-3]['edges']),goal='stack',max_mass=24,candidate_cap=1000000,loser_cap=1000000)]),indent=2)+'\n',encoding='utf-8',newline='\n');plan=Path('sessions/S014/PLAN_AMENDMENT_53.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files=[old,B/'inputs.json',plan,plan.with_suffix('.sha256'),Path('research/S014_ISOMETRIC_TREE_BRIDGE.md'),Path('research/S014_CROWN_ISOMETRIC_TREE_OBSTRUCTION.md'),Path('tools/s014_circulant_engine.py'),Path('tools/s014_circulant_engine_verify.py'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_retract*.py')]
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM53 frozen31 graphs, every induced subset, one crown threshold')
