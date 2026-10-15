"""Bounded S012 cold checks, historical bytes preserved."""
import hashlib,json,sys
from pathlib import Path
from s009_checks import run

def main():
    names=['s011_trees','s011_trees_verify','s011_transport','s011_transport_verify','s011_root_types','s011_root_types_verify','s010_counts','s010_counts_verify','s010_reflect','s010_reflect_verify','s010_roots','s010_roots_verify']
    before={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for folder in ['evidence/S011','sessions/S011'] for p in Path(folder).rglob('*') if p.is_file()}
    rows=[]
    for name in names:
        row=run([sys.executable,f'tools/{name}.py','--check-only']);rows.append(row)
        Path('evidence/S012/cold_checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(json.dumps({k:v for k,v in row.items() if k not in ('stdout','stderr')}),flush=True)
        if row['exit_code'] or row['resource_failure']:print(row['stdout']);print(row['stderr']);sys.exit(1)
    assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in before.items())
    print('All12 checks passed; S011 bytes unchanged.',flush=True)
if __name__=='__main__':main()
