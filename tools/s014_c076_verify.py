import hashlib,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/neighbor_ascent');start=time.monotonic()
for pre in [B/'preflight.json',B/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes())['cases'];saved=json.loads(lzma.decompress((B/'result.json.xz').read_bytes()));assert len(cfg)==len(saved)==142
states=bipcases=records=extensions=failed=failedtwo=critical=0;fail=[]
for case,row in zip(cfg,saved):
    assert row['case']==case['id'];n=case['n'];parent=list(range(n));offset=[0]*n;degree=[0]*n
    def find(u):
        x=0
        while parent[u]!=u:x^=offset[u];u=parent[u]
        return u,x
    bip=True
    for u,v in case['edges']:
        degree[u]+=1;degree[v]+=1;a,x=find(u);b,y=find(v)
        if a==b:
            if x^y!=1:bip=False
        else:parent[a]=b;offset[a]=x^y^1
    assert len({find(v)[0] for v in range(n)})==1 and bip==row['bipartite']
    if not bip:assert set(row)=={'case','bipartite'};continue
    bipcases+=1;sign=[1 if find(v)[1]==find(0)[1] else -1 for v in range(n)];S=set()
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);assert count<=1000000
            for _ in range(count):raw=f.read(16);assert len(raw)==16 and not any(raw[n:]) and sum(raw[:n])==mass;S.add(tuple(raw[:n]))
    assert len(S)==row['states'];states+=len(S);assert states<=2000000;expected={}
    for c in S:
        if sum(a*e for a,e in zip(c,sign))%3:continue
        for v in range(n):
            if not(c[v]>0 and c[v]%2==0):continue
            ns=[]
            for w in range(n):
                if sorted([v,w]) not in [sorted(e) for e in case['edges']]:continue
                d=tuple(a-int(u==v)+2*int(u==w) for u,a in enumerate(c));assert sum(d)==sum(c)+1 and sum(a*e for a,e in zip(d,sign))%3==0;ns.append([w,d in S]);extensions+=1
            expected[c,v]=ns;records+=1
            if not any(b for w,b in ns):
                failed+=1;failedtwo+=c[v]==2;critical+=sum(c)==case['threshold']-1
                if len(fail)<10:fail.append(dict(case=case['id'],n=n,edges=case['edges'],threshold=case['threshold'],mass=sum(c),c=list(c),v=v,neighbors=ns,minimum_degree=min(degree)))
        assert time.monotonic()-start<540
    actual={(tuple(r['c']),r['v']):r['neighbors'] for r in row['rows']};assert len(actual)==len(row['rows']) and expected==actual
assert records<=1000000 and extensions<=5000000
report=dict(all_input_neighbor_inventories_and_memberships_equal=True,cases=142,bipartite_cases=bipcases,states=states,records=records,extensions=extensions,failed_input_vertex_pairs=failed,failures_at_pile2=failedtwo,failures_at_actual_critical_mass=critical,first_failures=fail,scope='Finite challenge of unproved some-neighbor strengthening;114b unchanged; universal ASH* OPEN',seconds=time.monotonic()-start)
(B/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in report.items() if k!='first_failures'}))
