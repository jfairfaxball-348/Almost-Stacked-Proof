"""Hash immutable S010 only; mutable mirrors pinned by authored commit, no self-hash."""
import hashlib
from pathlib import Path

def main():
    paths=[p for folder in ('sessions/S010','evidence/S010') for p in Path(folder).glob('*') if p.is_file() and p.name!='HASHES.md']
    paths+=list(Path('tools').glob('s010*.py'))+list(Path('research').glob('S010*.md'))
    lines=['# S010 immutable canonical byte hashes','','Invocation/plans/proofs/primary metadata/code/inputs/outputs/logs/failures. No copyrighted PDFs or committed self-hash. Current mutable mirrors structurally checked and pinned by atomic commit; historical manifests unchanged.','']
    for p in sorted(set(paths)):
        raw=p.read_bytes()
        if p.suffix!='.xz':assert b'\r\n' not in raw,p
        lines.append(f'`{hashlib.sha256(raw).hexdigest()}` `{p.as_posix()}`')
    Path('evidence/S010/HASHES.md').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
    print('S010 immutable hashes:',len(set(paths)))

if __name__=='__main__':main()
