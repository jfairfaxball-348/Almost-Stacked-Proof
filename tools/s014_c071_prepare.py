import hashlib,json,os
from pathlib import Path
B=Path('evidence/S014/highpile_cegis');B.mkdir(exist_ok=True);assert not (B/'preflight.json').exists()
def write(p,t):
    p=Path(p)
    if not isinstance(t,str):t=json.dumps(t,indent=2)+'\n'
    assert not p.exists() or p.read_text(encoding='utf-8')==t,str(p)
    p.write_text(t,encoding='utf-8',newline='\n')
for suffix in ['cegis','verify','potential','lrat_verify','run']:
    t=Path('tools',f's014_c068_{suffix}.py').read_text(encoding='utf-8').replace('evidence/S014/mass11_cegis','evidence/S014/highpile_cegis').replace('evidence/S014/mass11_lrat','evidence/S014/highpile_lrat').replace('s014_c068_','s014_c071_');write(Path('tools',f's014_c071_{suffix}.py'),t)
spec=[('H8_5551',8,[5,5,5,1]),('H8_7711',8,[7,7,1,1]),('H8_9531',8,[9,5,3,1]),('H8_5533',8,[5,5,3,3]),('H8_7733',8,[7,7,3,3]),('H9_5551',9,[5,5,5,1]),('H8_4444',8,[4,4,4,4]),('H8_6622',8,[6,6,2,2])];cases=[dict(id='control2',n=2,c=[2,2],source=None,permutations=[[0,1]],control=True)];files=[];oldcases=[];cuts={}
for folder in ['split_cegis','mass11_cegis']:
    old=Path('evidence/S014')/folder;cfg=json.loads((old/'inputs.json').read_bytes());assert json.loads((old/'summary.json').read_bytes())['certified']==(32 if folder=='split_cegis' else 44);files.extend([old/'inputs.json',old/'summary.json'])
    for case in cfg['cases']:
        if case['control']:continue
        D=old/case['id'];files.extend([D/'constraints.jsonl',D/'clause_verification.json']);records=[json.loads(x) for x in (D/'constraints.jsonl').read_text(encoding='utf-8').splitlines()];oldcases.append((D,case,records))
        for row in records:
            if row['kind']=='cut':cuts.setdefault((case['n'],tuple(row['clause'])),row)
for name,n,counts in spec:
    c=sorted([0]*(n-len(counts))+counts);D=B/'sources'/name;D.mkdir(parents=True,exist_ok=True);records=[r for (order,_),r in cuts.items() if order==n];seen={tuple(r['clause']) for r in records};origins=[]
    for old,case,rows in oldcases:
        a=case['c']
        if n!=case['n'] or any(x<z or (x-z)%3 or x>z and not z for x,z in zip(c,a)):continue
        for number,row in enumerate(rows):
            if row['kind']!='c_win' or tuple(row['clause']) in seen:continue
            moves=row['moves'];edges={tuple(sorted(e)) for e in moves};prefix=[];valid=True
            for u in range(n):
                if c[u]==a[u]:continue
                neighbors=sorted(v if u==w else w for w,v in edges if u in [w,v])
                if not neighbors:valid=False;break
                v=neighbors[0]
                for _ in range((c[u]-a[u])//3):prefix.extend([[u,v],[u,v],[v,u]])
            if not valid:continue
            records.append(dict(kind='c_win',moves=prefix+moves,clause=row['clause']));seen.add(tuple(row['clause']));origins.append(dict(source=(old/'constraints.jsonl').as_posix(),row=number,old_c=a,prefix_moves=len(prefix)))
    write(D/'constraints.jsonl',''.join(json.dumps(r,separators=(',',':'))+'\n' for r in records));write(D/'origins.json',origins);files.extend([D/'constraints.jsonl',D/'origins.json']);cases.append(dict(id=name,n=n,c=c,source=D.as_posix(),permutations=[list(range(n))],control=False))
runtime=json.loads(Path('evidence/S014/mass11_cegis/inputs.json').read_bytes())['runtime'];write(B/'inputs.json',dict(cases=cases,runtime=runtime));plan=Path('sessions/S014/PLAN_AMENDMENT_71.md');write(plan.with_suffix('.sha256'),hashlib.sha256(plan.read_bytes()).hexdigest()+'\n');files.extend([B/'inputs.json',plan,plan.with_suffix('.sha256'),Path('research/S014_PROVED_GRAPH_SYMMETRY.md'),Path('research/S014_THREE_LAYER_AS_TAIL.md'),Path('tools/s014_lex_cnf.py'),Path('tools/s014_cegis_clauses_verify.py'),Path('tools/s014_tail_screen_verify.py'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_c071_*.py')]);write(B/'preflight.json',dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files},native_binary='C:/Earth-Moon-problem/artifacts/tmp/S004/drat-trim-mingw.exe',native_sha256='970caaea97a15c8a27d4747e0e92e058ac1b1d9d4e04a95e3fc58b069ed4c03e'));print(json.dumps(dict(patterns=len(spec),imports=[dict(case=c['id'],records=sum(1 for _ in (Path(c['source'])/'constraints.jsonl').open(encoding='utf-8'))) for c in cases if not c['control']])))
