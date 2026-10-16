import hashlib,itertools,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/sector_exchange');start=time.monotonic()
for pre in [B/'preflight.json',B/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes())['cases'];saved=json.loads((B/'result.json').read_bytes());assert len(cfg)==30;registered=[];colors={};by={c['id']:c for c in cfg}
for case in cfg:
    n=case['n'];parent=list(range(n));offset=[0]*n
    def find(u):
        parity=0
        while parent[u]!=u:parity^=offset[u];u=parent[u]
        return u,parity
    bip=True
    for u,v in case['edges']:
        a,x=find(u);b,y=find(v)
        if a==b:
            if x^y!=1:bip=False
        else:parent[a]=b;offset[a]=x^y^1
    assert len({find(v)[0] for v in range(n)})==1
    if not bip:continue
    signs=[(-1)**find(v)[1] for v in range(n)];colors[case['id']]=signs
    for z in range(3**n):
        r=[z//(3**(n-1-u))%3 for u in range(n)]
        if sum((1+2*r[u])*signs[u] for u in range(n))%3==0:registered.extend(dict(case=case['id'],r=r,K=K) for K in range(5))
rows=saved['groups'];assert [{k:r[k] for k in ['case','r','K']} for r in rows]==registered[:len(rows)];states=queries=checks=0;parsed=[];current=None;failure=None
for number,row in enumerate(rows):
    case=by[row['case']];n=case['n'];r=row['r'];K=row['K']
    if current!=case['id']:
        S=set();parsed.append(case['id']);current=case['id']
        with lzma.open(case['certificate'],'rb') as f:
            while raw:=f.read(12):
                mass,count=struct.unpack('<IQ',raw);assert count<=1000000
                for _ in range(count):z=f.read(16);assert len(z)==16 and not any(z[n:]) and sum(z[:n])==mass;S.add(tuple(z[:n]))
        states+=len(S);assert states<=2000000
    vectors=sorted(tuple(multiset.count(u) for u in range(n)) for multiset in itertools.combinations_with_replacement(range(n),K));W=[]
    for k in vectors:
        c=tuple(1+2*r[u]+6*k[u] for u in range(n))
        if c not in S:W.append(k)
    queries+=len(vectors);assert len(vectors)==row['compositions'] and len(W)==row['winning'];count=0
    if len(W)==len(vectors) or len(W)<=1:assert row['checked']==0 and row['completed'];continue
    Wset=set(W);done=False
    for a,b in itertools.product(W,repeat=2):
        for i in [u for u in range(n) if a[u]>b[u]]:
            if not row['completed'] and count==row['checked']:done=True;break
            count+=1;checks+=1;options=[]
            for j in [u for u in range(n) if a[u]<b[u]]:
                aa=list(a);bb=list(b);aa[i]-=1;aa[j]+=1;bb[i]+=1;bb[j]-=1;options.append(dict(j=j,a_wins=tuple(aa) in Wset,b_wins=tuple(bb) in Wset))
            if all(not(o['a_wins'] and o['b_wins']) for o in options):
                failure=dict(case=case['id'],r=r,K=K,n=n,edges=case['edges'],a=list(a),b=list(b),i=i,options=options);assert number==len(rows)-1 and saved['status']=='AUXILIARY_EXCHANGE_FALSE' and count==row['checked'];done=True;break
        if done:break
    assert count==row['checked']
assert queries==saved['membership_queries'] and checks==saved['pair_source_checks'] and failure==saved['first_failure'] and queries<=2000000 and checks<=2000000
if saved['status'].endswith('UNKNOWN'):
    assert saved['parsed_cases'][:len(parsed)]==parsed
    for name in saved['parsed_cases'][len(parsed):]:
        case=by[name];countall=0
        with lzma.open(case['certificate'],'rb') as f:
            while raw:=f.read(12):mass,count=struct.unpack('<IQ',raw);countall+=count;assert len(f.read(16*count))==16*count
        states+=countall
else:assert parsed==saved['parsed_cases']
assert states==saved['states']
if saved['status']=='COMPLETE_REGISTERED_SCOPE':assert len(rows)==len(registered) and all(r['completed'] for r in rows)
elif saved['status']=='AUXILIARY_EXCHANGE_FALSE':assert failure and not rows[-1]['completed']
else:assert saved['status'].endswith('UNKNOWN') and not failure
report=dict(complete_tested_prefix_and_all_exchange_options_equal=True,status=saved['status'],cases_registered=30,registered_groups=len(registered),executed_groups=len(rows),unexecuted_groups=len(registered)-sum(r['completed'] for r in rows),states=states,membership_queries=queries,pair_source_checks=checks,first_failure=failure,scope='Rescaled-sector exchange only; universal ASH* OPEN',seconds=time.monotonic()-start)
(B/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in report.items() if k!='first_failure'}))
