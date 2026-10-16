import hashlib,json,sys,time
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/circulant')
def main():
    for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    inputs=json.loads((B/'inputs.json').read_bytes())['cases'];start=time.monotonic();summary=[]
    for case in inputs:
        name=case['graph']['graph'];logs=[];failed=False
        if time.monotonic()-start>=7200:break
        for mode in ['produce','verify']:
            row=run([sys.executable,'tools/s014_circulant_job.py',name,mode]);logs.append(row);(B/(name+'_checks.json')).write_text(json.dumps(logs,indent=2)+'\n',encoding='utf-8',newline='\n')
            if row['exit_code'] or row['resource_failure']:failed=True;break
        if failed:summary.append(dict(graph=name,status='PROCESS_CUTOFF_OR_FAILURE_UNKNOWN'))
        else:
            result=json.loads((B/(name+'_stack_threshold_verification.json')).read_bytes());summary.append(result)
            if result['threshold'] is not None and result['L_AS_exact']<result['threshold']-1:
                (B/'POTENTIAL_COUNTEREXAMPLE.json').write_text(json.dumps(dict(case=case,verification=result),indent=2)+'\n',encoding='utf-8',newline='\n');print('POTENTIAL_COUNTEREXAMPLE '+name,flush=True);break
        (B/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(graph=name,status=summary[-1].get('scope',summary[-1].get('status')),threshold=summary[-1].get('threshold'))),flush=True)
    (B/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':main()
