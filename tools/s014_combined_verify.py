"""Independent recursion for alpha and full Floyd/subset score comparison."""
import hashlib,itertools,json,lzma,struct,sys
from pathlib import Path
B=Path('evidence/S014/combined_bound');shard=int(sys.argv[1]);D=B/f'shard{shard}'
for pre in [B/'preflight.json',D/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cases=json.loads((B/'inputs.json').read_bytes())['cases'];rows=json.loads((D/'results.json').read_bytes());selected=[c for c in cases if c['index']%2==shard];assert len(rows)==len(selected)
def matrix(V,E):
    m={(u,v):(0 if u==v else 1 if frozenset([u,v]) in E else 1000) for u in V for v in V}
    for k in V:
        for u in V:
            for v in V:m[u,v]=min(m[u,v],m[u,k]+m[k,v])
    return m
trees=0;gaps=[]
for c,r in zip(selected,rows):
    n=c['n'];V=list(range(n));E={frozenset(e) for e in c['edges']};dist=matrix(V,E);assert all(dist[0,v]<1000 for v in V) and all((dist[0,u]-dist[0,v])%2 for u,v in c['edges']);adj={u:{v for v in V if frozenset([u,v]) in E} for u in V};best=0;maxima=set()
    def independent(available,chosen):
        global best,maxima
        if len(available)+len(chosen)<best:return
        if not available:
            if len(chosen)>best:best=len(chosen);maxima=set()
            if len(chosen)==best:maxima.add(frozenset(chosen))
            return
        u=min(available);independent(available-{u}-adj[u],chosen|{u});independent(available-{u},chosen)
    independent(set(V),set());assert best==r['alpha'];actual={frozenset(v for v in V if mask>>v&1) for mask in r['maximum_independent_sets']};assert len(actual)==len(r['maximum_independent_sets']) and actual==maxima
    expected={}
    for size in range(2,n+1):
        for S in itertools.combinations(V,size):
            F={e for e in E if e<=set(S)}
            if len(F)!=size-1:continue
            td=matrix(S,F)
            if any(td[u,v]!=dist[u,v] for u,v in itertools.product(S,repeat=2)):continue
            deg={u:sum(u in e for e in F) for u in S};scores={str(root):1+sum(deg[v]*(1<<td[root,v]) for v in S if v==root or deg[v]!=1)+sum(deg[v]==1 and v!=root for v in S) for root in S};expected[sum(1<<v for v in S)]=scores
    assert len(expected)==len(r['trees']) and {x['mask'] for x in r['trees']}==set(expected)
    for t in r['trees']:assert t['scores']==expected[t['mask']] and t['threshold']==max(t['scores'].values())
    R=max(max(scores.values()) for scores in expected.values());bound=max(n+1,3*best+1 if best>=2 else 0,R);assert (r['R'],r['bound'],r['threshold'])==(R,bound,c['threshold']) and r['strict_gap']==(c['threshold']>bound);assert bound<=c['threshold'];trees+=len(expected)
    if r['strict_gap']:
        witness=r['critical_AS_witness']
        if witness is not None:
            assert len(witness)==n and sum(witness)==c['threshold']-1 and sum(z>1 for z in witness)<=1;found=False
            with lzma.open(c['certificate'],'rb') as f:
                while head:=f.read(12):
                    mass,count=struct.unpack('<IQ',head)
                    for _ in range(count):
                        z=f.read(16)
                        if mass==c['threshold']-1 and list(z[:n])==witness:found=True
            assert found
        gaps.append(dict(index=c['index'],source=c['id'],threshold=c['threshold'],bound=bound,R=R,alpha=best,critical_AS_witness=witness))
out=dict(shard=shard,cases=len(rows),full_isometric_tree_sets=trees,all_alpha_maximum_sets_equal=True,all_root_scores_equal=True,strict_gaps=gaps,scope='Fixed certified thresholds only; proposed combined ceiling UNPROVED unless refuted by listed strict gap; universal ASH* OPEN')
(D/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(shard=shard,cases=len(rows),trees=trees,strict_gaps=len(gaps))))
