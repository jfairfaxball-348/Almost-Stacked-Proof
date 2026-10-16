import gzip,hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/fano_layers');cfg=json.loads((B/'inputs.json').read_bytes());mode=sys.argv[1]
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
if mode=='build':
    r=run([cfg['powershell'],'tools/s014_c066_build.ps1']);(B/'build_checks.json').write_text(json.dumps([r],indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(r),flush=True)
    if r['exit_code'] or r['resource_failure']:sys.exit(1)
    files=[B/'producer.dll',B/'build_checks.json',B/'preflight.json',Path('tools/s014_c066_layer.cs'),Path('tools/s014_c066_job.ps1'),Path(cfg['powershell'])];(B/'binary_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');sys.exit(0)
for p,h in json.loads((B/'binary_preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
if mode=='control':chosen=[c for c in cfg['cases'] if c['control']]
else:assert mode=='main' and json.loads((B/'control_summary.json').read_bytes())['both_controls_pass'];chosen=[c for c in cfg['cases'] if not c['control']]
summaries=[]
for case in chosen:
    name=case['id'];D=B/name;D.mkdir(exist_ok=True);threshold=None;status='COMPLETE_TO_BOUND';last=0
    for mass in range(1,case['max_mass']+1):
        stem=D/f'mass{mass}';rows=[];files=[B/'inputs.json',B/'producer.dll',Path('tools/s014_c066_layer.cs'),Path('tools/s014_c066_job.ps1')]
        if mass>1:files.extend([D/f'mass{mass-1}.bin.gz',D/f'mass{mass-1}_verification.json'])
        Path(str(stem)+'_input_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n')
        for phase in ['produce','verify']:
            if phase=='verify':
                r0=json.loads(stem.with_suffix('.json').read_bytes())
                if r0['status']!='COMPLETE_LAYER':status=r0['status'];break
                files=[stem.with_suffix('.json'),D/r0['certificate'],Path('tools/s014_c066_verify.py')];Path(str(stem)+'_derived_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n')
            cmd=[cfg['powershell'],'tools/s014_c066_job.ps1',name,str(mass)] if phase=='produce' else [sys.executable,'tools/s014_c066_verify.py',name,str(mass)];r=run(cmd);rows.append(r);Path(str(stem)+'_checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:r[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
            if r['exit_code'] or r['resource_failure']:status='PROCESS_CUTOFF_OR_FAILURE_UNKNOWN';break
        if status not in ['COMPLETE_TO_BOUND']:break
        verified=json.loads(Path(str(stem)+'_verification.json').read_bytes())
        if not verified['all_full_orbit_losing_sets_equal']:status=verified['status'];break
        last=mass
        if mass>case['n'] and verified['loser_orbits']==0:threshold=mass;status='EXACT_THRESHOLD';break
        if not case['control'] and mass==case['max_mass'] and verified['loser_orbits']:
            with gzip.open(D/f'mass{mass}.bin.gz','rb') as f:f.read(12);c=list(f.read(16)[:case['n']])
            (B/'POTENTIAL_COUNTEREXAMPLE.json').write_text(json.dumps(dict(graph=case,c=c,mass=mass,exact_AS_maximum=case['exact_AS_maximum'],scope='Awaiting fresh cold audit'),indent=2)+'\n',encoding='utf-8',newline='\n');status='POTENTIAL_ACTUAL_COUNTEREXAMPLE';break
    row=dict(graph=name,status=status,threshold=threshold,last_verified_mass=last);summaries.append(row);(B/(name+'_summary.json')).write_text(json.dumps(row,indent=2)+'\n',encoding='utf-8',newline='\n')
    if case['control'] and threshold!=case['expected_threshold']:break
if mode=='control':(B/'control_summary.json').write_text(json.dumps(dict(both_controls_pass=len(summaries)==2 and all(r['status']=='EXACT_THRESHOLD' for r in summaries),controls=summaries),indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(summaries),flush=True)
