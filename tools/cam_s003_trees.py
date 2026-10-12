#!/usr/bin/env python3
"""CAM-S003-01 T3: trees with KNOWN stacking number.

stack(T) = estim(T) for every finite tree with >= 2 vertices is the earlier TreeStack
theorem (arXiv:2609.31811; Lean TreeStack.stack_eq_estim_of_two_le_card), with estim as
in October Definition 5.1 / April p.26:
    rho_T(r) = sum over v = r or deg(v) > 1 of deg(v) * 2^dist(r,v),
    leaf_T(r) = #leaves of T other than r,
    estim(T) = max{2, 1 + max_r (rho_T(r) + leaf_T(r))}.
For each tree we run tools/cam_s003_as.c with S = estim(T): for every t in (n, S-1] it
searches an almost-stacked non-stackable configuration (exact memoised reachability).
Reported: literal AS-gap masses (where every AS configuration of size t is stackable) and
whether an AS loser exists at t = S-1 (critical form).  For n <= 6 estim is compared with
the exhaustive T2 thresholds.
usage: cam_s003_trees.py AS_BIN OUT.json NMAX [PER_TREE_SECONDS] [T2_SUMMARY]
"""
import json
import os
import resource
import subprocess
import sys
from collections import deque

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cam_s003_graphs as G  # noqa: E402


def estim(n, edges):
    if n == 1:
        return 2
    adj = {v: [] for v in range(n)}
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    best = None
    for r in range(n):
        dist = {r: 0}; q = deque([r])
        while q:
            u = q.popleft()
            for w in adj[u]:
                if w not in dist:
                    dist[w] = dist[u] + 1; q.append(w)
        rho = sum(len(adj[v]) * 2 ** dist[v] for v in range(n) if v == r or len(adj[v]) > 1)
        leaf = sum(1 for v in range(n) if v != r and len(adj[v]) == 1)
        best = rho + leaf if best is None else max(best, rho + leaf)
    return max(2, 1 + best)


def main():
    asbin, out, nmax = sys.argv[1], sys.argv[2], int(sys.argv[3])
    cap = int(sys.argv[4]) if len(sys.argv) > 4 else 600
    t2 = {}
    if len(sys.argv) > 5:
        for r in json.load(open(sys.argv[5])):
            if len(r['edges'].split(',')) == r['n'] - 1 or r['n'] == 1:
                key = G._tree_code(r['n'], [tuple(map(int, e.split('-'))) for e in r['edges'].split(',') if e])
                t2[(r['n'], key)] = r['analysis']['stack']['threshold']
    res = []
    for n in range(2, nmax + 1):
        for i, e in enumerate(G.nonisomorphic_trees(n)):
            S = estim(n, e)
            name = f'T{n}_{i:03d}'
            rec = {'tree': name, 'n': n, 'edges': G.edge_string(e), 'estim': S}
            key = (n, G._tree_code(n, e))
            if key in t2:
                rec['t2_exhaustive_threshold'] = t2[key]
                rec['estim_matches_exhaustive'] = t2[key] == S
            try:
                lim = lambda: resource.setrlimit(resource.RLIMIT_AS, (3 << 30, 3 << 30))
                p = subprocess.run([asbin, name, str(n), G.edge_string(e), str(S)], capture_output=True, text=True, timeout=cap, check=True, preexec_fn=lim)
                lines = [json.loads(x) for x in p.stdout.splitlines()]
                rows = [x for x in lines if 't' in x]
                rec['gaps'] = [x['t'] for x in rows if x.get('GAP')]
                rec['as_loser_at_S_minus_1'] = next((x['as_loser'] for x in rows if x['t'] == S - 1 and 'as_loser' in x), None)
                rec['complete'] = len(rows) == max(0, S - 1 - n)
                rec['memo'] = lines[-1].get('memo')
            except subprocess.TimeoutExpired:
                rec['complete'] = False; rec['timeout_seconds'] = cap
            except subprocess.CalledProcessError as err:
                rec['complete'] = False; rec['failure'] = f'exit {err.returncode} (3 GiB memory limit)'
            res.append(rec)
            print(name, n, S, rec.get('gaps'), rec.get('as_loser_at_S_minus_1'), rec.get('estim_matches_exhaustive'), rec['complete'], flush=True)
    json.dump(res, open(out, 'w'), sort_keys=True, separators=(',', ':'))


if __name__ == '__main__':
    main()
