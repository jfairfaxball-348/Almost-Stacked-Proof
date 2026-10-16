"""Independent tuple DAG replay and exact source-orbit/query inventory."""
import hashlib,itertools,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/cube_tail');start=time.monotonic()
for pre in [B/'preflight.json',B/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes());n=cfg['n'];assert n==16;E={frozenset(e) for e in cfg['edges']};assert E=={frozenset([u,u^(1<<i)]) for u in range(16) for i in range(4)};assert cfg['source']==0 and cfg['buffer_vertices']==list(range(1,16)) and cfg['masses']==[31,32,33] and cfg['masks']==list(range(32768)) and cfg['query_count']==98304
for s,f in enumerate(cfg['maps']):assert len(f)==len(set(f))==16 and f[0]==s and all(f[v]==v^s for v in range(16)) and {frozenset([f[u],f[v]]) for u,v in cfg['edges']}==E
assert len(cfg['maps'])==16;ss={}
with lzma.open(B/'states.bin.xz','rb') as f:
    while raw:=f.read(18):assert len(raw)==18;z=tuple(raw[:16]);assert z not in ss;ss[z]=struct.unpack('<H',raw[16:])[0]
assert len(ss)<=2000000;truth={};negative=dependencies=0;adj=[[v for v in range(16) if frozenset([u,v]) in E] for u in range(16)]
for j,(x,k) in enumerate(sorted(ss.items(),key=lambda kv:sum(kv[0]))):
    if j%1000==0:assert time.monotonic()-start<540
    assert sum(x)>0
    if k==65535:assert sum(z>0 for z in x)==1;truth[x]=True
    elif k==65534:
        assert sum(z>0 for z in x)>1;negative+=1
        for u in range(16):
            if x[u]<2:continue
            for v in adj[u]:y=list(x);y[u]-=2;y[v]+=1;assert tuple(y) in truth and not truth[tuple(y)];dependencies+=1
        truth[x]=False
    else:
        u,v=divmod(k,16);assert 0<=u<16 and v in adj[u] and x[u]>=2;y=list(x);y[u]-=2;y[v]+=1;assert truth[tuple(y)];truth[x]=True;dependencies+=1
queries=json.loads((B/'queries.json').read_bytes());result=json.loads((B/'result.json').read_bytes());assert len(queries)==result['queries'] and len(ss)==result['states'];bad=[]
for j,(mass,mask,ok) in enumerate(queries):
    assert [mass,mask]==[31+j//32768,j%32768];x=(mass-mask.bit_count(),)+tuple(int(mask>>(v-1)&1) for v in range(1,16));assert truth[x]==ok
    if not ok:bad.append(dict(mass=mass,mask=mask,input=list(x)))
complete=result['status']=='COMPLETE_AS_TAIL'
if complete:assert len(queries)==98304 and not bad and result['bad'] is None
elif result['status']=='AS_LOSER_FOUND_REJECT_T31':assert len(bad)==1 and bad[0]==result['bad'] and queries[-1][2] is False
else:assert result['status'] in ['STATE_CAP_UNKNOWN','TIME_BOUND_UNKNOWN'] and not bad
out=dict(status=result['status'],completed_queries=len(queries),verified_states=len(ss),verified_dependencies=dependencies,negative_states=negative,all_completed_queries_certified=True,all16_XOR_maps_verified=True,complete_AS_tail_upper31=complete,exact_L_AS=30 if complete else None,AS_bad=result['bad'],scope='Only AS-tail status; no full general threshold or ASH* conclusion',seconds=time.monotonic()-start);(B/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
