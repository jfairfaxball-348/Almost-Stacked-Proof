"""Preregistered independently supervised fourteen thresholds and path challenge."""
import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/matching')
def main():
    for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    inp=json.loads((B/'threshold_inputs.json').read_bytes())
    jobs=[(g['graph']+'_'+goal,['s014_matching_threshold','s014_matching_threshold_verify'],[g['graph'],goal]) for g in inp['graphs'] for goal in ['stack','clear']]
    jobs.append(('paths',['s014_matching','s014_matching_verify'],[]))
    for name,scripts,args in jobs:
        rows=[]
        for script in scripts:
            row=run([sys.executable,'tools/'+script+'.py']+args);rows.append(row);(B/(name+'_checks.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
            print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','peak_working_set_bytes','resource_failure','stderr']})+' '+row['stdout'].splitlines()[-1],flush=True)
            if row['exit_code'] or row['resource_failure']:sys.exit(1)
if __name__=='__main__':main()
