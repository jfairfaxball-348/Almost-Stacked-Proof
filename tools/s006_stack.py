"""Rooted stack buffer optimizer: concatenate exact clearing forests."""
import json
import lzma
from pathlib import Path


def main():
    clear = json.loads(lzma.decompress(Path('evidence/S006/grammar_certificates.json.xz').read_bytes()))['buffer']
    cells = clear['cells']
    index = {(c['vertex'], tuple(c['off']), c['kind']): i for i, c in enumerate(cells)}
    values = [c['value'] for c in cells]
    nodes = []
    roots = []
    for i, c in enumerate(cells):
        if c['value'] is None:
            roots.append(None)
        else:
            roots.append(len(nodes))
            nodes.append({'cell': i, 'clear_node': c['witness'], 'children': None})
    rules = []
    for i, a in enumerate(cells):
        for j, b in enumerate(cells):
            if a['vertex'] != b['vertex']:
                continue
            d = tuple(x + y for x, y in zip(a['off'], b['off']))
            if any(x > y for x, y in zip(d, clear['box'])):
                continue
            kind = 3 if a['kind'] == b['kind'] == 3 else (a['kind'] % 3 + b['kind'] % 3) % 3
            rules.append((index[a['vertex'], d, kind], i, j))
    for rounds in range(len(cells) + 1):
        changed = False
        for p, a, b in rules:
            if values[a] is None or values[b] is None:
                continue
            value = values[a] + values[b]
            if values[p] is None or values[p] > value:
                values[p] = value
                roots[p] = len(nodes)
                nodes.append({'cell': p, 'clear_node': None, 'children': [roots[a], roots[b]]})
                changed = True
        if not changed:
            break
    else:
        raise AssertionError('forest height bound')
    out = {'clear_certificate': 'grammar_certificates.json.xz:buffer',
           'values': values, 'roots': roots, 'nodes': nodes, 'rounds': rounds + 1}
    Path('evidence/S006/stack_buffer_certificate.json').write_text(json.dumps(out, indent=2) + '\n', newline='\n')
    print(json.dumps({'cells': len(cells), 'finite': sum(x is not None for x in values),
                      'rounds': rounds + 1, 'forest_nodes': len(nodes)}))


if __name__ == '__main__':
    main()
