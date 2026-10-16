import hashlib,json,lzma,struct,time,sys
from pathlib import Path
BASE=Path('evidence/S014/bip_odd_larger');B=BASE;start=time.monotonic()
B=BASE/sys.argv[1]
for pre in [BASE/'preflight.json',B/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=[c for c in json.loads((BASE/'inputs.json').read_bytes())['cases'] if c['id']==sys.argv[1]];saved=json.loads(lzma.decompress((B/'result.json.xz').read_bytes()));out=saved['cases'];assert len(out)<=len(cfg)==1;states=inputs=bipcases=failures=candidates=0;first=None
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
    bipcases+=1;sign=[1 if find(v)[1]==find(0)[1] else -1 for v in range(n)];S=set()
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);assert count<=1000000
            for _ in range(count):raw=f.read(16);assert len(raw)==16 and not any(raw[n:]) and sum(raw[:n])==mass;S.add(tuple(raw[:n]))
    assert len(S)==row['saved_losers'];states+=len(S);assert states<=2000000
    wanted=sorted([c for c in S if sum(a>1 for a in c)>1 and all(a==0 or a%2 for a in c) and sum(a*e for a,e in zip(c,sign))%3==0],key=lambda c:bytes(reversed(c)));given=row['rows'];assert len(given)<=len(wanted)
    for j,rec in enumerate(given):
        c=tuple(rec['c']);assert c==wanted[j];inputs+=1;w=rec['witness'];p=tuple(a&1 for a in c);F=sum(c)-sum(p)
        if w:
            q,delta=w['q'],w['delta'];assert 0<=q<n and delta in [0,2,4];d=tuple(p[u]+(F+delta if u==q else 0) for u in range(n));assert d==tuple(w['d']) and d in S and sum(d)==sum(c)+delta and sum(a>1 for a in d)==1 and all((a-b)%2==0 for a,b in zip(c,d)) and sum(a*e for a,e in zip(d,sign))%3==0
        else:
            assert j==len(given)-1 and row==out[-1] and saved['status']=='B_ODD_AUXILIARY_REFUTED';count=0
            for q in range(n):
                for delta in range(0,5,2):
                    d=tuple((sum(c)-sum(a&1 for v,a in enumerate(c) if v!=q)+delta) if u==q else a&1 for u,a in enumerate(c))
                    if sum(a*e for a,e in zip(d,sign))%3:continue
                    assert d not in S;count+=1
            assert count==rec['tested'];candidates+=count;failures+=1;first=dict(case=case,c=list(c),mass=sum(c),candidates=count)
        assert time.monotonic()-start<540
    if not failures:assert len(given)==len(wanted)
assert states==saved['parsed_states'] and (len(out)==len(cfg) if not failures else failures==1)
report=dict(status=saved['status'],complete_tested_prefix_verified=True,cases=len(out),bipartite_cases=bipcases,inputs=inputs,states=states,failed_inputs=failures,failed_candidates_independently_checked=candidates,first_failure=first,scope='Only finite odd-positive bipartite parity challenge; universal ASH* OPEN',seconds=time.monotonic()-start);(B/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(report))
