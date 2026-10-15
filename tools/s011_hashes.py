"""Immutable S011 canonical-byte manifest; mutable mirrors pinned by commit."""
import hashlib
from pathlib import Path

def main():
    paths={p for folder in ['sessions/S011','evidence/S011'] for p in Path(folder).glob('*') if p.is_file() and p.name!='HASHES.md'}
    paths|=set(Path('tools').glob('s011*.py'))|set(Path('research').glob('S011*.md'))
    lines=['# S011 immutable canonical byte hashes','','Actual invocation/plans/proofs/code/primary metadata/inputs/outputs/logs/failures. Current mutable mirrors are pinned by the authored commit and structurally validated; old manifests unchanged. No copyrighted PDFs or committed self-hash.','']
    for p in sorted(paths):
        raw=p.read_bytes()
        if p.suffix!='.xz':assert b'\r\n' not in raw,p
        lines.append(f'`{hashlib.sha256(raw).hexdigest()}` `{p.as_posix()}`')
    Path('evidence/S011/HASHES.md').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
    print('S011 immutable entries',len(paths))

if __name__=='__main__':main()
