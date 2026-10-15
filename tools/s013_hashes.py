"""Immutable canonical-byte S013 manifest; mutable mirrors pinned by commit."""
import hashlib
from pathlib import Path
def main():
    paths={p for folder in ['sessions/S013','evidence/S013'] for p in Path(folder).glob('*') if p.is_file() and p.name!='HASHES.md'}
    paths|=set(Path('tools').glob('s013*.py'))|set(Path('research').glob('S013*.md'))
    lines=['# S013 immutable canonical byte hashes','','No self-hash or copyrighted mirror. Current mutable mirrors are pinned by the authored commit; all historical manifests/bytes remain unchanged.','']
    for p in sorted(paths):
        b=p.read_bytes()
        if p.suffix!='.xz':assert b'\r\n' not in b,p
        lines.append(f'`{hashlib.sha256(b).hexdigest()}` `{p.as_posix()}`')
    Path('evidence/S013/HASHES.md').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n');print('S013 immutable entries',len(paths))
if __name__=='__main__':main()
