"""Hash immutable S008 material; current authority mirrors checked separately.

Historical mutable S007 bytes are covered through explicit frozen snapshots.
No manifest self-hash and no invented future commit identifier.
"""
import hashlib
from pathlib import Path

def main():
    paths=[p for folder in ('sessions/S008','evidence/S008') for p in Path(folder).glob('*') if p.is_file() and p.name!='HASHES.md']
    paths+=list(Path('tools').glob('s008*.py'))
    paths.append(Path('research/S008_HOSTILE_AUDIT_AND_UNIVERSAL_ROUTES.md'))
    lines=['# S008 immutable canonical byte hashes','','Plans, proof, code, inputs/outputs/checks and pinned historical snapshots. Current authority mirrors are validated structurally and pinned by the atomic commit; no manifest or future-commit self-hash.','']
    for p in sorted(set(paths)):
        if p.suffix!='.xz':assert b'\r\n' not in p.read_bytes(),p
        lines.append(f'`{hashlib.sha256(p.read_bytes()).hexdigest()}` `{p.as_posix()}`')
    Path('evidence/S008/HASHES.md').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
    print('S008 immutable hash entries:',len(set(paths)))

if __name__=='__main__':main()
