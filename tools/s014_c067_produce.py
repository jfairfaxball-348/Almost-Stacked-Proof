"""Packed forward closure; finite challenge to109, no universal inference."""
import gzip,hashlib,json,time
from pathlib import Path
B=Path('evidence/S014/shell_witness');start=time.monotonic()
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes());graphs={g['id']:g for g in cfg['graphs']};results=[];total=0;stop=False
for row in cfg['rows']:
    if not row['forward_check']:results.append(dict(id=row['id'],status='VALUATION_ONLY'));continue
    if stop:results.append(dict(id=row['id'],status='UNEXECUTED_AFTER_CAP'));continue
    g=graphs[row['graph']];n=g['n'];adj=[[] for _ in range(n)]
    for u,v in g['edges']:adj[u].append(v);adj[v].append(u)
    values=[0]*n;values[row['source']]=row['N']
    for u in row['U']:values[u]=1
    x=int.from_bytes(bytes(values),'little');seen={x};todo=[x];cursor=0;status='COMPLETE_NEGATIVE_CLOSURE'
    while cursor<len(todo):
        if cursor%1024==0 and time.monotonic()-start>540:status='TIME_CAP_UNKNOWN';break
        z=todo[cursor];cursor+=1;data=z.to_bytes(n,'little')
        if sum(v>0 for v in data)==1:status='POTENTIAL_THEOREM_FAILURE';break
        for u,a in enumerate(data):
            if a>=2:
                for v in adj[u]:
                    y=z-(2<<(8*u))+(1<<(8*v))
                    if y not in seen:
                        if len(seen)>=300000 or total+len(seen)>=2000000:status='STATE_CAP_UNKNOWN';break
                        seen.add(y);todo.append(y)
                if status!='COMPLETE_NEGATIVE_CLOSURE':break
        if status!='COMPLETE_NEGATIVE_CLOSURE':break
    path=B/f"query{row['id']}.bin.gz"
    with gzip.open(path,'wb') as f:
        for z in sorted(seen):f.write(z.to_bytes(n,'little'))
    results.append(dict(id=row['id'],status=status,states=len(seen),certificate=path.as_posix(),sha256=hashlib.sha256(path.read_bytes()).hexdigest()));total+=len(seen)
    if status!='COMPLETE_NEGATIVE_CLOSURE':stop=True
(B/'result.json').write_text(json.dumps(dict(rows=results,stored_states=total,seconds=time.monotonic()-start),indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(dict(stored_states=total,queries=len(results),stopped=stop)))
