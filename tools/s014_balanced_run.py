"""Fourteen separately capped exact source cases, with preflight/import hashes."""
import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/balanced')
def main():
    for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    for case in json.loads((B/'ray_inputs.json').read_bytes())['cases']:
        rows=[];ident=case['id']
        for script in ['s014_balanced_rays','s014_balanced_verify']:
            result=run([sys.executable,'tools/'+script+'.py',ident]);rows.append(result);(B/(ident+'_checks.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
            print(json.dumps({k:result[k] for k in ['command','exit_code','seconds','peak_working_set_bytes','resource_failure','stdout','stderr']}),flush=True)
            if result['exit_code'] or result['resource_failure']:sys.exit(1)
if __name__=='__main__':main()
