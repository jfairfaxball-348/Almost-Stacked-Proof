import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/lrat');B.mkdir(exist_ok=True);P=Path('evidence/S014/cegis_orbits_v2');exe=Path('C:/Earth-Moon-problem/artifacts/tmp/S004/drat-trim-mingw.exe');digest='970caaea97a15c8a27d4747e0e92e058ac1b1d9d4e04a95e3fc58b069ed4c03e';assert hashlib.sha256(exe.read_bytes()).hexdigest()==digest
plan=Path('sessions/S014/PLAN_AMENDMENT_45.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n')
paths=[plan,Path(__file__),Path('tools/s014_lrat_verify.py'),Path('tools/s009_checks.py')]
for name in ['C6','C9a','C9b']:paths.extend([P/name/'formula.cnf',P/name/'proof.drup',P/name/'clause_verification.json'])
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},native_binary=str(exe),native_sha256=digest,official_source='https://github.com/marijnheule/drat-trim'),indent=2)+'\n',encoding='utf-8',newline='\n')
for name in sys.argv[1:]:
    D=B/name;D.mkdir(exist_ok=True);rows=[];native=run([str(exe),str(P/name/'formula.cnf'),str(P/name/'proof.drup'),'-L',str(D/'proof.lrat'),'-U','-t','540']);rows.append(native);(D/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:native[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
    assert hashlib.sha256(exe.read_bytes()).hexdigest()==digest
    if native['resource_failure'] or 's VERIFIED' not in native['stdout']:sys.exit(1)
    paths=[D/'proof.lrat',P/name/'formula.cnf',P/name/'proof.drup',P/name/'clause_verification.json',Path('tools/s014_lrat_verify.py')]
    (D/'derived_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}),indent=2)+'\n',encoding='utf-8',newline='\n')
    row=run([sys.executable,'tools/s014_lrat_verify.py',name]);rows.append(row);(D/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
    if row['exit_code'] or row['resource_failure']:sys.exit(1)
