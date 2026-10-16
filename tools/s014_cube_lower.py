"""Full inequality audit; no dynamic optimizer or SAT/producer imports."""
import array,hashlib,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/cube_lower');S=Path('evidence/S014/cube_dag');start=time.monotonic()
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
upper=json.loads((S/'verification_v2.json').read_bytes());assert upper['complete_AS_tail_upper31'] and upper['every_node_has_sound_well_founded_production'];raw=lzma.decompress((S/'nodes.bin.xz').read_bytes());assert len(raw)==32768*48*8;flat=[x[0] for x in struct.iter_unpack('<IBBH',raw)];trees=[];anytree=[];two=[];three=[];P=[2**v.bit_count() for v in range(16)];sign=[(-1)**v.bit_count() for v in range(16)];adj=[[v^(1<<j) for j in range(4)] for v in range(16)];imb=[0]*32768
for mask in range(32768):
    offset=mask*48;t=flat[offset:offset+16];f2=flat[offset+16:offset+32];f3=flat[offset+32:offset+48];trees.append(t);two.append(f2);three.append(f3);a=t.copy()
    if mask and mask&(mask-1)==0:a[mask.bit_length()]=0
    anytree.append(a)
    if mask:
        bit=mask&-mask;imb[mask]=imb[mask^bit]+sign[bit.bit_length()]
    for k,row in [(1,t),(2,f2),(3,f3)]:assert all(0<row[q]<=1024 and (row[q]+imb[mask]-k*sign[q])%3==0 for q in range(16))
assert trees[0]==P and two[0]==[2*z for z in P] and three[0]==[3*z for z in P];partitions=inequalities=0
for mask in range(1,32768):
    if mask%64==0 and time.monotonic()-start>540:raise RuntimeError('TIME_CAP_UNKNOWN')
    t=trees[mask];a=anytree[mask];f2=two[mask];f3=three[mask];need=[]
    for u in range(16):
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
            for q in range(16):assert need[q]<=aa[q]+bb[q] and f3[q]<=aa[q]+tb[q] and f3[q]<=bb[q]+ta[q]
            partitions+=1;inequalities+=16*7
        part=(part-1)&mask
choices=json.loads((S/'choices.json').read_bytes());assert len(choices)==32768;maximum=16;critical=[]
for mask in range(32768):
    minima=[min(table[mask][q] for table in [trees,two,three] for q in range(16) if table[mask][q]%3==r) for r in range(3)];assert minima==[z[0] for z in choices[mask]]
    for z in minima:
        if z-3>=1:maximum=max(maximum,z-3+mask.bit_count())
    N=30-mask.bit_count()
    if N>=1 and N<minima[N%3]:critical.append(dict(mask=mask,N=N,input=[N]+[int(mask>>(v-1)&1) for v in range(1,16)]))
assert maximum==30 and critical
out=dict(exact_binary_buffer_AS_oracle_certified=True,source=0,masks=32768,nodes=1572864,proper_unordered_partitions=partitions,full_inequalities=inequalities,all_signed_residues_verified=True,all_global_minima_equal=True,exact_L_AS=maximum,source0_critical_AS=critical,scope='Exact AS only on fixed Q4, all XOR sources; no general threshold or universal ASH* conclusion',seconds=time.monotonic()-start);(B/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k!='source0_critical_AS'}))
