#!/usr/bin/env python3
"""CAM-S015-89 (M2): explicit certificates for G9 = HCQTaXi.
(a) complete forward closed reachable sets from the two critical losers;
(b) a legal winning move sequence for EVERY almost-stacked configuration of
    masses 14, 15, 16 (pile at r of size >=2 plus 0/1 elsewhere, or 0/1 vectors);
(c) winning sequences for every 98th mass-15 configuration (lexicographic order).
Winning sequences are found by memoised depth-first search; a configuration for
which no sequence is found is reported, never silently skipped.
usage: s015_cert_make.py OUT.json"""
import sys, json
from functools import lru_cache
from itertools import product

EDGES = [(0, 3), (1, 4), (0, 5), (3, 5), (0, 6), (2, 6), (3, 6), (1, 7), (4, 7),
         (5, 7), (1, 8), (2, 8), (4, 8), (6, 8)]
N = 9
ADJ = [[] for _ in range(N)]
for a, b in EDGES:
    ADJ[a].append(b); ADJ[b].append(a)

def succ(c):
    for u in range(N):
        if c[u] >= 2:
            for v in ADJ[u]:
                d = list(c); d[u] -= 2; d[v] += 1
                yield (u, v), tuple(d)

sys.setrecursionlimit(10000)

@lru_cache(maxsize=None)
def solve(c):
    """None if losing, else tuple of moves to a single pile."""
    if sum(1 for x in c if x) <= 1:
        return ()
    for mv, d in succ(c):
        r = solve(d)
        if r is not None:
            return (mv,) + r
    return None

def closed_set(c):
    seen = {c}; todo = [c]
    while todo:
        x = todo.pop()
        for _, y in succ(x):
            if y not in seen:
                seen.add(y); todo.append(y)
    return sorted(seen)

def as_configs(m):
    out = set()
    for mask in range(1 << N):
        b = [(mask >> i) & 1 for i in range(N)]
        if sum(b) == m:
            out.add(tuple(b))
        for r in range(N):
            if b[r]:
                continue
            k = m - sum(b)
            if k >= 2:
                c = list(b); c[r] = k; out.add(tuple(c))
    return sorted(out)

def compositions(m, k):
    if k == 1:
        yield (m,); return
    for f in range(m, -1, -1):
        for rest in compositions(m - f, k - 1):
            yield (f,) + rest

def main():
    cert = {'graph6': 'HCQTaXi', 'edges': EDGES}
    neg = {}
    for c in [(0, 0, 1, 0, 0, 5, 0, 8, 0), (0, 0, 1, 0, 0, 8, 0, 5, 0)]:
        S = closed_set(c)
        assert all(sum(1 for x in s if x) >= 2 for s in S)
        neg['.'.join(map(str, c))] = [list(s) for s in S]
        print('closed set', c, len(S), flush=True)
    cert['negative_closed_sets'] = neg
    wins = {}; missing = []
    for m in (14, 15, 16):
        lst = as_configs(m)
        for c in lst:
            r = solve(c)
            if r is None:
                missing.append(list(c))
            else:
                wins['.'.join(map(str, c))] = [list(x) for x in r]
        print('AS mass', m, len(lst), 'missing', len(missing), flush=True)
    cert['AS_winning_sequences'] = wins
    cert['AS_without_sequence'] = missing
    sample = {}; i = 0
    for c in compositions(15, N):
        if i % 98 == 0:
            r = solve(c)
            if r is None:
                missing.append(list(c))
            else:
                sample['.'.join(map(str, c))] = [list(x) for x in r]
        i += 1
    cert['mass15_sample_sequences'] = sample
    cert['mass15_sample_missing'] = [x for x in missing if sum(x) == 15 and sum(1 for y in x if y > 1) > 1]
    print('mass15 sample', len(sample), flush=True)
    json.dump(cert, open(sys.argv[1], 'w'))

if __name__ == '__main__':
    main()
