"""Independent tuple reachability, whole selected sets and literal parser."""
import hashlib,itertools,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/coordinate_maximal')
for file in ['preflight.json','analysis_preflight.json']:
    for p,h in json.loads((B/file).read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
a=json.loads((B/'analysis.json').read_bytes());d=(9,0,0,3);neighbors=[[1],[0,2],[1,3],[2]]
closed={d};todo=[d]
for c in todo:
    assert len(closed)<=5000 and sum(z>0 for z in c)>1
    for u in range(4):
        if c[u]<2:continue
        for v in neighbors[u]:
            y=list(c);y[u]-=2;y[v]+=1;y=tuple(y)
            if y not in closed:closed.add(y);todo.append(y)
raw=lzma.decompress((B/'d_negative.bin.xz').read_bytes());assert len(raw)%16==0
saved=[tuple(raw[i:i+4]) for i in range(0,len(raw),16)];assert all(not any(raw[i+4:i+16]) for i in range(0,len(raw),16));assert len(saved)==len(set(saved))==a['negative_states'] and set(saved)==closed
expected=[]
for k in [1,2]:
    for sites in itertools.combinations_with_replacement(range(4),k):
        c=list(d)
        for v in sites:c[v]+=1
        expected.append((c,None,list(sites)))
expected.extend(([d[v]+int(v==s) for v in range(4)],s,None) for s in range(4));assert len(a['witnesses'])==len(expected)==18
total=0
for row,(initial,root,sites) in zip(a['witnesses'],expected):
    assert row['input']==initial and row['root']==root and row['winning'] and row.get('insertions')==sites;x=initial.copy();balance=[0]*4
    assert len(row['moves'])<=100
    for u,v in row['moves']:
        assert v in neighbors[u] and x[u]>=2;x[u]-=2;x[v]+=1;balance[u]+=2;balance[v]-=1;total+=1
    assert x==row['final'] and sum(z>0 for z in x)==1
    if root is not None:assert x==[int(v==root) for v in range(4)] and tuple(balance)==d
layer=None
with lzma.open(B/'P4_stack_threshold.bin.xz','rb') as f:
    while head:=f.read(12):
        mass,count=struct.unpack('<IQ',head);cs=[tuple(f.read(16)[:4]) for _ in range(count)]
        if mass==12:layer=set(cs)
assert layer==set(map(tuple,a['mass12_losers'])) and not any(sum(z>=2 for z in c)<=1 for c in layer)
heavy=min(sum(z>=2 for z in c) for c in layer);Q=max(sum(z*z for z in c) for c in layer);qm={c for c in layer if sum(z*z for z in c)==Q};P=min(c[0]+2*c[1]+2*c[2]+c[3] for c in qm);qpm={c for c in qm if c[0]+2*c[1]+2*c[2]+c[3]==P}
assert (heavy,Q,P)==(a['minimum_heavy'],a['Q'],a['P'])==(2,90,12) and qm==set(map(tuple,a['Qmax'])) and qpm==set(map(tuple,a['QPmax']))=={d,d[::-1]}
for name,T in [('P4',15),('P4plus02',8),('P4plus03',7),('P4plus13',8)]:
    r=json.loads((B/(name+'_stack_threshold_verification.json')).read_bytes());assert r['scope']=='EXACT_THRESHOLD' and r['threshold']==T
out=dict(full_negative_states=len(closed),literal_witnesses=18,literal_moves=total,neutral_roots=4,positive_insertions_checked=14,mass12_losers=len(layer),minimum_heavy=heavy,Q=Q,P=P,thresholds=[15,8,7,8],complete_selected_sets_equal=True,all_coordinate_extensions_win_by_threshold_and_witnesses=True,scope='Actual noncritical P4 obstruction only; universal ASH* OPEN')
(B/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
