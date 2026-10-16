"""New numbered wrapper generation; never overwrite an earlier tool version."""
import hashlib,itertools,json,os
from pathlib import Path
B=Path('evidence/S014/mass11_cegis');B.mkdir(exist_ok=True);assert not (B/'preflight.json').exists()
def write(p,t):
    p=Path(p)
    if not isinstance(t,str):t=json.dumps(t,indent=2)+'\n'
    assert not p.exists() or p.read_text(encoding='utf-8')==t,str(p)
    p.write_text(t,encoding='utf-8',newline='\n')
for suffix,source in [('cegis','s014_split_cegis.py'),('verify','s014_mass_split_verify.py'),('potential','s014_split_potential.py'),('lrat_verify','s014_split_lrat_verify.py'),('run','s014_split_run.py')]:
    t=Path('tools',source).read_text(encoding='utf-8').replace('evidence/S014/split_cegis','evidence/S014/mass11_cegis').replace('evidence/S014/split_lrat','evidence/S014/mass11_lrat').replace('s014_split_','s014_c068_')
    write(Path('tools',f's014_c068_{suffix}.py'),t)
patterns=[list(c) for c in itertools.combinations_with_replacement(range(12),8) if sum(c)==11 and sum(z>=2 for z in c)>=2];assert len(patterns)<=256
old=Path('evidence/S014/split_cegis');imports=[];files=[Path('evidence/S014/split_cegis/summary.json')];assert json.loads(files[0].read_bytes())['complete_mass10_order8_exclusion'];seen=set();provenance=[]
D=B/'imported';D.mkdir(exist_ok=True)
for i in range(32):
    source=old/f'P{i:02d}';verification=Path(f'evidence/S014/split_lrat/P{i:02d}/verification.json');assert json.loads(verification.read_bytes())['fixed_input_class_exclusion_certified'];files.extend([source/'constraints.jsonl',source/'clause_verification.json',verification])
    for line,raw in enumerate((source/'constraints.jsonl').read_text(encoding='utf-8').splitlines(),1):
        r=json.loads(raw)
        if r['kind'] not in ['cut','AS_loss']:continue
        if r['kind']=='AS_loss' and not 11<=sum(r['input'])<=13:continue
        key=tuple(sorted(r['clause']))
        if key in seen:continue
        seen.add(key);provenance.append(dict(source=(source/'constraints.jsonl').as_posix(),line=line,record_sha256=hashlib.sha256(raw.encode()).hexdigest()))
        if r['kind']=='AS_loss':
            cert=(source/r['certificate']).resolve();files.append(cert);r['certificate']=Path(os.path.relpath(cert,D)).as_posix()
        imports.append(r)
write(D/'constraints.jsonl',''.join(json.dumps(r,separators=(',',':'))+'\n' for r in imports));write(D/'provenance.json',provenance);files.extend([D/'constraints.jsonl',D/'provenance.json'])
cases=[dict(id='control2',n=2,c=[2,2],source=None,permutations=[[0,1]],control=True)]+[dict(id=f'P{i:03d}',n=8,c=c,source=D.as_posix(),permutations=[list(range(8))],control=False) for i,c in enumerate(patterns)]
runtime=json.loads((old/'inputs.json').read_bytes())['runtime'];write(B/'inputs.json',dict(cases=cases,runtime=runtime));plan=Path('sessions/S014/PLAN_AMENDMENT_68.md');write(plan.with_suffix('.sha256'),hashlib.sha256(plan.read_bytes()).hexdigest()+'\n')
files.extend([B/'inputs.json',plan,plan.with_suffix('.sha256'),Path('research/S014_SHARED_INPUT_REDUCTION.md'),Path('research/S014_PROVED_GRAPH_SYMMETRY.md'),Path('research/S014_THREE_LAYER_AS_TAIL.md'),Path('tools/s014_lex_cnf.py'),Path('tools/s014_cegis_clauses_verify.py'),Path('tools/s014_tail_screen_verify.py'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_c068_*.py')])
write(B/'preflight.json',dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files},native_binary='C:/Earth-Moon-problem/artifacts/tmp/S004/drat-trim-mingw.exe',native_sha256='970caaea97a15c8a27d4747e0e92e058ac1b1d9d4e04a95e3fc58b069ed4c03e'));print(json.dumps(dict(patterns=len(patterns),imported_necessary_clauses=len(imports))))
