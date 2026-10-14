"""Independent forest optimality/legality and two rooted stack DP traversals."""
import itertools
import json
import lzma
import sys
from pathlib import Path


def configurations(n, t):
    for cuts in itertools.combinations(range(t + n - 1), n - 1):
        marks = (-1,) + cuts + (t + n - 1,)
        yield tuple(marks[i + 1] - marks[i] - 1 for i in range(n))


def main():
    from s006_verify import check
    clear = json.loads(lzma.decompress(Path('evidence/S006/grammar_certificates.json.xz').read_bytes()))['buffer']
    check(clear)
    data = json.loads(Path('evidence/S006/stack_buffer_certificate.json').read_text())
    cells, n, source = clear['cells'], clear['n'], clear['source']
    edges = {tuple(sorted(e)) for e in clear['edges']}
    arcs = [(u, v) for a, b in edges for u, v in ((a, b), (b, a))]
    index = {(c['vertex'], tuple(c['off']), c['kind']): i for i, c in enumerate(cells)}
    values = data['values']
    assert len(values) == len(cells) == len(data['roots'])
    clear_vectors = []
    for node in clear['nodes']:
        if node['children'] is None:
            vec = tuple(int(v == node['leaf']) for v in range(n))
        else:
            a, b = node['children']
            vec = tuple(x + y for x, y in zip(clear_vectors[a], clear_vectors[b]))
        clear_vectors.append(vec)
    decoded = []
    for i, node in enumerate(data['nodes']):
        cell = cells[node['cell']]
        if node['children'] is None:
            ref = node['clear_node']
            assert clear['nodes'][ref]['cell'] == node['cell']
            vec, output = clear_vectors[ref], 1
        else:
            a, b = node['children']
            assert a < i and b < i and node['clear_node'] is None
            va, ra, na = decoded[a]
            vb, rb, nb = decoded[b]
            assert ra == rb == cell['vertex']
            vec, output = tuple(x + y for x, y in zip(va, vb)), na + nb
        assert tuple(vec[v] for v in clear['off_vertices']) == tuple(cell['off'])
        assert (3 if vec[source] == 0 else vec[source] % 3) == cell['kind']
        decoded.append((vec, cell['vertex'], output))
    finite = inequalities = 0
    for i, cell in enumerate(cells):
        val = values[i]
        cval = cell['value']
        if cval is not None:
            assert val is not None and val <= cval
        if val is None:
            assert data['roots'][i] is None
            continue
        vec, root, count = decoded[data['roots'][i]]
        assert root == cell['vertex'] and vec[source] == val and count > 0
        assert val >= 0 and (val == 0) == (cell['kind'] == 3)
        current = list(vec)
        # Collect and execute the constituent clearing trees, never merge forests.
        todo = [data['roots'][i]]
        while todo:
            node = data['nodes'][todo.pop()]
            if node['children'] is not None:
                todo.extend(node['children'])
                continue
            stack = [(node['clear_node'], False)]
            while stack:
                ref, ready = stack.pop()
                branch = clear['nodes'][ref]
                if branch['children'] is None:
                    continue
                if ready:
                    child = clear['nodes'][branch['children'][0]]
                    u, v = cells[child['cell']]['vertex'], cells[branch['cell']]['vertex']
                    assert current[u] >= 2 and tuple(sorted((u, v))) in edges
                    current[u] -= 2
                    current[v] += 1
                else:
                    stack.append((ref, True))
                    stack.extend((kid, False) for kid in branch['children'])
        assert current == [count if v == root else 0 for v in range(n)]
        finite += 1
    for i, a in enumerate(cells):
        if values[i] is None:
            continue
        for j, b in enumerate(cells):
            if values[j] is None or a['vertex'] != b['vertex']:
                continue
            d = tuple(x + y for x, y in zip(a['off'], b['off']))
            if any(x > y for x, y in zip(d, clear['box'])):
                continue
            total = values[i] + values[j]
            key = (a['vertex'], d, 3 if total == 0 else total % 3)
            p = index[key]
            assert values[p] is not None and values[p] <= total
            inequalities += 1
    prev_f, prev_r = {}, {}
    layers = []
    tested = 0
    for t in range(1, 17):
        f = {}
        for c in configurations(n, t):
            mask = (1 << c.index(t)) if t in c else 0
            for u, v in arcs:
                if c[u] >= 2:
                    d = list(c)
                    d[u] -= 2
                    d[v] += 1
                    mask |= prev_f.get(tuple(d), 0)
            if mask:
                f[c] = mask
        r = {tuple(t if v == q else 0 for v in range(n)): 1 << q for q in range(n)}
        for c, mask in prev_r.items():
            for u, v in arcs:
                if c[v]:
                    d = list(c)
                    d[v] -= 1
                    d[u] += 2
                    d = tuple(d)
                    r[d] = r.get(d, 0) | mask
        assert f == r
        for c in configurations(n, t):
            if max(c[1:]) <= 2:
                for q in range(n):
                    kind = 3 if c[0] == 0 else c[0] % 3
                    val = values[index[q, c[1:], kind]]
                    predicted = val is not None and (c[0] == 0 or c[0] >= val)
                    assert predicted == bool(f.get(c, 0) & (1 << q)), (c, q, val)
                    tested += 1
        layers.append({'mass': t, 'full_forward_reverse_equal': True, 'winning': len(f)})
        prev_f, prev_r = f, r
    result = {'finite_forest_cells': finite, 'concatenation_inequalities': inequalities,
              'buffer_source_target_tests': tested, 'layers': layers,
              'all_legal_and_optimal': True}
    if '--check-only' not in sys.argv:
        Path('evidence/S006/stack_buffer_verification.json').write_text(json.dumps(result, indent=2) + '\n', newline='\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'layers'}))


if __name__ == '__main__':
    main()
