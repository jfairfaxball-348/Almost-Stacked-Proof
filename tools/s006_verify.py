"""Independent proof-certificate checker: no optimizer/forward-solver import.

Attaining binary trees give upper bounds; every local production inequality
gives a lower bound by induction on ANY ancestry tree. Infinity is fail-closed.
"""
import collections
import hashlib
import itertools
import json
import lzma
import sys
from pathlib import Path


def check(cert):
    n, source = cert['n'], cert['source']
    edges = {frozenset(e) for e in cert['edges']}
    off = cert['off_vertices']
    assert off == [v for v in range(n) if v != source]
    box = tuple(cert['box'])
    cells = cert['cells']
    table = {(c['vertex'], tuple(c['off']), c['kind']): c for c in cells}
    vecs = list(itertools.product(*(range(k + 1) for k in box)))
    assert len(table) == len(cells) == n * len(vecs) * 4
    assert set(table) == {(v, d, k) for v in range(n) for d in vecs for k in range(4)}
    # Decode every derivation independently into its exact input vector.
    decoded = []
    for i, node in enumerate(cert['nodes']):
        cell = cells[node['cell']]
        if node['children'] is None:
            v = node['leaf']
            assert cell['vertex'] == v and 0 <= v < n
            configuration = tuple(int(w == v) for w in range(n))
        else:
            assert node['leaf'] is None and len(node['children']) == 2
            a, b = node['children']
            assert 0 <= a < i and 0 <= b < i
            ca, va = decoded[a]
            cb, vb = decoded[b]
            assert va == vb and frozenset((va, cell['vertex'])) in edges
            configuration = tuple(x + y for x, y in zip(ca, cb))
        assert configuration[source] == node['source_count']
        assert tuple(configuration[v] for v in off) == tuple(cell['off'])
        kind = 3 if configuration[source] == 0 else configuration[source] % 3
        assert kind == cell['kind'] and sum(configuration) > 0
        decoded.append((configuration, cell['vertex']))
    finite = 0
    for c in cells:
        value = c['value']
        if value is None:
            assert c['witness'] is None
            continue
        assert isinstance(value, int) and value >= 0
        assert (value == 0) == (c['kind'] == 3)
        assert c['kind'] == 3 or value % 3 == c['kind']
        configuration, root = decoded[c['witness']]
        assert root == c['vertex'] and configuration[source] == value
        assert tuple(configuration[v] for v in off) == tuple(c['off'])
        # Actual legal postorder evaluation, retaining every original pebble.
        current = list(configuration)
        stack = [(c['witness'], False)]
        while stack:
            j, ready = stack.pop()
            node = cert['nodes'][j]
            if node['children'] is None:
                continue
            if not ready:
                stack.append((j, True))
                stack.extend((child, False) for child in node['children'])
            else:
                child = cert['nodes'][node['children'][0]]
                u = cells[child['cell']]['vertex']
                v = cells[node['cell']]['vertex']
                assert current[u] >= 2 and frozenset((u, v)) in edges
                current[u] -= 2
                current[v] += 1
        assert current == [int(v == c['vertex']) for v in range(n)]
        finite += 1
    # Bounds must hold for EVERY base and production, including zero-source ones.
    def upper_bound(key, candidate):
        val = table[key]['value']
        assert val is not None and val <= candidate, (key, val, candidate)
    zero = (0,) * len(off)
    upper_bound((source, zero, 1), 1)
    for j, v in enumerate(off):
        if box[j] >= 1:
            d = list(zero)
            d[j] = 1
            upper_bound((v, tuple(d), 3), 0)
    finite_by_vertex = {u: [c for c in cells if c['vertex'] == u and c['value'] is not None]
                        for u in range(n)}
    productions = 0
    for u in range(n):
        neighbours = [v for v in range(n) if frozenset((u, v)) in edges]
        for a in finite_by_vertex[u]:
            for b in finite_by_vertex[u]:
                d = tuple(x + y for x, y in zip(a['off'], b['off']))
                if any(x > y for x, y in zip(d, box)):
                    continue
                total = a['value'] + b['value']
                kind = 3 if total == 0 else total % 3
                for v in neighbours:
                    upper_bound((v, d, kind), total)
                    productions += 1
    return {'graph': cert['graph'], 'source': source, 'cells': len(cells),
            'finite_cells': finite, 'production_inequalities': productions,
            'attaining_derivations_legally_replayed': finite, 'all_equal': True}


def main():
    raw = lzma.decompress(Path('evidence/S006/grammar_certificates.json.xz').read_bytes())
    data = json.loads(raw)
    expected = {}
    for row in json.loads(Path('evidence/S003/T2_analysis.json').read_text()):
        if 2 <= row['n'] <= 5:
            es = {tuple(map(int, e.split('-'))) for e in row['edges'].split(',')}
            for s in range(row['n']):
                expected[row['graph'], s] = (row['n'], es)
    for length in range(1, 4):
        n = length + 3
        es = {(0, 1), (0, 2), (1, 2)} | {(0 if i == 3 else i-1, i) for i in range(3, n)}
        for s in range(n):
            expected[f'triangle_tail{length}', s] = (n, es)
    assert len(data['pure']) == len(expected) == 152
    assert {(c['graph'], c['source']) for c in data['pure']} == set(expected)
    for c in data['pure']:
        n, es = expected[c['graph'], c['source']]
        assert c['n'] == n and {tuple(e) for e in c['edges']} == es
        assert c['box'] == [0] * (n - 1)
    b = data['buffer']
    assert b['n'] == 4 and b['source'] == 0 and b['box'] == [2, 2, 2]
    assert {tuple(e) for e in b['edges']} == {(0, 1), (0, 2), (1, 2), (0, 3)}
    results = [check(c) for c in data['pure'] + [data['buffer']]]
    # Independent BFS distance/odd-walk check against cold-audited Theorem19.
    pure_values = 0
    for c in data['pure']:
        adj = [[] for _ in range(c['n'])]
        for u, v in c['edges']:
            adj[u].append(v)
            adj[v].append(u)
        dist = {c['source']: 0}
        queue = [c['source']]
        for u in queue:
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        h = min((dist[u] for u, v in c['edges'] if dist[u] == dist[v]), default=None)
        values = {r: min((x['value'] for x in c['cells'] if x['kind'] == r and x['value'] is not None), default=None)
                  for r in range(3)}
        assert values == {0: None if h is None else 3 * 2**h, 1: 1, 2: 2}
        if h is None:
            for x in c['cells']:
                expected = 2**dist[x['vertex']]
                assert x['value'] == (expected if x['kind'] == expected % 3 else None)
        else:
            assert all(x['value'] is not None for x in c['cells'] if x['kind'] != 3)
        pure_values += sum(x['value'] is not None for x in c['cells'])
    output = {'certificate_sha256': hashlib.sha256(raw).hexdigest(),
              'cases': results, 'pure_finite_values': pure_values,
              'all_grammar_bounds_and_legal_derivations': True}
    if '--check-only' not in sys.argv:
        Path('evidence/S006/grammar_verification.json').write_text(json.dumps(output, indent=2) + '\n', newline='\n')
    print(json.dumps({'cases': len(results), 'pure_finite_values': pure_values,
                      'attaining_derivations': sum(r['finite_cells'] for r in results),
                      'production_inequalities': sum(r['production_inequalities'] for r in results),
                      'all_verified': True}))


if __name__ == '__main__':
    main()
