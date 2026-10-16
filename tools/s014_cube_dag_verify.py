"""Independent inductive production parser, no optimizer/producer imports."""
import array,hashlib,itertools,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/cube_dag');start=time.monotonic()
for pre in [B/'preflight.json',B/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes());result=json.loads((B/'result.json').read_bytes());count=result['completed_masks'];assert 1<=count<=32768;E={frozenset(e) for e in cfg['edges']};assert E=={frozenset([u,u^(1<<j)]) for u in range(16) for j in range(4)};assert cfg['masses']==[31,32,33] and cfg['masks']==list(range(32768)) and cfg['buffer_vertices']==list(range(1,16)) and cfg['source']==0
for s,f in enumerate(cfg['maps']):assert len(f)==len(set(f))==16 and f[0]==s and all(f[v]==v^s for v in range(16)) and {frozenset([f[u],f[v]]) for u,v in cfg['edges']}==E
assert len(cfg['maps'])==16;raw=lzma.decompress((B/'nodes.bin.xz').read_bytes());assert len(raw)==count*48*8;cost=array.array('I');kind=array.array('B');neighbor=array.array('B');split=array.array('H')
for z,k,u,a in struct.iter_unpack('<IBBH',raw):assert 1<=z<=1024;cost.append(z);kind.append(k);neighbor.append(u);split.append(a)
assert len(cost)==result['nodes']<=2000000;P=[2**sum((v>>j)&1 for j in range(4)) for v in range(16)]
def idx(mask,typ,q):return (mask*3+typ)*16+q
def anycost(mask,q):return 0 if mask==(1<<(q-1)) and q>0 else cost[idx(mask,0,q)]
for mask in range(count):
    if mask%128==0:assert time.monotonic()-start<540
    checked=set()
    for q in sorted(range(16),key=lambda q:cost[idx(mask,0,q)]):
        i=idx(mask,0,q);z=cost[i];k=kind[i];u=neighbor[i];a=split[i]
        if mask==0:assert k==0 and z==P[q]
        elif k==1:assert u in checked and frozenset([u,q]) in E and z==cost[idx(mask,0,u)]+P[u] and cost[idx(mask,0,u)]<z
        elif k==2:assert frozenset([u,q]) in E and a and a<mask and a&mask==a and a!=mask;assert z==anycost(a,u)+anycost(mask^a,u)
        else:assert k==3 and mask==1<<(u-1) and u>0 and frozenset([u,q]) in E and z==P[u]
        checked.add(q)
    for q in range(16):
        i=idx(mask,1,q);k=kind[i];a=split[i]
        if mask==0:assert k==7 and cost[i]==2*P[q]
        elif k==4:assert cost[i]==anycost(mask,q)+P[q]
        else:assert k==5 and 0<a<mask and a&mask==a and cost[i]==anycost(a,q)+anycost(mask^a,q)
    for q in range(16):
        i=idx(mask,2,q);k=kind[i];a=split[i]
        if mask==0:assert k==8 and cost[i]==3*P[q]
        else:assert k==6 and a&mask==a and cost[i]==(P[q] if a==0 else anycost(a,q))+cost[idx(mask^a,1,q)]
choices=json.loads((B/'choices.json').read_bytes());assert len(choices)==count;queries=missing=0;first=None
for mask,row in enumerate(choices):
    assert len(row)==3
    for residue,(z,q,k) in enumerate(row):assert 0<=q<16 and 1<=k<=3 and z==cost[idx(mask,k-1,q)] and z>0 and z%3==residue
    for mass in [31,32,33]:
        N=mass-mask.bit_count();z,q,k=row[N%3];queries+=1
        if z>N:
            missing+=1
            if first is None:first=dict(mask=mask,mass=mass,N=N,certified_cost=z,q=q,k=k)
        else:assert N>=z>=1 and (N-z)%3==0
assert first==result['first_missing'];full=count==32768 and missing==0
if full:assert result['status']=='COMPLETE_AS_TAIL_UPPER31' and queries==98304
elif count==32768:assert result['status']=='UPPER_WITNESS_MISSING_UNKNOWN'
else:assert result['status']=='TIME_BOUND_UNKNOWN'
out=dict(status=result['status'],verified_nodes=len(cost),completed_masks=count,queries_examined=queries,upper_witnesses_missing=missing,every_node_has_sound_well_founded_production=True,all16_XOR_maps_verified=True,complete_AS_tail_upper31=full,exact_L_AS=30 if full else None,scope='Positive upper certificates only; no general threshold, loss from missing witness, or universal ASH* claim',seconds=time.monotonic()-start);(B/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
