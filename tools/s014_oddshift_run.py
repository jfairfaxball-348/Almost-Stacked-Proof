import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/oddshift')
def main():
    for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    for p,h in json.loads(Path('evidence/S014/parity_archive/inputs.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    rows=[]
    for script in ['s014_oddshift','s014_oddshift_verify']:
        row=run([sys.executable,'tools/'+script+'.py']);rows.append(row);(B/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','peak_working_set_bytes','resource_failure','stdout','stderr']}),flush=True)
        if row['exit_code'] or row['resource_failure']:sys.exit(1)
if __name__=='__main__':main()
