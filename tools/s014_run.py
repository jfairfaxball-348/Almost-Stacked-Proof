"""Bounded S014 producer/checker runner; new logs only."""
import hashlib,json,sys
from pathlib import Path
from s009_checks import run

def main():
    name=sys.argv[1];out=Path('evidence/S014')/(name+('_replay.json' if '--check-only' in sys.argv else '_checks.json'))
    scripts=[f'tools/s014_{name}.py',f'tools/s014_{name}_verify.py']
    plan=Path('sessions/S014/PLAN_AMENDMENT_'+sys.argv[2]+'.md')
    assert plan.with_suffix('.sha256').read_text().split()[0]==hashlib.sha256(plan.read_bytes()).hexdigest()
    rows=[]
    for script in scripts:
        row=run([sys.executable,script]+sys.argv[3:]);rows.append(row)
        out.write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','peak_working_set_bytes','resource_failure','stdout','stderr']}),flush=True)
        if row['exit_code'] or row['resource_failure']:sys.exit(1)
if __name__=='__main__':main()
