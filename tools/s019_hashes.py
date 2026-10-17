#!/usr/bin/env python3
"""S019: write evidence/S019/HASHES.md over sessions/S019, evidence/S019, tools/s019*, the S019-changed
formal files (superseding S017 hashes recorded in STATE.json s019) and the new formal files."""
import hashlib, json, pathlib
root = pathlib.Path(__file__).resolve().parents[1]
st = json.loads((root / 'authoritative/STATE.json').read_text(encoding='utf-8'))['s019']
paths = {p.relative_to(root).as_posix() for d in ['sessions/S019', 'evidence/S019'] for p in (root / d).rglob('*') if p.is_file() and p.name != 'HASHES.md'}
paths |= {p.relative_to(root).as_posix() for p in (root / 'tools').glob('s019*') if p.is_file()}
paths |= set(st['superseded_s017_hashes']) | set(st['superseded_s018_hashes'])
lines = ['# S019 immutable hashes', '', 'Superseded S017/S018 bytes are recorded in authoritative/STATE.json s019 (superseded_s017_hashes, superseded_s018_hashes), not rewritten.', '']
for p in sorted(paths):
    lines.append(f'`{hashlib.sha256((root / p).read_bytes()).hexdigest()}`  `{p}`')
(root / 'evidence/S019/HASHES.md').write_bytes(('\n'.join(lines) + '\n').encode('utf-8'))
print(len(paths))
