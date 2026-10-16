import hashlib,json,sys
from pathlib import Path
from s009_checks import run
V=Path('evidence/S014/indexed_drup');V.mkdir(exist_ok=True)
plan=Path('sessions/S014/PLAN_AMENDMENT_39.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n')
files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in [plan,Path(__file__),Path('tools/s014_indexed_drup.py'),Path('tools/s009_checks.py')]}
(V/'preflight.json').write_text(json.dumps(dict(files=files),indent=2)+'\n',encoding='utf-8',newline='\n')
rows=[]
for name in sys.argv[1:]:
    row=run([sys.executable,'tools/s014_indexed_drup.py',name]);rows.append(row);(V/('checks_'+name+'.json')).write_text(json.dumps([row],indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
    if row['exit_code'] or row['resource_failure']:sys.exit(1)
