import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/cube_general');rows=[]
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
for phase in ['produce','verify']:
    if phase=='verify':
        files=[B/'states.bin.xz',B/'anchors.bin.xz',B/'results.json',B/'result.json'];(B/'derived_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n')
    r=run([sys.executable,'tools/s014_cube_general_'+phase+'.py']);rows.append(r);(B/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:r[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
    if r['exit_code'] or r['resource_failure']:sys.exit(1)
