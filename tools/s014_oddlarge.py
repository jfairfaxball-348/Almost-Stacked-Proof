"""CAM21 finite true-head challenge: complete negative DAG / positive moves."""
import itertools,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/oddlarge')
def main():
    inputs=json.loads((B/'inputs.json').read_bytes()); summaries=[]
    for gi,g in enumerate(inputs['graphs']):
        n=g['n']; units=[1<<(8*i) for i in range(n)];N=[set() for _ in range(n)]
        for u,v in g['edges']:N[u].add(v);N[v].add(u)
        arcs=sorted((u,v) for u in range(n) for v in N[u]); memo={}; cap=False
        def win(x):
            if x in memo:return memo[x]!=254
            if len(memo)>=300000:raise RuntimeError('STATE_CAP_UNKNOWN')
            if sum(bool((x>>(8*i))&255) for i in range(n))==1:
                memo[x]=255;return True
            for u,v in arcs:
                if ((x>>(8*u))&255)<2:continue
                y=x-2*units[u]+units[v]
                if win(y):memo[x]=u*n+v;return True
            memo[x]=254;return False
        rows=[]; seen=0; negatives=0
        try:
            for a,b in itertools.product([3,5,7],[3,5,7,9]):
                if a>b:continue
                for bits in itertools.product([0,1],repeat=n-3):
                    c=(a,b,0)+bits;x=sum(z*units[i] for i,z in enumerate(c));cw=win(x);seen+=1
                    if cw:continue
                    negatives+=1
                    for s,t in [(0,1),(1,0)]:
                        if c[s]>c[t]:continue
                        candidates=[]
                        for v in sorted(N[s]-N[t]-{t}):
                            if c[v]:continue
                            d=list(c);d[s]=0;d[t]+=c[s]-1;d[v]=1
                            y=sum(z*units[i] for i,z in enumerate(d));dw=win(y)
                            candidates.append(dict(v=v,d=d,losing=not dw))
                        if candidates:rows.append(dict(c=c,s=s,t=t,candidates=candidates,failed=all(not r['losing'] for r in candidates)))
        except RuntimeError as e:
            assert str(e)=='STATE_CAP_UNKNOWN';cap=True
        cert=B/(g['id']+'.bin.xz')
        with lzma.open(cert,'wb') as f:
            for x,k in sorted(memo.items()):f.write(struct.pack('<QB',x,k))
        summaries.append(dict(graph=g['id'],status='STATE_CAP_UNKNOWN' if cap else 'COMPLETE_REGISTERED_BOX',inputs=seen,losing_inputs=negatives,states=len(memo),rows=rows))
        if gi%10==0:print(json.dumps(dict(graph=gi,states=len(memo),failed_pairs=sum(r['failed'] for r in rows),status=summaries[-1]['status'])),flush=True)
    (B/'results.json.xz').write_bytes(lzma.compress((json.dumps(summaries,separators=(',',':'))+'\n').encode()))
    print(json.dumps(dict(graphs=len(summaries),inputs=sum(r['inputs'] for r in summaries),losers=sum(r['losing_inputs'] for r in summaries),eligible_pairs=sum(len(r['rows']) for r in summaries),failed_pairs=sum(t['failed'] for r in summaries for t in r['rows']),unknown=sum(r['status']!='COMPLETE_REGISTERED_BOX' for r in summaries))),flush=True)
if __name__=='__main__':main()
