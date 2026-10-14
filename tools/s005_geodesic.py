"""Bounded independent BFS challenge to the proposed two-site AS witness."""
import json,collections,hashlib,time
from pathlib import Path

def bfs(c,e,goal):
 arcs=[(a,b) for u,v in e for a,b in [(u,v),(v,u)]];start=tuple(c);parent={start:None};q=[start]
 for x in q:
  if goal(x):
   path=[];z=x
   while parent[z] is not None:
    prev,move=parent[z];path.append({'from':prev,'move':move,'to':z});z=prev
   return True,len(parent),list(reversed(path)),None
  for u,v in arcs:
   if x[u]>=2:
    y=list(x);y[u]-=2;y[v]+=1;y=tuple(y)
    if y not in parent:parent[y]=(x,(u,v));q.append(y)
 return False,len(parent),None,hashlib.sha256(json.dumps(sorted(parent),separators=(',',':')).encode()).hexdigest()
def main():
 out=[];st=time.monotonic()
 for r in json.loads(Path('evidence/S003/T2_analysis.json').read_text()):
  n=r['n']
  if not 2<=n<=5:continue
  e=[tuple(map(int,p.split('-'))) for p in r['edges'].split(',')];adj=[[] for _ in range(n)]
  for u,v in e:adj[u].append(v);adj[v].append(u)
  for root in range(n):
   dist={root:0};q=[root]
   for u in q:
    for v in adj[u]:
     if v not in dist:dist[v]=dist[u]+1;q.append(v)
   for s in range(n):
    if s==root:continue
    d=dist[s];c=[0]*n;c[root]=(1<<(d+1))-3;c[s]=1
    win,count,path,dig=bfs(c,e,lambda x:sum(a>0 for a in x)==1)
    out.append({'graph':r['graph'],'n':n,'edges':e,'root':root,'singleton':s,'distance':d,'configuration':c,'stackable':win,'visited':count,'winning_trace':path,'closure_sha256':dig})
 Path('evidence/S005/geodesic_tests.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'tests':len(out),'counterexamples':sum(r['stackable'] for r in out),'first_failure':next((r for r in out if r['stackable']),None),'seconds':time.monotonic()-st}))
if __name__=='__main__':main()
