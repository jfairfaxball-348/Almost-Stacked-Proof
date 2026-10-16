import hashlib,itertools,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/cube_general');start=time.monotonic()
for pre in [B/'preflight.json',B/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes());lower=json.loads(Path('evidence/S014/cube_lower/verification.json').read_bytes());assert lower['exact_binary_buffer_AS_oracle_certified'] and lower['exact_L_AS']==30;choices=json.loads(Path('evidence/S014/cube_dag/choices.json').read_bytes());E={frozenset(e) for e in cfg['edges']};assert E=={frozenset([u,u^(1<<j)]) for u in range(16) for j in range(4)};anchors={};literal_moves=0
with lzma.open(B/'anchors.bin.xz','rb') as f:
    while head:=f.read(17):
        assert len(head)==17;x=tuple(head[:16]);length=head[16];assert length<=100 and x not in anchors;codes=f.read(length);assert len(codes)==length;y=list(x)
        for code in codes:u,v=divmod(code,16);assert frozenset([u,v]) in E and y[u]>=2;y[u]-=2;y[v]+=1;literal_moves+=1
        assert sum(z>0 for z in y)==1;anchors[x]=codes
ss={}
with lzma.open(B/'states.bin.xz','rb') as f:
    while raw:=f.read(18):assert len(raw)==18;x=tuple(raw[:16]);assert x not in ss;ss[x]=struct.unpack('<H',raw[16:])[0]
assert len(ss)<=2000000;truth={};ordinary_negative=AS_negative=macros=dependencies=0;used=set()
for j,(x,k) in enumerate(sorted(ss.items(),key=lambda kv:sum(kv[0]))):
    if j%1000==0:assert time.monotonic()-start<540
    assert sum(x)>0
    if k==65535:assert sum(z>0 for z in x)==1;truth[x]=True
    elif k==65533:assert x in anchors;used.add(x);truth[x]=True
    elif k==65532:
        heavy=[v for v,z in enumerate(x) if z>=2];assert len(heavy)==1;s=heavy[0];N=x[s];assert all(z<=1 for v,z in enumerate(x) if v!=s);mask=sum(1<<((v^s)-1) for v,z in enumerate(x) if v!=s and z);assert N<choices[mask][N%3][0];truth[x]=False;AS_negative+=1
    elif k==65534:
        assert sum(z>0 for z in x)>1
        for u,z in enumerate(x):
            if z<2:continue
            for v in range(16):
                if frozenset([u,v]) not in E:continue
                y=list(x);y[u]-=2;y[v]+=1;assert tuple(y) in truth and not truth[tuple(y)];dependencies+=1
        truth[x]=False;ordinary_negative+=1
    elif 256<=k<272:
        u=k-256;assert x[u]>=4;y=list(x);w=u^1
        for a,b in [(u,w),(u,w),(w,u)]:assert y[a]>=2 and frozenset([a,b]) in E;y[a]-=2;y[b]+=1
        expected=list(x);expected[u]-=3;assert y==expected and truth[tuple(y)];truth[x]=True;macros+=1
    else:
        u,v=divmod(k,16);assert 0<=u<16 and frozenset([u,v]) in E and x[u]>=2;y=list(x);y[u]-=2;y[v]+=1;assert truth[tuple(y)];truth[x]=True;dependencies+=1
assert used==set(anchors);rows=json.loads((B/'results.json').read_bytes());result=json.loads((B/'result.json').read_bytes());assert len(rows)==result['completed'] and len(ss)==result['states'];potential=[]
for j,r in enumerate(rows):
    case=cfg['candidates'][j];assert r['id']==j==case['id'] and sum(case['c'])==case['mass'] and case['mass'] in [31,32,33] and sum(z>=2 for z in case['c'])>=2
    if r['winning'] is None:assert r['status'] in ['QUERY_STATE_CAP_UNKNOWN','GLOBAL_STATE_CAP_UNKNOWN','TIME_BOUND_UNKNOWN'];continue
    assert truth[tuple(case['c'])]==r['winning']
    if not r['winning']:potential.append(case)
assert len(potential)<=1 and (potential[0] if potential else None)==result['potential'];out=dict(status=result['status'],candidates_checked=len(rows),winning_inputs=sum(r['winning'] is True for r in rows),unknown=sum(r['winning'] is None for r in rows),verified_states=len(ss),literal_AS_anchors=len(anchors),literal_moves=literal_moves,exact_AS_negative_anchors=AS_negative,ordinary_negative_states=ordinary_negative,triple_macros=macros,verified_legal_dependencies=dependencies,potential=potential,all_completed_answers_certified=True,scope='Frozen general inputs only; potential requires fresh cold audit, winning samples prove no full threshold',seconds=time.monotonic()-start);(B/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
