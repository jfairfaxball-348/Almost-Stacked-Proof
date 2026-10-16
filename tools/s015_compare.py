#!/usr/bin/env python3
"""CAM-S015-82 comparison of producer per-graph L_all against frozen S003
records (T2/T2b orders<=7 and A3 order-8 partial atlas, cap_t=26), matched by
the repository's own S003 canonical form.  Read-only on frozen evidence.
usage: s015_compare.py producer_file frozen_kind(T2b|T2|A3)"""
import sys, json, lzma
sys.path.insert(0, 'tools')
import cam_s003_graphs as G

def edges_of(s):
    return [tuple(map(int, t.split('-'))) for t in s.split(',')] if s and s != '-' else []

prod = {}
for line in open(sys.argv[1]):
    f = line.split()
    n = int(f[1])
    from s015_graphs import g6_decode
    nn, e = g6_decode(f[0])
    prod[G._canon(n, e)[0]] = (int(f[3]), int(f[5]), f[-1])
kind = sys.argv[2]
if kind == 'A3':
    d = json.load(lzma.open('evidence/S003/A3_n8_analysis.json.xz'))
    recs = [(g[1], 8, g[3][0], g[3][3]) for g in d['graphs']]
else:
    d = json.load(open(f'evidence/S003/{kind}_analysis.json'))
    recs = []
    for g in d:
        st = g['analysis']['stack']
        thr = st.get('threshold') if st.get('scope') == 'EXACT_THRESHOLD_FOUND' else None
        recs.append((g['edges'], g['n'], thr, g['analysis'].get('computed_tmax')))
agree = mism = unknown = missing = 0
for es, n, thr, tmax in recs:
    k = G._canon(n, edges_of(es))[0]
    if k not in prod:
        missing += 1; continue
    lall = prod[k][0]
    if thr is None:
        # frozen record capped at tmax: consistent iff producer threshold exceeds cap
        if lall + 1 > tmax: unknown += 1
        else: mism += 1; print('CAP_INCONSISTENT', es, lall, tmax)
    elif thr == lall + 1: agree += 1
    else: mism += 1; print('MISMATCH', es, thr, lall)
print(kind, 'records', len(recs), 'agree', agree, 'capped_consistent', unknown, 'mismatch', mism, 'missing', missing)
