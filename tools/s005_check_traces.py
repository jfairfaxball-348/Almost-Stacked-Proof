"""Independent arithmetic/legal-edge replay of auxiliary winning certificates."""
import json
from pathlib import Path

def replay(configuration,steps,edges,mode):
 c=list(configuration);allowed={frozenset(e) for e in edges}
 for step in steps:
  assert list(step['from'])==c
  u,v=step['move'];assert u!=v and frozenset((u,v)) in allowed and c[u]>=2
  d=c.copy();d[u]=c[u]-2;d[v]=c[v]+1
  assert list(step['to'])==d and sum(d)==sum(c)-1 and min(d)>=0;c=d
 assert sum(c)==1 if mode=='clear' else sum(x>0 for x in c)==1
 return c

def main():
 rows=json.loads(Path('evidence/S005/geodesic_tests.json').read_text());n=0
 for r in rows:
  if r['stackable']:
   replay(r['configuration'],r['winning_trace'],r['edges'],'stack');n+=1
 assert n==3 and len(rows)==506
 p=json.loads(Path('evidence/S005/pure_theorem_tests.json').read_text())
 replay([6,0,0],p['K3_pile6_trace'],[(0,1),(1,2),(0,2)],'clear')
 leaf=[{'from':[1,0,4],'move':[2,1],'to':[1,1,2]},
 {'from':[1,1,2],'move':[2,1],'to':[1,2,0]},
 {'from':[1,2,0],'move':[1,0],'to':[2,0,0]},
 {'from':[2,0,0],'move':[0,1],'to':[0,1,0]}]
 replay([1,0,4],leaf,[(0,1),(1,2)],'clear')
 print('PASS: all 3 geodesic failures, K3 pure6 and deferred leaf debt traces')
if __name__=='__main__':main()
