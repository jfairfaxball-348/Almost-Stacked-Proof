#!/usr/bin/env python3
"""S016: compare a producer run with a checker run that was STOPPED early (owner request).
Only graphs whose checker line is complete are compared, with the same criteria as
s016_clear_compare.py; all other graphs are reported as PRODUCER_ONLY (not dual-verified).
usage: s016_partial_compare.py prod.txt prodcrit.txt chkparts... --out summary.json"""
import json, sys
args = sys.argv[1:]
out = args[args.index('--out') + 1]
prod, crit, chks = args[0], args[1], args[2:args.index('--out')]
P = {l.split()[0]: l.split() for l in open(prod) if l.strip()}
C = {}
for l in open(crit):
    f = l.split()
    if f:
        C[f[0]] = (int(f[1]), sorted(f[2:]))
K = {}
for fn in chks:
    for l in open(fn):
        if not l.endswith('\n') or not l.strip():
            continue  # a line cut by the stop is ignored
        head, _, lst = l.partition(' | ')
        f = head.split()
        K[f[0]] = (f, sorted(lst.split()))
res = {'graphs': len(P), 'checker_completed': 0, 'dual_ok': 0, 'dual_fail': [], 'bipartite_agree': 0,
       'checker_unknown': [], 'disagree': [], 'producer_status_counts': {}}
for g, f in P.items():
    res['producer_status_counts'][f[3]] = res['producer_status_counts'].get(f[3], 0) + 1
    if g not in K:
        continue
    res['checker_completed'] += 1
    kf, kl = K[g]
    st = f[3]
    if st in ('BIPARTITE_SKIP', 'DISCONNECTED_SKIP'):
        if kf[1] == st:
            res['bipartite_agree'] += 1
        else:
            res['disagree'].append(g)
        continue
    if st not in ('ASH_OK', 'ASH_FAIL') or kf[1] not in ('ASH_OK', 'ASH_FAIL'):
        res['checker_unknown'].append([g, st, kf[1]])
        continue
    ok = (kf[1] == st and [int(x) for x in kf[2:6]] == [int(x) for x in f[4:8]]
          and C[g][0] == int(f[4]) and C[g][1] == kl)
    if not ok:
        res['disagree'].append(g)
    elif st == 'ASH_OK':
        res['dual_ok'] += 1
    else:
        res['dual_fail'].append(g)
res['producer_only'] = res['graphs'] - res['checker_completed']
json.dump(res, open(out, 'w', newline='\n'), indent=1, sort_keys=True)
print(json.dumps({k: v for k, v in res.items() if k != 'checker_unknown'}), 'checker_unknown', len(res['checker_unknown']))
