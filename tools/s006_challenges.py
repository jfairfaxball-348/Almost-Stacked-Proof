"""Preregistered full forward/reverse rooted layers and attachment challenges.

All configurations are labelled tuples. No optimizer code is imported. Full
dictionary equality is checked at each layer; hashes only preserve the log.
"""
import hashlib
import itertools
import json
import lzma
import math
import sys
import time
from pathlib import Path


def compositions(n, total):
    if n == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in compositions(n - 1, total - first):
            yield (first,) + rest


def forward(n, edges, total, previous):
    current = {}
    for c in compositions(n, total):
        if total == 1:
            mask = 1 << c.index(1)
        else:
            mask = 0
            for u, v in [(u, v) for a, b in edges for u, v in ((a, b), (b, a))]:
                if c[u] >= 2:
                    d = list(c)
                    d[u] -= 2
                    d[v] += 1
                    mask |= previous.get(tuple(d), 0)
        if mask:
            current[c] = mask
    return current


def reverse(n, edges, total, previous):
    if total == 1:
        return {tuple(int(i == v) for i in range(n)): 1 << v for v in range(n)}
    current = {}
    # Own previous winning table, inverse production, no universe enumeration.
    for c, mask in previous.items():
        for a, b in edges:
            for source, target in ((a, b), (b, a)):
                if c[target] > 0:
                    d = list(c)
                    d[target] -= 1
                    d[source] += 2
                    d = tuple(d)
                    current[d] = current.get(d, 0) | mask
    return current


def closure(configuration, edges):
    start = tuple(configuration)
    parents = {start: None}
    queue = [start]
    first_goal = None
    for c in queue:
        if sum(c) == 1 and first_goal is None:
            first_goal = c
        for a, b in edges:
            for u, v in ((a, b), (b, a)):
                if c[u] >= 2:
                    d = list(c)
                    d[u] -= 2
                    d[v] += 1
                    d = tuple(d)
                    if d not in parents:
                        parents[d] = (c, (u, v))
                        queue.append(d)
    trace = []
    x = first_goal
    while x is not None and parents[x] is not None:
        c, move = parents[x]
        trace.append({'from': c, 'move': move, 'to': x})
        x = c
    return {'configuration': start, 'edges': edges, 'reachable': sorted(parents),
            'clearable': first_goal is not None, 'trace': list(reversed(trace))}


def main():
    start = time.monotonic()
    certs = json.loads(lzma.decompress(Path('evidence/S006/grammar_certificates.json.xz').read_bytes()))
    grouped = {}
    for c in certs['pure']:
        grouped.setdefault(c['graph'], []).append(c)
    # Tail0 K3 uses canonical labels independently of inherited atlas labels.
    extra = {'triangle_tail0': (3, [[0, 1], [0, 2], [1, 2]], 16),
             'triangle_tail4': (7, [[0, 1], [0, 2], [1, 2], [0, 3], [3, 4], [4, 5], [5, 6]], 10)}
    tails = {}
    results = []
    tests = 0
    buffer_tests = 0
    buffer_table = {(c['vertex'], tuple(c['off']), c['kind']): c['value'] for c in certs['buffer']['cells']}
    names = list(grouped) + list(extra)
    for name in names:
        if time.monotonic() - start > 300:
            results.append({'graph': name, 'scope': 'TOTAL_TIME_CUTOFF', 'last_layer': 0})
            continue
        cases = grouped.get(name, [])
        if cases:
            n, edges = cases[0]['n'], cases[0]['edges']
            maximum = max(c['value'] or 0 for q in cases for c in q['cells'])
            cap = min(32, maximum + 3)
            if name.startswith('triangle_tail'):
                cap = max(cap, 16)
        else:
            n, edges, cap = extra[name]
        tables = {c['source']: {(r['vertex'], r['kind']): r['value'] for r in c['cells']}
                  for c in cases}
        prev_f, prev_r = {}, {}
        layers = []
        scopes = 'BOUNDED_COMPLETE'
        small = {}
        for total in range(1, cap + 1):
            if math.comb(total + n - 1, n - 1) > 300_000:
                scopes = 'STATE_LIMIT'
                break
            if time.monotonic() - start > 300:
                scopes = 'TOTAL_TIME_CUTOFF'
                break
            f = forward(n, edges, total, prev_f)
            r = reverse(n, edges, total, prev_r)
            assert f == r, (name, total, 'full rooted-mask dictionary mismatch')
            for source, table in tables.items():
                pile = tuple(total if v == source else 0 for v in range(n))
                actual = f.get(pile, 0)
                predicted = sum(1 << v for v in range(n)
                                if table[v, total % 3] is not None and total >= table[v, total % 3])
                assert actual == predicted, (name, source, total, actual, predicted)
                tests += n
            if name == 'triangle_tail1' and total <= 16:
                for c in compositions(n, total):
                    if max(c[1:]) > 2:
                        continue
                    for target in range(n):
                        value = buffer_table[target, c[1:], 3 if c[0] == 0 else c[0] % 3]
                        prediction = value is not None and (c[0] == 0 or c[0] >= value)
                        assert prediction == bool(f.get(c, 0) & (1 << target)), (c, target, value)
                        buffer_tests += 1
            if name.startswith('triangle_tail') and total <= 16:
                small[total] = f
            digest = hashlib.sha256()
            for c, mask in sorted(f.items()):
                digest.update(bytes(c) + bytes([mask]))
            layers.append({'mass': total, 'configurations': math.comb(total + n - 1, n - 1),
                           'rooted_winning_configurations': len(f), 'full_forward_reverse_equal': True,
                           'root_mask_sha256': digest.hexdigest()})
            prev_f, prev_r = f, r
        if small:
            tails[name] = (n, edges, small)
        row = {'graph': name, 'n': n, 'edges': edges, 'cap': cap, 'last_layer': len(layers),
               'scope': scopes, 'layers': layers}
        results.append(row)
        print(json.dumps({k: row[k] for k in ('graph', 'last_layer', 'scope')}), flush=True)
    scalar = []
    first_pos = first_neg = None
    for length in range(1, 5):
        name = f'triangle_tail{length}'
        base_name = f'triangle_tail{length-1}'
        if name not in tails or base_name not in tails:
            continue
        n, edges, layers = tails[name]
        _, _, core = tails[base_name]
        false_pos = false_neg = count = 0
        for total in sorted(layers):
            if total > (16 if length <= 3 else 10):
                continue
            for c in compositions(n, total):
                m = c[-1]
                gain = m // 2 if m % 2 == 0 else (m - 3) // 2
                adjusted = list(c[:-1])
                adjusted[0 if length == 1 else n - 2] += gain
                good = bool(min(adjusted) >= 0 and core.get(sum(adjusted), {}).get(tuple(adjusted), 0))
                actual = bool(layers[total].get(c, 0))
                count += 1
                false_pos += good and not actual
                false_neg += actual and not good
                if good and not actual and first_pos is None:
                    first_pos = closure(c, edges)
                    first_pos['adjusted_core'] = adjusted
                if actual and not good and first_neg is None:
                    first_neg = closure(c, edges)
                    first_neg['adjusted_core'] = adjusted
        scalar.append({'graph': name, 'tested': count, 'false_positive': false_pos, 'false_negative': false_neg})
    # Fixed-target failure: K3 5e0 clears somewhere, but never at its source.
    rooted_example = closure((5, 0, 0), [[0, 1], [0, 2], [1, 2]])
    assert rooted_example['clearable'] and (1, 0, 0) not in map(tuple, rooted_example['reachable'])
    output = {'graphs': results, 'pure_source_target_tests': tests,
              'buffer_source_target_tests': buffer_tests, 'scalar': scalar,
              'first_scalar_false_positive': first_pos, 'first_scalar_false_negative': first_neg,
              'K3_fixed_target_obstruction': rooted_example, 'seconds': time.monotonic() - start}
    if '--check-only' not in sys.argv:
        Path('evidence/S006/rooted_challenges.json').write_text(json.dumps(output, indent=2) + '\n', newline='\n')
    else:
        saved = json.loads(Path('evidence/S006/rooted_challenges.json').read_text())
        actual = json.loads(json.dumps(output))
        assert {k: v for k, v in saved.items() if k != 'seconds'} == {k: v for k, v in actual.items() if k != 'seconds'}
    print(json.dumps({'pure_tests': tests, 'buffer_tests': buffer_tests, 'scalar': scalar,
                      'seconds': output['seconds']}), flush=True)


if __name__ == '__main__':
    main()
