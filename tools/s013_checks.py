"""Final bounded twelve check-only replays with complete historical-byte guard."""
import hashlib,json,sys
from pathlib import Path
from s009_checks import run
def main():
    names=[f's013_{n}{suffix}' for n in ['gap_scan','precision','concentration','full_exchange','residual','synthesis'] for suffix in ['','_verify']]
    before={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for i in range(3,13) for folder in [f'evidence/S{i:03d}',f'sessions/S{i:03d}'] for p in Path(folder).rglob('*') if p.is_file()}
    rows=[]
    for n in names:
        r=run([sys.executable,f'tools/{n}.py','--check-only']);rows.append(r)
        Path('evidence/S013/local_checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(json.dumps({k:r[k] for k in ['command','exit_code','seconds','peak_working_set_bytes','resource_failure']}),flush=True)
        if r['exit_code'] or r['resource_failure']:print(r['stdout']);print(r['stderr']);sys.exit(1)
    assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in before.items())
    print('Twelve new checks PASS; historical evidence/session bytes unchanged.',flush=True)
if __name__=='__main__':main()
