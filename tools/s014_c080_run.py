import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/odd_leaf_contraction');rows=[]
for suffix in ['produce','verify']:
    if suffix=='verify':
        cfg=json.loads((B/'result.json').read_bytes());files=[B/'result.json',*[Path(c['file']) for c in cfg['cases']]];(B/'derived_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n')
    r=run([sys.executable,f'tools/s014_c080_{suffix}.py']);rows.append(r);(B/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(r),flush=True)
    if r['exit_code'] or r['resource_failure']:sys.exit(1)
