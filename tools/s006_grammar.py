"""Exact minimum source-pile certificates for a fixed off-source box.

The optimizer uses repeated min-plus grammar relaxation. s006_verify.py checks
all production inequalities and attaining ancestry trees without this import.
No legal-move balance relaxation, state symmetry or implicit discarded pebbles.
"""
import itertools
import json
import lzma
import sys
import time
from pathlib import Path


def solve(n, edges, source, box=None):
    off_vertices = [v for v in range(n) if v != source]
    box = tuple(box or [0] * (n - 1))
    vectors = list(itertools.product(*(range(k + 1) for k in box)))
    # kind 3 means exactly zero source pebbles; 0,1,2 mean positive/residue.
    keys = [(v, d, k) for v in range(n) for d in vectors for k in range(4)]
    index = {key: i for i, key in enumerate(keys)}
    value = [None] * len(keys)
    witness = [None] * len(keys)
    nodes = []

    def improve(i, cost, children=None, leaf=None):
        if value[i] is None or cost < value[i]:
            value[i] = cost
            witness[i] = len(nodes)
            nodes.append({'cell': i, 'source_count': cost,
                          'children': children, 'leaf': leaf})
            return True
        return False

    zero = (0,) * (n - 1)
    improve(index[source, zero, 1], 1, leaf=source)
    for j, v in enumerate(off_vertices):
        if box[j]:
            d = list(zero)
            d[j] = 1
            improve(index[v, tuple(d), 3], 0, leaf=v)
    rules = []
    for a in vectors:
        for b in vectors:
            d = tuple(x + y for x, y in zip(a, b))
            if any(x > y for x, y in zip(d, box)):
                continue
            for u, v in [(u, v) for x, y in edges for u, v in ((x, y), (y, x))]:
                for ka in range(4):
                    for kb in range(4):
                        k = 3 if ka == kb == 3 else ((ka % 3) + (kb % 3)) % 3
                        rules.append((index[v, d, k], index[u, a, ka], index[u, b, kb]))
    for rounds in range(len(keys) + 1):
        changed = False
        for parent, a, b in rules:
            if value[a] is not None and value[b] is not None:
                cost = value[a] + value[b]
                # Zero/positive status is encoded in the rule, not inferred by residue.
                changed |= improve(parent, cost, [witness[a], witness[b]])
        if not changed:
            break
    else:
        raise AssertionError('minimum derivation height bound exceeded')
    return {'n': n, 'edges': edges, 'source': source,
            'off_vertices': off_vertices, 'box': box, 'rounds': rounds + 1,
            'cells': [{'vertex': v, 'off': d, 'kind': k, 'value': value[i],
                       'witness': witness[i]} for i, (v, d, k) in enumerate(keys)],
            'nodes': nodes}


def catalogue():
    rows = json.loads(Path('evidence/S003/T2_analysis.json').read_text())
    return [{'graph': r['graph'], 'n': r['n'],
             'edges': [list(map(int, e.split('-'))) for e in r['edges'].split(',')]}
            for r in rows if 2 <= r['n'] <= 5]


def main():
    start = time.monotonic()
    out = []
    for graph in catalogue():
        for s in range(graph['n']):
            cert = solve(graph['n'], graph['edges'], s)
            cert['graph'] = graph['graph']
            out.append(cert)
    for length in range(1, 4):
        n = 3 + length
        edges = [[0, 1], [0, 2], [1, 2]] + [[0 if i == 3 else i - 1, i] for i in range(3, n)]
        for s in range(n):
            cert = solve(n, edges, s)
            cert['graph'] = f'triangle_tail{length}'
            out.append(cert)
    buffer = solve(4, [[0, 1], [0, 2], [1, 2], [0, 3]], 0, [2, 2, 2])
    buffer['graph'] = 'triangle_leaf_buffer'
    result = {'pure': out, 'buffer': buffer, 'seconds': time.monotonic() - start}
    raw = json.dumps(result, separators=(',', ':')).encode()
    if '--check-only' not in sys.argv:
        Path('evidence/S006/grammar_certificates.json.xz').write_bytes(lzma.compress(raw))
    print(json.dumps({'pure_cases': len(out), 'buffer_cells': len(buffer['cells']),
                      'buffer_finite_cells': sum(c['value'] is not None for c in buffer['cells']),
                      'seconds': result['seconds']}))


if __name__ == '__main__':
    main()
