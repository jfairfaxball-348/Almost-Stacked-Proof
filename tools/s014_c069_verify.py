import hashlib,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/mass_slack');start=time.monotonic()
for pre in [B/'preflight.json',B/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes())['cases'];saved=json.loads(lzma.decompress((B/'result.json.xz').read_bytes()));out=saved['cases'];assert len(out)<=len(cfg);inputs=parsed=failures=candidates=0;first=None
for case,row in zip(cfg,out):
    assert row['case']==case['id'];n=case['n'];S=set()
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);assert count<=1000000
            for _ in range(count):
                raw=f.read(16);assert len(raw)==16 and not any(raw[n:]);c=tuple(raw[:n]);assert sum(c)==mass;S.add(c)
    assert len(S)==row['saved_losers'];parsed+=len(S);assert parsed<=2000000
    wanted=sorted([c for c in S if sum(z>=2 for z in c)>=2],key=lambda c:bytes(reversed(c)));given=row['rows'];assert len(given)<=len(wanted)
    for number,rec in enumerate(given):
        c=tuple(rec['c']);assert c==wanted[number];inputs+=1;w=rec['witness']
        if w:
            s,t,r,delta=w['s'],w['t'],w['r'],w['delta'];U=w['U'];assert s!=t and c[s]>=2 and c[t]>=2 and r in [0,1] and delta in [0,1,2] and len(U)==len(set(U))<=2 and r+len(U)<=c[s] and all(c[u]==0 for u in U)
            d=tuple(r if u==s else c[t]+c[s]-r-len(U)+delta if u==t else 1 if u in U else c[u] for u in range(n));assert d==tuple(w['d']) and d in S and sum(d)==sum(c)+delta and sum(z>=2 for z in d)==sum(z>=2 for z in c)-1
        else:
            assert number==len(given)-1 and row==out[-1] and saved['status']=='H_UP2_AUXILIARY_REFUTED';count=0
            for s in range(n):
                for t in range(n):
                    if s==t or c[s]<2 or c[t]<2:continue
                    for r in range(2):
                        for mask in range(1<<n):
                            U=[u for u in range(n) if mask>>u&1]
                            if len(U)>2 or r+len(U)>c[s] or any(c[u] for u in U):continue
                            for delta in range(3):
                                d=tuple(r if u==s else c[t]+c[s]-r-len(U)+delta if u==t else 1 if u in U else c[u] for u in range(n));assert d not in S;count+=1
            assert count==rec['tested'];candidates+=count;failures+=1;first=dict(case=case,c=list(c),mass=sum(c),candidates=count)
        assert time.monotonic()-start<540
    if not failures:assert len(given)==len(wanted)
assert parsed==saved['parsed_states'] and (len(out)==len(cfg) if not failures else failures==1)
report=dict(status=saved['status'],complete_tested_prefix_verified=True,cases=len(out),inputs=inputs,parsed_states=parsed,failed_inputs=failures,first_failure=first,independently_checked_failed_candidates=candidates,scope='Only finite H_up2 challenge; universal ASH* OPEN',seconds=time.monotonic()-start)
(B/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(report))
