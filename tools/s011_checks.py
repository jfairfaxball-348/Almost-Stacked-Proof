"""Bounded read-only replay of all six S011 mathematical producer/checkers."""
import json,sys
from pathlib import Path
from s009_checks import run

def main():
    scripts=['s011_trees','s011_trees_verify','s011_transport','s011_transport_verify','s011_root_types','s011_root_types_verify'];rows=[]
    for name in scripts:
        row=run([sys.executable,f'tools/{name}.py','--check-only']);rows.append(row)
        Path('evidence/S011/local_checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(json.dumps({k:v for k,v in row.items() if k not in ('stdout','stderr')}),flush=True)
        if row['exit_code'] or row['resource_failure']:print(row['stdout']);print(row['stderr']);sys.exit(1)

if __name__=='__main__':main()
