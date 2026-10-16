#!/usr/bin/env python3
"""CAM-S015-84 hostile finite challenge of symbolic items S015-122/123 on
COMPLETE critical layers (membership only: every tested configuration has
mass exactly L_all, so it loses iff it lies in the complete critical layer).
122 (two-step shift): for critical c on connected G (not K2), every v with c_v>=1
    and every w~v, SOME x in N(w)\\{v} has c-e_v+e_x winning.
123 (one-step shift): for every v with c_v>=1, SOME u~v has c-e_v+e_u winning.
123h (heavy): for heavy s and EVERY x, SOME u~s has c+e_x-2e_s+e_u winning.
Also tallies heavy parities in critical non-AS inputs.
usage: s015_shift.py crit_file"""
import sys
sys.path.insert(0, 'tools')
from s015_graphs import g6_decode

def main():
    bad = {'122': 0, '123': 0, '123h': 0}
    checks = {'122': 0, '123': 0, '123h': 0}
    even_heavy_inputs = 0; nonas = 0; examples = []
    for line in open(sys.argv[1]):
        f = line.split()
        n, E = g6_decode(f[0])
        if n == 2:
            continue
        nb = [[] for _ in range(n)]
        for a, b in E:
            nb[a].append(b); nb[b].append(a)
        C = {tuple(map(int, x.split('.'))) for x in f[2:]}
        def win(d):
            return tuple(d) not in C
        for c in C:
            hv = [i for i in range(n) if c[i] > 1]
            if len(hv) >= 2:
                nonas += 1
                if any(c[i] % 2 == 0 for i in hv):
                    even_heavy_inputs += 1
                    if len(examples) < 20: examples.append((f[0], c))
            for v in range(n):
                if c[v] < 1:
                    continue
                checks['123'] += 1
                ok = False
                for u in nb[v]:
                    d = list(c); d[v] -= 1; d[u] += 1
                    if win(d): ok = True
                if not ok: bad['123'] += 1
                for w in nb[v]:
                    checks['122'] += 1
                    ok = False
                    for x in nb[w]:
                        if x == v: continue
                        d = list(c); d[v] -= 1; d[x] += 1
                        if win(d): ok = True
                    if not ok: bad['122'] += 1
            for s in hv:
                for x in range(n):
                    checks['123h'] += 1
                    ok = False
                    for u in nb[s]:
                        d = list(c); d[x] += 1; d[s] -= 2; d[u] += 1
                        if win(d): ok = True
                    if not ok: bad['123h'] += 1
    print('checks', checks, 'failures', bad, 'nonAS_critical', nonas, 'with_even_heavy', even_heavy_inputs)
    for g, c in examples:
        print('EVEN_HEAVY', g, '.'.join(map(str, c)))

if __name__ == '__main__':
    main()
