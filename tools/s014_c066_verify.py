"""Independent complete canonical-first-parent replay; no native imports."""
import gzip,hashlib,itertools,json,struct,sys,time
from pathlib import Path
B=Path('evidence/S014/fano_layers');name=sys.argv[1];mass=int(sys.argv[2]);cfg=json.loads((B/'inputs.json').read_bytes());case=next(c for c in cfg['cases'] if c['id']==name);n=case['n'];D=B/name;stem=D/f'mass{mass}';start=time.monotonic()
for pre in [B/'preflight.json',B/'binary_preflight.json',Path(str(stem)+'_derived_preflight.json')]:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
report=json.loads(stem.with_suffix('.json').read_bytes());assert report['status']=='COMPLETE_LAYER' and report['graph']==name and report['n']==n and report['mass']==mass;units=[1<<(8*v) for v in range(n)];edges={frozenset(e) for e in case['edges']};adj=[[v for v in range(n) if frozenset([u,v]) in edges] for u in range(n)];first=[min(vs) for vs in adj];maps={tuple(f) for f in case['maps']};assert tuple(range(n)) in maps
for f in maps:
    assert set(f)==set(range(n)) and {frozenset([f[u],f[v]]) for u,v in case['edges']}==edges
    for g in maps:assert tuple(f[g[v]] for v in range(n)) in maps
bylast=[[f for f in maps if f[-1]==p] for p in range(n)]
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
try:
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
    oracle=json.loads(Path('evidence/S014/fano_AS/choices.json').read_bytes()) if name=='FanoInc14' else None
    if name=='FanoInc14':assert json.loads(Path('evidence/S014/fano_AS/verification.json').read_bytes())['exact_binary_buffer_AS_oracle_certified']
    for number,c in enumerate(candidates):
        if number%128==0 and time.monotonic()-start>540:raise RuntimeError('CHECKER_TIME_BOUND_UNKNOWN')
        data=c.to_bytes(16,'little')[:n];occupied=[u for u in range(n) if data[u]]
        if len(occupied)==1:continue
        heavy=[u for u in occupied if data[u]>=2]
        if name=='FanoInc14' and len(heavy)==1:
            s=heavy[0];N=data[s];f=case['source_maps'][s];mask=sum(1<<(q-1) for q in range(1,n) if data[f[q]]);losing=N<oracle[mask][N%3][0];AS_calls+=1
        else:losing=all(canonical(c-2*units[u]+units[v]) in previous for u in heavy for v in adj[u])
        if losing:computed.add(c)
    assert computed==provided,(name,mass,len(computed),len(provided),len(computed-provided),len(provided-computed))
    if name in ['Q1','Q3']:
        old=Path('evidence/S014/cube_layers_full')/('d1' if name=='Q1' else 'd3');assert json.loads((old/f'mass{mass}_verification.json').read_bytes())['all_full_orbit_losing_sets_equal'];assert computed==read(old/f'mass{mass}.bin.gz',mass)
except RuntimeError as e:status=str(e)
out=dict(graph=name,group_size=len(maps),n=n,mass=mass,status=status,all_full_orbit_losing_sets_equal=status=='COMPLETE_LAYER_VERIFIED',loser_orbits=len(provided),checker_candidates=len(candidates),canonical_first_parent_instances=parents,exact_AS_oracle_calls=AS_calls,seconds=time.monotonic()-start,scope='Full XOR-orbit layer only if equality flag true; no universal ASH* inference');Path(str(stem)+'_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
