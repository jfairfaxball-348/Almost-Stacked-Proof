import hashlib,itertools,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/sector_exchange');start=time.monotonic()
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes())['cases'];out=[];states=queries=checks=0;status='COMPLETE_REGISTERED_SCOPE';failure=None;parsed=[]
def comp(n,K):
    if n==1:yield (K,);return
    for x in range(K+1):
        for t in comp(n-1,K-x):yield (x,)+t
class StopRun(Exception):pass
try:
    for case in cfg:
        n=case['n'];adj=[[] for _ in range(n)]
        for u,v in case['edges']:adj[u].append(v);adj[v].append(u)
        color={0:1};queue=[0];bip=True
        for u in queue:
            for v in adj[u]:
                if v not in color:color[v]=-color[u];queue.append(v)
                elif color[v]==color[u]:bip=False
        if not bip:continue
        S=set();parsed.append(case['id'])
        with lzma.open(case['certificate'],'rb') as f:
            while raw:=f.read(12):
                mass,count=struct.unpack('<IQ',raw);assert count<=1000000
                for _ in range(count):z=f.read(16);assert len(z)==16;S.add(int.from_bytes(z,'little'))
        states+=len(S);assert states<=2000000
        for r in itertools.product(range(3),repeat=n):
            if sum((1+2*r[u])*color[u] for u in range(n))%3:continue
            for K in range(5):
                vectors=list(comp(n,K));key=dict(case=case['id'],r=list(r),K=K)
                if queries+len(vectors)>2000000 or time.monotonic()-start>540:status='BEFORE_GROUP_CAP_UNKNOWN';raise StopRun
                W={k for k in vectors if int.from_bytes(bytes(1+2*r[u]+6*k[u] for u in range(n)),'little') not in S};queries+=len(vectors)
                row={**key,'compositions':len(vectors),'winning':len(W),'checked':0,'completed':True};out.append(row)
                if len(W)==len(vectors) or len(W)<=1:continue
                for a in sorted(W):
                    for b in sorted(W):
                        for i in range(n):
                            if a[i]<=b[i]:continue
                            if checks>=2000000 or time.monotonic()-start>540:status='PAIR_OR_TIME_CAP_UNKNOWN';row['completed']=False;raise StopRun
                            checks+=1;row['checked']+=1;options=[]
                            for j in range(n):
                                if a[j]>=b[j]:continue
                                aa=tuple(x-int(u==i)+int(u==j) for u,x in enumerate(a));bb=tuple(x+int(u==i)-int(u==j) for u,x in enumerate(b));options.append(dict(j=j,a_wins=aa in W,b_wins=bb in W))
                            if not any(o['a_wins'] and o['b_wins'] for o in options):
                                failure={**key,'n':n,'edges':case['edges'],'a':list(a),'b':list(b),'i':i,'options':options};status='AUXILIARY_EXCHANGE_FALSE';row['completed']=False;raise StopRun
except StopRun:pass
report=dict(status=status,cases_registered=30,groups=out,parsed_cases=parsed,states=states,membership_queries=queries,pair_source_checks=checks,first_failure=failure,scope='Only rescaled THREE-sector exchange; universal ASH* OPEN')
(B/'result.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in report.items() if k not in ['groups','first_failure','parsed_cases']}))
