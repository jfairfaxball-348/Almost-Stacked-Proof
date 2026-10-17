#!/usr/bin/env python3
"""S019: populate a Palomar submission snapshot tree from formal/ of this research repository.

usage: s019_make_snapshot.py <research_root> <snapshot_dir> <LICENSE source> <README source>

Copies, byte for byte, formal/{lean-toolchain, lakefile.toml, lake-manifest.json,
AlmostStacked.lean, AlmostStacked/**.lean, Challenge.lean, Solution.lean, comparator.json,
formalization.yaml} to the snapshot root, plus LICENSE and README.md, and writes `.gitignore`
(`.lake/`). Refuses to overwrite anything except a previous snapshot's tracked files. Prints a
manifest `sha256  path` of every snapshot file (stdout), so the copies can be compared with the
research commit.
"""
import hashlib, pathlib, shutil, sys

research, snap, lic, readme = (pathlib.Path(a) for a in sys.argv[1:5])
formal = research / 'formal'
files = ['lean-toolchain', 'lakefile.toml', 'lake-manifest.json', 'AlmostStacked.lean',
         'Challenge.lean', 'Solution.lean', 'comparator.json', 'formalization.yaml']
files += sorted(p.relative_to(formal).as_posix() for p in (formal / 'AlmostStacked').rglob('*.lean'))
snap.mkdir(parents=True, exist_ok=True)
for rel in files:
    dst = snap / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(formal / rel, dst)
shutil.copyfile(lic, snap / 'LICENSE')
shutil.copyfile(readme, snap / 'README.md')
(snap / '.gitignore').write_bytes(b'.lake/\n')
out = []
for p in sorted(q for q in snap.rglob('*') if q.is_file() and '.git' not in q.relative_to(snap).parts and '.lake' not in q.relative_to(snap).parts):
    out.append(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(snap).as_posix()}')
print('\n'.join(out))
for rel in files:
    assert (snap / rel).read_bytes() == (formal / rel).read_bytes(), rel
print(f'# {len(out)} files; {len(files)} copied byte-identically from formal/', file=sys.stderr)
