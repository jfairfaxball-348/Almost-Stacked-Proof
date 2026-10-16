import hashlib,itertools,json
from pathlib import Path
B=Path('evidence/S014/trace_cegis');B.mkdir(exist_ok=True);cfg=json.loads(Path('evidence/S014/cegis/inputs.json').read_bytes());case=next(c for c in cfg['cases'] if c['id']=='C10');c=case['c'];n=case['n'];groups=[[i for i,z in enumerate(c) if z==v] for v in sorted(set(c))];ps=[]
for rev in [False,True]:
    for shifts in itertools.product(*(range(len(g)) for g in groups)):
        p=list(range(n))
        for g,k in zip(groups,shifts):
            for j,u in enumerate(g):p[u]=g[((-j if rev else j)+k)%len(g)]
        if p not in ps:ps.append(p)
case['permutations']=ps;cfg['cases']=[case];(B/'inputs.json').write_text(json.dumps(cfg,indent=2)+'\n',encoding='utf-8',newline='\n')
t=Path('tools/s014_cegis_orbits_v2.py').read_text(encoding='utf-8').replace("B=Path('evidence/S014/cegis_orbits_v2')","B=Path('evidence/S014/trace_cegis')")
t=t.replace("            for line in (old/'constraints.jsonl').read_text(encoding='utf-8').splitlines():", "            minimized_cache={}\n            for line in (old/'constraints.jsonl').read_text(encoding='utf-8').splitlines():")
t=t.replace("                add(rec,False)","""                if rec['kind']=='c_win':
                    support={tuple(sorted((u,v))) for u,v in rec['moves']};key=frozenset(support)
                    if key in minimized_cache:moves=minimized_cache[key]
                    else:
                        aa,mm,ww,hh=oracle(support);assert ww(root);moves=hh(root)
                        for e in sorted(support.copy()):
                            if time.monotonic()-start>540:raise RuntimeError('TIME_BOUND_UNKNOWN')
                            if e not in support:continue
                            aa,mm,ww,hh=oracle(support-{e})
                            if ww(root):moves=hh(root);support={tuple(sorted((u,v))) for u,v in moves}
                        minimized_cache[key]=moves
                    rec['moves']=moves;rec['clause']=sorted({-vid[tuple(sorted((u,v)))] for u,v in moves})
                add(rec,False)""")
t=t.replace("['ORACLE_STATE_CAP_UNKNOWN','CLAUSE_CAP_UNKNOWN']","['ORACLE_STATE_CAP_UNKNOWN','CLAUSE_CAP_UNKNOWN','TIME_BOUND_UNKNOWN']")
Path('tools/s014_trace_cegis.py').write_text(t,encoding='utf-8',newline='\n')
t=Path('tools/s014_cegis_orbits_verify_v2.py').read_text(encoding='utf-8').replace("B=Path('evidence/S014/cegis_orbits_v2')","B=Path('evidence/S014/trace_cegis')")
Path('tools/s014_trace_cegis_verify.py').write_text(t,encoding='utf-8',newline='\n')
plan=Path('sessions/S014/PLAN_AMENDMENT_43.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n')
paths=[plan,B/'inputs.json',Path('evidence/S014/cegis/environment.json'),*Path('tools').glob('*trace_cegis*.py'),Path('tools/s014_cegis_orbits_v2.py'),Path('tools/s014_cegis_clauses_verify.py'),Path('tools/s014_cegis_orbits_verify_v2.py'),Path('tools/s014_watched_drup.py'),Path('tools/s014_watched_drup_run.py'),Path('tools/s014_tail_screen_verify.py'),Path('tools/s009_checks.py'),*Path('evidence/S014/cegis/C10').rglob('*')]
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths if p.is_file()}),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM43 frozen',len(ps),'permutations')
