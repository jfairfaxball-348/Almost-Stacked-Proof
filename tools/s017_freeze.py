#!/usr/bin/env python3
"""S017: write formal/FROZEN_MODULES.md for the given green modules.

usage: s017_freeze.py formal AXIOMS_LOG DATE SESSION MODULE...
Each module path is hashed (sha256 of the source bytes).  AXIOMS_LOG is the output of the
`#print axioms` run (tools/s017_print_axioms.py); it must show only the standard axioms
propext, Classical.choice, Quot.sound for every printed declaration."""
import hashlib, pathlib, re, sys

root = pathlib.Path(sys.argv[1])
log = pathlib.Path(sys.argv[2]).read_text(encoding='utf-8')
date, session, mods = sys.argv[3], sys.argv[4], sys.argv[5:]
allowed = {'propext', 'Classical.choice', 'Quot.sound'}
for m in re.finditer(r"'([^']+)' depends on axioms: \[([^\]]*)\]", log):
    axs = {a.strip() for a in m.group(2).split(',') if a.strip()}
    assert axs <= allowed, (m.group(1), axs)
assert 'sorryAx' not in log and 'ofReduceBool' not in log
toolchain = (root / 'lean-toolchain').read_text().strip()
rev = re.search(r'rev = "([0-9a-f]{40})"', (root / 'lakefile.toml').read_text()).group(1)
rows = []
for mod in mods:
    p = root / (mod.replace('.', '/') + '.lean')
    rows.append(f'| `{mod}` | `{hashlib.sha256(p.read_bytes()).hexdigest()}` | {toolchain} | `{rev}` | propext, Classical.choice, Quot.sound (subset) | {date} | {session} |')
text = f"""# Frozen Lean modules

A frozen module compiled with no `sorry`/`admit`, and every declaration printed by
`tools/s017_print_axioms.py` depends only on standard axioms (a subset of propext,
Classical.choice, Quot.sound). A frozen module is not edited: a change needs a new module or an
explicit un-freeze entry below. `validation/validate_governance.py` re-hashes every row.

| module | source sha256 | toolchain | Mathlib commit | axioms printed | date | session |
|---|---|---|---|---|---|---|
""" + '\n'.join(rows) + '\n\n## Un-freeze entries\n\nNone.\n'
(root / 'FROZEN_MODULES.md').write_text(text, encoding='utf-8', newline='\n')
print(len(rows), 'modules frozen')
