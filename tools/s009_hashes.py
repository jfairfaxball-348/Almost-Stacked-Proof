"""Canonical immutable S009 hashes; current mutable mirrors pinned by commit."""
import hashlib
from pathlib import Path

def main():
    paths=[p for folder in ('sessions/S009','evidence/S009') for p in Path(folder).glob('*') if p.is_file() and p.name!='HASHES.md']
    paths+=list(Path('tools').glob('s009*.py'))
    paths+=list(Path('research').glob('S009*.md'))
    lines=['# S009 immutable canonical byte hashes','','Plans, primary digest/entry/check logs, proofs, code, exact inputs/outputs and retained failed attempts. Current state/spec/catalogue/ledger/workflow/validator mirrors are validated structurally and pinned by the atomic commit. No manifest or committed self-hash.','']
    for p in sorted(set(paths)):
        raw=p.read_bytes()
        if p.suffix!='.xz':assert b'\r\n' not in raw,p
        lines.append(f'`{hashlib.sha256(raw).hexdigest()}` `{p.as_posix()}`')
    Path('evidence/S009/HASHES.md').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
    print('S009 immutable hashes:',len(set(paths)))

if __name__=='__main__':main()
