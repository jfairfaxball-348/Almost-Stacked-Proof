import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/shell_witness');rows=[]
for tool in ['produce','verify']:
    if tool=='verify':
        files=[B/'result.json',*B.glob('query*.bin.gz')];(B/'derived_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n')
    row=run([sys.executable,f'tools/s014_c067_{tool}.py']);rows.append(row);(B/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(row),flush=True)
    if row['exit_code'] or row['resource_failure']:sys.exit(1)
