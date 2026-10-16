#!/usr/bin/env python3
"""CAM-S015-86 descriptive statistics on COMPLETE critical layers (membership only).
Per file: (a) is EVERY Q-maximal (Q=sum c_v^2) critical loser AS? (b) H2r with the
receiver restricted to a LARGEST heavy pile; (c) H2r restricted to k=0, r=c_s mod 2
("all pairs to t"); (d) graph distance between the two largest heavy sites;
(e) number of graphs whose critical layer contains a non-AS loser.
usage: s015_crit_stats.py crit_file"""
import sys
from itertools import combinations
from collections import Counter
sys.path.insert(0, 'tools')
from s015_graphs import g6_decode

def h(c): return sum(1 for x in c if x > 1)

def h2r(c, C, recv_max=False, pairs_only=False):
    n = len(c); hv = [i for i in range(n) if c[i] > 1]; empty = [i for i in range(n) if c[i] == 0]
    mx = max(c[i] for i in hv)
    for s in hv:
        for t in hv:
            if s == t or (recv_max and c[t] != mx): continue
            for r in ((c[s] % 2,) if pairs_only else (0, 1)):
                for k in ((0,) if pairs_only else (0, 1, 2)):
                    if r + k > c[s]: continue
                    for U in combinations(empty, k):
                        d = list(c); d[t] += c[s] - r - k; d[s] = r
                        for u in U: d[u] += 1
                        if tuple(d) in C: return True
    return False

def dist(n, E, a):
    nb = [[] for _ in range(n)]
    for x, y in E: nb[x].append(y); nb[y].append(x)
    D = {a: 0}; Q = [a]
    for x in Q:
        for y in nb[x]:
            if y not in D: D[y] = D[x] + 1; Q.append(y)
    return D

st = Counter(); dc = Counter(); qfail = []
for line in open(sys.argv[1]):
    f = line.split(); C = {tuple(map(int, x.split('.'))) for x in f[2:]}
    n, E = g6_decode(f[0]); st['graphs'] += 1
    qmax = max(sum(x * x for x in c) for c in C)
    if any(h(c) > 1 for c in C if sum(x * x for x in c) == qmax):
        st['Qmax_nonAS_graphs'] += 1; qfail.append(f[0])
    if any(h(c) > 1 for c in C): st['graphs_with_nonAS_critical'] += 1
    for c in C:
        if h(c) < 2: continue
        st['nonAS'] += 1
        if h2r(c, C, recv_max=True): st['h2r_recv_max'] += 1
        if h2r(c, C, pairs_only=True): st['h2r_pairs_only'] += 1
        hv = sorted(range(n), key=lambda i: -c[i])[:2]
        dc[dist(n, E, hv[0])[hv[1]]] += 1
print(dict(st), 'heavy_distance', dict(sorted(dc.items())))
for g in qfail[:10]: print('QMAX_NONAS', g)
