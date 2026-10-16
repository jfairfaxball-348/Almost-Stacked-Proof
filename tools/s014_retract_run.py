import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/retract_trees')
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
mode=sys.argv[1];rows=[]
for phase in ['produce','verify']:
    if mode=='trees' and phase=='verify':
        files=[B/'trees.json'];(B/'trees_derived_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n')
    cmd=[sys.executable,'tools/s014_retract_'+phase+'.py'] if mode=='trees' else [sys.executable,'tools/s014_retract_job.py',phase]
    r=run(cmd);rows.append(r);(B/(mode+'_checks.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:r[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
    if r['exit_code'] or r['resource_failure']:sys.exit(1)
