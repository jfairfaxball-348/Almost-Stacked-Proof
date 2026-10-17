#!/usr/bin/env python3
"""S017 forbidden-placeholder and Palomar mechanical scan of formal/ (sources only).
Checks: every .lean file outside .lake starts with a `module` header (after comments),
has at most 10,000 physical lines; no `sorry`/`admit`/`native_decide`/`axiom`/`ofReduceBool`
outside Challenge.lean (Challenge may contain deliberate `sorry` only); Challenge <= 1,000
lines and 100 KiB; no compiled artefacts outside .lake."""
import pathlib, re, sys
root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else 'formal')
bad = []
files = [p for p in root.rglob('*') if p.is_file() and '.lake' not in p.parts]
for p in files:
    if p.suffix in {'.olean', '.ilean', '.a', '.bc', '.dll', '.dylib', '.o', '.obj', '.so', '.trace'}:
        bad.append(f'compiled artefact {p}')
for p in sorted(x for x in files if x.suffix == '.lean'):
    text = p.read_text(encoding='utf-8')
    lines = text.splitlines()
    if len(lines) > 10000:
        bad.append(f'{p}: {len(lines)} lines')
    code = re.sub(r'/-.*?-/', '', text, flags=re.S)
    code = re.sub(r'--[^\n]*', '', code)
    first = next((l for l in code.splitlines() if l.strip()), '')
    if p.name != 'lakefile.lean' and first.strip() != 'module':
        bad.append(f'{p}: no module header')
    toks = set(re.findall(r'\b(sorry|admit|native_decide|axiom|ofReduceBool|implemented_by|extern)\b', code))
    if p.name == 'Challenge.lean' and p.parent == root:
        toks -= {'sorry'}
        if len(lines) > 1000 or len(text.encode()) > 100 * 1024:
            bad.append('Challenge too large')
    if toks:
        bad.append(f'{p}: forbidden tokens {sorted(toks)}')
print('files', len(files), 'lean', sum(1 for x in files if x.suffix == '.lean'))
print('\n'.join(bad) if bad else 'SCAN_PASS')
sys.exit(1 if bad else 0)
