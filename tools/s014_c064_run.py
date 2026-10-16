import gzip,hashlib,json,struct,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/cube_layers_full');cfg=json.loads((B/'inputs.json').read_bytes());mode=sys.argv[1]
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
if mode=='build':
    r=run([cfg['powershell'],'tools/s014_c064_build.ps1']);(B/'build_checks.json').write_text(json.dumps([r],indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(r),flush=True)
    if r['exit_code'] or r['resource_failure']:sys.exit(1)
    files=[B/'producer.dll',B/'build_checks.json',B/'preflight.json',Path('tools/s014_c064_layer.cs'),Path('tools/s014_c064_job.ps1'),Path(cfg['powershell'])];(B/'binary_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');sys.exit(0)
for p,h in json.loads((B/'binary_preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
if mode=='control':dimensions=[1,3]
else:
    assert mode=='4' and json.loads((B/'control_summary.json').read_bytes())['both_controls_pass'];dimensions=[4]
summaries=[]
for d in dimensions:
    D=B/f'd{d}';D.mkdir(exist_ok=True);threshold=None;status='COMPLETE_TO_BOUND';last=0
    for mass in range(1,cfg['max_mass'][str(d)]+1):
        stem=D/f'mass{mass}';rows=[];files=[B/'inputs.json',B/'producer.dll',Path('tools/s014_c064_layer.cs'),Path('tools/s014_c064_job.ps1')]
        if mass>1:files.extend([D/f'mass{mass-1}.bin.gz',D/f'mass{mass-1}_verification.json'])
        Path(str(stem)+'_input_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n')
        r=run([cfg['powershell'],'tools/s014_c064_job.ps1',str(d),str(mass)]);rows.append(r);Path(str(stem)+'_checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:r[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
        if r['exit_code'] or r['resource_failure']:status='PROCESS_CUTOFF_OR_FAILURE_UNKNOWN';break
        report=json.loads(stem.with_suffix('.json').read_bytes())
        if report['status']!='COMPLETE_LAYER':status=report['status'];break
        files=[stem.with_suffix('.json'),D/report['certificate'],Path('tools/s014_c064_verify.py')];Path(str(stem)+'_derived_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n')
        r=run([sys.executable,'tools/s014_c064_verify.py',str(d),str(mass)]);rows.append(r);Path(str(stem)+'_checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:r[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
        if r['exit_code'] or r['resource_failure']:status='CHECKER_PROCESS_CUTOFF_OR_FAILURE_UNKNOWN';break
        verified=json.loads(Path(str(stem)+'_verification.json').read_bytes())
        if not verified['all_full_orbit_losing_sets_equal']:status=verified['status'];break
        last=mass
        if mass>(1<<d) and report['losers']==0:threshold=mass;status='EXACT_THRESHOLD';break
        if d==4 and mass==31 and report['losers']:
            with gzip.open(D/report['certificate'],'rb') as f:header=f.read(12);c=list(f.read(16))
            potential=dict(n=16,edges=[[u,u^(1<<j)] for u in range(16) for j in range(4) if u<(u^(1<<j))],c=c,mass=31,exact_AS_maximum=30,scope='Potential universal counterexample awaiting fresh cold audit');(B/'POTENTIAL_COUNTEREXAMPLE.json').write_text(json.dumps(potential,indent=2)+'\n',encoding='utf-8',newline='\n');status='POTENTIAL_ACTUAL_COUNTEREXAMPLE';break
    result=dict(dimension=d,status=status,threshold=threshold,last_verified_mass=last);summaries.append(result);(B/f'd{d}_summary.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    if mode=='control' and (status!='EXACT_THRESHOLD' or threshold!=cfg['controls'][str(d)]):break
if mode=='control':
    ok=len(summaries)==2 and all(r['status']=='EXACT_THRESHOLD' and r['threshold']==cfg['controls'][str(r['dimension'])] for r in summaries);(B/'control_summary.json').write_text(json.dumps(dict(both_controls_pass=ok,controls=summaries),indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(summaries),flush=True)
