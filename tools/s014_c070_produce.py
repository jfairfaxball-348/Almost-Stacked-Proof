import hashlib,itertools,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/two_pool');start=time.monotonic()
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cases=json.loads((B/'inputs.json').read_bytes())['cases'];out=[];total=tests=0;stop=False;status='COMPLETE_REGISTERED_CASES'
def options(c):
    n=len(c);heavy=[v for v,z in enumerate(c) if z>=2];empty=[v for v,z in enumerate(c) if z==0]
    for s,t in itertools.combinations(heavy,2):
        for q in range(n):
            for rs,rt in itertools.product([0,1],repeat=2):
                F=c[s]-rs+c[t]-rt
                for k in range(min(2,F)+1):
                    for U in itertools.combinations([u for u in empty if u!=q],k):
                        for delta in range(3):
                            d=c.copy();d[s]=rs;d[t]=rt;d[q]+=F-k+delta
                            for u in U:d[u]=1
                            yield dict(s=s,t=t,q=q,rs=rs,rt=rt,U=list(U),delta=delta,d=d)
for case in cases:
    if stop:break
    n=case['n'];S=set()
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);assert count<=1000000
            for _ in range(count):z=f.read(16);assert len(z)==16;S.add(int.from_bytes(z,'little'))
    total+=len(S);assert total<=2000000;rows=[]
    for x in sorted(S):
        c=list(x.to_bytes(16,'little')[:n])
        if sum(z>=2 for z in c)<2:continue
        witness=None;tested=0
        for w in options(c):
            tests+=1;tested+=1;assert tests<=20000000 and time.monotonic()-start<540
            if int.from_bytes(bytes(w['d']),'little') in S:witness=w;break
        rows.append(dict(c=c,witness=witness,tested=tested))
        if witness is None:stop=True;status='H_POOL2_AUXILIARY_REFUTED';break
    out.append(dict(case=case['id'],rows=rows,saved_losers=len(S)))
(B/'result.json.xz').write_bytes(lzma.compress(json.dumps(dict(status=status,cases=out,parsed_states=total,candidates_tested=tests),separators=(',',':')).encode()));print(json.dumps(dict(status=status,cases=len(out),inputs=sum(len(c['rows']) for c in out),candidates=tests,parsed_states=total)))
