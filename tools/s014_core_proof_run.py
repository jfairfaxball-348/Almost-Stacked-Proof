import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/core_proof');B.mkdir(exist_ok=True);P=Path('evidence/S014/cegis_orbits_v2')
plan=Path('sessions/S014/PLAN_AMENDMENT_40.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n')
(B/'inputs.json').write_bytes((P/'inputs.json').read_bytes())
files=[plan,Path('sessions/S014/PLAN_AMENDMENT_39.md'),B/'inputs.json',Path('tools/s014_indexed_drup.py'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_core_proof*.py')]
for name in ['C6','C9a','C9b','C10']:files.extend([P/name/'formula.cnf',P/name/'clause_verification.json',P/name/'derived_preflight.json'])
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n')
for name in ['C6','C9a','C9b','C10']:
    D=B/name;D.mkdir(exist_ok=True);rows=[]
    for script in ['s014_core_proof','s014_core_proof_verify','s014_core_proof_drup']:
        if script=='s014_core_proof_verify':
            paths=[p for p in D.rglob('*') if p.is_file() and p.name!='checks.json'];paths.extend([P/name/'formula.cnf',P/name/'clause_verification.json'])
            (D/'derived_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}),indent=2)+'\n',encoding='utf-8',newline='\n')
        # The generic independent checker also freezes the provenance inputs it expects.
        if script=='s014_core_proof_drup' and json.loads((D/'result.json').read_bytes())['status']=='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE':
            (D/'clause_sources.bin').write_bytes((D/'indices.json').read_bytes());(D/'constraints.jsonl').write_bytes((D/'derived_preflight.json').read_bytes())
        row=run([sys.executable,'tools/'+script+'.py',name]);rows.append(row);(D/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
        if row['exit_code'] or row['resource_failure']:sys.exit(1)
