#!/usr/bin/env python3
"""CAM-S015-89 (M2b): explicit winning move sequence for EVERY configuration of
mass 15 on G9.  Loser sets L_m (m<=14) are first recomputed by the bare
definition over all configurations; each mass-15 configuration is then driven
greedily along moves into non-losers until one vertex remains occupied.  Output
(xz-compressed text): one line per configuration '<c0..c8>:<u v u v ...>' using
digits.  The checker (s015_cert_full15_check.py) needs no loser sets.
usage: s015_cert_full15.py OUT.txt.xz"""
import sys, lzma
EDGES = [(0, 3), (1, 4), (0, 5), (3, 5), (0, 6), (2, 6), (3, 6), (1, 7), (4, 7), (5, 7), (1, 8), (2, 8), (4, 8), (6, 8)]
N = 9; NB = [[] for _ in range(N)]
for a, b in EDGES: NB[a].append(b); NB[b].append(a)

def comps(m, k):
    if k == 1: yield (m,); return
    for f in range(m, -1, -1):
        for r in comps(m - f, k - 1): yield (f,) + r

def kids(c):
    for u in range(N):
        if c[u] >= 2:
            for v in NB[u]:
                d = list(c); d[u] -= 2; d[v] += 1; yield u, v, tuple(d)

L = {0: set()}
for m in range(1, 15):
    L[m] = {c for c in comps(m, N) if sum(1 for x in c if x) > 1 and all(d in L[m - 1] for _, _, d in kids(c))}
out = lzma.open(sys.argv[1], 'wt'); count = 0
for c in comps(15, N):
    x = c; seq = []
    while sum(1 for t in x if t) > 1:
        for u, v, d in kids(x):
            if d not in L[sum(d)]:
                seq.append(f'{u}{v}'); x = d; break
        else:
            raise SystemExit('NO WINNING MOVE FROM ' + str(x))
    out.write(''.join(map(str, c)) if max(c) < 10 else '.'.join(map(str, c)))
    out.write(':' + ' '.join(seq) + '\n'); count += 1
out.close(); print('mass15 configurations certified', count)
