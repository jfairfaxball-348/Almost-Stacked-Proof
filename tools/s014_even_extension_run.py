import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/even_extension')
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
rows=[]
for script in ['s014_even_extension','s014_even_extension_verify']:
    if script.endswith('_verify'):
        p=B/'results.json';(B/'derived_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest()}),indent=2)+'\n',encoding='utf-8',newline='\n')
    row=run([sys.executable,'tools/'+script+'.py']);rows.append(row);(B/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
    if row['exit_code'] or row['resource_failure']:sys.exit(1)
