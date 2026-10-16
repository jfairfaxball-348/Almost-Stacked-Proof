#!/usr/bin/env python3
"""CAM-S015 summary builder (read-only over campaign output files).
For a set of (producer stdout, producer crit, checker stdout, checker crit) files:
byte-compare crit files, parse per-graph status, and report counts of ASH_OK,
UNKNOWN (capped/overflow) and ASH_FAIL, the largest L_all, and graphs listed.
usage: s015_summarize.py OUT.json graphs.txt prefix_prod prefix_chk  [chunk ids...]"""
import sys, json, hashlib

def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()

out, graphs, pp, pc = sys.argv[1:5]
chunks = sys.argv[5:] or ['']
names = [l.split()[0] for l in open(graphs)]
res = {'graphs_listed': len(names), 'chunks': {}, 'ASH_OK_DUAL': 0, 'UNKNOWN': [], 'ASH_FAIL': [], 'max_Lall': None, 'max_Lall_graph': None}
prod, chk = {}, {}
for c in chunks:
    a, b = f'{pp}{c}', f'{pc}{c}'
    ca, cb = a.replace('prod_', 'crit_prod_') + '.txt', b.replace('chk_', 'crit_chk_') + '.txt'
    same = open(ca, 'rb').read() == open(cb, 'rb').read()
    res['chunks'][c or 'all'] = {'crit_identical': same, 'crit_prod_sha256': sha(ca), 'crit_chk_sha256': sha(cb), 'prod_sha256': sha(a + '.txt'), 'chk_sha256': sha(b + '.txt')}
    for l in open(a + '.txt'):
        f = l.split(); prod[f[0]] = f
    for l in open(b + '.txt'):
        f = l.split(); chk[f[0]] = f
    for l in open(ca):
        pass
crit_ok = all(v['crit_identical'] for v in res['chunks'].values())
for g in names:
    p, q = prod.get(g), chk.get(g)
    if not p or not q or 'Lall' not in p or len(q) < 8 or not q[2].lstrip('-').isdigit():
        res['UNKNOWN'].append(g); continue
    Lall, LAS = int(p[3]), int(p[5])
    if (Lall, LAS) != (int(q[2]), int(q[3])) or int(p[7]) != int(q[4]) or int(p[9]) != int(q[5]):
        res['UNKNOWN'].append(g + ':DISAGREE'); continue
    if Lall == LAS and crit_ok: res['ASH_OK_DUAL'] += 1
    elif Lall != LAS: res['ASH_FAIL'].append(g)
    if res['max_Lall'] is None or Lall > res['max_Lall']: res['max_Lall'], res['max_Lall_graph'] = Lall, g
res['all_crit_identical'] = crit_ok
json.dump(res, open(out, 'w'), indent=1)
print({k: (v if not isinstance(v, list) else len(v)) for k, v in res.items() if k != 'chunks'}, 'crit_identical', crit_ok)
