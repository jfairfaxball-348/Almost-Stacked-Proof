from pathlib import Path
def save(name,t):
    p=Path('tools')/name;raw=t.encode('utf-8')
    if p.exists():assert p.read_bytes()==raw,'Refuse differing source collision'
    else:p.write_bytes(raw)
t=Path('tools/s014_cube_dag_produce.py').read_text(encoding='utf-8');body=t[t.index('try:\n'):];body=body.replace('32768','limit').replace('range(16)','range(n)').replace('count*48','count*3*n')
a=body.index('    for mass in [31,32,33]:');b=body.index('with lzma.open',a);body=body[:a]+body[b:]
body=body.replace("if count==limit:status='UPPER_WITNESS_MISSING_UNKNOWN' if first_missing else 'COMPLETE_AS_TAIL_UPPER31'","if count==limit:status='COMPLETE_POSITIVE_TABLE'")
header='''import heapq,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/fano_AS');cfg=json.loads((B/'inputs.json').read_bytes());n=cfg['n'];limit=1<<(n-1);start=time.monotonic();adj=[[v for u,v in cfg['arcs'] if u==q] for q in range(n)];dist={0:0};todo=[0]
for u in todo:
    for v in adj[u]:
        if v not in dist:dist[v]=dist[u]+1;todo.append(v)
assert len(dist)==n;P=[1<<dist[v] for v in range(n)];INF=10**8;plus=[P.copy()];anytree=[P.copy()];two=[[2*x for x in P]];three=[[3*x for x in P]];porig=[[(0,0,0)]*n];torig=[[(7,0,0)]*n];forig=[[(8,0,0)]*n];status='COMPLETE_POSITIVE_TABLE';first_missing=None
'''
save('s014_c065_produce.py',header+body);print('CAM65 separate general-bipartite positive producer generated')
