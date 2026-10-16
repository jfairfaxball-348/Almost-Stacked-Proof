import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/bip_odd_larger');cfg=json.loads((B/'inputs.json').read_bytes());shard=int(sys.argv[1]);assert shard in [0,1];summaries=[]
for number,(case,inventory) in enumerate(zip(cfg['cases'],cfg['inventory'])):
    if number%2!=shard:continue
    if (B/'STOP_AUXILIARY_FAILURE.json').exists():break
    if inventory['status']!='READY':summaries.append(inventory);continue
    D=B/case['id'];D.mkdir(parents=True,exist_ok=True);rows=[]
    for suffix in ['produce','verify']:
        if suffix=='verify':
            p=D/'result.json.xz';(D/'derived_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest()}),indent=2)+'\n',encoding='utf-8',newline='\n')
        r=run([sys.executable,f'tools/s014_c074_{suffix}.py',case['id']]);rows.append(r);(D/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:r[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
        if r['exit_code'] or r['resource_failure']:sys.exit(1)
    v=json.loads((D/'verification.json').read_bytes());summaries.append(dict(case=case['id'],status=v['status'],inputs=v['inputs'],failed=v['failed_inputs']))
    if v['failed_inputs']:(B/'STOP_AUXILIARY_FAILURE.json').write_text(json.dumps(dict(case=case['id']))+'\n',encoding='utf-8',newline='\n');break
(B/f'shard{shard}_summary.json').write_text(json.dumps(summaries,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(summaries),flush=True)
