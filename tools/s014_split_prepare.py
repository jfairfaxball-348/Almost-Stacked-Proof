import hashlib,json,os
from pathlib import Path
B=Path('evidence/S014/split_cegis');B.mkdir(exist_ok=True);old=Path('evidence/S014/fair_cegis/N8_M10');cfg=json.loads((old.parent/'inputs.json').read_bytes());source=next(c for c in cfg['cases'] if c['id']=='N8_M10');assert len(source['patterns'])==32 and json.loads((old/'clause_verification.json').read_bytes())['counterexample_exists_implies_formula_satisfiable'];records=[json.loads(line) for line in (old/'constraints.jsonl').read_text(encoding='utf-8').splitlines()];cases=[dict(id='control2',n=2,c=[2,2],source=None,permutations=[[0,1]],control=True)];files=[old.parent/'inputs.json',*list(old.rglob('*'))]
for j,c in enumerate(source['patterns']):
    name=f'P{j:02d}';D=B/'sources'/name;D.mkdir(parents=True,exist_ok=True);imported=[]
    for r0 in records:
        r=r0.copy()
        if r['kind']=='independent_set':continue
        if r['kind']=='c_win':
            if r['pattern']!=j:continue
            assert -(28+1+j) in r['clause'];r['clause']=[x for x in r['clause'] if abs(x)<=28];r.pop('pattern')
        elif r['kind']=='AS_loss':r['certificate']=Path(os.path.relpath((old/r['certificate']).resolve(),D)).as_posix()
        else:assert r['kind']=='cut'
        imported.append(r)
    p=D/'constraints.jsonl';p.write_text(''.join(json.dumps(r,separators=(',',':'))+'\n' for r in imported),encoding='utf-8',newline='\n');files.append(p);cases.append(dict(id=name,n=8,c=c,source=D.as_posix(),permutations=[list(range(8))],control=False))
(B/'inputs.json').write_text(json.dumps(dict(cases=cases,runtime=cfg['runtime']),indent=2)+'\n',encoding='utf-8',newline='\n');plan=Path('sessions/S014/PLAN_AMENDMENT_56.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files.extend([plan,plan.with_suffix('.sha256'),B/'inputs.json',Path('research/S014_SHARED_INPUT_REDUCTION.md'),Path('research/S014_PROVED_GRAPH_SYMMETRY.md'),Path('research/S014_THREE_LAYER_AS_TAIL.md'),Path('tools/s014_lex_cnf.py'),Path('tools/s014_cegis_clauses_verify.py'),Path('tools/s014_tail_screen_verify.py'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_split*.py')]);files=[p for p in files if p.is_file()]
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files},native_binary='C:/Earth-Moon-problem/artifacts/tmp/S004/drat-trim-mingw.exe',native_sha256='970caaea97a15c8a27d4747e0e92e058ac1b1d9d4e04a95e3fc58b069ed4c03e'),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM56 frozen32 fixed graph predicates and control')
