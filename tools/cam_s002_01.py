#!/usr/bin/env python3
"""Exact finite ASH threshold comparison on SIX preregistered 8-vertex graphs.

Proof obligation: every transition strictly decreases mass, so recursion covers all
reachable states; every size-t input is visited without quotienting or pruning.
Independent BFS cold checks for bounded deterministic samples of states.
"""
import argparse
import functools
import hashlib
import itertools
import json
import platform
import sys
import time
from collections import deque

N=8

def edge_list(name):
    if name == 'C8_chord_04':
        return [(i,(i+1)%8) for i in range(8)]+[(0,4)]
    if name == 'C8_triangle_chords':
        return [(i,(i+1)%8) for i in range(8)]+[(0,2),(4,6)]
    if name == 'W8':
        return [(0,i) for i in range(1,8)]+[(i, (i%7)+1) for i in range(1,8)]
    if name == 'K4_bridge_K4':
        return list(itertools.combinations(range(4),2))+list(itertools.combinations(range(4,8),2))+[(3,4)]
    if name == 'K2_6':
        return [(i,j) for i in range(2) for j in range(2,8)]
    if name == 'triangular_ladder':
        return [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(2,3),(6,0),(7,5)]
    raise KeyError(name)

def compositions(m,n=N):
    if n==1:
        yield (m,)
    else:
        for k in range(m+1):
            for tail in compositions(m-k,n-1):
                yield (k,)+tail

def is_as(c):
    return sum(x>1 for x in c)<=1

def solve(name,cutoff):
    edges=sorted({tuple(sorted((a,b))) for a,b in edge_list(name)})
    adj=[[] for _ in range(N)]
    for a,b in edges:
        adj[a].append(b);adj[b].append(a)
    @functools.lru_cache(None)
    def winning(c):
        tot=sum(c)
        if tot==0:return 0
        flag = (1 if sum(x>0 for x in c)==1 else 0) | (2 if tot==1 else 0)
        if flag==3:return flag
        for i,k in enumerate(c):
            if k<2:continue
            for j in adj[i]:
                nxt=list(c);nxt[i]-=2;nxt[j]+=1
                flag |= winning(tuple(nxt))
                if flag==3:return 3
        return flag
    def bfs_independent(start):
        q=deque([start]);seen={start};can_stack=False;can_clear=False
        while q:
            c=q.popleft()
            if sum(x>0 for x in c)==1:can_stack=True
            if sum(c)==1:can_clear=True
            if can_stack and can_clear:return 3
            # Different move generator: iterate the undirected edge list in two orientations.
            for u,v in edges:
                for i,j in ((u,v),(v,u)):
                    if c[i]>=2:
                        nxt=tuple(c[k]-2*(k==i)+(k==j) for k in range(N))
                        if nxt not in seen:
                            seen.add(nxt);q.append(nxt)
        return int(can_stack)+2*int(can_clear)
    rows=[];mismatches=[];time0=time.monotonic(); samples=0; first_fail=None
    for t in range(2,cutoff+1):
        row=dict(t=t,total=0,as_total=0,nonstack=0,as_nonstack=0,nonclear=0,as_nonclear=0)
        candidates=[]
        for c in compositions(t):
            row['total']+=1
            q=is_as(c)
            if q:row['as_total']+=1
            w=winning(c)
            if not (w&1): row['nonstack']+=1;row['as_nonstack']+=int(q)
            if not (w&2): row['nonclear']+=1;row['as_nonclear']+=int(q)
            if t in (2,5,8,11,cutoff) and (row['total']%1009==1 or (q and row['as_total']%547==1)):
                candidates.append((c,w))
            if first_fail is None and row['as_nonstack']==0 and row['nonstack']>0:pass
        rows.append(row)
        # Check complete t<=4 and deterministic samples for larger t via separate BFS.
        if t<=4:
            candidates=[(c,winning(c)) for c in compositions(t)]
        for c,w in candidates[:12]:
            b=bfs_independent(c);samples+=1
            if b!=w:mismatches.append((t,list(c),w,b))
        print(name,'t',t,'all',row['total'],'as',row['as_total'],'stack loss',row['nonstack'],'as loss',row['as_nonstack'],'clear loss',row['nonclear'],'as loss',row['as_nonclear'], 'memo',winning.cache_info().currsize,flush=True)
    counterexamples=[]
    for goal in ('stack','clear'):
        suffix= 'nonstack' if goal=='stack' else 'nonclear';a='as_'+suffix
        for row in rows:
            if row[a]==0 and row[suffix]>0:
                t=row['t']; bad = next(c for c in compositions(t) if not winning(c)&(1 if goal=='stack' else 2))
                counterexamples.append(dict(goal=goal,t=t,graph=name,c=list(bad),bitmask=winning(bad),bfs_bitmask=bfs_independent(bad)))
                break
    return dict(graph=name,edges=[list(e) for e in edges],cutoff=cutoff,rows=rows,conditional_threshold_gaps=counterexamples,independent_bfs_cases=samples,mismatches=mismatches,seconds=round(time.monotonic()-time0,2),python=sys.version,platform=platform.platform())

def main():
    p=argparse.ArgumentParser();p.add_argument('--max-total',type=int,default=14);p.add_argument('--graph',type=str,default='all');args=p.parse_args()
    names=['C8_chord_04','C8_triangle_chords','W8','K4_bridge_K4','K2_6','triangular_ladder']
    for name in ([args.graph] if args.graph!='all' else names):
        result=solve(name,args.max_total)
        print('RESULT_JSON '+json.dumps(result,sort_keys=True,separators=(',',':')),flush=True)
if __name__=='__main__':main()
