#!/usr/bin/env python3
"""Independent reverse-edge dynamic programming for full eight-vertex threshold layers.

Construct win(m) from legal predecessor of win(m-1); stack additionally
has every singleton-support state as a seed at all m. No recursion or calls
to forward solver. Emit counts for every layer up to cutoff.
"""
import sys
import json
from itertools import combinations

N=8

def comps(t,n=N):
    # Stars and bars by independently enumerating divider positions.
    for div in combinations(range(t+n-1),n-1):
        prev=-1;out=[]
        for pos in div:
            out.append(pos-prev-1);prev=pos
        out.append(t+n-2-prev)
        yield tuple(out)

def compute(name,edges,limit):
    win_stack=set();win_clear=set(); rows=[]
    # All inverse steps derive parent p from winner child d: p_i=d_i+2, p_j=d_j-1.
    for t in range(1,limit+1):
        ss={tuple(t if i==j else 0 for i in range(N)) for j in range(N)}
        if t>1:
            for child in win_stack:
                for a,b in edges:
                    for i,j in ((a,b),(b,a)):
                        if child[j]>0:
                            parent=list(child);parent[i]+=2;parent[j]-=1
                            ss.add(tuple(parent))
        cs=set()
        if t==1:cs=set(comps(1))
        else:
            for child in win_clear:
                for a,b in edges:
                    for i,j in ((a,b),(b,a)):
                        if child[j]>0:
                            parent=list(child);parent[i]+=2;parent[j]-=1
                            cs.add(tuple(parent))
        win_stack,win_clear=ss,cs
        if t>=2:
            all_t=set(comps(t))
            ash={c for c in all_t if sum(x>1 for x in c)<=1}
            rows.append(dict(t=t,total=len(all_t),as_total=len(ash),nonstack=len(all_t-ss),as_nonstack=len(ash-ss),nonclear=len(all_t-cs),as_nonclear=len(ash-cs)))
    return dict(graph=name,rows=rows)

def main():
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--max-total',type=int,default=14);a=p.parse_args()
    reported=[json.loads(l[12:]) for l in open(a.input) if l.startswith('RESULT_JSON ')]
    results=[]
    for x in reported:
        if x['graph'] not in ('W8','K4_bridge_K4'):continue
        independently=compute(x['graph'],x['edges'],a.max_total)
        expected=[r for r in x['rows'] if r['t']<=a.max_total]
        assert independently['rows']==expected,(x['graph'],independently['rows'],expected)
        results.append(dict(graph=x['graph'],rows_checked=len(expected),same=True))
    print(json.dumps(results,sort_keys=True))
if __name__=='__main__':main()
