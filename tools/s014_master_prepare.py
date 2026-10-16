import hashlib,itertools,json,os
from pathlib import Path
B=Path('evidence/S014/master_cegis');B.mkdir(exist_ok=True)
plan=Path('sessions/S014/PLAN_AMENDMENT_48.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n')
spec=[(2,4,[]),(9,11,['cegis_orbits_v2/C9a','lex_cegis/E9','continued_cegis/F9']),(10,12,['lex_cegis/E10','continued_cegis/M10','continued_cegis/T10']),(10,17,['lex_cegis/C10']),(12,13,['lex_cegis/T12']),(12,16,['lex_cegis/D12'])];cases=[];files=[]
def partitions(total,slots,largest):
    if not slots:
        if not total:yield ()
        return
    for first in range(min(total,largest),-1,-1):
        if total-first>(slots-1)*first:continue
        for rest in partitions(total-first,slots-1,first):yield (first,)+rest
runtime=json.loads(Path('evidence/S014/cegis/inputs.json').read_bytes())['runtime']
for n,M,sources in spec:
    patterns=[list(p) for p in partitions(M,n,M) if sum(x>=2 for x in p)>=2];patterns.sort(key=lambda p:(sum(x>=2 for x in p),sum(x>=2 and x%2==0 for x in p),max(p)-min(x for x in p if x>=2),tuple(p)));assert 0<len(patterns)<=300
    name=f'N{n}_M{M}';D=B/name;D.mkdir(exist_ok=True);pairs=list(itertools.combinations(range(n),2));vid={e:i+1 for i,e in enumerate(pairs)};selectors=list(range(len(pairs)+1,len(pairs)+len(patterns)+1));lookup={tuple(p):i for i,p in enumerate(patterns)};imports=[];resolved=[]
    for source in sources:
        old=Path('evidence/S014')/source;assert (old/'result.json').exists() and (old/'clause_verification.json').exists(),source
        prov=json.loads((old/'clause_verification.json').read_bytes());assert prov.get('all_clauses_necessary_for_fixed_input_counterexample') or prov.get('all_graph_clauses_necessary'),source
        cfg=json.loads((old.parent/'inputs.json').read_bytes());oc=next(c for c in cfg['cases'] if c['id']==old.name);assert oc['n']==n and sum(oc['c'])==M;order=sorted(range(n),key=lambda v:(-oc['c'][v],v));mapping={old:new for new,old in enumerate(order)};index=lookup[tuple(oc['c'][v] for v in order)]
        for lineno,line in enumerate((old/'constraints.jsonl').read_text(encoding='utf-8').splitlines()):
            r=json.loads(line);r['origin']=[old.as_posix(),lineno]
            if r['kind']=='c_win':
                r['pattern']=index;r['moves']=[[mapping[u],mapping[v]] for u,v in r['moves']];r['clause']=sorted({-selectors[index]}|{-vid[tuple(sorted((u,v)))] for u,v in r['moves']})
            elif r['kind']=='AS_loss':r['certificate']=Path(os.path.relpath(old/r['certificate'],D)).as_posix()
            else:assert r['kind']=='cut'
            imports.append(r)
        resolved.append(dict(path=old.as_posix(),source_input=oc['c'],mapped_pattern=index,source_status=json.loads((old/'result.json').read_bytes())['status']));files.append(old.parent/'inputs.json');files.extend(p for p in old.rglob('*') if p.is_file())
    ip=D/'imports.jsonl';ip.write_text(''.join(json.dumps(r,separators=(',',':'))+'\n' for r in imports),encoding='utf-8',newline='\n');files.append(ip);cases.append(dict(id=name,n=n,mass=M,patterns=patterns,sources=resolved,control=n==2))
(B/'inputs.json').write_text(json.dumps(dict(cases=cases,runtime=runtime),indent=2)+'\n',encoding='utf-8',newline='\n')
t=Path('tools/s014_lrat_verify.py').read_text(encoding='utf-8').replace("B=Path('evidence/S014/lrat');P=Path('evidence/S014/cegis_orbits_v2')","B=Path('evidence/S014/master_lrat');P=Path('evidence/S014/master_cegis')").replace("['all_clauses_necessary_for_fixed_input_counterexample']","['counterexample_exists_implies_formula_satisfiable']").replace('fixed_input_class_exclusion_certified','fixed_mass_graph_class_exclusion_certified').replace('ONLY exact fixed-c graph-class exclusion; universal ASH* OPEN','ONLY all mass-M inputs on n-vertex graphs; universal ASH* OPEN')
Path('tools/s014_master_lrat_verify.py').write_text(t,encoding='utf-8',newline='\n')
files.extend([plan,plan.with_suffix('.sha256'),B/'inputs.json',Path('evidence/S014/cegis/environment.json'),Path('research/S014_SHARED_INPUT_REDUCTION.md'),Path('research/S014_PROVED_GRAPH_SYMMETRY.md'),Path('research/S004_ASHSTAR_ATTACK.md'),Path('research/S005_ASHSTAR_EXTREMA_AND_ROOTED_CLEARING.md'),Path('research/S014_THREE_LAYER_AS_TAIL.md'),*Path('tools').glob('s014_master*.py'),Path('tools/s014_lrat_verify.py'),Path('tools/s014_tail_screen_verify.py'),Path('tools/s009_checks.py')])
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files},native_binary='C:/Earth-Moon-problem/artifacts/tmp/S004/drat-trim-mingw.exe',native_sha256='970caaea97a15c8a27d4747e0e92e058ac1b1d9d4e04a95e3fc58b069ed4c03e'),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM48 frozen',[(c['id'],len(c['patterns'])) for c in cases])
