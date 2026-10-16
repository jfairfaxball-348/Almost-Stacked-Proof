"""Eight independently capped book-star producer/checker precision cases."""
import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/book_family')
def main():
    for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    for case in json.loads((B/'threshold_inputs.json').read_bytes())['cases']:
        name=case['graph']['graph'];goal=case['goal'];rows=[]
        for script in ['s014_book_threshold','s014_book_verify']:
            result=run([sys.executable,'tools/'+script+'.py',name,goal]);rows.append(result);(B/(name+'_'+goal+'_checks.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
            print(json.dumps({k:result[k] for k in ['command','exit_code','seconds','peak_working_set_bytes','resource_failure','stderr']})+' '+result['stdout'].splitlines()[-1],flush=True)
            if result['exit_code'] or result['resource_failure']:sys.exit(1)
if __name__=='__main__':main()
