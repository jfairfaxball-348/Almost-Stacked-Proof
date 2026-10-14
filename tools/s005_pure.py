"""Independent theorem prediction versus complete finite layer certificates."""
import collections,json,itertools,time,sys
from pathlib import Path
from s005_verify import load
from s005_geodesic import bfs

def levels(n,edges,r):
 adj=[[] for _ in range(n)]
 for u,v in edges:adj[u].append(v);adj[v].append(u)
 d={r:0};q=[r]
 for u in q:
  for v in adj[u]:
   if v not in d:d[v]=d[u]+1;q.append(v)
 hs=[d[u] for u,v in edges if d[u]==d[v]]
 return d,min(hs) if hs else None

def main():
 out=[];tests=0;st=time.monotonic()
 for path in sorted(Path('evidence/S005').glob('A[2-6]_*.summary.json')):
  m=json.loads(path.read_text())
  if m['mode']!='clear':continue
  _,B=load(Path(str(path).replace('.summary.json','.bin.xz')))
  for r in range(m['n']):
   d,h=levels(m['n'],m['edges'],r);assert h is not None
   tested=0
   for N,layer in enumerate(B,1):
    predicted=N%3!=0 or N>=3*(1<<h)
    actual=(N<<(8*r)) not in layer
    assert predicted==actual,(path,r,h,N,predicted)
    tested+=1
   tests+=tested;out.append({'graph':m['graph'],'edges':m['edges'],'root':r,'h':h,'minimal_clear_multiple3':3*(1<<h),'tested_piles':tested,'all_agree':True})
 e=[(0,1),(1,2),(0,2)];win,count,path,dig=bfs([6,0,0],e,lambda c:sum(c)==1);assert win
 x=[6,0,0]
 for step in path:
  u,v=step['move'];assert tuple(x)==tuple(step['from']) and x[u]>=2 and tuple(sorted((u,v))) in e
  x[u]-=2;x[v]+=1;assert tuple(x)==tuple(step['to'])
 assert sum(x)==1
 result={'pure_tests':tests,'root_graph_cases':len(out),'rows':out,'K3_pile6_trace':path,'seconds':time.monotonic()-st}
 if '--check-only' not in sys.argv:Path('evidence/S005/pure_theorem_tests.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['pure_tests','root_graph_cases','K3_pile6_trace','seconds']}))
if __name__=='__main__':main()
