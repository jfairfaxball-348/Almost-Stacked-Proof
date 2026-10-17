#!/usr/bin/env python3
"""S019: local Palomar mechanical pre-checks of a submission snapshot (NOT a Palomar verification).

usage: python -I s019_palomar_mech.py <PalomarSubmission checkout> <snapshot checkout>

Calls Palomar's own functions where they are plain checks (formalization.yaml loader,
Lean-source rules, comparator config loader, licence-file locator, preservable-checkout check,
tree size, toolchain support) and adds the remaining policy checks written from the policy text
(compiled-artefact suffixes, Challenge size, Mathlib toolchain equality, taxonomies, licence
SPDX). Prints one line per check and MECH_PASS / MECH_FAIL.
"""
import json, pathlib, sys, traceback
ps, snap = pathlib.Path(sys.argv[1]).resolve(), pathlib.Path(sys.argv[2]).resolve()
sys.path.insert(0, str(ps))
from scripts import submission_contract as sc, source_requirements as sr, verify_submission as vs  # noqa: E402

results = []
def check(name, fn):
    try:
        detail = fn()
        results.append((name, True, detail))
    except Exception as e:  # report every failure, keep going
        results.append((name, False, f'{type(e).__name__}: {e}'))

def no_compiled():
    bad = [p.relative_to(snap).as_posix() for p in snap.rglob('*')
           if p.is_file() and '.git' not in p.relative_to(snap).parts and '.lake' not in p.relative_to(snap).parts
           and (p.suffix in vs.COMPILED_ARTIFACT_SUFFIXES or p.name.endswith(vs.COMPILED_ARTIFACT_NAME_SUFFIXES))]
    assert not bad, bad
    return 'none'
def size():
    n = vs.tree_size(snap); assert n <= vs.MAX_SOURCE_BYTES, n
    return f'{n} bytes (cap {vs.MAX_SOURCE_BYTES})'
def lean_sources():
    summary, issues = sr.inspect_lean_sources(snap)
    assert not issues, [str(i) for i in issues]
    return json.dumps(summary)[:300]
def metadata():
    d = sc.load_formalization_metadata(snap / 'formalization.yaml')
    return f"name={d['project']['name'][:60]!r} license={d['project']['license']}"
def licence():
    f = vs.repository_license_file(snap)
    text = f.read_text(encoding='utf-8')
    assert 'Apache License' in text and 'Version 2.0, January 2004' in text
    d = sc.load_formalization_metadata(snap / 'formalization.yaml')
    assert d['project']['license'] == 'Apache-2.0'
    return f'{f.name} Apache-2.0'
def comparator():
    c = vs.load_comparator_config(snap / 'comparator.json')
    assert set(c['permitted_axioms']) <= vs.STANDARD_AXIOMS
    return f"{len(c['theorem_names'])} theorems, axioms {sorted(c['permitted_axioms'])}"
def challenge():
    b = (snap / 'Challenge.lean').read_bytes()
    lines = len(b.decode('utf-8').splitlines())
    assert len(b) <= vs.MAX_CHALLENGE_BYTES and lines <= vs.MAX_CHALLENGE_LINES
    imports = [l for l in b.decode('utf-8').splitlines() if 'import ' in l and not l.lstrip().startswith('--')]
    assert all(l.split()[-1].startswith('Mathlib.') for l in imports), imports
    return f'{len(b)} bytes, {lines} lines, imports Mathlib only'
def toolchain():
    tc = (snap / 'lean-toolchain').read_text().strip()
    vs.supported_toolchain(tc)
    man = json.loads((snap / 'lake-manifest.json').read_text())
    ml = [p for p in man['packages'] if p['name'] == 'mathlib']
    assert len(ml) == 1 and ml[0]['rev'] == '56a005855ea17e0b0958f73ec801ae140b0a1679'
    assert (snap / 'lakefile.toml').is_file() and not (snap / 'lakefile.lean').exists()
    return f'{tc}; mathlib {ml[0]["rev"]}; single TOML lakefile; committed manifest'
def preservable():
    vs.validate_preservable_git_checkout(snap, label='snapshot')
    return 'no submodules / LFS'
def symlinks():
    bad = [p for p in snap.rglob('*') if p.is_symlink()]
    assert not bad, bad
    return 'none'

for name, fn in [('tree_size', size), ('compiled_artifacts', no_compiled), ('symlinks', symlinks),
                 ('preservable_checkout', preservable), ('lean_sources', lean_sources),
                 ('formalization_yaml', metadata), ('licence', licence), ('comparator_json', comparator),
                 ('challenge', challenge), ('toolchain', toolchain)]:
    check(name, fn)
for name, ok, detail in results:
    print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
print('MECH_PASS' if all(ok for _, ok, _ in results) else 'MECH_FAIL')
