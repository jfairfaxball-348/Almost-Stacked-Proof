#!/usr/bin/env python3
"""CAM-S015-85 order-9 summary over the restructured file set (amendment 11).
For every (producer stdout, producer crit, checker stdout, checker crit) quadruple
listed below, rows are keyed by graph6 name.  A graph is ASH_OK_DUAL iff some
quadruple contains complete rows for it from BOTH tools with equal (L_all, L_AS,
critical count, AS critical count) AND byte-equal critical-layer lines, and
L_all == L_AS.  ASH_FAIL requires the same agreement with L_all != L_AS.
Everything else in graphs_9.txt is UNKNOWN (missing, capped, overflow, single tool).
usage: s015_summarize9.py OUT.json"""
import sys, json, hashlib, os
D = 'evidence/S015/cam85/'
quads = [('chunk_0%d' % i, 'chunk_0%d' % i) for i in range(1, 8)] + [('chunk_00', 'chunk_00')]
quads += [('chunk_00r_00', 'chunk_00r_00.par'), ('chunk_00r_01', 'chunk_00r_01'), ('chunk_00r_02', 'chunk_00r_02')]
quads += [('chunk_00s_0%d' % i, 'chunk_00s_0%d' % i) for i in range(4)] + [('chunk_00u_0%d' % i, 'chunk_00u_0%d' % i) for i in range(3)] + [('chunk_00t_0%d' % i, 'chunk_00t_0%d' % i) for i in range(2)]
def rows(p):
    out = {}
    if os.path.exists(p):
        for l in open(p):
            f = l.split()
            if f: out[f[0]] = f
    return out
def crit(p):
    out = {}
    if os.path.exists(p):
        for l in open(p):
            f = l.split(' ', 1)
            out[f[0]] = l
    return out
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as fh:
        for b in iter(lambda: fh.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
names = [l.split()[0] for l in open('evidence/S015/cam83/graphs_9.txt')]
status = {}; files = {}
for pp, cc in quads:
    P, C = rows(D + f'prod_{pp}.txt'), rows(D + f'chk_{cc}.txt')
    PC, CC = crit(D + f'crit_prod_{pp}.txt'), crit(D + f'crit_chk_{cc}.txt')
    for f in [f'prod_{pp}.txt', f'chk_{cc}.txt', f'crit_prod_{pp}.txt', f'crit_chk_{cc}.txt']:
        if os.path.exists(D + f): files[f] = sha(D + f)
    for g, p in P.items():
        q = C.get(g)
        if status.get(g, ('',))[0] in ('ASH_OK_DUAL', 'ASH_FAIL_DUAL'): continue
        if not q or len(p) < 10 or p[2] != 'Lall' or len(q) < 8 or not q[2].lstrip('-').isdigit():
            status[g] = ('UNKNOWN', pp); continue
        agree = (int(p[3]), int(p[5]), int(p[7]), int(p[9])) == (int(q[2]), int(q[3]), int(q[4]), int(q[5])) and PC.get(g) is not None and PC.get(g) == CC.get(g)
        if not agree: status[g] = ('UNKNOWN_DISAGREE', pp); continue
        status[g] = ('ASH_OK_DUAL' if p[3] == p[5] else 'ASH_FAIL_DUAL', pp, int(p[3]), int(p[5]))
ok = [g for g in names if status.get(g, ('',))[0] == 'ASH_OK_DUAL']
fail = [g for g in names if status.get(g, ('',))[0] == 'ASH_FAIL_DUAL']
unk = [g for g in names if status.get(g, ('',))[0] not in ('ASH_OK_DUAL', 'ASH_FAIL_DUAL')]
trees = {l.split()[0] for l in open('evidence/S015/cam83/graphs_9.txt') if l.split()[2].count('-') == 8}
res = {'campaign': 'CAM-S015-85', 'graphs_listed': len(names), 'ASH_OK_DUAL': len(ok), 'ASH_FAIL': fail,
       'ASH_FAIL_detail': {g: status[g][2:] for g in fail}, 'UNKNOWN': unk, 'UNKNOWN_trees': [g for g in unk if g in trees],
       'UNKNOWN_nontrees': [g for g in unk if g not in trees], 'trees_total': len(trees),
       'max_Lall': max((status[g][2] for g in ok + fail), default=None),
       'scope': 'nauty-geng -c 9 list (261080 = OEIS A001349); dual compiled per amendments 4, 11; UNKNOWN trees satisfy critical ASH* by EARLIER TreeStack + S003 Thm 8 (not by this computation)',
       'file_sha256': files}
json.dump(res, open(sys.argv[1], 'w'), indent=1)
print({k: (len(v) if isinstance(v, (list, dict)) and k != 'ASH_FAIL' else v) for k, v in res.items() if k not in ('file_sha256', 'scope')})
