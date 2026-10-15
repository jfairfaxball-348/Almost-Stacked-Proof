"""Sequential bounded check-only replay; writes only new S011 logs."""
import hashlib
import json
import sys
from pathlib import Path
from s009_checks import run

def main():
    names=['s010_counts','s010_counts_verify','s010_roots','s010_roots_verify','s010_reflect','s010_reflect_verify',
        's009_ports','s009_ports_verify','s009_credit','s009_credit_verify',
        's004_cold','s004_structure','s004_witness_tests','s005_pure','s005_check_traces',
        's006_verify','s006_stack_verify','s006_challenges','s006_extrema','s006_obstruction_verify',
        's007_tail_verify','s007_tail_verify --stack','s008_tip_verify','s008_symbolic','s008_branches_verify']
    before={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for folder in ['evidence/S010','sessions/S010'] for p in Path(folder).rglob('*') if p.is_file()}
    rows=[]
    for name in names:
        words=name.split();cmd=[sys.executable,'tools/'+words[0]+'.py','--check-only']+words[1:]
        row=run(cmd);rows.append(row)
        Path('evidence/S011/cold_checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(json.dumps({k:v for k,v in row.items() if k not in ('stdout','stderr')}),flush=True)
        if row['exit_code'] or row['resource_failure']:
            print(row['stdout']);print(row['stderr']);sys.exit(1)
    assert all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in before.items())
    print('All25 checks passed; historical S010 bytes unchanged.',flush=True)

if __name__=='__main__':main()
