"""Freeze fixed full shell inventory before mathematical challenge."""
import hashlib,json
from pathlib import Path
B=Path('evidence/S014/shell_witness');B.mkdir(exist_ok=True)
assert not (B/'preflight.json').exists(),'Already frozen; do not overwrite'
def read(p):return json.loads(Path(p).read_bytes())
def write(p,v):Path(p).write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8',newline='\n')
graphs=[dict(id='A'+str(g['id']),n=g['n'],edges=g['edges'],small=True) for g in read('evidence/S014/onebit/inputs.json')['graphs']]
graphs.append(dict(id='Q4',n=16,edges=[[v,v^(1<<j)] for v in range(16) for j in range(4) if v<(v^(1<<j))],small=False))
f=read('evidence/S014/fano_AS/inputs.json');graphs.append(dict(id='FanoInc14',n=14,edges=f['edges'],small=False))
a=read('evidence/S014/metric_gap/inputs.json')['cases'][0]['graph'];graphs.append(dict(id='A182',n=a['n'],edges=a['edges'],small=False))
rows=[]
for g in graphs:
    adj=[[] for _ in range(g['n'])]
    for u,v in g['edges']:adj[u].append(v);adj[v].append(u)
    for s in range(g['n']):
        dist={s:0};todo=[s]
        for u in todo:
            for v in adj[u]:
                if v not in dist:dist[v]=dist[u]+1;todo.append(v)
        assert len(dist)==g['n']
        for ell in range(1,max(dist.values())+1):
            U=sorted(v for v in dist if dist[v]==ell);N=(1<<(ell-1))*(len(U)+3)-3
            rows.append(dict(id=len(rows),graph=g['id'],source=s,ell=ell,U=U,N=N,forward_check=g['small'] and ell<=3))
assert len(graphs)==30 and len(rows)<=1000
write(B/'inputs.json',dict(graphs=graphs,rows=rows))
plan=Path('sessions/S014/PLAN_AMENDMENT_67.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n')
files=[B/'inputs.json',plan,plan.with_suffix('.sha256'),Path('research/S014_BIPARTITE_SHELL_AS_WITNESS.md'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_c067_*.py')]
for p in ['evidence/S014/onebit/inputs.json','evidence/S014/metric_gap/inputs.json','evidence/S014/cube_lower/verification.json','evidence/S014/cube_dag/choices.json','evidence/S014/fano_AS/inputs.json','evidence/S014/fano_AS/verification.json','evidence/S014/fano_AS/choices.json']:files.append(Path(p))
write(B/'preflight.json',dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}))
print(json.dumps(dict(graphs=len(graphs),shell_rows=len(rows),forward_queries=sum(r['forward_check'] for r in rows))))
