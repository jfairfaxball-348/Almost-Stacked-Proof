#!/usr/bin/env python3
"""S016 comparator: s016_clear_layers (producer stdout + critfile) versus
s016_clear_check.mjs output.  usage: s016_clear_compare.py prod.txt prodcrit.txt chk.txt summary.json
Per graph: status, L_all, L_AS, |crit|, critAS and exact critical lists must agree; a graph
counts as ASH_OK/ASH_FAIL only when both tools completed and agree; otherwise UNKNOWN."""
import json, sys
prod, crit, chk, out = sys.argv[1:5]
P = {}
for line in open(prod):
    f = line.split()
    if not f:
        continue
    P[f[0]] = f
C = {}
for line in open(crit):
    f = line.split()
    if f:
        C[f[0]] = (int(f[1]), sorted(f[2:]))
K = {}
for line in open(chk):
    if not line.strip():
        continue
    head, _, lst = line.partition(' | ')
    f = head.split()
    K[f[0]] = (f, sorted(lst.split()))
assert set(P) == set(K), 'graph sets differ'
res = {'graphs': len(P), 'ASH_OK': [], 'ASH_FAIL': [], 'BIPARTITE_SKIP': 0, 'UNKNOWN': [], 'DISAGREE': []}
for g, f in P.items():
    kf, klist = K[g]
    st = f[3]
    if st in ('BIPARTITE_SKIP', 'DISCONNECTED_SKIP'):
        if kf[1] != st:
            res['DISAGREE'].append(g)
        elif st == 'BIPARTITE_SKIP':
            res['BIPARTITE_SKIP'] += 1
        continue
    if st not in ('ASH_OK', 'ASH_FAIL') or kf[1] not in ('ASH_OK', 'ASH_FAIL'):
        res['UNKNOWN'].append([g, st, kf[1]])
        continue
    lall, las, nc, cas = map(int, f[4:8])
    ok = (kf[1] == st and [int(x) for x in kf[2:6]] == [lall, las, nc, cas]
          and C[g][0] == lall and C[g][1] == klist and len(klist) == nc)
    if not ok:
        res['DISAGREE'].append(g)
        continue
    rec = {'graph': g, 'n': int(f[1]), 'L_all': lall, 'L_AS': las, 'crit': nc, 'critAS': cas}
    if st == 'ASH_OK':
        res['ASH_OK'].append(g)
    else:
        rec['critical_layer'] = klist
        res['ASH_FAIL'].append(rec)
res['ASH_OK_count'] = len(res['ASH_OK'])
res['ASH_FAIL_count'] = len(res['ASH_FAIL'])
res['thresholds'] = {g: int(P[g][4]) + 1 for g in res['ASH_OK']}
for r in res['ASH_FAIL']:
    res['thresholds'][r['graph']] = r['L_all'] + 1
del res['ASH_OK']
json.dump(res, open(out, 'w'), indent=1, sort_keys=True)
print('graphs', res['graphs'], 'ASH_OK', res['ASH_OK_count'], 'ASH_FAIL', res['ASH_FAIL_count'],
      'bipartite_skip', res['BIPARTITE_SKIP'], 'UNKNOWN', len(res['UNKNOWN']), 'DISAGREE', len(res['DISAGREE']))
print('ASH_FAIL graphs:', ' '.join(r['graph'] for r in res['ASH_FAIL']))
