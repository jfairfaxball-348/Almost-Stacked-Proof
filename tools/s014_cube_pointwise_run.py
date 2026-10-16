import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/cube_pointwise');shard=sys.argv[1];D=B/f'shard{shard}';D.mkdir(exist_ok=True);rows=[]
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
def job(args):
    r=run([sys.executable]+args);rows.append(r);(D/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:r[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True);assert not r['exit_code'] and not r['resource_failure']
job(['tools/s014_cube_pointwise_produce.py',shard]);files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in D.rglob('*') if p.is_file() and p.name not in ['checks.json','derived_preflight.json']};(D/'derived_preflight.json').write_text(json.dumps(dict(files=files),indent=2)+'\n',encoding='utf-8',newline='\n');job(['tools/s014_cube_pointwise_verify.py',shard]);v=json.loads((D/'verification.json').read_bytes())
for potential in v['potential']:
    O=Path(potential['path']);files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in O.rglob('*') if p.is_file() and p.name not in ['preflight.json','derived_preflight.json']};(O/'derived_preflight.json').write_text(json.dumps(dict(files=files),indent=2)+'\n',encoding='utf-8',newline='\n');(O/'preflight.json').write_bytes((B/'preflight.json').read_bytes());job(['tools/s014_cube_pointwise_potential_verify.py',O.as_posix()])
