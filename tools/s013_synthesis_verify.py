"""Independent bitset/union-find full extremizer and maxima check."""
import itertools,json,lzma,sys
from pathlib import Path
B=Path('evidence/S013')
def load(n):
    p=B/n;raw=p.read_bytes();return json.loads(lzma.decompress(raw) if p.suffix=='.xz' else raw)
def main():
    expected=[]
    for g,table in zip(load('precision_inputs.json'),load('precision_tables.json.xz')):
        n=g['n'];E={frozenset(e) for e in g['edges']};N=[sum(1<<w for w in range(n) if frozenset([v,w]) in E) for v in range(n)];deg=[x.bit_count() for x in N]
        minimal=[v for v in range(n) if not any(N[w]!=N[v] and N[w]&N[v]==N[w] for w in range(n))];triangles=[t for t in itertools.combinations(range(n),3) if all(frozenset(e) in E for e in itertools.combinations(t,2))];TE={frozenset(e) for t in triangles for e in itertools.combinations(t,2)};tri={v for t in triangles for v in t};parent=list(range(n))
        def find(v):
            while parent[v]!=v:v=parent[v]
            return v
        for u,v in (tuple(e) for e in E-TE):parent[find(u)]=find(v)
        parts=sorted([sorted(v for v in range(n) if find(v)==r) for r in set(find(v) for v in range(n))],key=lambda p:p[0]);condition=all((N[s]&N[t] in [N[s],N[t]]) for part in parts for s in part for t in part if s not in tri and t not in tri)
        extrema=[];maxima=[];thresholds={}
        for goal,j in [('stack',1),('clear',0)]:
            maxima_by_type=[-1]*4
            thresholds[goal]=next((t for t in range(n+1,len(table['layers'])) if all(m[j] for c,m in table['layers'][t])),None)
            for mass,layer in enumerate(table['layers']):
                losses=[c for c,m in layer if m[j]==0]
                if not losses:continue
                for c in losses:
                    heavy=[v for v in range(n) if c[v]>1];good=all(v in minimal for v in heavy) and len({N[v] for v in heavy})==len(heavy)
                    predicates=[True,len(heavy)<=1,good,len(heavy)<=1 and all(v in minimal for v in heavy)]
                    for k,p in enumerate(predicates):
                        if p:maxima_by_type[k]=mass
                if mass>=4:
                    def score(c):return (sum(v*v for v in c),-sum(deg[v]*c[v] for v in range(n)))
                    best=max(map(score,losses));selected=sorted(c for c in losses if score(c)==best)
                    for c in selected:
                        hv=[v for v in range(n) if c[v]>1];assert all(v in minimal for v in hv) and all(N[u]&N[v]!=N[u] for u in hv for v in hv if u!=v)
                    extrema.append(dict(goal=goal,mass=mass,Q=best[0],P=-best[1],selected=selected))
            if n>=4 and thresholds[goal]:
                a,b,c,d=maxima_by_type;assert a==c==thresholds[goal]-1 and b==d
                maxima.append(dict(goal=goal,L_all=a,L_AS=b,L_R=c,L_AS_minimal=d))
        s,c=thresholds['stack'],thresholds['clear'];ap=bool(c and c-s>=2 and condition)
        if ap:
            critical=[x for x,m in table['layers'][c-1] if not m[0]];Q=max(sum(a*a for a in x) for x in critical);assert all(sum(a>1 for a in x)<=1 for x in critical if sum(a*a for a in x)==Q)
        expected.append(dict(graph=g['graph'],minimal=minimal,H_components=parts,condition68=condition,applicable68=ap,extrema=extrema,maxima=maxima))
    assert expected==load('synthesis.json')
    result=dict(graphs=len(expected),full_losing_layers=sum(len(r['extrema']) for r in expected),selected_extremizers=sum(len(e['selected']) for r in expected for e in r['extrema']),restricted_comparisons=sum(len(r['maxima']) for r in expected),applicable68=[r['graph'] for r in expected if r['applicable68']],all_equal=True)
    p=B/'synthesis_verification.json';raw=(json.dumps(result,indent=2)+'\n').encode()
    if '--check-only' in sys.argv:assert p.read_bytes()==raw
    else:p.write_bytes(raw)
    print(json.dumps(result))
if __name__=='__main__':main()
