#!/usr/bin/env python3
"""Check stacking/clearing certificates (Python 3.8+, standard library only).

Usage:  python3 verify_certificates.py cert_P4_stack_t12.json cert_bull_clear_t12.json

Move u=>v along an edge needs c(u)>=2 and sets c(u)-=2, c(v)+=1. "stack": the goal is a
configuration with one-vertex support; "clear": the goal is total size 1. For each file:
  1. the listed configurations are exactly the almost stacked configurations of size t
     (re-enumerated here independently), and each listed move sequence is legal and
     ends at a goal configuration;
  2. the losing configuration has size t, lies in the listed set, the set is closed under
     every legal move, contains no goal configuration, and equals the set reached by an
     independent breadth-first search from the loser.
Hence every almost stacked configuration of size t reaches the goal, and the loser does not.
Prints one PASS line per file; exits with status 1 on the first failure.
"""
import json, sys
from collections import deque
from itertools import combinations


def check(path):
    C = json.load(open(path))
    n, t, goal = C["n"], C["t"], C["goal"]
    adj = {v: set() for v in range(n)}
    for u, v in C["edges"]:
        adj[u].add(v); adj[v].add(u)
    is_goal = (lambda c: sum(x > 0 for x in c) == 1) if goal == "stack" else (lambda c: sum(c) == 1)

    def moves(c):
        for u in range(n):
            if c[u] >= 2:
                for v in adj[u]:
                    d = list(c); d[u] -= 2; d[v] += 1
                    yield tuple(d)

    want = set()                                   # all almost stacked configurations of size t
    for v0 in range(n):
        rest = [u for u in range(n) if u != v0]
        for k in range(min(t, n - 1) + 1):
            for S in combinations(rest, k):
                want.add(tuple(t - k if u == v0 else int(u in S) for u in range(n)))
    listed = [tuple(e["config"]) for e in C["as_winning_sequences"]]
    assert set(listed) == want and len(listed) == len(want) == C["as_count"], "AS list mismatch"
    for e in C["as_winning_sequences"]:
        c = list(e["config"])
        for u, v in e["moves"]:
            assert v in adj[u] and c[u] >= 2, ("illegal move", e["config"], (u, v))
            c[u] -= 2; c[v] += 1
        assert is_goal(c), ("sequence does not reach goal", e["config"])

    loser = tuple(C["losing_witness"]["config"])
    R = {tuple(x) for x in C["losing_witness"]["reachable_set"]}
    assert sum(loser) == t and loser in R, "loser not in set"
    assert all(d in R for c in R for d in moves(c)), "set not closed under moves"
    assert not any(is_goal(c) for c in R), "set contains a goal configuration"
    seen, queue = {loser}, deque([loser])          # independent breadth-first search
    while queue:
        for d in moves(queue.popleft()):
            if d not in seen:
                seen.add(d); queue.append(d)
    assert seen == R, "set differs from breadth-first reachable set"
    print(f"PASS {path}: {C['graph']}, goal={goal}, t={t}: all {len(want)} almost stacked "
          f"configurations reach the goal; loser {list(loser)} has {len(R)} reachable "
          f"configurations, none a goal")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for p in sys.argv[1:]:
        try:
            check(p)
        except (AssertionError, KeyError, ValueError) as err:
            print(f"FAIL {p}: {err}")
            sys.exit(1)
