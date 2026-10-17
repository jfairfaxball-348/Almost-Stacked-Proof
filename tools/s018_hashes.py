#!/usr/bin/env python3
"""S018: write evidence/S018/HASHES.md over sessions/S018, evidence/S018, tools/s018*, the S018-changed
formal files (superseding S017 hashes recorded in STATE.json s018) and the new formal files."""
import hashlib, json, pathlib
root = pathlib.Path(__file__).resolve().parents[1]
st = json.loads((root / 'authoritative/STATE.json').read_text(encoding='utf-8'))['s018']
paths = {p.relative_to(root).as_posix() for d in ['sessions/S018', 'evidence/S018'] for p in (root / d).rglob('*') if p.is_file() and p.name != 'HASHES.md'}
paths |= {p.relative_to(root).as_posix() for p in (root / 'tools').glob('s018*') if p.is_file()}
paths |= set(st['superseded_s017_hashes']) | set(st['new_formal_files'])
lines = ['# S018 immutable hashes', '', 'Superseded S017 bytes (recorded, not rewritten): ' + ', '.join(f'{k} was {v}' for k, v in sorted(st['superseded_s017_hashes'].items())), '']
for p in sorted(paths):
    lines.append(f'`{hashlib.sha256((root / p).read_bytes()).hexdigest()}`  `{p}`')
(root / 'evidence/S018/HASHES.md').write_bytes(('\n'.join(lines) + '\n').encode('utf-8'))
print(len(paths))
