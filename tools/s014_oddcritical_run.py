import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/oddcritical')
def main():
    for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    rows=[]
    for case in json.loads((B/'inputs.json').read_bytes())['cases']:
        for script in ['s014_oddcritical','s014_oddcritical_verify']:
            row=run([sys.executable,'tools/'+script+'.py',case['graph']['graph'],'stack']);rows.append(row);(B/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
            print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','resource_failure','stderr']}),flush=True)
            if row['exit_code'] or row['resource_failure']:sys.exit(1)
if __name__=='__main__':main()
