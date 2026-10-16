import hashlib,json
from pathlib import Path
B=Path('evidence/S014/twofuel_cegis');B.mkdir(exist_ok=True);assert not (B/'preflight.json').exists()
def write(p,t):
    p=Path(p)
    if not isinstance(t,str):t=json.dumps(t,indent=2)+'\n'
    assert not p.exists() or p.read_text(encoding='utf-8')==t,str(p)
    p.write_text(t,encoding='utf-8',newline='\n')
sources=[]
for suffix in ['cegis','verify','potential','lrat_verify','run']:
    source=Path('tools',f's014_c071_{suffix}.py');sources.append(source)
    t=source.read_text(encoding='utf-8').replace('evidence/S014/highpile_cegis','evidence/S014/twofuel_cegis').replace('evidence/S014/highpile_lrat','evidence/S014/twofuel_lrat').replace('s014_c071_','s014_c077_')
    if suffix=='run':
        t=t.replace("assert mode in ['control','0','1']", "assert mode in ['control','F8','F9','F10','F12']")
        t=t.replace("chosen=[c for i,c in enumerate([c for c in cases if not c['control']]) if i%2==int(mode)]", "chosen=[c for c in cases if c['id']==mode];assert len(chosen)==1")
    write(Path('tools',f's014_c077_{suffix}.py'),t)
cases=[dict(id='control2',n=2,c=[2,2],source=None,permutations=[[0,1]],control=True)]
for n in [8,9,10,12]:cases.append(dict(id=f'F{n}',n=n,c=[1]*(n-2)+[3,3],source=None,permutations=[list(range(n))],control=False))
runtime=json.loads(Path('evidence/S014/highpile_cegis/inputs.json').read_bytes())['runtime'];write(B/'inputs.json',dict(cases=cases,runtime=runtime));plan=Path('sessions/S014/PLAN_AMENDMENT_77.md');write(plan.with_suffix('.sha256'),hashlib.sha256(plan.read_bytes()).hexdigest()+'\n')
files=[B/'inputs.json',plan,plan.with_suffix('.sha256'),Path('research/S014_TWO_PAIR_FUEL_SPANNING_WALKS.md'),Path('research/S014_PROVED_GRAPH_SYMMETRY.md'),Path('research/S014_THREE_LAYER_AS_TAIL.md'),Path('tools/s014_lex_cnf.py'),Path('tools/s014_cegis_clauses_verify.py'),Path('tools/s014_tail_screen_verify.py'),Path('tools/s009_checks.py'),*sources,*Path('tools').glob('s014_c077_*.py')]
write(B/'preflight.json',dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files},native_binary='C:/Earth-Moon-problem/artifacts/tmp/S004/drat-trim-mingw.exe',native_sha256='970caaea97a15c8a27d4747e0e92e058ac1b1d9d4e04a95e3fc58b069ed4c03e'));print('CAM77 frozen, four full-buffer fixed classes, one child at a time')
