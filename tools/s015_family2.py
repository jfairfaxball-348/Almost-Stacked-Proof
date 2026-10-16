#!/usr/bin/env python3
"""CAM-S015-91 path-bridge family P(a,b,l,k): two K_a/K_b-minus-edge blocks (tips u1,w1 /
u2,w2), edge w1-w2, k vertices adjacent to both w1 and w2, and the other tips joined by a
path u1 - p_1 - ... - p_l - u2 with l internal vertices (l=0: edge u1-u2; P(4,4,0,1)=G9).
usage: s015_family2.py > list"""
def kminus(base, a):
    vs = list(range(base, base + a))
    return vs[0], vs[1], [(vs[i], vs[j]) for i in range(a) for j in range(i + 1, a) if not (i == 0 and j == 1)]

def P(a, b, l, k):
    u1, w1, E1 = kminus(0, a); u2, w2, E2 = kminus(a, b)
    E = E1 + E2 + [(w1, w2)]; nxt = a + b
    chain = [u1] + list(range(nxt, nxt + l)) + [u2]; nxt += l
    E += [(chain[i], chain[i + 1]) for i in range(len(chain) - 1)]
    for _ in range(k):
        E += [(nxt, w1), (nxt, w2)]; nxt += 1
    return nxt, E

rows = [(4, 4, l, 1) for l in range(0, 7)] + [(4, 4, l, 2) for l in range(0, 5)] + \
       [(a, b, l, 1) for a in (3, 4, 5) for b in (4, 5) if a <= b for l in (2, 3, 4)] + [(4, 4, l, 0) for l in range(0, 5)]
seen = set()
for a, b, l, k in rows:
    if (a, b, l, k) in seen: continue
    seen.add((a, b, l, k))
    n, E = P(a, b, l, k)
    print(f'PB_{a}_{b}_{l}_{k}', n, ','.join(f'{x}-{y}' for x, y in sorted(set(tuple(sorted(e)) for e in E))))
