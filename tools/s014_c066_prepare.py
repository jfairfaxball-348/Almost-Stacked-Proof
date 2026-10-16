import hashlib,itertools,json
from pathlib import Path
B=Path('evidence/S014/fano_layers');B.mkdir(exist_ok=True);S=Path('evidence/S014/fano_AS');a=json.loads((S/'inputs.json').read_bytes());v=json.loads((S/'verification.json').read_bytes());assert v['exact_binary_buffer_AS_oracle_certified'] and v['exact_L_AS']==29;cases=[]
for d in [1,3]:
    n=1<<d;maps=[]
    for perm in itertools.permutations(range(d)):
        coords=[sum(((u>>j)&1)<<perm[j] for j in range(d)) for u in range(n)]
        for s in range(n):maps.append([u^s for u in coords])
    cases.append(dict(id='Q'+str(d),n=n,edges=[[u,u^(1<<j)] for u in range(n) for j in range(d) if u<(u^(1<<j))],maps=maps,max_mass=3 if d==1 else 15,control=True,expected_threshold=3 if d==1 else 15))
cases.append(dict(id='FanoInc14',n=14,edges=a['edges'],maps=a['maps'],source_maps=a['source_maps'],max_mass=30,control=False,exact_AS_maximum=29));cfg=dict(cases=cases,powershell=json.loads(Path('evidence/S014/cube_layers/inputs.json').read_bytes())['powershell']);(B/'inputs.json').write_text(json.dumps(cfg,separators=(',',':'))+'\n',encoding='utf-8',newline='\n');plan=Path('sessions/S014/PLAN_AMENDMENT_66.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files=[B/'inputs.json',plan,plan.with_suffix('.sha256'),S/'inputs.json',S/'nodes.bin.xz',S/'choices.json',S/'verification.json',S/'repair_preflight.json',Path('research/S014_COMPLETE_ORBIT_LAYERS.md'),Path('research/S014_BINARY_BUFFER_LOWER_ANNOTATIONS.md'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_c066_*')]
for d,M in [(1,3),(3,15)]:
    for m in range(1,M+1):files.extend([Path(f'evidence/S014/cube_layers_full/d{d}/mass{m}.bin.gz'),Path(f'evidence/S014/cube_layers_full/d{d}/mass{m}_verification.json')])
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM66 graph/group/all-input target30 and generic controls frozen')
