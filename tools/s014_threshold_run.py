"""Four separately capped precision threshold cases; preserve actual UNKNOWN."""
import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014')
def main():
    pre=json.loads((B/'threshold_preflight.json').read_bytes())
    for p,h in pre['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    inp=json.loads((B/'threshold_inputs.json').read_bytes())
    for p,h in inp['source_certificate_hashes'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    for case in inp['cases']:
        name=case['graph']['graph'];goal=case['goal'];rows=[]
        print('START '+name+' '+goal,flush=True)
        for script in ['s014_threshold','s014_threshold_verify']:
            result=run([sys.executable,'tools/'+script+'.py',name,goal]);rows.append(result)
            (B/(name+'_'+goal+'_threshold_checks.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
            print(json.dumps({k:result[k] for k in ['command','exit_code','seconds','peak_working_set_bytes','resource_failure','stdout','stderr']}),flush=True)
            if result['exit_code'] or result['resource_failure']:sys.exit(1)
if __name__=='__main__':main()
