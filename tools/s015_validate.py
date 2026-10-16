#!/usr/bin/env python3
"""CAM-S015-82 independent validator (separately written, pure Python).

Different organisation from the compiled producer: winners are never stored;
losers of mass t are kept as a frozenset of tuples.  For each mass t the
candidate set is built from BOTH sources independently of the producer:
  (a) every 0/1 vector with t ones (no move available, support t>=2);
  (b) every predecessor p of a loser q of mass t-1, where the move of p
      along an ordered true edge (a->b) produces q:  p = q + 2e_a - e_b.
A candidate is accepted iff it has >=2 occupied sites and EVERY legal move
leads into the previous losing layer.  Stop after the first empty layer at
t>=n.  Additionally each critical loser is re-proved losing by an explicit
closed forward reachable-set search (no use of the layer sets), and each
reported AS critical witness likewise.

usage: s015_validate.py < graphs  (lines: name n a-b,c-d,...)  -> one line/graph
"""
import sys


def parse(line):
    name, n, es = line.split()
    n = int(n)
    nb = [[] for _ in range(n)]
    if es != '-':
        for tok in es.split(','):
            a, b = map(int, tok.split('-'))
            nb[a].append(b)
            nb[b].append(a)
    return name, n, [tuple(sorted(x)) for x in nb]


def moves(c, nb):
    for a, k in enumerate(c):
        if k >= 2:
            for b in nb[a]:
                l = list(c)
                l[a] -= 2
                l[b] += 1
                yield tuple(l)


def occupied(c):
    return sum(1 for k in c if k)


def forward_loses(c, nb):
    """Closed forward reachable set; True iff no reachable single pile."""
    seen = {c}
    stack = [c]
    while stack:
        x = stack.pop()
        if occupied(x) <= 1:
            return False
        for y in moves(x, nb):
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return True


def binaries(n, t):
    from itertools import combinations
    for S in combinations(range(n), t):
        c = [0] * n
        for i in S:
            c[i] = 1
        yield tuple(c)


def run(n, nb):
    prev = frozenset()
    t = 1
    last = None
    las = None
    layers = {}
    while True:
        t += 1
        cand = set()
        if t <= n:
            cand.update(binaries(n, t))
        for q in prev:
            for b in range(n):
                if q[b] == 0:
                    continue
                for a in nb[b]:
                    p = list(q)
                    p[a] += 2
                    p[b] -= 1
                    cand.add(tuple(p))
        cur = set()
        for p in cand:
            if occupied(p) < 2:
                continue
            if all(s in prev for s in moves(p, nb)):
                cur.add(p)
        if cur:
            last = t
            layers = cur
            if any(sum(1 for k in p if k > 1) <= 1 for p in cur):
                las = t
        if not cur and t >= n:
            break
        prev = frozenset(cur)
    return last, las, layers


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        name, n, nb = parse(line)
        last, las, crit = run(n, nb)
        ascount = sum(1 for p in crit if sum(1 for k in p if k > 1) <= 1)
        # independent forward re-proof of one AS and every non-AS critical loser
        nonas = sorted(p for p in crit if sum(1 for k in p if k > 1) > 1)
        aswit = min((p for p in crit if sum(1 for k in p if k > 1) <= 1), default=None)
        fw_ok = True
        for p in nonas + ([aswit] if aswit else []):
            if not forward_loses(p, nb):
                fw_ok = False
        print(name, n, 'Lall', last, 'LAS', las, 'crit', len(crit), 'critAS', ascount,
              'nonAS', '.'.join(map(str, nonas[0])) if nonas else '-',
              'FWD_OK' if fw_ok else 'FWD_FAIL',
              'ASH_OK' if las == last else 'ASH_FAIL', flush=True)


if __name__ == '__main__':
    main()
