#!/usr/bin/env python3
"""Standalone independent losing-layer recurrence verification of G9."""
from itertools import combinations
edges=[(0,3),(0,5),(0,6),(1,4),(1,7),(1,8),(2,6),(2,8),(3,5),(3,6),(4,7),(4,8),(5,7),(6,8)]
adj=[[] for _ in range(9)]
for u,v in edges:adj[u].append(v);adj[v].append(u)
expected={"STACK":[36,128,383,930,1862,2887,3280,2510,1301,473,124,21,2,0],
          "CLEAR":[36,137,384,932,1863,2887,3280,2510,1301,473,124,21,2,0]}
star={(0,0,1,0,0,5,0,8,0),(0,0,1,0,0,8,0,5,0)}
w13=(0,0,1,0,1,11,0,0,0)
def successors(c):
    for u in range(9):
        if c[u]>=2:
            for v in adj[u]:
                s=list(c);s[u]-=2;s[v]+=1;yield tuple(s)
def candidates(previous,t):
    for subset in combinations(range(9),t):
        c=[0]*9
        for i in subset:c[i]=1
        yield tuple(c)
    for s in previous:
        for v in range(9):
            if s[v]:
                for u in adj[v]:
                    c=list(s);c[u]+=2;c[v]-=1;yield tuple(c)
for mode in ("STACK","CLEAR"):
    previous=set()
    counts=[]
    for t in range(2,16):
        pool=set(candidates(previous,t))
        losers={c for c in pool if not (mode=="STACK" and sum(x>0 for x in c)==1)
                and all(d in previous for d in successors(c))}
        counts.append(len(losers))
        if t==13:assert w13 in losers
        if t==14:assert losers==star
        if t==15:assert not losers
        previous=losers
    assert counts==expected[mode],(mode,counts)
    print(mode,counts,"PASS")
print("S021_INDEPENDENT_RECURRENCE_PASS")
