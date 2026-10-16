import hashlib,json,lzma,struct,time,sys
from pathlib import Path
BASE=Path('evidence/S014/bip_odd_larger');B=BASE;start=time.monotonic()
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
out=[];total=tests=0;stop=False;status='COMPLETE_REGISTERED_CASES'
chosen=next(c for c in json.loads((BASE/'inputs.json').read_bytes())['cases'] if c['id']==sys.argv[1]);B=BASE/chosen['id'];B.mkdir(parents=True,exist_ok=True)
for case in [chosen]:
    if stop:break
    n=case['n'];adj=[[] for _ in range(n)]
    for u,v in case['edges']:adj[u].append(v);adj[v].append(u)
    color={0:0};queue=[0];bip=True
    for u in queue:
        for v in adj[u]:
            if v not in color:color[v]=1-color[u];queue.append(v)
            elif color[v]==color[u]:bip=False
    assert len(color)==n
    if not bip:out.append(dict(case=case['id'],bipartite=False));continue
    sign=[1 if color[u]==0 else -1 for u in range(n)];S=set()
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);assert count<=1000000
            for _ in range(count):raw=f.read(16);assert len(raw)==16;S.add(int.from_bytes(raw,'little'))
    total+=len(S);assert total<=2000000;rows=[]
    for x in sorted(S):
        c=list(x.to_bytes(16,'little')[:n])
        if sum(a>=2 for a in c)<2 or any(a>0 and a%2==0 for a in c) or sum(a*e for a,e in zip(c,sign))%3:continue
        p=[a%2 for a in c];F=sum(c)-sum(p);witness=None;tested=0
        for q in range(n):
            if witness:break
            for delta in [0,2,4]:
                d=p.copy();d[q]+=F+delta
                if sum(a*e for a,e in zip(d,sign))%3:continue
                tested+=1;tests+=1;assert tests<=20000000 and time.monotonic()-start<540
                if int.from_bytes(bytes(d),'little') in S:witness=dict(q=q,delta=delta,d=d);break
        rows.append(dict(c=c,witness=witness,tested=tested))
        if witness is None:stop=True;status='B_ODD_AUXILIARY_REFUTED';break
    out.append(dict(case=case['id'],bipartite=True,rows=rows,saved_losers=len(S)))
(B/'result.json.xz').write_bytes(lzma.compress(json.dumps(dict(status=status,cases=out,parsed_states=total,candidates_tested=tests),separators=(',',':')).encode()));print(json.dumps(dict(status=status,cases=len(out),bipartite_cases=sum(r['bipartite'] for r in out),inputs=sum(len(r.get('rows',[])) for r in out),candidates=tests,states=total)))
