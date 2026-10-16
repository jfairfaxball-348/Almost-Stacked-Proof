"""Full finite inventory and complete independent chain aggregation."""
import hashlib,json
from pathlib import Path
B=Path('evidence/S014/mass11_cegis');V=Path('evidence/S014/mass11_lrat')
for p,h in json.loads((B/'summary_preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes());inv=json.loads((B/'inventory_verification.json').read_bytes());assert inv['whole_sorted_mass11_order8_inventory_equal'] and inv['patterns']==44
added=hints=certified=0;statuses=[]
for case in cfg['cases']:
    D=B/case['id'];O=V/case['id'];result=json.loads((D/'result.json').read_bytes());clause=json.loads((D/'clause_verification.json').read_bytes());proof=json.loads((O/'verification.json').read_bytes());rows=json.loads((D/'checks.json').read_bytes())
    assert len(rows)==4 and all(r['exit_code']==0 and r['resource_failure'] is None for r in rows) and 's VERIFIED' in rows[2]['stdout']
    assert result['status']=='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE' and result['case']==case and clause['counterexample_exists_implies_formula_satisfiable'] and proof['fixed_input_class_exclusion_certified']
    for pre in [D/'derived_preflight.json',O/'derived_preflight.json']:
        for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    if not case['control']:certified+=1;added+=proof['verified_RUP_additions'];hints+=proof['hint_visits'];statuses.append(dict(case=case['id'],status='INDEPENDENTLY_EXCLUDED'))
assert certified==44 and not (B/'STOP_FOR_POTENTIAL.json').exists()
report=dict(patterns=44,certified=certified,complete_mass11_order8_exclusion=True,control_pass=True,verified_RUP_additions=added,hint_visits=hints,scope='ONLY all connected order8 graphs/fixed mass11; universal ASH* OPEN',cases=statuses)
(B/'summary.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in report.items() if k!='cases'}))
