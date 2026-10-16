#!/usr/bin/env python3
"""S016 CAM-S016-04(ii) separate verifier (Python) for G9 CLEAR certificates.
usage: s016_g9_clear_cert_check.py cert.txt.xz
Replays every line: each move u>v must be along a G9 edge with >=2 pebbles at u; the final
total mass must be 1.  Coverage: the set of certified configurations must equal (all AS
configurations of mass 14) union (all configurations of mass 15), enumerated here
independently.  Also re-checks the non-clearability of both critical losers from scratch by
an explicit forward closure (no mass-1 state reachable)."""
import lzma, sys, itertools
E = {(0, 3), (0, 5), (0, 6), (1, 4), (1, 7), (1, 8), (2, 6), (2, 8), (3, 5), (3, 6), (4, 7), (4, 8), (5, 7), (6, 8)}
ADJ = E | {(b, a) for a, b in E}
n = 9

def configs(m):
    for bars in itertools.combinations(range(m + n - 1), n - 1):
        prev, c = -1, []
        for b in bars + (m + n - 1,):
            c.append(b - prev - 1)
            prev = b
        yield tuple(c)

need = {c for c in configs(14) if sum(1 for a in c if a > 1) <= 1} | set(configs(15))
seen, bad = set(), 0
for line in lzma.open(sys.argv[1], 'rt'):
    f = line.split()
    if not f:
        continue
    c = tuple(int(x) for x in f[0].split('.'))
    d = list(c)
    ok = True
    for mv in f[1:]:
        u, v = map(int, mv.split('>'))
        if (u, v) not in ADJ or d[u] < 2:
            ok = False
            break
        d[u] -= 2
        d[v] += 1
    if not ok or sum(d) != 1:
        bad += 1
    seen.add(c)
print('required', len(need), 'certified', len(seen), 'missing', len(need - seen), 'extra', len(seen - need), 'bad', bad)

def closure(c):
    S, st = {c}, [c]
    while st:
        x = st.pop()
        for u, v in ADJ:
            if x[u] >= 2:
                y = list(x); y[u] -= 2; y[v] += 1; y = tuple(y)
                if y not in S:
                    S.add(y); st.append(y)
    return S

neg_ok = True
for c in [(0, 0, 1, 0, 0, 5, 0, 8, 0), (0, 0, 1, 0, 0, 8, 0, 5, 0)]:
    S = closure(c)
    m1 = sum(1 for x in S if sum(x) == 1)
    print('closure', c, 'states', len(S), 'mass1_states', m1)
    neg_ok &= m1 == 0
print('G9_CLEAR_CERT_OK' if bad == 0 and need == seen and neg_ok else 'G9_CLEAR_CERT_FAIL')
