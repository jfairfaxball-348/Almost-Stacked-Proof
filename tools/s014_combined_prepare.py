import hashlib,json
from pathlib import Path
B=Path('evidence/S014/combined_bound');B.mkdir(exist_ok=True);old=Path('evidence/S014/critical_even/inputs.json');raw=json.loads(old.read_bytes())['cases'];raw.append(dict(id='fresh_crown5',n=10,edges=json.loads(Path('evidence/S014/retract_trees/inputs.json').read_bytes())['graphs'][-3]['edges'],threshold=16,summary='evidence/S014/retract_trees/crown5_stack_threshold.json',certificate='evidence/S014/retract_trees/crown5_stack_threshold.bin.xz'));cases=[];lookup={};files=[old,Path('evidence/S014/critical_even/preflight.json'),Path('evidence/S014/critical_even/verification.json'),Path('evidence/S014/retract_trees/crown5_stack_threshold_verification.json')]
for c in raw:
    n=c['n'];adj=[[] for _ in range(n)]
    for u,v in c['edges']:adj[u].append(v);adj[v].append(u)
    color={0:0};todo=[0];bip=True
    for u in todo:
        for v in adj[u]:
            if v not in color:color[v]=1-color[u];todo.append(v)
            if color[v]==color[u]:bip=False
    assert len(color)==n
    if not bip:continue
    key=(n,tuple(sorted(tuple(sorted(e)) for e in c['edges'])))
    if key in lookup:
        r=cases[lookup[key]];assert r['threshold']==c['threshold'];r['source_ids'].append(c['id']);continue
    d=dict(c,index=len(cases),source_ids=[c['id']]);lookup[key]=len(cases);cases.append(d);files.extend([Path(c['summary']),Path(c['certificate'])])
assert len(cases)<=638 and all(c['n']<=14 for c in cases)
(B/'inputs.json').write_text(json.dumps(dict(cases=cases),indent=2)+'\n',encoding='utf-8',newline='\n');plan=Path('sessions/S014/PLAN_AMENDMENT_54.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files.extend([B/'inputs.json',plan,plan.with_suffix('.sha256'),Path('research/S014_METRIC_RETRACTION_AUDIT.md'),Path('research/S014_ISOMETRIC_TREE_BRIDGE.md'),Path('research/S014_CROWN_ISOMETRIC_TREE_OBSTRUCTION.md'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_combined*.py')])
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM54 frozen',len(cases),'complete labeled bipartite cases')
