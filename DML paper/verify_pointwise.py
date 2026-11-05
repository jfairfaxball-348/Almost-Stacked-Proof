#!/usr/bin/env python3
"""Exact pointwise ASH counterexample checker; independent of G9 Lean proof."""
from functools import lru_cache

CASES = [
    ("P4 STACK", 4, [(0,1),(1,2),(2,3)], "stack", (1,0,2,9), 32),
    ("Bull CLEAR", 5, [(0,4),(1,3),(2,3),(2,4),(3,4)],
     "clear", (1,9,0,2,0), 80),
]

def compositions(n, t):
    if n == 1:
        yield (t,)
    else:
        for x in range(t+1):
            for tail in compositions(n-1, t-x):
                yield (x,) + tail

def run(name, n, edges, goal, witness, as_count):
    neighbours = [set() for _ in range(n)]
    for u,v in edges:
        neighbours[u].add(v)
        neighbours[v].add(u)
    @lru_cache(None)
    def win(c):
        if (sum(x > 0 for x in c) == 1 if goal == "stack"
                else sum(c) == 1):
            return True
        for u in range(n):
            if c[u] >= 2:
                for v in neighbours[u]:
                    d = list(c)
                    d[u] -= 2
                    d[v] += 1
                    if win(tuple(d)):
                        return True
        return False
    losses = []
    for t in range(12,16):
        vectors = list(compositions(n,t))
        losses.append(sum(not win(c) for c in vectors))
        if t == 12:
            AS = [c for c in vectors if sum(x >= 2 for x in c) <= 1]
            assert len(AS) == as_count
            assert all(win(c) for c in AS)
            assert not win(witness)
    assert losses == [4,2,2,0], losses
    print(f"{name}: all {as_count} AS configurations win at 12;"
          f" losing layer counts {losses}; PASS")

if __name__ == "__main__":
    for case in CASES:
        run(*case)
