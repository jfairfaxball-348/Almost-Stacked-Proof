"""Fresh direct full-input negative closures and positive histories, CAM26."""
import json,lzma
from pathlib import Path
B=Path('evidence/S014/criticalcert')
def main():
    out=[]
    for case in json.loads((B/'inputs.json').read_bytes())['cases']:
        n=case['graph']['n'];arcs=sorted((u,v) for e in case['graph']['edges'] for u,v in [e,e[::-1]]);negatives=[]
        for c in [case['c'],case['AS']]:
            root=tuple(c);seen={root};todo=[root]
            for x in todo:
                assert sum(z>0 for z in x)>1
                for u,v in arcs:
                    if x[u]<2:continue
                    y=list(x);y[u]-=2;y[v]+=1;y=tuple(y)
                    if y not in seen:seen.add(y);todo.append(y)
                if len(seen)>300000:raise RuntimeError('STATE_CAP_UNKNOWN')
            negatives.append(dict(c=c,states=sorted(seen)))
        winners=[]
        for row in case['pairs']:
            for cand in row['candidates']:
                memo={}
                def trace(x):
                    if x in memo:return memo[x]
                    if len(memo)>300000:raise RuntimeError('STATE_CAP_UNKNOWN')
                    if sum(z>0 for z in x)==1:memo[x]=[];return []
                    for u,v in arcs:
                        if x[u]<2:continue
                        y=list(x);y[u]-=2;y[v]+=1;tail=trace(tuple(y))
                        if tail is not None:memo[x]=[[u,v]]+tail;return memo[x]
                    memo[x]=None;return None
                moves=trace(tuple(cand['d']));assert moves is not None;winners.append(dict(s=row['s'],t=row['t'],v=cand['v'],d=cand['d'],moves=moves))
        out.append(dict(case=case,negative=negatives,winners=winners))
    (B/'certificates.json.xz').write_bytes(lzma.compress((json.dumps(out,separators=(',',':'))+'\n').encode()));print('Fresh complete negative closures and literal positive histories saved.',flush=True)
if __name__=='__main__':main()
