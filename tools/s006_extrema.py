"""Cold fixed-support/residue challenge on inherited complete critical sets."""
import collections
import hashlib
import json
import lzma
import struct
import sys
import time
from pathlib import Path


def main():
    start = time.monotonic()
    out = []
    examples = []
    for path in sorted(Path('evidence/S005').glob('A[2-6]_*.summary.json')):
        m = json.loads(path.read_text())
        if not m['threshold']:
            continue
        raw = lzma.decompress(Path(str(path).replace('.summary.json', '.bin.xz')).read_bytes())
        assert hashlib.sha256(raw).hexdigest() == m['certificate_sha256']
        off = 0
        critical = None
        while off < len(raw):
            total, count = struct.unpack_from('<IQ', raw, off)
            off += 12
            if total == m['threshold'] - 1:
                critical = [tuple((int.from_bytes(raw[k:k+16], 'little') >> (8*v)) & 255
                                  for v in range(m['n'])) for k in range(off, off + 16*count, 16)]
            off += 16 * count
        assert critical
        classes = collections.defaultdict(list)
        for c in critical:
            classes[tuple(0 if x == 0 else 1 + (x - 1) % 3 for x in c)].append(c)
        q = lambda c: sum(x*x for x in c)
        global_q = max(map(q, critical))
        assert all(sum(x > 1 for x in c) <= 1 for c in critical if q(c) == global_q)
        failed = 0
        for key, states in classes.items():
            class_q = max(map(q, states))
            bad = [c for c in states if q(c) == class_q and sum(x > 1 for x in c) > 1]
            failed += len(bad)
            if bad:
                examples.append({'graph': m['graph'], 'n': m['n'], 'edges': m['edges'],
                                 'mode': m['mode'], 'critical_mass': m['threshold'] - 1,
                                 'configuration': min(bad), 'support_residue': key,
                                 'class_Qmax': class_q, 'global_Qmax': global_q,
                                 'class_has_AS': any(sum(x > 1 for x in c) <= 1 for c in states),
                                 'class_states': sorted(states),
                                 'global_AS_maximizer': min(c for c in critical if q(c) == global_q)})
        out.append({'graph': m['graph'], 'mode': m['mode'], 'critical_mass': m['threshold'] - 1,
                    'critical_states': len(critical), 'classes': len(classes),
                    'nonAS_class_Qmaximizers': failed, 'global_Qmax_all_AS': True})
    examples.sort(key=lambda r: (r['n'], r['critical_mass'], r['graph'], r['mode'], r['configuration']))
    result = {'cases': out, 'failed_nonAS_class_maxima': sum(r['nonAS_class_Qmaximizers'] for r in out),
              'first_failure': examples[0], 'seconds': time.monotonic() - start,
              'scope': 'inherited exact n=2..6 critical layers only; no new threshold search'}
    if '--check-only' not in sys.argv:
        Path('evidence/S006/extremal_challenge.json').write_text(json.dumps(result, indent=2) + '\n', newline='\n')
    else:
        saved = json.loads(Path('evidence/S006/extremal_challenge.json').read_text())
        actual = json.loads(json.dumps(result))
        assert {k: v for k, v in saved.items() if k != 'seconds'} == {k: v for k, v in actual.items() if k != 'seconds'}
    print(json.dumps({'cases': len(out), 'failed_nonAS_class_maxima': result['failed_nonAS_class_maxima'],
                      'first_failure': result['first_failure'], 'seconds': result['seconds']}))


if __name__ == '__main__':
    main()
