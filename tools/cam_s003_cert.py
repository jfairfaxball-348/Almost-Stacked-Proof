#!/usr/bin/env python3
"""CAM-S003-01 certificate builder and independent checker (no code shared with the C tools).

A *literal AS-gap certificate* for graph G, goal g in {stack, clear} and mass t consists of
  (W) for EVERY almost-stacked configuration of exact size t, an explicit legal move
      sequence ending in a goal configuration (stacked / cleared), and
  (L) one configuration of exact size t together with its COMPLETE reachable set, none of
      whose members is a goal configuration.
Checking (W) only replays moves; checking (L) recomputes the reachable set by BFS and
confirms closure (every legal successor of a member is a member).  With n=|V| < t this
certifies   least{t' >= 2 : all AS configs of size t' are g-able} <= t < g(G),
i.e. the literal Hypothesis 3.2 / 9.1 equality fails on G (proof: research/S003_AS_GAP_AND_ATTACKS.md).

usage: cam_s003_cert.py build NAME N "a-b,..." GOAL T OUT.json
       cam_s003_cert.py check CERT.json
"""
import itertools
import json
import sys
from collections import deque


def parse_edges(n, es):
    edges = sorted({tuple(sorted(map(int, e.split('-')))) for e in es.split(',') if e})
    assert all(0 <= a < b < n for a, b in edges)
    return edges


def arcs(edges):
    return [(a, b) for a, b in edges] + [(b, a) for a, b in edges]


def is_goal(c, goal):
    return sum(1 for x in c if x > 0) == 1 if goal == 'stack' else sum(c) == 1


def step(c, u, v):
    if c[u] < 2:
        raise ValueError('illegal move')
    d = list(c); d[u] -= 2; d[v] += 1
    return tuple(d)


def reach(c0, A):
    seen = {c0}; q = deque([c0]); parent = {c0: None}
    while q:
        c = q.popleft()
        for u, v in A:
            if c[u] >= 2:
                d = step(c, u, v)
                if d not in seen:
                    seen.add(d); parent[d] = (c, (u, v)); q.append(d)
    return seen, parent


def path_to(parent, target):
    moves = []
    while parent[target] is not None:
        prev, mv = parent[target]
        moves.append(list(mv)); target = prev
    return moves[::-1]


def as_configs(n, t):
    out = set()
    for v0 in range(n):
        for bits in itertools.product((0, 1), repeat=n - 1):
            rest = sum(bits)
            if rest > t:
                continue
            c = list(bits[:v0]) + [t - rest] + list(bits[v0:])
            out.add(tuple(c))
    return sorted(out)


def bipartite(n, edges):
    col = [-1] * n
    for s in range(n):
        if col[s] >= 0:
            continue
        col[s] = 0; q = deque([s])
        while q:
            u = q.popleft()
            for a, b in edges:
                for x, y in ((a, b), (b, a)):
                    if x == u:
                        if col[y] < 0:
                            col[y] = 1 - col[u]; q.append(y)
                        elif col[y] == col[u]:
                            return False
    return True


def build(name, n, es, goal, t, out):
    edges = parse_edges(n, es); A = arcs(edges)
    if goal == 'clear':
        assert not bipartite(n, edges), 'clearing only for non-bipartite graphs'
    wins = []
    for c in as_configs(n, t):
        seen, parent = reach(c, A)
        tgt = next((d for d in sorted(seen) if is_goal(d, goal)), None)
        if tgt is None:
            raise SystemExit(f'AS configuration {c} is NOT {goal}-able: no gap at t={t}')
        wins.append({'config': list(c), 'moves': path_to(parent, tgt)})
    loser = None
    for c in sorted(itertools.product(range(t + 1), repeat=n)):
        if sum(c) != t:
            continue
        seen, _ = reach(c, A)
        if not any(is_goal(d, goal) for d in seen):
            loser = {'config': list(c), 'reachable_set': sorted(map(list, seen))}
            break
    if loser is None:
        raise SystemExit(f'every configuration of size {t} is {goal}-able: no gap')
    cert = {'graph': name, 'n': n, 'edges': [list(e) for e in edges], 'goal': goal, 't': t,
            'as_count': len(wins), 'as_winning_sequences': wins, 'losing_witness': loser}
    json.dump(cert, open(out, 'w'), sort_keys=True, separators=(',', ':'))
    print(json.dumps({'built': out, 'as_count': len(wins), 'loser': loser['config'],
                      'reachable': len(loser['reachable_set'])}))


def check(path):
    C = json.load(open(path))
    n, t, goal = C['n'], C['t'], C['goal']
    edges = [tuple(e) for e in C['edges']]; A = arcs(edges)
    assert all(0 <= a < b < n for a, b in edges)
    # connectivity
    seen = {0}; q = [0]
    while q:
        u = q.pop()
        for a, b in edges:
            for x, y in ((a, b), (b, a)):
                if x == u and y not in seen:
                    seen.add(y); q.append(y)
    assert len(seen) == n, 'graph not connected'
    if goal == 'clear':
        assert not bipartite(n, edges)
    assert t > n >= 2
    # (W): the certificate lists exactly the AS configurations of size t, each with a replayed win
    listed = sorted(tuple(w['config']) for w in C['as_winning_sequences'])
    expected = as_configs(n, t)
    assert listed == expected, 'AS list incomplete or wrong'
    for w in C['as_winning_sequences']:
        c = tuple(w['config'])
        for u, v in w['moves']:
            assert (min(u, v), max(u, v)) in edges
            c = step(c, u, v)
        assert is_goal(c, goal), ('sequence does not reach goal', w)
    # (L): recompute reachable set and check closure and goal-freeness
    c0 = tuple(C['losing_witness']['config'])
    assert sum(c0) == t
    R = {tuple(x) for x in C['losing_witness']['reachable_set']}
    assert c0 in R
    for c in R:
        assert not is_goal(c, goal)
        for u, v in A:
            if c[u] >= 2:
                assert step(c, u, v) in R, 'reachable set not closed'
    recomputed, _ = reach(c0, A)
    assert recomputed == R
    print(json.dumps({'checked': path, 'graph': C['graph'], 'goal': goal, 't': t, 'as_configs_replayed': len(listed),
                      'loser': list(c0), 'reachable_closed_goal_free': len(R), 'verdict': 'LITERAL_AS_GAP_CERTIFIED'}))


if __name__ == '__main__':
    if sys.argv[1] == 'build':
        build(sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5], int(sys.argv[6]), sys.argv[7])
    else:
        check(sys.argv[2])
