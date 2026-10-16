"""Independent complete canonical-first-parent replay; no native imports."""
import gzip,hashlib,itertools,json,struct,sys,time
from pathlib import Path
B=Path('evidence/S014/cube_layers_full');d,mass=map(int,sys.argv[1:3]);n=1<<d;D=B/f'd{d}';stem=D/f'mass{mass}';start=time.monotonic()
for pre in [B/'preflight.json',B/'binary_preflight.json',Path(str(stem)+'_derived_preflight.json')]:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
report=json.loads(stem.with_suffix('.json').read_bytes());assert report['status']=='COMPLETE_LAYER' and report['dimension']==d and report['n']==n and report['mass']==mass;low=[];high=[];shifts=[];units=[1<<(8*v) for v in range(n)];adj=[[u^(1<<j) for j in range(d)] for u in range(n)];first=[min(vs) for vs in adj]
for j in range(d):low.append(sum(255<<(8*v) for v in range(n) if v&(1<<j)==0));high.append(sum(255<<(8*v) for v in range(n) if v&(1<<j)));shifts.append(8*(1<<j))
maps=[]
for perm in itertools.permutations(range(d)):
    coords=[sum(((v>>j)&1)<<perm[j] for j in range(d)) for v in range(n)]
    for s in range(n):maps.append(tuple(v^s for v in coords))
mapset=set(maps);assert len(mapset)==n*__import__('math').factorial(d) and tuple(range(n)) in mapset
bylast=[[f for f in maps if f[-1]==p] for p in range(n)]
generators=[tuple(v^(1<<j) for v in range(n)) for j in range(d)]
for j in range(d-1):generators.append(tuple(v if ((v>>j)&1)==((v>>(j+1))&1) else v^(1<<j)^(1<<(j+1)) for v in range(n)))
edges={frozenset([u,v]) for u in range(n) for v in adj[u]}
for f in maps:
    assert len(set(f))==n and {frozenset([f[u],f[v]]) for u in range(n) for v in adj[u]}==edges
    for g in generators:assert tuple(f[g[v]] for v in range(n)) in mapset
def canonical(x):
    data=x.to_bytes(16,'little')[:n];biggest=max(data)
    return max(int.from_bytes(bytes(data[v] for v in f),'little') for p,a in enumerate(data) if a==biggest for f in bylast[p])
def orbit(x):
    data=x.to_bytes(16,'little')[:n];return {int.from_bytes(bytes(data[v] for v in f),'little') for f in maps}
def read(path,expected):
    with gzip.open(path,'rb') as f:
        head=f.read(12);saved,count=struct.unpack('<IQ',head);assert saved==expected and count<=2000000;values=[]
        for _ in range(count):
            raw=f.read(16);assert len(raw)==16 and not any(raw[n:]) and sum(raw[:n])==expected;x=int.from_bytes(raw,'little');assert canonical(x)==x;values.append(x)
        assert not f.read(1)
    assert len(values)==len(set(values)) and values==sorted(values);return set(values)
previous=set() if mass==1 else read(D/f'mass{mass-1}.bin.gz',mass-1)
if mass>1:assert json.loads((D/f'mass{mass-1}_verification.json').read_bytes())['all_full_orbit_losing_sets_equal']
provided=read(D/report['certificate'],mass);assert len(provided)==report['losers'] and hashlib.sha256((D/report['certificate']).read_bytes()).hexdigest()==report['sha256'];candidates=set();status='COMPLETE_LAYER_VERIFIED';computed=set();parents=0;AS_calls=0
def add(x):
    if len(candidates)>=2000000 and x not in candidates:raise RuntimeError('CHECKER_CANDIDATE_CAP_UNKNOWN')
    candidates.add(x)
refined=None
old=Path('evidence/S014/cube_layers')/f'd{d}'
oldv=old/f'mass{mass}_verification.json'
if oldv.exists() and json.loads(oldv.read_bytes())['all_full_orbit_losing_sets_equal']:
    refined=set()
    with gzip.open(old/f'mass{mass}.bin.gz','rb') as handle:
        om,oc=struct.unpack('<IQ',handle.read(12));assert om==mass
        for _ in range(oc):raw=handle.read(16);assert len(raw)==16 and not any(raw[n:]) and sum(raw[:n])==mass;refined.add(canonical(int.from_bytes(raw,'little')))
        assert not handle.read(1)
try:
    if d==4 and mass<=13:
        assert refined is not None;computed=refined;assert computed==provided
    else:
        if mass<=n:
            for U in itertools.combinations(range(n),mass):add(canonical(sum(units[u] for u in U)))
        for number,z in enumerate(previous):
            if number%128==0 and time.monotonic()-start>540:raise RuntimeError('CHECKER_TIME_BOUND_UNKNOWN')
            for child in orbit(z):
                counts=child.to_bytes(16,'little');H=sum(1<<v for v in range(n) if counts[v]>=2)
                for u in range(n):
                    v=first[u]
                    if not counts[v]:continue
                    parentH=H|(1<<u)
                    if counts[v]==2:parentH&=~(1<<v)
                    if parentH&-parentH!=1<<u:continue
                    c=child+2*units[u]-units[v];data=c.to_bytes(16,'little')[:n]
                    if data[n-1]!=max(data) or canonical(c)!=c:continue
                    add(c);parents+=1
        oracle=json.loads(Path('evidence/S014/cube_dag/choices.json').read_bytes()) if d==4 else None
        if d==4:assert json.loads(Path('evidence/S014/cube_lower/verification.json').read_bytes())['exact_binary_buffer_AS_oracle_certified']
        for number,c in enumerate(candidates):
            if number%128==0 and time.monotonic()-start>540:raise RuntimeError('CHECKER_TIME_BOUND_UNKNOWN')
            data=c.to_bytes(16,'little')[:n];occupied=[u for u in range(n) if data[u]]
            if len(occupied)==1:continue
            heavy=[u for u in occupied if data[u]>=2]
            if d==4 and len(heavy)==1:
                s=heavy[0];N=data[s];mask=sum(1<<((v^s)-1) for v in occupied if v!=s);losing=N<oracle[mask][N%3][0];AS_calls+=1
            else:losing=all(canonical(c-2*units[u]+units[v]) in previous for u in heavy for v in adj[u])
            if losing:computed.add(c)
        assert computed==provided,(d,mass,len(computed),len(provided),len(computed-provided),len(provided-computed))
    if refined is not None:assert computed==refined
except RuntimeError as e:status=str(e)
out=dict(group_size=len(maps),method='REFINED_PREVIOUS_COMPLETE_LAYER' if d==4 and mass<=13 else 'FULL_CANONICAL_FIRST_PARENT',dimension=d,n=n,mass=mass,status=status,all_full_orbit_losing_sets_equal=status=='COMPLETE_LAYER_VERIFIED',loser_orbits=len(provided),checker_candidates=len(candidates),canonical_first_parent_instances=parents,exact_AS_oracle_calls=AS_calls,seconds=time.monotonic()-start,scope='Full XOR-orbit layer only if equality flag true; no universal ASH* inference');Path(str(stem)+'_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
