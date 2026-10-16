"""Independent all-production and all-inequality audit, fixed bipartite graph."""
import array,hashlib,itertools,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/fano_AS');start=time.monotonic()
for pre in [B/'preflight.json',B/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes());n=cfg['n'];limit=1<<(n-1);assert n==14 and cfg['source']==0 and cfg['masks']==list(range(8192));E={frozenset(e) for e in cfg['edges']};assert E=={frozenset([p,7+l]) for p in range(7) for l in range(7) if ((p+1)&(l+1)).bit_count()%2==0};adj=[[v for v in range(n) if frozenset([u,v]) in E] for u in range(n)];dist={0:0};todo=[0]
for u in todo:
    for v in adj[u]:
        if v not in dist:dist[v]=dist[u]+1;todo.append(v)
assert len(dist)==n and all((dist[u]-dist[v])%2 for u,v in cfg['edges']);P=[2**dist[v] for v in range(n)];sign=[(-1)**dist[v] for v in range(n)];maps={tuple(f) for f in cfg['maps']};assert len(maps)==336 and tuple(range(n)) in maps
for f in maps:
    assert set(f)==set(range(n)) and {frozenset([f[u],f[v]]) for u,v in cfg['edges']}==E
    for g in maps:assert tuple(f[g[v]] for v in range(n)) in maps
assert len(cfg['source_maps'])==n and all(tuple(f) in maps and f[0]==v for v,f in enumerate(cfg['source_maps']))
result=json.loads((B/'result.json').read_bytes());assert result['status']=='COMPLETE_POSITIVE_TABLE' and result['completed_masks']==limit;raw=lzma.decompress((B/'nodes.bin.xz').read_bytes());assert len(raw)==limit*3*n*8;cost=array.array('I');kind=array.array('B');neighbor=array.array('B');split=array.array('H')
for z,k,u,a in struct.iter_unpack('<IBBH',raw):assert 1<=z<=1024;cost.append(z);kind.append(k);neighbor.append(u);split.append(a)
def idx(mask,typ,q):return (mask*3+typ)*n+q
def anycost(mask,q):return 0 if q>0 and mask==1<<(q-1) else cost[idx(mask,0,q)]
trees=[];anytree=[];two=[];three=[];imb=[0]*limit
for mask in range(limit):
    if mask%128==0:assert time.monotonic()-start<540
    checked=set()
    for q in sorted(range(n),key=lambda q:cost[idx(mask,0,q)]):
        i=idx(mask,0,q);z=cost[i];k=kind[i];u=neighbor[i];a=split[i]
        if mask==0:assert k==0 and z==P[q]
        elif k==1:assert u in checked and u in adj[q] and z==cost[idx(mask,0,u)]+P[u] and cost[idx(mask,0,u)]<z
        elif k==2:assert u in adj[q] and 0<a<mask and a&mask==a and z==anycost(a,u)+anycost(mask^a,u)
        else:assert k==3 and u>0 and mask==1<<(u-1) and u in adj[q] and z==P[u]
        checked.add(q)
    for q in range(n):
        i=idx(mask,1,q);k=kind[i];a=split[i]
        if mask==0:assert k==7 and cost[i]==2*P[q]
        elif k==4:assert cost[i]==anycost(mask,q)+P[q]
        else:assert k==5 and 0<a<mask and a&mask==a and cost[i]==anycost(a,q)+anycost(mask^a,q)
    for q in range(n):
        i=idx(mask,2,q);a=split[i]
        if mask==0:assert kind[i]==8 and cost[i]==3*P[q]
        else:assert kind[i]==6 and a&mask==a and cost[i]==(P[q] if a==0 else anycost(a,q))+cost[idx(mask^a,1,q)]
    t=[cost[idx(mask,0,q)] for q in range(n)];f2=[cost[idx(mask,1,q)] for q in range(n)];f3=[cost[idx(mask,2,q)] for q in range(n)];trees.append(t);two.append(f2);three.append(f3);ar=t.copy()
    if mask and mask&(mask-1)==0:ar[mask.bit_length()]=0
    anytree.append(ar)
    if mask:
        bit=mask&-mask;imb[mask]=imb[mask^bit]+sign[bit.bit_length()]
    for k,row in [(1,t),(2,f2),(3,f3)]:assert all((row[q]+imb[mask]-k*sign[q])%3==0 for q in range(n))
parts=inequalities=0
for mask in range(1,limit):
    if mask%64==0:assert time.monotonic()-start<540
    t=trees[mask];a=anytree[mask];f2=two[mask];f3=three[mask];need=[]
    for u in range(n):
        for q in adj[u]:assert t[q]<=t[u]+P[u];inequalities+=1
        need.append(max(f2[u],*(t[q] for q in adj[u])));assert f2[u]<=a[u]+P[u] and f3[u]<=P[u]+f2[u] and f3[u]<=a[u]+2*P[u];inequalities+=3
    if mask&(mask-1)==0:
        u=mask.bit_length()
        for q in adj[u]:assert t[q]<=P[u];inequalities+=1
    part=(mask-1)&mask
    while part:
        other=mask^part
        if part<other:
            aa=anytree[part];bb=anytree[other];ta=two[part];tb=two[other]
            for q in range(n):assert need[q]<=aa[q]+bb[q] and f3[q]<=aa[q]+tb[q] and f3[q]<=bb[q]+ta[q]
            parts+=1;inequalities+=n*6
        part=(part-1)&mask
choices=json.loads((B/'choices.json').read_bytes());assert len(choices)==limit;maximum=n
for mask,row in enumerate(choices):
    minima=[min(table[mask][q] for table in [trees,two,three] for q in range(n) if table[mask][q]%3==r) for r in range(3)];assert minima==[z[0] for z in row]
    for residue,(z,q,k) in enumerate(row):assert z==cost[idx(mask,k-1,q)] and z%3==residue
    for z in minima:
        if z>=4:maximum=max(maximum,z-3+mask.bit_count())
critical=[]
for mask,row in enumerate(choices):
    N=maximum-mask.bit_count()
    if N>=1 and N<row[N%3][0]:critical.append(dict(mask=mask,N=N,input=[N]+[int(mask>>(v-1)&1) for v in range(1,n)]))
assert critical and choices[-1][1][0]>1;out=dict(graph='FanoInc14',n=n,group_size=len(maps),all14_source_maps_verified=True,nodes=len(cost),masks=limit,proper_partitions=parts,full_inequalities=inequalities,every_attaining_node_and_lower_inequality_checked=True,exact_binary_buffer_AS_oracle_certified=True,exact_L_AS=maximum,source0_critical_AS=critical,scope='Exact AS only, all sources/unbounded positive source count; no general threshold or universal ASH* conclusion',seconds=time.monotonic()-start);(B/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k!='source0_critical_AS'}))
