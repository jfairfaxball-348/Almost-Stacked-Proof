import hashlib,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/bip_odd_larger');B.mkdir(exist_ok=True);assert not (B/'preflight.json').exists()
def write(p,t):
    p=Path(p)
    if not isinstance(t,str):t=json.dumps(t,indent=2)+'\n'
    assert not p.exists() or p.read_text(encoding='utf-8')==t,str(p)
    p.write_text(t,encoding='utf-8',newline='\n')
for suffix in ['produce','verify']:
    t=Path(f'tools/s014_c073_{suffix}.py').read_text(encoding='utf-8').replace('import hashlib,json,lzma,struct,time','import hashlib,json,lzma,struct,time,sys').replace("B=Path('evidence/S014/bip_odd_slack');start=time.monotonic()","BASE=Path('evidence/S014/bip_odd_larger');B=BASE;start=time.monotonic()")
    if suffix=='produce':
        old="for case in json.loads((B/'inputs.json').read_bytes())['cases']:";new="chosen=next(c for c in json.loads((BASE/'inputs.json').read_bytes())['cases'] if c['id']==sys.argv[1]);B=BASE/chosen['id'];B.mkdir(parents=True,exist_ok=True)\nfor case in [chosen]:";assert t.count(old)==1;t=t.replace(old,new)
    else:
        t=t.replace("for pre in [B/'preflight.json',B/'derived_preflight.json']:","B=BASE/sys.argv[1]\nfor pre in [BASE/'preflight.json',B/'derived_preflight.json']:")
        t=t.replace("cfg=json.loads((B/'inputs.json').read_bytes())['cases'];", "cfg=[c for c in json.loads((BASE/'inputs.json').read_bytes())['cases'] if c['id']==sys.argv[1]];")
        t=t.replace('len(cfg)==142','len(cfg)==1')
    write(f'tools/s014_c074_{suffix}.py',t)
old=Path('evidence/S014/critical_even');source=json.loads((old/'inputs.json').read_bytes())['cases'];cases=[];inventory=[]
for case in source:
    n=case['n'];adj=[[] for _ in range(n)]
    for u,v in case['edges']:adj[u].append(v);adj[v].append(u)
    color={0:0};queue=[0];bip=True
    for u in queue:
        for v in adj[u]:
            if v not in color:color[v]=1-color[u];queue.append(v)
            elif color[v]==color[u]:bip=False
    if not bip or n<=6:continue
    countall=0;largest=0
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);countall+=count;largest=max(largest,count);remaining=count*16
            while remaining:part=f.read(min(remaining,1048576));assert part;remaining-=len(part)
    ok=countall<=2000000 and largest<=1000000 and case['threshold']<=252;inventory.append(dict(case=case['id'],states=countall,largest_layer=largest,status='READY' if ok else 'PRIOR_SCOPE_CUTOFF_UNKNOWN'));cases.append(case)
assert len(cases)==21;write(B/'inputs.json',dict(cases=cases,inventory=inventory));plan=Path('sessions/S014/PLAN_AMENDMENT_74.md');write(plan.with_suffix('.sha256'),hashlib.sha256(plan.read_bytes()).hexdigest()+'\n');files=[B/'inputs.json',plan,plan.with_suffix('.sha256'),old/'inputs.json',old/'preflight.json',old/'verification.json',Path('evidence/S014/bip_parity/verification.json'),Path('evidence/S014/bip_odd_slack/verification.json'),Path('research/S014_TRIVALENT_BOUNDARY_AND_BIPARTITE_PARITY.md'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_c074_*.py')]
for c in cases:files.extend([Path(c['certificate']),Path(c['summary'])])
write(B/'preflight.json',dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}));print(json.dumps(dict(cases=len(cases),ready=sum(r['status']=='READY' for r in inventory),largest=max(r['states'] for r in inventory))))
