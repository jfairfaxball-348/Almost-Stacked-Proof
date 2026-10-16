import hashlib,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/bip_parity');start=time.monotonic()
for pre in [B/'preflight.json',B/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes())['cases'];out=json.loads(lzma.decompress((B/'result.json.xz').read_bytes()));assert len(cfg)==len(out)==638;states=tests=nonAS=bipcases=heavyfail=0;fail=[]
for case,row in zip(cfg,out):
    assert row['case']==case['id'];n=case['n'];parent=list(range(n));parity=[0]*n
    def find(u):
        p=0
        while parent[u]!=u:p^=parity[u];u=parent[u]
        return u,p
    bip=True
    for u,v in case['edges']:
        a,x=find(u);b,y=find(v)
        if a==b:
            if x^y!=1:bip=False
        else:parent[a]=b;parity[a]=x^y^1
    assert len({find(v)[0] for v in range(n)})==1 and bip==row['bipartite']
    if not bip:assert set(row)=={'case','bipartite'};continue
    bipcases+=1;S=set()
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw)
            if mass!=case['threshold']-1:
                remaining=count*16
                while remaining:part=f.read(min(remaining,1048576));assert part;remaining-=len(part)
                continue
            assert count<=1000000
            for _ in range(count):raw=f.read(16);assert len(raw)==16 and not any(raw[n:]) and sum(raw[:n])==mass;S.add(tuple(raw[:n]))
            break
    assert len(S)==row['critical'];states+=len(S);assert states<=3000000
    expected={c for c in S if sum(a>1 for a in c)>1};given={tuple(r['c']):r for r in row['rows']};assert len(given)==len(row['rows']) and set(given)==expected
    for c,rec in given.items():
        sources=[]
        for q in range(n):
            d=tuple((sum(c)-sum(a&1 for v,a in enumerate(c) if v!=q)) if u==q else a&1 for u,a in enumerate(c));assert sum(d)==sum(c) and all((a-b)%2==0 for a,b in zip(c,d)) and sum(a>1 for a in d)==1
            if d in S:sources.append(q)
            tests+=1;assert tests<=1000000
        assert sources==rec['losing_sources'] and rec['all_source_failure']==(not sources) and rec['heavy_source_failure']==(not any(c[q]>1 for q in sources));nonAS+=1;heavyfail+=rec['heavy_source_failure']
        if not sources:fail.append(dict(case=case,c=list(c)))
        assert time.monotonic()-start<540
report=dict(complete_all_candidate_memberships_equal=True,cases=638,bipartite_cases=bipcases,critical_states=states,nonAS_inputs=nonAS,candidates=tests,all_source_failures=len(fail),heavy_source_failures=heavyfail,first_failures=fail[:4],scope='Finite critical bipartite parity challenge only; universal B_par and ASH* unproved',seconds=time.monotonic()-start);(B/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(report))
