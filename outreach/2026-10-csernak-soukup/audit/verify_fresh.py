#!/usr/bin/env python3
"""Fresh pre-send verifier for the Csernak-Soukup correspondence (standard library only).

Written without reading any tools/cam_s003_* source. Model: a move u=>v along an edge needs
c(u)>=2 and sets c(u)-=2, c(v)+=1. Stacked = support of size 1; cleared = size 1.

Usage:
  python3 verify_fresh.py core              # P4, bull, K_{a,b} checks -> fresh_core.json
  python3 verify_fresh.py spot T2b.json N [OUT [CAP]]  # pre-registered check -> OUT (default spotcheck_T2b.json)
"""
import json, random, sys, time
from collections import deque
from itertools import combinations
from math import comb


def adjacency(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def moves(c, adj):
    for u, cu in enumerate(c):
        if cu >= 2:
            for v in adj[u]:
                d = list(c)
                d[u] -= 2
                d[v] += 1
                yield tuple(d)


def is_goal(c, goal):
    if goal == "stack":
        return sum(1 for x in c if x) == 1
    return sum(c) == 1


def reachable(c, adj):
    seen, queue = {c}, deque([c])
    while queue:
        for d in moves(queue.popleft(), adj):
            if d not in seen:
                seen.add(d)
                queue.append(d)
    return seen


def gable(c, adj, goal):
    return any(is_goal(d, goal) for d in reachable(c, adj))


def compositions(t, n):
    if n == 1:
        yield (t,)
        return
    for first in range(t, -1, -1):
        for rest in compositions(t - first, n - 1):
            yield (first,) + rest


def almost_stacked(t, n):
    out = set()
    for v0 in range(n):
        others = [u for u in range(n) if u != v0]
        for k in range(0, min(t, n - 1) + 1):
            for S in combinations(others, k):
                c = [0] * n
                c[v0] = t - k
                for u in S:
                    c[u] = 1
                out.add(tuple(c))
    return out


def is_as(c):
    return sum(1 for x in c if x >= 2) <= 1


def bipartite(n, adj):
    col = [None] * n
    for s in range(n):
        if col[s] is None:
            col[s] = 0
            stack = [s]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if col[v] is None:
                        col[v] = 1 - col[u]
                        stack.append(v)
                    elif col[v] == col[u]:
                        return False
    return True


def layers(n, adj, goal, tmax):
    """Layered DP: W_t = goal configs of size t, or configs with a move into W_{t-1}.
    Returns per t (2..tmax): number of losers, AS-loser example (or None), number of AS configs."""
    prev = set(compositions(1, n))  # every size-1 configuration is stacked and cleared
    rows = {}
    for t in range(2, tmax + 1):
        cur, losers, as_loser, as_total = set(), 0, None, 0
        for c in compositions(t, n):
            if is_goal(c, goal) or any(d in prev for d in moves(c, adj)):
                cur.add(c)
            else:
                losers += 1
                if as_loser is None and is_as(c):
                    as_loser = c
        rows[t] = {"losers": losers, "as_loser_example": as_loser}
        prev = cur
    return rows


def summarise(n, rows):
    ts = sorted(rows)
    g = next((t for t in ts if rows[t]["losers"] == 0), None)
    out = {"threshold": g}
    if g is None:
        return out
    assert g > n, "threshold must exceed n (Lemma 1)"
    out["all_win_from_threshold_to_tmax"] = all(rows[t]["losers"] == 0 for t in ts if t >= g)
    out["as_threshold_literal"] = next(t for t in ts if rows[t]["as_loser_example"] is None)
    # for n=1, g-1=1 < 2: the size-(g-1) form is vacuous (|V|>=2 boundary), recorded as no AS loser
    out["as_loser_at_threshold_minus_1"] = rows[g - 1]["as_loser_example"] if g - 1 >= 2 else None
    out["ASHstar"] = out["as_loser_at_threshold_minus_1"] is not None
    out["literal_gaps"] = [t for t in ts if n < t < g and rows[t]["as_loser_example"] is None]
    out["ASH_literal"] = not out["literal_gaps"]
    return out


def core():
    res = {}
    # P4 = v1-v2-v3-v4, repository labels 0-1-2-3
    n, E = 4, [(0, 1), (1, 2), (2, 3)]
    adj = adjacency(n, E)
    AS12 = sorted(almost_stacked(12, n))
    a = [c for c in AS12 if not gable(c, adj, "stack")]
    L = (1, 0, 2, 9)
    R = reachable(L, adj)
    closed = all(d in R for c in R for d in moves(c, adj))
    rows = layers(n, adj, "stack", 16)
    res["P4"] = {
        "a_AS12_count": len(AS12), "a_AS12_nonstackable": a,
        "b_loser": L, "b_reachable_size": len(R), "b_closed": closed,
        "b_contains_stacked": any(is_goal(c, "stack") for c in R),
        "c_AS_loser_per_t_2_to_11": {t: rows[t]["as_loser_example"] for t in range(2, 12)},
        "c_AS_loser_t12": rows[12]["as_loser_example"],
        "d_losers_per_t": {t: rows[t]["losers"] for t in rows},
        "summary": summarise(n, rows),
    }
    # Bull: repository labels, edges 0-4, 1-3, 2-3, 2-4, 3-4
    n, E = 5, [(0, 4), (1, 3), (2, 3), (2, 4), (3, 4)]
    adj = adjacency(n, E)
    deg = [len(x) for x in adj]
    tri = [v for v in range(n) if deg[v] >= 2]
    pend = {v: adj[v][0] for v in range(n) if deg[v] == 1}
    AS12 = sorted(almost_stacked(12, n))
    L = (1, 9, 0, 2, 0)
    R = reachable(L, adj)
    res["bull"] = {
        "e_bipartite": bipartite(n, adj), "triangle": tri, "pendant_of": pend,
        "f_AS12_count": len(AS12),
        "f_AS12_nonclearable": [c for c in AS12 if not gable(c, adj, "clear")],
        "f_AS12_nonstackable": [c for c in AS12 if not gable(c, adj, "stack")],
        "g_loser": L, "g_reachable_size": len(R),
        "g_closed": all(d in R for c in R for d in moves(c, adj)),
        "g_contains_cleared": any(is_goal(c, "clear") for c in R),
        "g_contains_stacked": any(is_goal(c, "stack") for c in R),
        "h_clear": summarise(n, layers(n, adj, "clear", 16)),
        "h_stack": summarise(n, layers(n, adj, "stack", 16)),
    }
    # K_{a,b}: witness (2*alpha+1) e_w + sum_{x in B'} e_x, |B| = alpha = max(a,b)
    kab = {}
    for a_, b_ in [(1, 2), (2, 2), (1, 3), (2, 3), (3, 3), (2, 4), (1, 5)]:
        A, B = list(range(a_)), list(range(a_, a_ + b_))
        n = a_ + b_
        adj = adjacency(n, [(x, y) for x in A for y in B])
        alpha = b_
        w = [0] * n
        w[B[0]] = 2 * alpha + 1
        for x in B[1:]:
            w[x] = 1
        s = summarise(n, layers(n, adj, "stack", 3 * alpha + 2))
        kab[f"K{a_},{b_}"] = {"witness": w, "witness_size": sum(w), "witness_is_AS": is_as(w),
                              "witness_stackable": gable(tuple(w), adj, "stack"),
                              "stack": s["threshold"], "3alpha+1": 3 * alpha + 1, "ASHstar": s["ASHstar"]}
    res["Kab"] = kab
    return res


def spot(path, want, cap=1_500_000, seed=20261012):
    data = json.load(open(path))
    order = random.Random(seed).sample(range(len(data)), len(data))
    full, partial = [], []
    for i in order:
        if len(full) >= want:
            break
        rec = data[i]
        n = rec["n"]
        E = [tuple(map(int, e.split("-"))) for e in rec["edges"].split(",") if e]
        adj = adjacency(n, E)
        an = rec["analysis"]
        goals = ["stack"] + ([] if bipartite(n, adj) else ["clear"])
        ths = [an[g]["threshold"] for g in goals if isinstance(an[g], dict) and an[g].get("threshold")]
        entry = {"index": i, "graph": rec["graph"], "edges": rec["edges"], "bipartite_fresh": bipartite(n, adj),
                 "bipartite_repo": an["bipartite"]}
        if len(ths) < len(goals) or comb(max(ths) + n - 1, n - 1) > cap:
            entry["mode"] = "SKIPPED_ABOVE_CAP_OR_UNDECIDED"
            entry["repo_thresholds"] = {g: (an[g].get("threshold") if isinstance(an[g], dict) else an[g]) for g in goals}
            partial.append(entry)
            continue
        t0 = time.time()
        entry["mode"] = "FULL"
        for g in goals:
            s = summarise(n, layers(n, adj, g, an[g]["threshold"] + 1))
            r = an[g]
            entry[g] = {"fresh": s, "agree": (s["threshold"] == r["threshold"]
                        and s["as_threshold_literal"] == r["as_threshold"]
                        and s["ASHstar"] == r["as_loss_at_threshold_minus_1"]
                        and s["literal_gaps"] == r["gap_masses"]
                        and s["ASH_literal"] == r["ASH_on_graph"])}
        entry["seconds"] = round(time.time() - t0, 1)
        entry["agree_all"] = all(entry[g]["agree"] for g in goals) and entry["bipartite_fresh"] == entry["bipartite_repo"]
        full.append(entry)
        print(entry["graph"], entry["agree_all"], {g: entry[g]["fresh"]["threshold"] for g in goals}, entry["seconds"], flush=True)
    return {"seed": seed, "cap_layer_size": cap, "requested_full": want, "full": full, "skipped": partial,
            "all_full_agree": all(e["agree_all"] for e in full),
            "all_full_ASHstar": all(e[g]["fresh"]["ASHstar"] for e in full for g in ("stack", "clear") if g in e)}


if __name__ == "__main__":
    if sys.argv[1] == "core":
        out = core()
        json.dump(out, open("fresh_core.json", "w"), indent=1, default=list)
        print(json.dumps(out, indent=1, default=list))
    else:
        outp = sys.argv[4] if len(sys.argv) > 4 else "spotcheck_T2b.json"
        cap = int(sys.argv[5]) if len(sys.argv) > 5 else 1_500_000
        out = spot(sys.argv[2], int(sys.argv[3]), cap)
        json.dump(out, open(outp, "w"), indent=1)
        print("full:", len(out["full"]), "skipped:", len(out["skipped"]),
              "agree:", out["all_full_agree"], "ASH*:", out["all_full_ASHstar"])
