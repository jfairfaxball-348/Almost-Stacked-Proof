import hashlib,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/leaf_ascent');start=time.monotonic()
for pre in [B/'preflight.json',B/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes())['cases'];saved=json.loads(lzma.decompress((B/'result.json.xz').read_bytes()));assert len(cfg)==len(saved)==142;states=bipcases=extensions=empty=0;fail=[]
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
        for w in range(n):
            if degree[w]!=1:continue
            v=next(b if a==w else a for a,b in case['edges'] if w in [a,b])
            if not(c[v]>0 and c[v]%2==0):continue
            d=tuple(a-int(u==v)+2*int(u==w) for u,a in enumerate(c));assert sum(d)==sum(c)+1 and sum(a*e for a,e in zip(d,sign))%3==0;expected[c,v,w]=d in S;extensions+=1;empty+=c[w]==0
            if d not in S:fail.append(dict(case=case,c=list(c),v=v,w=w,d=list(d)))
        assert time.monotonic()-start<540
    actual={(tuple(r['c']),r['v'],r['w']):r['loses'] for r in row['rows']};assert len(actual)==len(row['rows']) and expected==actual
assert extensions<=1000000;report=dict(all_input_leaf_extension_memberships_equal=True,cases=142,bipartite_cases=bipcases,states=states,extensions=extensions,initially_empty_leaf_extensions=empty,failures=len(fail),first_failures=fail[:4],scope='Finite challenge only;114 written proof needed; universal ASH* OPEN',seconds=time.monotonic()-start);(B/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(report))
