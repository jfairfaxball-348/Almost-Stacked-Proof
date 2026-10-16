import hashlib,json
from pathlib import Path
B=Path('evidence/S014/continued_cegis');B.mkdir(exist_ok=True);cases=[];files=[]
for name in ['C10','E9','E10','M10','F9','T10','T12']:
    old=Path('evidence/S014')/('trace_cegis' if name=='C10' else 'even_cegis');cfg=json.loads((old/'inputs.json').read_bytes());case=next(c for c in cfg['cases'] if c['id']==name).copy();case['source']=(old/name).as_posix();cases.append(case);files.append(old/'inputs.json');files.extend(p for p in (old/name).rglob('*') if p.is_file())
cfg['cases']=cases;(B/'inputs.json').write_text(json.dumps(cfg,indent=2)+'\n',encoding='utf-8',newline='\n')
t=Path('tools/s014_cegis_orbits_v2.py').read_text(encoding='utf-8').replace("B=Path('evidence/S014/cegis_orbits_v2')","B=Path('evidence/S014/continued_cegis')").replace("old=Path('evidence/S014/cegis')/case['id']","old=Path(case['source'])").replace('range(1,1001)','range(1,3001)')
anchor="    (D/'constraints.jsonl').write_text"
assert anchor in t
t=t.replace(anchor,"""    if status=='CLAUSE_CAP_UNKNOWN' and time.monotonic()-start<530:
        with Glucose3(bootstrap_with=clauses,with_proof=True) as final:
            if not final.solve():
                proof=final.get_proof();(D/'proof.drup').write_text('\\n'.join(proof)+'\\n',encoding='ascii',newline='\\n');status='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE' if len(proof)<=500000 else 'PROOF_SIZE_BOUND_UNKNOWN'
"""+anchor)
Path('tools/s014_continued_cegis.py').write_text(t,encoding='utf-8',newline='\n')
t=Path('tools/s014_cegis_orbits_verify_v2.py').read_text(encoding='utf-8').replace("B=Path('evidence/S014/cegis_orbits_v2')","B=Path('evidence/S014/continued_cegis')");Path('tools/s014_continued_cegis_verify.py').write_text(t,encoding='utf-8',newline='\n')
plan=Path('sessions/S014/PLAN_AMENDMENT_46.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n')
files.extend([plan,B/'inputs.json',Path('evidence/S014/cegis/environment.json'),*Path('tools').glob('s014_continued*.py'),Path('tools/s014_cegis_orbits_v2.py'),Path('tools/s014_cegis_clauses_verify.py'),Path('tools/s014_cegis_orbits_verify_v2.py'),Path('tools/s014_lrat_verify.py'),Path('tools/s014_tail_screen_verify.py'),Path('tools/s009_checks.py')])
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files},native_binary='C:/Earth-Moon-problem/artifacts/tmp/S004/drat-trim-mingw.exe',native_sha256='970caaea97a15c8a27d4747e0e92e058ac1b1d9d4e04a95e3fc58b069ed4c03e'),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM46 frozen',len(cases),'fixed-input classes')
