import hashlib,json
from pathlib import Path
B=Path('evidence/S014/lex_cegis');B.mkdir(exist_ok=True);files=[];cases=[]
for name in ['E9','E10','C10','T12']:
    old=Path('evidence/S014')/('trace_cegis' if name=='C10' else 'even_cegis');cfg=json.loads((old/'inputs.json').read_bytes());case=next(c for c in cfg['cases'] if c['id']==name).copy();case['source']=(old/name).as_posix();case['permutations']=[list(range(case['n']))];cases.append(case);files.append(old/'inputs.json');files.extend(p for p in (old/name).rglob('*') if p.is_file())
cases.append(dict(id='D12',n=12,c=[3,3,1,1,0,0,3,3,1,1,0,0],source=None,permutations=[list(range(12))]));cfg['cases']=cases;(B/'inputs.json').write_text(json.dumps(cfg,indent=2)+'\n',encoding='utf-8',newline='\n')
t=Path('tools/s014_cegis_orbits_v2.py').read_text(encoding='utf-8').replace("B=Path('evidence/S014/cegis_orbits_v2')","B=Path('evidence/S014/lex_cegis')").replace('import itertools,json,lzma,os,struct,sys,time','import itertools,json,lzma,os,struct,sys,time\nfrom s014_lex_cnf import build').replace('range(1,1001)','range(1,10001)').replace('500000:raise RuntimeError(\'CLAUSE_CAP_UNKNOWN\')','50000:raise RuntimeError(\'CLAUSE_CAP_UNKNOWN\')')
t=t.replace('    def image(C,j):',"    variables,lex_clauses,lex_blocks=build(n,c)\n    (D/'lex_blocks.json').write_text(json.dumps(lex_blocks)+'\\n',encoding='utf-8',newline='\\n')\n    def image(C,j):")
a=t.index("            old=Path('evidence/S014/cegis')/case['id']");b=t.index('            for iteration in range(1,10001):',a)
t=t[:a]+"""            for C in lex_clauses:sat.add_clause(C)
            if case['source']:
                old=Path(case['source'])
                for line in (old/'constraints.jsonl').read_text(encoding='utf-8').splitlines():
                    rec=json.loads(line)
                    if rec['kind']=='AS_loss':rec['certificate']=Path(os.path.relpath(old/rec['certificate'],D)).as_posix()
                    add(rec,False)
            else:
                for v in range(n):add(dict(kind='cut',vertices=[v],clause=[vid[e] for e in pairs if v in e]))
"""+t[b:]
t=t.replace('bootstrap_with=clauses,with_proof=True','bootstrap_with=clauses+lex_clauses,with_proof=True')
t=t.replace("(D/'formula.cnf').write_text(cnf,encoding='ascii',newline='\\n')","(D/'graph_formula.cnf').write_text(cnf,encoding='ascii',newline='\\n');(D/'formula.cnf').write_text(f'p cnf {variables} {len(clauses)+len(lex_clauses)}\\n'+''.join(' '.join(map(str,C))+' 0\\n' for C in clauses+lex_clauses),encoding='ascii',newline='\\n')")
t=t.replace('        def win(x):','        def raw_win(x):')
t=t.replace('        def history(x):',"""        depth=0;queried=None
        def win(x):
            nonlocal depth,queried
            if not depth:queried=x
            depth+=1
            try:return raw_win(x)
            except RuntimeError as error:
                if depth==1:(D/'oracle_cap.json').write_text(json.dumps(dict(status=str(error),queried_graph=sorted(E),queried_input=[(queried>>(8*i))&255 for i in range(n)],case_input=c,scope='UNKNOWN query, may be temporary support graph; no loss or criticality claim'))+'\\n',encoding='utf-8',newline='\\n')
                raise
            finally:depth-=1
        def history(x):""")
Path('tools/s014_lex_cegis.py').write_text(t,encoding='utf-8',newline='\n')
t=Path('tools/s014_lrat_verify.py').read_text(encoding='utf-8').replace("B=Path('evidence/S014/lrat');P=Path('evidence/S014/cegis_orbits_v2')","B=Path('evidence/S014/lex_lrat');P=Path('evidence/S014/lex_cegis')").replace("['all_clauses_necessary_for_fixed_input_counterexample']","['counterexample_exists_implies_formula_satisfiable']")
Path('tools/s014_lex_lrat_verify.py').write_text(t,encoding='utf-8',newline='\n')
plan=Path('sessions/S014/PLAN_AMENDMENT_47.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n')
files.extend([plan,B/'inputs.json',Path('evidence/S014/cegis/environment.json'),Path('research/S014_PROVED_GRAPH_SYMMETRY.md'),*Path('tools').glob('s014_lex*.py'),Path('tools/s014_cegis_orbits_v2.py'),Path('tools/s014_cegis_clauses_verify.py'),Path('tools/s014_lrat_verify.py'),Path('tools/s014_tail_screen_verify.py'),Path('tools/s009_checks.py')]);(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files},native_binary='C:/Earth-Moon-problem/artifacts/tmp/S004/drat-trim-mingw.exe',native_sha256='970caaea97a15c8a27d4747e0e92e058ac1b1d9d4e04a95e3fc58b069ed4c03e'),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM47 frozen five graph classes')
