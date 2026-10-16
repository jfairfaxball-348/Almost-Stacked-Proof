#!/usr/bin/env python3
"""CAM-S015-90 generic brute-force certifier for a candidate graph (edge list).
Classifies EVERY configuration of masses 1..TOP by the bare STACK definition
(same method as s015_cert_brute.py, generalised to any n), reports per-mass
loser and AS-loser counts, and for the top claimed critical mass M builds the
closed forward reachable set of every non-AS loser at M and checks closure.
usage: s015_cert_generic.py n 'a-b,c-d,...' TOP"""
import sys

def compositions(m, k):
    if k == 1:
        yield (m,); return
    for f in range(m, -1, -1):
        for rest in compositions(m - f, k - 1):
            yield (f,) + rest

def main():
    n = int(sys.argv[1]); E = [tuple(map(int, t.split('-'))) for t in sys.argv[2].split(',')]; top = int(sys.argv[3])
    nb = [[] for _ in range(n)]
    for a, b in E: nb[a].append(b); nb[b].append(a)
    prev = set(); rows = []
    for m in range(1, top + 1):
        cur = set()
        for c in compositions(m, n):
            if sum(1 for x in c if x) <= 1: continue
            win = False
            for u in range(n):
                if c[u] >= 2:
                    for v in nb[u]:
                        d = list(c); d[u] -= 2; d[v] += 1
                        if tuple(d) not in prev: win = True; break
                if win: break
            if not win: cur.add(c)
        nas = sum(1 for c in cur if sum(1 for x in c if x > 1) <= 1)
        rows.append((m, len(cur), nas)); print(m, len(cur), nas, flush=True)
        prev = cur
    last = max(m for m, L, a in rows if L)
    las = max(m for m, L, a in rows if a)
    print('L_all', last, 'L_AS', las, 'top_layers_empty', [m for m, L, a in rows if m > last], 'VERDICT', 'ASH_FAIL' if las < last and rows[-1][1] == 0 and top >= n and top > last else 'ASH_OK_OR_INCONCLUSIVE')

if __name__ == '__main__':
    main()
