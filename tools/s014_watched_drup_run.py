import hashlib,json,sys
from pathlib import Path
from s009_checks import run
V=Path('evidence/S014/watched_drup');V.mkdir(exist_ok=True)
plan=Path('sessions/S014/PLAN_AMENDMENT_42.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n')
paths=[plan,Path(__file__),Path('tools/s014_watched_drup.py'),Path('tools/s009_checks.py')]
preflight=V/'preflight.json'
if not preflight.exists():preflight.write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}),indent=2)+'\n',encoding='utf-8',newline='\n')
for p,h in json.loads(preflight.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
for pair in sys.argv[1:]:
    directory,label=pair.split('=');row=run([sys.executable,'tools/s014_watched_drup.py',directory,label]);(V/('checks_'+label+'.json')).write_text(json.dumps([row],indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
    if row['exit_code'] or row['resource_failure']:sys.exit(1)
