"""Independent distance matrices, exhaustive subsets and edge-by-edge maps."""
import hashlib,itertools,json
from pathlib import Path
B=Path('evidence/S014/retract_trees')
for pre in [B/'preflight.json',B/'trees_derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes());saved=json.loads((B/'trees.json').read_bytes());assert len(saved)==len(cfg['graphs'])==31;count=maps=0
def matrix(V,E):
    m={(u,v):(0 if u==v else 1 if frozenset([u,v]) in E else 1000) for u in V for v in V}
    for k in V:
        for u in V:
            for v in V:m[u,v]=min(m[u,v],m[u,k]+m[k,v])
    return m
for g,row in zip(cfg['graphs'],saved):
    n=g['n'];V=list(range(n));E={frozenset(e) for e in g['edges']};D=matrix(V,E);assert len(E)==len(g['edges']) and all(len(e)==2 for e in E);assert all(D[0,v]<1000 for v in V) and all((D[0,u]-D[0,v])%2 for u,v in g['edges']);expected={}
    for size in range(2,n+1):
        for S in itertools.combinations(V,size):
            F={e for e in E if e<=set(S)}
            if len(F)!=size-1:continue
            td=matrix(S,F)
            if any(td[u,v]!=D[u,v] for u,v in itertools.product(S,repeat=2)):continue
            deg={u:sum(u in e for e in F) for u in S};scores={str(r):1+sum(deg[v]*(1<<td[r,v]) for v in S if v==r or deg[v]!=1)+sum(deg[v]==1 and v!=r for v in S) for r in S};expected[S]=(F,scores)
    assert len(row['trees'])==len(expected) and {tuple(r['vertices']) for r in row['trees']}==set(expected)
    for r in row['trees']:
        S=tuple(r['vertices']);F,scores=expected[S];f=r['retraction'];assert len(f)==n and set(f)<=set(S) and all(f[v]==v for v in S);assert all(frozenset([f[u],f[v]]) in F for u,v in g['edges']);assert r['scores']==scores and r['threshold']==max(scores.values());count+=1;maps+=len(E)
    R=max(max(scores.values()) for F,scores in expected.values());assert row['graph']==g['id'] and row['name']==g['name'] and row['maximum']==R
    if 'k' in g:
        k=g['k'];assert R==max(3*k-2,15)<3*k+1;assert E=={frozenset([i,k+j]) for i in range(k) for j in range(k) if i!=j}
        witness=[2*k+1]+[1]*(k-1)+[0]*k;support={v for v,z in enumerate(witness) if z};assert sum(witness)==3*k and len(support)==k and all(not(e<=support) for e in E) and sum(z>1 for z in witness)==1
out=dict(graphs=31,isometric_trees=count,ambient_edges_mapped=maps,all_full_subtree_sets_equal=True,all_retractions_true_loopless_edge_maps=True,all_earlier_TreeStack_root_scores_equal=True,crown_maxima=[r['maximum'] for r in saved[-3:]],crown_AS_lower_thresholds=[16,19,22],scope='Scoped bridge101 and actual stronger-selection obstruction102; universal ASH* OPEN')
(B/'trees_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
