#!/usr/bin/env python3
"""S016: compare s016_clear_layers CLEAR output with frozen S003 T2/T2b and S004 clear data.
usage: s016_frozen_compare.py prod.txt out.json
Frozen fields: analysis.clear.threshold and analysis.clear.as_loss_at_threshold_minus_1
(scope EXACT_THRESHOLD_FOUND), S004 A7_*_clear.summary.json for the three S003-UNKNOWN graphs."""
import json, sys, glob
prod, out = sys.argv[1:3]
frozen = {}
for fn in ['evidence/S003/T2_analysis.json', 'evidence/S003/T2b_analysis.json']:
    for r in json.load(open(fn)):
        cl = r['analysis']['clear']
        if isinstance(cl, dict) and cl.get('scope') == 'EXACT_THRESHOLD_FOUND':
            frozen[r['graph']] = (cl['threshold'], bool(cl['as_loss_at_threshold_minus_1']), 'S003')
        elif isinstance(cl, dict):
            frozen.setdefault(r['graph'], None)
        else:
            frozen[r['graph']] = 'BIPARTITE'
s004 = {}
for fn in glob.glob('evidence/S004/A7_*_clear.summary.json'):
    s004[fn.split('/')[-1].split('\\')[-1][:7]] = json.load(open(fn))
res = {'agree': 0, 'disagree': [], 'bipartite_agree': 0, 'no_frozen_value': [], 's004_records': {}}
for line in open(prod):
    f = line.split()
    if not f:
        continue
    g, st = f[0], f[3]
    fz = frozen.get(g, 'MISSING')
    if st == 'BIPARTITE_SKIP':
        if fz == 'BIPARTITE':
            res['bipartite_agree'] += 1
        else:
            res['disagree'].append([g, 'bipartite?', str(fz)])
        continue
    if st not in ('ASH_OK', 'ASH_FAIL'):
        res['disagree'].append([g, st, str(fz)])
        continue
    thr, ash = int(f[4]) + 1, st == 'ASH_OK'
    if fz is None or fz == 'MISSING':
        res['no_frozen_value'].append([g, thr, ash])
        if g in s004:
            res['s004_records'][g] = {'ours': [thr, ash], 's004_summary': s004[g]}
        continue
    if fz == 'BIPARTITE' or (thr, ash) != fz[:2]:
        res['disagree'].append([g, [thr, ash], str(fz)])
    else:
        res['agree'] += 1
json.dump(res, open(out, 'w'), indent=1, sort_keys=True)
print('agree', res['agree'], 'bipartite_agree', res['bipartite_agree'], 'disagree', len(res['disagree']),
      'no_frozen_value', len(res['no_frozen_value']))
for g, v in res['s004_records'].items():
    print(g, v['ours'], json.dumps(v['s004_summary'])[:400])
