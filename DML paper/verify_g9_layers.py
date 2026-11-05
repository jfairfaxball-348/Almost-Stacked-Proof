#!/usr/bin/env python3
"""Independent exact graph pebbling losing-layer verification for the G9 result.

Reconstructs all losing configurations at masses 2..15 using the
mathematically exact reverse-predecessor candidate recurrence.
No Lean data, historical certificates, external libraries or graph6 tools.
"""
from itertools import combinations

N = 9
EDGES = ((0,3),(0,5),(0,6),(1,4),(1,7),(1,8),(2,6),(2,8),
         (3,5),(3,6),(4,7),(4,8),(5,7),(6,8))
EXPECTED_STACK = (36,128,383,930,1862,2887,3280,2510,1301,473,124,21,2,0)
EXPECTED_CLEAR = (36,137,384,932,1863,2887,3280,2510,1301,473,124,21,2,0)
CRITICAL = {(0,0,1,0,0,5,0,8,0),(0,0,1,0,0,8,0,5,0)}
NEIGHBORS = [set() for _ in range(N)]
for u,v in EDGES:
    NEIGHBORS[u].add(v)
    NEIGHBORS[v].add(u)

def losing_next(previous, mass, goal):
    candidates = set()
    if mass <= N:
        for occupied in combinations(range(N), mass):
            c = [0]*N
            for v in occupied: c[v] = 1
            candidates.add(tuple(c))
    for successor in previous:
        for u in range(N):
            for v in NEIGHBORS[u]:
                if successor[v] > 0:
                    parent = list(successor)
                    parent[u] += 2
                    parent[v] -= 1
                    candidates.add(tuple(parent))

    def already_won(c):
        return (sum(x > 0 for x in c) == 1) if goal == 'STACK' else sum(c) == 1

    losers = set()
    for c in candidates:
        if already_won(c):
            continue
        losing = True
        for u in range(N):
            if c[u] >= 2:
                for v in NEIGHBORS[u]:
                    next_c = list(c)
                    next_c[u] -= 2
                    next_c[v] += 1
                    if tuple(next_c) not in previous:
                        losing = False
                        break
                if not losing:
                    break
        if losing:
            losers.add(c)
    return losers

def verify(goal, expected):
    previous = set()  # every mass-one configuration is winning
    counts = []
    for mass in range(2,16):
        previous = losing_next(previous, mass, goal)
        counts.append(len(previous))
        if mass == 13:
            assert any(sum(x >= 2 for x in c) <= 1 for c in previous)
        if mass == 14:
            assert previous == CRITICAL
            assert all(sum(x >= 2 for x in c) >= 2 for c in previous)
        if mass == 15:
            assert not previous
    assert tuple(counts) == expected, (goal, counts)
    print(f'{goal}: masses 2..15 = {counts}; G9 critical counterexample PASS')

if __name__ == '__main__':
    for game, expected_counts in (('STACK',EXPECTED_STACK),('CLEAR',EXPECTED_CLEAR)):
        verify(game, expected_counts)
