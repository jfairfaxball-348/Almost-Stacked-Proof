#!/usr/bin/env python3
"""CAM-S003-01 driver: run the preregistered tiers with the forward solver, cold-check
with the reverse C solver (all layers) and the Python reverse fixpoint (layers <= 5M),
and analyse every graph through the AS-gap reformulation (research/S003_AS_GAP_AND_ATTACKS.md):

    ASH-stack(G)  <=>  for every t with n < t < stack(G) some AS configuration of size t is losing
    (same for clear when G is non-bipartite).

usage: cam_s003_run.py TIER BIN_DIR OUT_DIR      TIER in {T1,T4,T2,T2b}
"""
import concurrent.futures as cf
import json
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cam_s003_graphs as G  # noqa: E402

LAYER_CAP = 60_000_000
PY_CAP = 5_000_000
KEYS = ['total', 'as_total', 'nonstack', 'as_nonstack', 'nonclear', 'as_nonclear', 'fp_stack', 'fp_clear']


def binom(a, b):
    from math import comb
    return comb(a, b)


def tcap(n, hard):
    t = 1
    while t + 1 <= hard and binom(t + 1 + n - 1, n - 1) <= LAYER_CAP:
        t += 1
    return t


def run(cmd, out):
    t0 = time.monotonic()
    with open(out, 'w') as f:
        subprocess.run(cmd, stdout=f, check=True)
    return round(time.monotonic() - t0, 3)


def rows_of(path):
    return {d['t']: d for d in map(json.loads, open(path)) if 't' in d}


def analyse(n, bip, rows):
    ts = sorted(rows)
    res = {'n': n, 'bipartite': bip, 'computed_tmax': ts[-1]}
    for goal, L, AL in (('stack', 'nonstack', 'as_nonstack'), ('clear', 'nonclear', 'as_nonclear')):
        if goal == 'clear' and bip:
            res['clear'] = 'UNDEFINED_BIPARTITE'
            continue
        thr = next((t for t in ts if t >= 2 and rows[t][L] == 0), None)
        as_thr = next((t for t in ts if t >= 2 and rows[t][AL] == 0), None)
        low_ok = all(rows[t][AL] > 0 for t in ts if 2 <= t <= n)
        gaps = [t for t in ts if t > n and rows[t][L] > 0 and rows[t][AL] == 0]
        above = [t for t in ts if t > n and rows[t][AL] > 0]
        interval = above == list(range(n + 1, n + 1 + len(above)))
        mono_after = thr is None or all(rows[t][L] == 0 for t in ts if t > thr)
        r = {'threshold': thr, 'as_threshold': as_thr, 'as_loss_at_every_t_le_n': low_ok,
             'gap_masses': gaps, 'as_loss_interval_above_n': interval,
             'as_loss_at_threshold_minus_1': (rows[thr - 1][AL] > 0) if thr and thr - 1 in rows else None,
             'all_win_after_threshold': mono_after}
        if thr is not None:
            r['ASH_on_graph'] = (as_thr == thr) and not gaps
            r['scope'] = 'EXACT_THRESHOLD_FOUND'
        else:
            r['ASH_on_graph'] = None
            r['scope'] = f'NO_GAP_UP_TO_{ts[-1]}' if not gaps else 'GAP_CANDIDATE'
        res[goal] = r
    return res


def job(name, n, edges, hard, bindir, outdir, pyrev, rev_only_if_found=False):
    es = G.edge_string(edges)
    T = tcap(n, hard)
    base = os.path.join(outdir, name)
    rec = {'graph': name, 'n': n, 'edges': es, 'tmax_requested': T}
    rec['fwd_seconds'] = run([os.path.join(bindir, 'fwd'), name, str(n), es, str(T), '--stop'], base + '.fwd.jsonl')
    f = rows_of(base + '.fwd.jsonl')
    Tdone = max(f)
    found = any(t >= 2 and f[t]['nonstack'] == 0 for t in f)
    if rev_only_if_found and not found:
        rec['rev_layers_agree'] = None
    else:
      rec['rev_seconds'] = run([os.path.join(bindir, 'rev'), name, str(n), es, str(Tdone)], base + '.rev.jsonl')
      r = rows_of(base + '.rev.jsonl')
      rec['rev_layers_agree'] = sorted(r) == sorted(f) and all(all(f[t][k] == r[t][k] for k in KEYS) for t in f)
    if pyrev:
        rec['pyrev_seconds'] = run([sys.executable, os.path.join(os.path.dirname(__file__), 'cam_s003_pyrev.py'), name, str(n), es, str(Tdone), str(PY_CAP)], base + '.pyrev.jsonl')
        p = rows_of(base + '.pyrev.jsonl')
        rec['pyrev_layers'] = len(p)
        rec['pyrev_layers_agree'] = all(all(f[t][k] == p[t][k] for k in KEYS) for t in p)
    head = json.loads(open(base + '.fwd.jsonl').readline())
    bip = head['bipartite']
    assert bip == G.bipartite(n, edges)
    rec['analysis'] = analyse(n, bip, f)
    rec['rows'] = [{k: f[t][k] for k in ['t'] + KEYS} for t in sorted(f)]
    rec['examples'] = {t: {k: f[t][k] for k in ('ex_stack', 'ex_as_stack', 'ex_clear', 'ex_as_clear')} for t in sorted(f)}
    return rec


def main():
    tier, bindir, outdir = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(outdir, exist_ok=True)
    N = G.named()
    jobs = []
    if tier == 'T1':
        hard = {'C6': 16, 'C7': 23, 'C8': 32, 'K2_6': 20, 'W8': 14}
        for name in ['C6', 'C7', 'C8', 'C8_chord_04', 'C8_triangle_chords', 'triangular_ladder', 'K2_6', 'W8']:
            n, e = N[name]
            jobs.append((name, n, e, hard.get(name, 40), True))
    elif tier == 'T4':
        for name, hard in (('W9', 30), ('C9_chord_04', 30), ('Petersen', 25)):
            n, e = N[name]
            jobs.append((name, n, e, hard, True))
    elif tier == 'A3':
        for i, e in enumerate(G.connected_atlas(8)):
            jobs.append((f'A8_{i:05d}', 8, e, 26, False))
    elif tier in ('T2', 'T2b'):
        sizes = range(1, 7) if tier == 'T2' else [7]
        for n in sizes:
            for i, e in enumerate(G.connected_atlas(n)):
                jobs.append((f'A{n}_{i:04d}', n, e, 1100 if tier == 'T2' else 55, False))
    out = []
    workers = 1 if tier in ('T1', 'T4') else 4
    with cf.ThreadPoolExecutor(workers) as ex:
        futs = [ex.submit(job, nm, n, e, h, bindir, outdir, py, tier == 'A3') for nm, n, e, h, py in jobs]
        for fu in futs:
            rec = fu.result()
            out.append(rec)
            a = rec['analysis']
            print(rec['graph'], rec['n'], 'bip' if a['bipartite'] else 'nonbip',
                  'stack', a['stack'] if isinstance(a['stack'], str) else (a['stack']['threshold'], a['stack']['ASH_on_graph'], a['stack']['gap_masses']),
                  'clear', a['clear'] if isinstance(a['clear'], str) else (a['clear']['threshold'], a['clear']['ASH_on_graph'], a['clear']['gap_masses']),
                  'rev', rec['rev_layers_agree'], 'py', rec.get('pyrev_layers_agree'), rec['fwd_seconds'], flush=True)
    json.dump(out, open(os.path.join(outdir, f'summary_{tier}.json'), 'w'), sort_keys=True, separators=(',', ':'))


if __name__ == '__main__':
    main()
