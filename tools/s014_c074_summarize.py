"""Aggregate the registered finite cases; do not extend any old state cap."""
import hashlib,json
from pathlib import Path
B=Path('evidence/S014/bip_odd_larger')
def read(p):return json.loads(Path(p).read_bytes())
for p,h in read(B/'preflight.json')['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=read(B/'inputs.json');shards=read(B/'shard0_summary.json')+read(B/'shard1_summary.json');by={r['case']:r for r in shards};assert len(by)==len(shards)==len(cfg['cases'])==21
files=[B/'preflight.json',B/'inputs.json',B/'shard0_summary.json',B/'shard1_summary.json',Path(__file__)];complete=[];unknown=[]
for case,inv in zip(cfg['cases'],cfg['inventory']):
    r=by[case['id']]
    if inv['status']!='READY':assert r==inv and r['status']=='PRIOR_SCOPE_CUTOFF_UNKNOWN';unknown.append(r);continue
    D=B/case['id'];v=read(D/'verification.json');checks=read(D/'checks.json');assert len(checks)==2 and v['status']=='COMPLETE_REGISTERED_CASES' and v['complete_tested_prefix_verified'] and v['failed_inputs']==0
    assert r['status']==v['status'] and r['inputs']==v['inputs'] and r['failed']==0
    for check in checks:assert check['exit_code']==0 and check['resource_failure'] is None and check['seconds']<600 and check['peak_working_set_bytes']<=2*1024**3 and hashlib.sha256(Path(check['command'][1]).read_bytes()).hexdigest()==check['code_sha256']
    for p,h in read(D/'derived_preflight.json')['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    files.extend([D/'verification.json',D/'checks.json',D/'derived_preflight.json']);complete.append(dict(case=case['id'],n=case['n'],inputs=v['inputs'],states=v['states'],failed_inputs=v['failed_inputs']))
assert len(complete)==18 and len(unknown)==3
pre=dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files});target=B/'summary_preflight.json';assert not target.exists() or read(target)==pre;target.write_text(json.dumps(pre,indent=2)+'\n',encoding='utf-8',newline='\n')
report=dict(status='COMPLETE_REGISTERED_18_EXECUTED_PLUS_3_PRIOR_SCOPE_UNKNOWN',cases=21,independently_completed_cases=18,prior_scope_unknown_cases=3,inputs=sum(r['inputs'] for r in complete),states=sum(r['states'] for r in complete),maximum_order=max(r['n'] for r in complete),failed_inputs=0,completed=complete,unknown=unknown,scope='Finite selected cases only; B_odd and universal ASH* OPEN')
(B/'summary.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in report.items() if k not in ['completed','unknown']}))
