"""Fixed all-F bounded experiment; no failure is silently expanded."""
import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/buffers')
def main():
    for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    inp=json.loads((B/'threshold_inputs.json').read_bytes());first=run([sys.executable,'tools/s014_buffers_weights.py']);(B/'weights_checks.json').write_text(json.dumps([first],indent=2)+'\n',encoding='utf-8',newline='\n');assert first['exit_code']==0 and not first['resource_failure']
    results=[]
    for case in inp['cases']:
        g=case['graph'];goal=case['goal'];name=g['graph'];rows=[]
        for script in ['s014_buffers_threshold','s014_buffers_verify']:
            row=run([sys.executable,'tools/'+script+'.py',name,goal]);rows.append(row);(B/(name+'_'+goal+'_checks.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
            if row['exit_code'] or row['resource_failure']:print(json.dumps(row),flush=True);sys.exit(1)
        report=json.loads((B/(name+'_'+goal+'_threshold_verification.json')).read_bytes());results.append(report);(B/'summary.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(json.dumps(report),flush=True)
if __name__=='__main__':main()
