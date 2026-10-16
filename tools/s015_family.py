#!/usr/bin/env python3
"""CAM-S015-90 graph-family generator around G9 = HCQTaXi (writes 'name n edges' lines).
Families (all connected, simple):
 X1: every one-vertex extension of G9: new vertex 9 joined to a nonempty subset S of 0..8 (511 graphs).
 F(a,b,k): two copies of K_a minus one edge (tips u1,w1 / u2,w2), bridge u1-u2, edge w1-w2,
           plus k new vertices each adjacent to both w1 and w2.  G9 = F(4,4,1).
           a,b in {3,4,5,6}, k in {0,1,2,3}.
 P(a,l): as F(a,a,1) but the bridge u1-u2 replaced by a path with l internal vertices, l in {1,2}.
 R(k): G9 with vertex 2 replaced by a path 6-x1-...-xk-8 (k internal vertices), k in {1,2,3} (k=1 is G9).
usage: s015_family.py > family.txt"""
G9 = [(0, 3), (1, 4), (0, 5), (3, 5), (0, 6), (2, 6), (3, 6), (1, 7), (4, 7), (5, 7), (1, 8), (2, 8), (4, 8), (6, 8)]

def out(name, n, E):
    print(name, n, ','.join(f'{a}-{b}' for a, b in sorted(set(tuple(sorted(e)) for e in E))))

for S in range(1, 1 << 9):
    out(f'X1_{S:03x}', 10, G9 + [(i, 9) for i in range(9) if S >> i & 1])

def kminus(base, a):
    vs = list(range(base, base + a))
    E = [(vs[i], vs[j]) for i in range(a) for j in range(i + 1, a) if not (i == 0 and j == 1)]
    return vs[0], vs[1], E  # tips vs[0], vs[1] nonadjacent

def F(a, b, k, l=0):
    u1, w1, E1 = kminus(0, a); u2, w2, E2 = kminus(a, b)
    E = E1 + E2 + [(w1, w2)]
    nxt = a + b
    if l == 0:
        E.append((u1, u2))
    else:
        path = list(range(nxt, nxt + l)); nxt += l
        chain = [u1] + path + [u2]
        E += [(chain[i], chain[i + 1]) for i in range(len(chain) - 1)]
    for _ in range(k):
        E += [(nxt, w1), (nxt, w2)]; nxt += 1
    return nxt, E

for a in (3, 4, 5, 6):
    for b in (3, 4, 5, 6):
        if b < a: continue
        for k in (0, 1, 2, 3):
            n, E = F(a, b, k)
            if n <= 16: out(f'F_{a}_{b}_{k}', n, E)
for a in (3, 4, 5):
    for l in (1, 2):
        n, E = F(a, a, 1, l)
        out(f'P_{a}_{l}', n, E)
for k in (2, 3):
    E = [e for e in G9 if 2 not in e]
    path = [6] + [2] + list(range(9, 9 + k - 1)) + [8]
    E += [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    out(f'R_{k}', 9 + k - 1, E)
