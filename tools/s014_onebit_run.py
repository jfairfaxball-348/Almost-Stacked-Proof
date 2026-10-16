import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/onebit');shard=sys.argv[1];D=B/f'shard{shard}';D.mkdir(exist_ok=True)
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
rows=[]
for mode in ['produce','verify']:
    if mode=='verify':
        files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in D.rglob('*') if p.is_file() and p.name!='derived_preflight.json'};(D/'derived_preflight.json').write_text(json.dumps(dict(files=files),indent=2)+'\n',encoding='utf-8',newline='\n')
    r=run([sys.executable,'tools/s014_onebit_'+mode+'.py',shard]);rows.append(r);(B/f'shard{shard}_checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:r[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
    if r['exit_code'] or r['resource_failure']:sys.exit(1)
