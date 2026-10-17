#!/usr/bin/env python3
"""S018 diagnostic: reconstruct one constant's type (and level params) from two lean4export
3.1.0 NDJSON files and print the first structural difference, binder names included.
usage: s018_export_diff.py A.export B.export Const.Name"""
import json, sys
sys.setrecursionlimit(100000)
def load(path):
    N = {0: ()}; L = {}; E = {}; consts = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            o = json.loads(line)
            if 'in' in o:
                k = 'str' if 'str' in o else 'num'
                v = o[k]; N[o['in']] = N[v['pre']] + ((v['str'] if k == 'str' else v['i']),)
            elif 'il' in o:
                L[o['il']] = {k: v for k, v in o.items() if k != 'il'}
            elif 'ie' in o:
                E[o['ie']] = {k: v for k, v in o.items() if k != 'ie'}
            else:
                for k, v in o.items():
                    if isinstance(v, dict) and 'name' in v:
                        consts[N[v['name']]] = (k, v)
                    elif isinstance(v, dict) and 'constVal' in v:
                        consts[N[v['constVal']['name']]] = (k, v['constVal'])
    return N, L, E, consts
def lvl(L, N, i):
    if i == 0: return 'zero'
    o = L[i]; (k, v), = o.items()
    if k == 'param': return ('param', N[v])
    if k == 'succ': return ('succ', lvl(L, N, v))
    return (k, tuple(lvl(L, N, x) for x in v))
def expr(D, i, depth=0):
    N, L, E, _ = D
    o = E[i]; out = {}
    for k, v in o.items():
        if k == 'bvar': out[k] = v
        elif k == 'sort': out[k] = lvl(L, N, v)
        elif k == 'const': out[k] = (N[v['name']], tuple(lvl(L, N, u) for u in v['us']))
        elif k in ('forallE', 'lam'):
            out[k] = dict(name=N[v['name']], bi=v['binderInfo'], type=expr(D, v['type']), body=expr(D, v['body']))
        elif k == 'app': out[k] = (expr(D, v['fn']), expr(D, v['arg']))
        elif k == 'mdata': out[k] = (repr(v.get('data')), expr(D, v['expr']))
        else: out[k] = repr(v)
    return out
def first_diff(a, b, path='type'):
    if type(a) != type(b): return path, a, b
    if isinstance(a, dict):
        if set(a) != set(b): return path, sorted(a), sorted(b)
        for k in a:
            r = first_diff(a[k], b[k], path + '.' + k)
            if r: return r
    elif isinstance(a, (list, tuple)):
        if len(a) != len(b): return path, a, b
        for j, (x, y) in enumerate(zip(a, b)):
            r = first_diff(x, y, f'{path}[{j}]')
            if r: return r
    elif a != b: return path, a, b
    return None
A, B = load(sys.argv[1]), load(sys.argv[2]); name = tuple(sys.argv[3].split('.'))
ca, cb = A[3][name], B[3][name]
print('kind', ca[0], cb[0])
for side, D, c in (('A', A, ca), ('B', B, cb)):
    print(side, 'levelParams', [D[0][x] for x in c[1].get('levelParams', [])])
r = first_diff(expr(A, ca[1]['type']), expr(B, cb[1]['type']))
print('FIRST_DIFF', r if r is None else (r[0], str(r[1])[:300], str(r[2])[:300]))
