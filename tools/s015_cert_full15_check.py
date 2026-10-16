#!/usr/bin/env python3
"""CAM-S015-89 (M3b): separately written replay checker for the full mass-15
certificate.  Verifies: every line's start configuration has mass 15 and 9
coordinates; all lines are distinct; their number equals the number of weak
compositions of 15 into 9 parts computed here by a binomial identity
C(15+8,8)=490314; every move u v is a true edge with >=2 pebbles at u; the end
state has exactly one occupied vertex.
usage: s015_cert_full15_check.py FILE.txt.xz"""
import sys, lzma
from math import comb
E = {frozenset(e) for e in [(0, 3), (1, 4), (0, 5), (3, 5), (0, 6), (2, 6), (3, 6), (1, 7), (4, 7), (5, 7), (1, 8), (2, 8), (4, 8), (6, 8)]}
seen = set(); bad = 0
for line in lzma.open(sys.argv[1], 'rt'):
    head, moves = line.rstrip('\n').split(':')
    c = [int(t) for t in head.split('.')] if '.' in head else [int(t) for t in head]
    if len(c) != 9 or sum(c) != 15: bad += 1; continue
    key = tuple(c)
    if key in seen: bad += 1
    seen.add(key)
    for mv in moves.split():
        u, v = int(mv[0]), int(mv[1])
        if c[u] < 2 or frozenset((u, v)) not in E: bad += 1; break
        c[u] -= 2; c[v] += 1
    if sum(1 for t in c if t) != 1: bad += 1
need = comb(15 + 8, 8)
print('lines', len(seen), 'required', need, 'bad', bad, 'FULL15_OK' if bad == 0 and len(seen) == need else 'FULL15_FAIL')
