import itertools,json,time
from pathlib import Path
B=Path('evidence/S014/retract_trees');start=time.monotonic();out=[]
def distances(vertices,edges):
    adj={u:[] for u in vertices}
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    D={}
    for s in vertices:
        dist={s:0};todo=[s]
        for u in todo:
            for v in adj[u]:
                if v not in dist:dist[v]=dist[u]+1;todo.append(v)
        D[s]=dist
    return adj,D
for g in json.loads((B/'inputs.json').read_bytes())['graphs']:
    n=g['n'];adj,D=distances(list(range(n)),g['edges']);assert all(len(D[u])==n for u in range(n));colors={u:D[0][u]%2 for u in range(n)};trees=[]
    for mask in range(1<<n):
        assert time.monotonic()-start<540
        V=[v for v in range(n) if mask>>v&1]
        if len(V)<2:continue
        E=[e for e in g['edges'] if all(mask>>v&1 for v in e)]
        if len(E)!=len(V)-1:continue
        ta,td=distances(V,E)
        if len(td[V[0]])<len(V) or any(td[u][v]!=D[u][v] for u,v in itertools.product(V,repeat=2)):continue
        f={v:v for v in V}
        for x in range(n):
            if x in f:continue
            possible=[y for y in V if colors[y]==colors[x] and all(td[y][f[u]]<=D[x][u] for u in f)];assert possible;f[x]=possible[0]
        scores={r:1+sum(len(ta[v])*2**td[r][v] for v in V if v==r or len(ta[v])>1)+sum(len(ta[v])==1 and v!=r for v in V) for r in V}
        trees.append(dict(vertices=V,retraction=[f[x] for x in range(n)],scores=scores,threshold=max(scores.values())))
    out.append(dict(graph=g['id'],name=g['name'],trees=trees,maximum=max(r['threshold'] for r in trees)))
(B/'trees.json').write_text(json.dumps(out,separators=(',',':'))+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(graphs=len(out),trees=sum(len(r['trees']) for r in out),crown_maxima=[r['maximum'] for r in out[-3:]],seconds=time.monotonic()-start)))
