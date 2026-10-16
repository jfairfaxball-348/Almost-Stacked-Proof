#!/usr/bin/env python3
"""CAM-S015-89 (M1): brute-force STACK truth table on the candidate graph G9.
Every configuration of every mass 1..TOP is classified by the bare definition:
a configuration WINS iff at most one vertex is occupied, or some legal move
(two pebbles off u, one onto a true neighbour v) produces a winning
configuration.  Masses are processed in increasing order; every configuration
of mass m is enumerated explicitly, so mass m-1 is completely classified when
mass m is processed.  No candidate-generation lemma is used.
usage: s015_cert_brute.py TOP OUT.json"""
import sys, json, hashlib

EDGES = [(0, 3), (1, 4), (0, 5), (3, 5), (0, 6), (2, 6), (3, 6), (1, 7), (4, 7),
         (5, 7), (1, 8), (2, 8), (4, 8), (6, 8)]
N = 9
NB = {v: [] for v in range(N)}
for a, b in EDGES:
    NB[a].append(b)
    NB[b].append(a)


def compositions(m, k):
    if k == 1:
        yield (m,)
        return
    for first in range(m, -1, -1):
        for rest in compositions(m - first, k - 1):
            yield (first,) + rest


def main():
    top = int(sys.argv[1])
    out = {'graph6': 'HCQTaXi', 'edges': EDGES, 'per_mass': {}}
    losers_prev = None
    for m in range(1, top + 1):
        losers = set()
        total = 0
        for c in compositions(m, N):
            total += 1
            occupied = sum(1 for x in c if x)
            if occupied <= 1:
                continue
            win = False
            for u in range(N):
                if c[u] >= 2:
                    for v in NB[u]:
                        d = list(c)
                        d[u] -= 2
                        d[v] += 1
                        if tuple(d) not in losers_prev:
                            win = True
                            break
                if win:
                    break
            if not win:
                losers.add(c)
        heavy = lambda c: sum(1 for x in c if x > 1)
        as_l = sorted(c for c in losers if heavy(c) <= 1)
        rec = {'configurations': total, 'losers': len(losers), 'AS_losers': len(as_l),
               'losers_sha256': hashlib.sha256(repr(sorted(losers)).encode()).hexdigest()}
        if m >= 10:
            rec['loser_list'] = sorted(losers) if len(losers) <= 400 else None
            rec['AS_loser_list'] = as_l if len(as_l) <= 400 else None
        out['per_mass'][m] = rec
        print(m, total, len(losers), len(as_l), flush=True)
        losers_prev = losers
    json.dump(out, open(sys.argv[2], 'w'), indent=0)


if __name__ == '__main__':
    main()
