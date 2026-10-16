"""Prepare separate CAM38 implementation and frozen, explicitly listed inputs."""
import hashlib,itertools,json
from pathlib import Path

B=Path('evidence/S014/cegis_orbits')
B.mkdir(exist_ok=True)
cfg=json.loads(Path('evidence/S014/cegis/inputs.json').read_bytes())
for case in cfg['cases']:
    groups=[[i for i,z in enumerate(case['c']) if z==value] for value in sorted(set(case['c']))]
    perms=[]
    for choices in itertools.product(*(list(itertools.permutations(g)) for g in groups)):
        p=list(range(case['n']))
        for group,image in zip(groups,choices):
            for u,v in zip(group,image):p[u]=v
        perms.append(p)
    case['permutations']=perms
(B/'inputs.json').write_text(json.dumps(cfg,indent=2)+'\n',encoding='utf-8',newline='\n')
src=Path('tools/s014_cegis.py').read_text(encoding='utf-8')
def replace(a,b):
    global src
    assert a in src,a[:100]
    src=src.replace(a,b)
replace('import itertools,json,lzma,sys,time','import itertools,json,lzma,os,struct,sys,time')
replace("B=Path('evidence/S014/cegis')","B=Path('evidence/S014/cegis_orbits')")
replace("clauses=[];records=[];start=", "clauses=[];records=[];sources=[];unique=set();perm_maps=[[vid[tuple(sorted((p[u],p[v])))] for u,v in pairs] for p in case['permutations']];start=")
left=src.index('    def add(record):')
right=src.index('    def oracle(E):')
src=src[:left]+'''    def image(C,j):
        mapping=perm_maps[j]
        return tuple(sorted((mapping[abs(x)-1] if x>0 else -mapping[abs(x)-1]) for x in C))
    def expand(i,j):
        C=image(records[i]['clause'],j)
        if C in unique:return
        if len(clauses)>=500000:raise RuntimeError('CLAUSE_CAP_UNKNOWN')
        unique.add(C);clauses.append(C);sources.append((i,j));sat.add_clause(C)
    def add(record,close=True):
        i=len(records);records.append(record);expand(i,0)
        if close:
            for j in range(1,len(perm_maps)):expand(i,j)
''' +src[right:]
replace("    (D/'constraints.jsonl').write_bytes(b'')\n",'')
replace("            for v in range(n):add(dict(kind='cut',vertices=[v],clause=[vid[e] for e in pairs if v in e]))\n            for iteration in range(1,5001):", """            old=Path('evidence/S014/cegis')/case['id']
            for line in (old/'constraints.jsonl').read_text(encoding='utf-8').splitlines():
                rec=json.loads(line)
                if rec['kind']=='AS_loss':rec['certificate']=Path(os.path.relpath(old/rec['certificate'],D)).as_posix()
                add(rec,False)
            for i in range(len(records)):
                for j in range(1,len(perm_maps)):expand(i,j)
            for iteration in range(1,1001):""")
replace("                    moves=history(root);add(dict(kind='c_win',moves=moves,clause=sorted({-vid[tuple(sorted((u,v)))] for u,v in moves})));continue", """                    moves=history(root);support={tuple(sorted((u,v))) for u,v in moves}
                    for e in sorted(support.copy()):
                        if e not in support:continue
                        aa,mm,ww,hh=oracle(support-{e})
                        if ww(root):moves=hh(root);support={tuple(sorted((u,v))) for u,v in moves}
                    add(dict(kind='c_win',moves=moves,clause=sorted(-vid[e] for e in support)));continue""")
replace("        assert str(error)=='ORACLE_STATE_CAP_UNKNOWN';status=str(error)","        assert str(error) in ['ORACLE_STATE_CAP_UNKNOWN','CLAUSE_CAP_UNKNOWN'];status=str(error)")
replace("    cnf=f'p cnf", """    (D/'constraints.jsonl').write_text(''.join(json.dumps(r,separators=(',',':'))+'\\n' for r in records),encoding='utf-8',newline='\\n')
    with (D/'clause_sources.bin').open('wb') as f:
        for source in sources:f.write(struct.pack('<II',*source))
    base=D/'base';bd=base/case['id'];bd.mkdir(parents=True,exist_ok=True)
    (base/'inputs.json').write_text(json.dumps(dict(cases=[case]))+'\\n',encoding='utf-8',newline='\\n')
    base_records=[]
    for record in records:
        rec=record.copy()
        if rec['kind']=='AS_loss':rec['certificate']=Path(os.path.relpath(D/rec['certificate'],bd)).as_posix()
        base_records.append(rec)
    (bd/'constraints.jsonl').write_text(''.join(json.dumps(r,separators=(',',':'))+'\\n' for r in base_records),encoding='utf-8',newline='\\n')
    (bd/'formula.cnf').write_text(f'p cnf {len(pairs)} {len(records)}\\n'+''.join(' '.join(map(str,r['clause']))+' 0\\n' for r in records),encoding='ascii',newline='\\n')
    cnf=f'p cnf""")
replace("iterations=iteration,clauses=len(clauses)","iterations=iteration,base_clauses=len(records),stabilizer_size=len(perm_maps),clauses=len(clauses)")
Path('tools/s014_cegis_orbits.py').write_text(src,encoding='utf-8',newline='\n')
plan=Path('sessions/S014/PLAN_AMENDMENT_38.md')
plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n')
files=[plan,plan.with_suffix('.sha256'),B/'inputs.json',Path('evidence/S014/cegis/environment.json')]
files+=list(Path('tools').glob('s014*orbits*.py'))
files+=list(Path('tools').glob('s014_cegis*.py'))
files+=list(Path('evidence/S014/cegis').rglob('*'))
digests={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files if p.is_file()}
(B/'preflight.json').write_text(json.dumps(dict(files=digests),indent=2)+'\n',encoding='utf-8',newline='\n')
print('CAM38 frozen',len(digests),'files; group sizes',[len(c['permutations']) for c in cfg['cases']])
