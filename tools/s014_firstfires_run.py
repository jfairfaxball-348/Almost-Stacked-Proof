import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/firstfires')
def main():
    for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    jobs=[('boundary',['s014_firstfires','s014_firstfires_verify'],[])]
    for c in json.loads((B/'threshold_inputs.json').read_bytes())['cases']:jobs.append((c['graph']['graph'],['s014_boundary_threshold','s014_boundary_threshold_verify'],[c['graph']['graph'],'clear']))
    jobs.append(('witnesses',['s014_boundary_witnesses'],[]))
    for name,scripts,args in jobs:
        rows=[]
        for script in scripts:
            row=run([sys.executable,'tools/'+script+'.py']+args);rows.append(row);(B/(name+'_checks.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','peak_working_set_bytes','resource_failure','stderr']})+' '+(row['stdout'].splitlines()[-1] if row['stdout'] else ''),flush=True)
            if row['exit_code'] or row['resource_failure']:sys.exit(1)
if __name__=='__main__':main()
