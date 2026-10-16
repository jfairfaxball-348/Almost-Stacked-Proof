import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/trace_cegis')
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
name='C10';D=B/name;D.mkdir(exist_ok=True);rows=[]
for script in ['s014_trace_cegis','s014_trace_cegis_verify','s014_trace_cegis_potential']:
    if script.endswith('_verify'):
        files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in D.rglob('*') if p.is_file() and p.name!='checks.json'};(D/'derived_preflight.json').write_text(json.dumps(dict(files=files),indent=2)+'\n',encoding='utf-8',newline='\n')
    if script.endswith('_potential') and json.loads((D/'result.json').read_bytes())['status']!='POTENTIAL_ACTUAL_COUNTEREXAMPLE':break
    row=run([sys.executable,'tools/'+script+'.py',name]);rows.append(row);(D/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
    if row['exit_code'] or row['resource_failure']:sys.exit(1)
