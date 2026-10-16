import hashlib,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/odd_leaf_contraction');start=time.monotonic()
for pre in [B/'preflight.json',B/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes())['cases'];result=json.loads((B/'result.json').read_bytes());assert len(cfg)==len(result['cases'])==142
states=records=failures=criticalall=0;counts=[0,0,0];first=[]
for case,row in zip(cfg,result['cases']):
    assert case['id']==row['case'];n=case['n'];incident=[[e for e in case['edges'] if u in e] for u in range(n)];S=set()
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);assert count<=1000000
            for _ in range(count):z=f.read(16);assert len(z)==16 and not any(z[n:]) and sum(z[:n])==mass;S.add(tuple(z[:n]))
    assert len(S)==row['states'];states+=len(S);assert states<=2000000;expected={};bad=critical=0
    for c in S:
        for w in range(n):
            if len(incident[w])!=1:continue
            v=next(u for u in incident[w][0] if u!=w)
            for kind,delta in [(0,-1),(1,1),(2,3)]:
                eligible=(c[w]%2==1 and c[v]>=2) if kind==0 else ((c[w]%2==0 and c[v]>=1) if kind==1 else (c[w]>0 and c[w]%2==0))
                if not eligible:continue
                y=tuple(a+delta*int(u==w)+(delta if kind<2 else 0)*int(u==v) for u,a in enumerate(c));assert min(y)>=0 and sum(y)==sum(c)+([-2,2,3][kind]);lose=y in S;expected[c,w,kind]=lose;counts[kind]+=1;records+=1;bad+=not lose
                if kind==2:critical+=sum(c)==case['threshold']-1
                if not lose and len(first)<5:first.append(dict(case=case['id'],c=list(c),w=w,kind=kind,y=list(y)))
        assert records<=2000000 and time.monotonic()-start<540
    actual={(tuple(c),w,kind):lose for c,w,kind,lose in json.loads(lzma.decompress(Path(row['file']).read_bytes()))};assert len(actual)==row['records'] and actual==expected and bad==row['failed_memberships'] and critical==row['critical_even_leafs'];failures+=bad;criticalall+=critical
assert states==result['states'] and records==result['records'] and counts==result['direction_counts'] and failures==result['failed_memberships']
out=dict(complete_both_direction_inventories_and_memberships_equal=True,cases=142,states=states,records=records,odd_leaf_down=counts[0],even_leaf_parent_up=counts[1],even_heavy_leaf_plus3=counts[2],failed_memberships=failures,critical_even_leafs=criticalall,first_failures=first,scope='Complete finite119b/120 challenge on142 fixed graphs, symbolic proofs separate; universal ASH* OPEN',seconds=time.monotonic()-start)
(B/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
