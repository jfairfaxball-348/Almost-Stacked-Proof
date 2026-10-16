import hashlib,json
from pathlib import Path
B=Path('evidence/S014/critical_even');B.mkdir(exist_ok=True);cases=json.loads(Path('evidence/S014/eliminate_residual/inputs.json').read_bytes())['cases'];sources=['evidence/S014/eliminate_residual/inputs.json','evidence/S014/eliminate_residual/verification.json']
for folder in ['regular_eliminate','circulant','coupled_threshold']:
    base=Path('evidence/S014')/folder;src=base/'inputs.json';sources.append(src.as_posix())
    for row in json.loads(src.read_bytes())['cases']:
        assert row['goal']=='stack';g=row['graph'];stem=base/(g['graph']+'_stack_threshold');summary=stem.with_suffix('.json');r=json.loads(summary.read_bytes());ver=Path(str(stem)+'_verification.json');v=json.loads(ver.read_bytes());assert r['scope']==v['scope']=='EXACT_THRESHOLD' and v['all_full_losing_layers_equal'] and r['threshold']==v['threshold'];sources.append(ver.as_posix())
        cases.append(dict(id=folder+'/'+g['graph'],n=g['n'],edges=g['edges'],threshold=r['threshold'],summary=summary.as_posix(),certificate=Path(str(stem)+'.bin.xz').as_posix()))
selected=[];seen=set()
for c in cases:
    key=(str(Path(c['certificate']).resolve()),c['threshold'])
    if key in seen:continue
    seen.add(key);selected.append(c)
(B/'inputs.json').write_text(json.dumps(dict(cases=selected),indent=2)+'\n',encoding='utf-8',newline='\n')
plan=Path('sessions/S014/PLAN_AMENDMENT_44.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n')
paths=[plan,B/'inputs.json',*Path('tools').glob('s014_critical_even*.py'),Path('tools/s009_checks.py'),*(Path(p) for p in sources)]
for c in selected:paths.extend([Path(c['summary']),Path(c['certificate'])])
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM44 frozen',len(selected),'complete critical sets')
