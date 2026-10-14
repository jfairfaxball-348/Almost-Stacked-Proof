"""Sequential inherited check-only replay, historical bytes untouched."""
import json
import sys
from pathlib import Path
from s009_checks import run

def main():
    commands = ['s009_ports','s009_ports_verify','s009_credit','s009_credit_verify',
                's004_cold','s004_structure','s004_witness_tests','s005_pure','s005_check_traces',
                's006_verify','s006_stack_verify','s006_challenges','s006_extrema','s006_obstruction_verify',
                's007_tail_verify','s007_tail_verify --stack','s008_tip_verify','s008_symbolic','s008_branches_verify']
    rows=[]
    dest=Path('evidence/S010/cold_checks.json')
    for name in commands:
        words=name.split(); cmd=[sys.executable,'tools/'+words[0]+'.py','--check-only']+words[1:]
        row=run(cmd); rows.append(row)
        dest.write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(json.dumps({k:v for k,v in row.items() if k not in ('stdout','stderr')}),flush=True)
        if row['exit_code']!=0: print(row['stderr'],flush=True);sys.exit(1)
    assert sum(r['seconds'] for r in rows)<1800

if __name__=='__main__':main()
