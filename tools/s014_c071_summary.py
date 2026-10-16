import hashlib,json
from pathlib import Path
B=Path('evidence/S014/highpile_cegis');V=Path('evidence/S014/highpile_lrat')
for p,h in json.loads((B/'summary_preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes());spec=[('H8_5551',8,[5,5,5,1]),('H8_7711',8,[7,7,1,1]),('H8_9531',8,[9,5,3,1]),('H8_5533',8,[5,5,3,3]),('H8_7733',8,[7,7,3,3]),('H9_5551',9,[5,5,5,1]),('H8_4444',8,[4,4,4,4]),('H8_6622',8,[6,6,2,2])]
assert [(c['id'],c['n'],c['c']) for c in cfg['cases'] if not c['control']]==[(name,n,sorted([0]*(n-4)+a)) for name,n,a in spec];added=hints=certified=0;out=[]
for case in cfg['cases']:
    D=B/case['id'];O=V/case['id'];result=json.loads((D/'result.json').read_bytes());clause=json.loads((D/'clause_verification.json').read_bytes());proof=json.loads((O/'verification.json').read_bytes());rows=json.loads((D/'checks.json').read_bytes());assert len(rows)==4 and all(r['exit_code']==0 and r['resource_failure'] is None for r in rows) and 's VERIFIED' in rows[2]['stdout'];assert result['status']=='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE' and result['case']==case and clause['counterexample_exists_implies_formula_satisfiable'] and proof['fixed_input_class_exclusion_certified']
    for pre in [D/'derived_preflight.json',O/'derived_preflight.json']:
        for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    if not case['control']:certified+=1;added+=proof['verified_RUP_additions'];hints+=proof['hint_visits'];out.append(dict(case=case['id'],n=case['n'],c=case['c'],status='INDEPENDENTLY_EXCLUDED'))
assert certified==8 and not (B/'STOP_FOR_POTENTIAL.json').exists();report=dict(patterns=8,certified=8,all_registered_patterns_independently_excluded=True,control_pass=True,verified_RUP_additions=added,hint_visits=hints,cases=out,scope='ONLY specified8 fixed-input graph classes, not full order/mass coverage; universal ASH* OPEN');(B/'summary.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in report.items() if k!='cases'}))
