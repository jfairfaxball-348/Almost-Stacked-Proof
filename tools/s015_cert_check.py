#!/usr/bin/env python3
"""CAM-S015-89 (M3): separately written verifier for the G9 certificate file.
Re-reads the edge list, rebuilds adjacency as a set of frozensets, and checks:
 1. each negative closed set contains its seed, every member has >=2 occupied
    vertices, and EVERY legal successor of every member (recomputed here) is a
    member (closure => no single pile is reachable => seed is not stackable);
 2. every winning sequence is legal step by step (source holds >=2, true edge)
    and ends with exactly one occupied vertex;
 3. coverage: an independent enumeration of ALL almost-stacked configurations
    of masses 14,15,16 (some vertex v0 with every other vertex <=1) is a subset
    of the certified winners; no AS configuration lacks a sequence.
usage: s015_cert_check.py cert.json"""
import sys, json
from itertools import product

cert = json.load(open(sys.argv[1]))
E = {frozenset(e) for e in cert['edges']}
n = 1 + max(max(e) for e in cert['edges'])
assert n == 9 and len(E) == 14 and all(len(e) == 2 for e in E)

def moves_of(x):
    res = []
    for u in range(n):
        if x[u] > 1:
            for v in range(n):
                if frozenset((u, v)) in E:
                    y = list(x); y[u] -= 2; y[v] += 1; res.append(tuple(y))
    return res

ok = True
for seed, members in cert['negative_closed_sets'].items():
    S = {tuple(m) for m in members}
    s0 = tuple(int(t) for t in seed.split('.'))
    ok &= s0 in S
    ok &= all(sum(1 for t in m if t > 0) >= 2 for m in S)
    ok &= all(y in S for m in S for y in moves_of(m))
    print('negative', seed, 'states', len(S), 'closed', ok)

def replay(start, seq):
    x = list(start)
    for u, v in seq:
        if x[u] < 2 or frozenset((u, v)) not in E:
            return False
        x[u] -= 2; x[v] += 1
    return sum(1 for t in x if t > 0) == 1

good = 0
for key, seq in list(cert['AS_winning_sequences'].items()) + list(cert['mass15_sample_sequences'].items()):
    s = tuple(int(t) for t in key.split('.'))
    if replay(s, seq):
        good += 1
    else:
        ok = False; print('BAD SEQUENCE', key)
print('replayed winning sequences', good)

certified = set(cert['AS_winning_sequences'])
need = 0
for m in (14, 15, 16):
    for v0 in range(n):
        for rest in product((0, 1), repeat=n - 1):
            k = m - sum(rest)
            if k < 0:
                continue
            c = list(rest[:v0]) + [k] + list(rest[v0:])
            need += 1
            if '.'.join(map(str, c)) not in certified:
                ok = False; print('UNCOVERED AS', c)
print('AS configurations (with multiplicity over v0) covered', need, 'missing', len(cert['AS_without_sequence']))
ok &= not cert['AS_without_sequence']
print('CERTIFICATE_OK' if ok else 'CERTIFICATE_FAIL')
