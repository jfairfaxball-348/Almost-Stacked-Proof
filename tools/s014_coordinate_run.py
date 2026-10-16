import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/coordinate_maximal')
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
rows=[]
def job(args):
    row=run([sys.executable]+args);rows.append(row);(B/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True);assert not row['exit_code'] and not row['resource_failure']
for case in json.loads((B/'inputs.json').read_bytes())['cases']:
    for mode in ['produce','verify']:job(['tools/s014_coordinate_job.py',case['graph']['graph'],mode])
job(['tools/s014_coordinate_analysis.py'])
files=[p for p in B.rglob('*') if p.is_file() and p.name not in ['checks.json','analysis_preflight.json']];(B/'analysis_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n')
job(['tools/s014_coordinate_verify.py'])
