import hashlib,json
from pathlib import Path
B=Path('evidence/S014/twofuel_cegis');V=Path('evidence/S014/twofuel_lrat')
def read(p):return json.loads(Path(p).read_bytes())
for p,h in read(B/'preflight.json')['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=read(B/'inputs.json');files=[B/'preflight.json',B/'inputs.json',Path(__file__)];out=[];certified=0
for case in cfg['cases']:
    D=B/case['id'];r=read(D/'result.json');c=read(D/'clause_verification.json');logs=read(D/'checks.json');assert r['case']==case and c['counterexample_exists_implies_formula_satisfiable']
    for log in logs:assert log['exit_code']==0 and log['resource_failure'] is None and log['seconds']<600 and log['peak_working_set_bytes']<=2*1024**3 and hashlib.sha256(Path(log['command'][1]).read_bytes()).hexdigest()==log['code_sha256']
    for p,h in read(D/'derived_preflight.json')['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    files.extend([D/'result.json',D/'clause_verification.json',D/'checks.json',D/'derived_preflight.json']);status=r['status']
    if status=='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE':
        proof=read(V/case['id']/'verification.json');assert proof['fixed_input_class_exclusion_certified'] and len(logs)==4 and 's VERIFIED' in logs[2]['stdout']
        for p,h in read(V/case['id']/'derived_preflight.json')['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
        files.extend([V/case['id']/'verification.json',V/case['id']/'derived_preflight.json']);status='INDEPENDENTLY_EXCLUDED';certified+=not case['control']
    else:assert status in ['ITERATION_BOUND_UNKNOWN','TIME_BOUND_UNKNOWN'] and len(logs)==2 and not case['control']
    if not case['control']:out.append(dict(case=case['id'],n=case['n'],c=case['c'],status=status,iterations=r['iterations']))
assert certified==1 and len(out)==4 and not (B/'STOP_FOR_POTENTIAL.json').exists()
pre=dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files});target=B/'summary_preflight.json';assert not target.exists() or read(target)==pre;target.write_text(json.dumps(pre,indent=2)+'\n',encoding='utf-8',newline='\n')
summary=dict(status='COMPLETE_REGISTERED_BOUNDED_CAMPAIGN',patterns=4,certified=1,unknown=3,control_pass=True,cases=out,verified_F8_RUP_additions=read(V/'F8'/'verification.json')['verified_RUP_additions'],scope='Only F8 fixed-input class excluded; F9/F10/F12 UNKNOWN; universal ASH* OPEN')
(B/'summary.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(summary))
