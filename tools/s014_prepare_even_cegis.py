import hashlib,itertools,json
from pathlib import Path
B=Path('evidence/S014/even_cegis');B.mkdir(exist_ok=True)
data=[('E8',[2,2,1,1,1,1,1,1]),('E9',[2,2,1,1,1,1,1,1,1]),('E10',[2,2,1,1,1,1,1,1,1,1]),('M9',[2,3,1,1,1,1,1,0,0]),('M10',[2,4,1,1,1,1,1,1,0,0]),('F9',[4,4,1,1,1,0,0,0,0]),('T10',[2,2,3,1,1,1,1,1,0,0]),('T12',[3,3,3,1,1,1,1,0,0,0,0,0])]
cases=[]
for name,c in data:
    n=len(c);assert sum(c)>=n+1;groups=[[v for v,z in enumerate(c) if z==x] for x in sorted(set(c))];perms=[]
    for rev in [False,True]:
        for shifts in itertools.product(*(range(len(g)) for g in groups)):
            p=list(range(n))
            for g,k in zip(groups,shifts):
                for j,u in enumerate(g):p[u]=g[((-j if rev else j)+k)%len(g)]
            if p not in perms:perms.append(p)
    cases.append(dict(id=name,n=n,c=c,permutations=perms))
cfg=json.loads(Path('evidence/S014/cegis/inputs.json').read_bytes());cfg['cases']=cases;(B/'inputs.json').write_text(json.dumps(cfg,indent=2)+'\n',encoding='utf-8',newline='\n')
t=Path('tools/s014_cegis_orbits_v2.py').read_text(encoding='utf-8').replace("B=Path('evidence/S014/cegis_orbits_v2')","B=Path('evidence/S014/even_cegis')")
a=t.index("            old=Path('evidence/S014/cegis')/case['id']");b=t.index('            for iteration in range(1,1001):',a)
t=t[:a]+"            for v in range(n):add(dict(kind='cut',vertices=[v],clause=[vid[e] for e in pairs if v in e]))\n"+t[b:]
Path('tools/s014_even_cegis.py').write_text(t,encoding='utf-8',newline='\n')
t=Path('tools/s014_cegis_orbits_verify_v2.py').read_text(encoding='utf-8').replace("B=Path('evidence/S014/cegis_orbits_v2')","B=Path('evidence/S014/even_cegis')")
Path('tools/s014_even_cegis_verify.py').write_text(t,encoding='utf-8',newline='\n')
plan=Path('sessions/S014/PLAN_AMENDMENT_41.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n')
files=[plan,B/'inputs.json',Path('evidence/S014/cegis/environment.json'),*Path('tools').glob('s014*even_cegis*.py'),Path('tools/s014_cegis_orbits_v2.py'),Path('tools/s014_cegis_clauses_verify.py'),Path('tools/s014_cegis_orbits_verify_v2.py'),Path('tools/s014_tail_screen_verify.py'),Path('tools/s009_checks.py')]
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM41 frozen',[(c['id'],len(c['permutations'])) for c in cases])
