import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/mass11_cegis');V=Path('evidence/S014/mass11_lrat');V.mkdir(exist_ok=True);pre=json.loads((B/'preflight.json').read_bytes())
for p,h in pre['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
exe=pre['native_binary'];assert hashlib.sha256(Path(exe).read_bytes()).hexdigest()==pre['native_sha256'];mode=sys.argv[1];assert mode in ['control','0','1'];cases=json.loads((B/'inputs.json').read_bytes())['cases']
if mode=='control':chosen=[c for c in cases if c['control']]
else:
    assert json.loads((V/'control2'/'verification.json').read_bytes())['fixed_input_class_exclusion_certified'];chosen=[c for i,c in enumerate([c for c in cases if not c['control']]) if i%2==int(mode)]
for case in chosen:
    if (B/'STOP_FOR_POTENTIAL.json').exists():break
    name=case['id'];D=B/name;D.mkdir(exist_ok=True);rows=[]
    for script in ['s014_c068_cegis','s014_c068_verify']:
        if script.endswith('_verify'):
            files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in D.rglob('*') if p.is_file() and p.name!='checks.json'};(D/'derived_preflight.json').write_text(json.dumps(dict(files=files),indent=2)+'\n',encoding='utf-8',newline='\n')
        row=run([sys.executable,'tools/'+script+'.py',name]);rows.append(row);(D/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
        if row['exit_code'] or row['resource_failure']:sys.exit(1)
    status=json.loads((D/'result.json').read_bytes())['status']
    if status=='POTENTIAL_ACTUAL_COUNTEREXAMPLE':
        (B/'STOP_FOR_POTENTIAL.json').write_text(json.dumps(dict(case=name))+'\n',encoding='utf-8',newline='\n');row=run([sys.executable,'tools/s014_c068_potential.py',name]);rows.append(row);(D/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True);break
    if status!='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE':continue
    O=V/name;O.mkdir(exist_ok=True);row=run([exe,str(D/'formula.cnf'),str(D/'proof.drup'),'-L',str(O/'proof.lrat'),'-U','-t','540']);rows.append(row);(D/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
    assert hashlib.sha256(Path(exe).read_bytes()).hexdigest()==pre['native_sha256']
    if row['resource_failure'] or 's VERIFIED' not in row['stdout']:sys.exit(1)
    files=[O/'proof.lrat',D/'formula.cnf',D/'proof.drup',D/'clause_verification.json',Path('tools/s014_c068_lrat_verify.py')];(O/'derived_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n')
    row=run([sys.executable,'tools/s014_c068_lrat_verify.py',name]);rows.append(row);(D/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
    if row['exit_code'] or row['resource_failure']:sys.exit(1)
