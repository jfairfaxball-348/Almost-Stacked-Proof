"""Bounded S012 final check-only replay with complete historical byte guard."""
import hashlib,json,sys
from pathlib import Path
from s009_checks import run

def main():
    names=['s012_reciprocity','s012_reciprocity_verify','s012_escape','s012_escape_verify','s012_exceptions','s012_exceptions_verify']
    before={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for i in range(3,12) for folder in [f'evidence/S{i:03d}',f'sessions/S{i:03d}'] for p in Path(folder).rglob('*') if p.is_file()}
    rows=[]
    for name in names:
        row=run([sys.executable,f'tools/{name}.py','--check-only']);rows.append(row)
        Path('evidence/S012/local_checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(json.dumps({k:v for k,v in row.items() if k not in ('stdout','stderr')}),flush=True)
        if row['exit_code'] or row['resource_failure']:print(row['stdout']);print(row['stderr']);sys.exit(1)
    assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in before.items())
    print('Six S012 checks PASS; all historical session/evidence bytes unchanged.',flush=True)
if __name__=='__main__':main()
