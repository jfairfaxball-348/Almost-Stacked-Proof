#!/usr/bin/env python3
"""CAM-S015-83 H2r challenge on COMPLETE critical layers (pure set membership).
For a largest loser c (mass M) with h(c)>=2 heavy sites, H2r (S014, UNPROVED)
asks for distinct heavy s,t, r in {0,1}, k in {0,1,2}, r+k<=c_s and a k-set U
of initially EMPTY sites with d=c-(c_s-r)e_s+(c_s-r-k)e_t+1_U losing.  |d|=M,
so d loses iff d is in the complete critical layer.  Also records variant
H2r0 (k=0 only) and the minimum heavy count over each critical layer.
usage: s015_h2r.py crit_file  -> per-graph line and a final summary."""
import sys
from itertools import combinations

def h(c):
    return sum(1 for x in c if x > 1)

def h2r_ok(c, C, kmax):
    n = len(c)
    hv = [i for i in range(n) if c[i] > 1]
    empty = [i for i in range(n) if c[i] == 0]
    for s in hv:
        for t in hv:
            if s == t:
                continue
            for r in (0, 1):
                for k in range(0, kmax + 1):
                    if r + k > c[s]:
                        continue
                    for U in combinations(empty, k):
                        d = list(c)
                        d[t] += c[s] - r - k
                        d[s] = r
                        for u in U:
                            d[u] += 1
                        if tuple(d) in C:
                            return True
    return False

tot_nonas = fail = fail0 = graphs = minh_bad = 0
fails = []
for line in open(sys.argv[1]):
    f = line.split()
    C = {tuple(map(int, x.split('.'))) for x in f[2:]}
    graphs += 1
    if min(h(c) for c in C) > 1:
        minh_bad += 1
    for c in C:
        if h(c) >= 2:
            tot_nonas += 1
            if not h2r_ok(c, C, 2):
                fail += 1
                fails.append((f[0], c))
            if not h2r_ok(c, C, 0):
                fail0 += 1
print('graphs', graphs, 'nonAS_critical', tot_nonas, 'H2r_fail', fail, 'H2r_k0_fail', fail0, 'layers_without_AS', minh_bad)
for g, c in fails[:50]:
    print('H2R_FAIL', g, '.'.join(map(str, c)))
