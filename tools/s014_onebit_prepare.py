import hashlib,itertools,json
from pathlib import Path
import networkx as nx
B=Path('evidence/S014/onebit');B.mkdir(exist_ok=True);graphs=[];pairs=[]
for a in nx.graph_atlas_g():
    if 2<=len(a)<=6 and nx.is_connected(a) and nx.is_bipartite(a):
        i=len(graphs);graphs.append(dict(id=i,n=len(a),edges=sorted([min(u,v),max(u,v)] for u,v in a.edges())))
        for s,t in itertools.permutations(range(len(a)),2):
            path=nx.shortest_path(a,s,t);d=len(path)-1;pairs.append(dict(id=len(pairs),graph=i,source=s,singleton=t,distance=d,path=path,queries=list(range(0,2**(d+1)+1)) if d<=3 else [],constructive_counts=[2**d,3*2**(d-1),2**(d+1)]))
assert len(graphs)==27 and len(pairs)==654 and sum(len(r['queries']) for r in pairs)<=12000
(B/'inputs.json').write_text(json.dumps(dict(graphs=graphs,pairs=pairs),indent=2)+'\n',encoding='utf-8',newline='\n');plan=Path('sessions/S014/PLAN_AMENDMENT_52.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files=[B/'inputs.json',plan,plan.with_suffix('.sha256'),Path('research/S014_BIPARTITE_ONE_BIT_CONDUCTORS.md'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_onebit*.py')]
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(frozen_graphs=len(graphs),ordered_pairs=len(pairs),queries=sum(len(p['queries']) for p in pairs))))
