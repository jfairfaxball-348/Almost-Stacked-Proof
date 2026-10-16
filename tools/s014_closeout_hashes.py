"""Recursive immutable S014 inventory; cache is only an optimization before independent validation."""
import hashlib,json
from pathlib import Path

excluded={'HASHES.md','working_hashes.json','checkpoint_hashes.json','scope81_hash_cache.json','scope81_hash_progress.json'}
paths={p for folder in ['sessions/S014','evidence/S014'] for p in Path(folder).rglob('*') if p.is_file() and p.name not in excluded}
paths|={p for p in Path('tools').glob('s014*') if p.is_file()};paths|=set(Path('research').glob('S014*.md'))
cache=json.loads(Path('evidence/S014/scope81_hash_cache.json').read_bytes());rows=[];fresh=0
for p in sorted(paths,key=lambda p:p.as_posix()):
 key=p.as_posix();s=p.stat();old=cache.get(key)
 if old and old['stat']==[s.st_size,s.st_mtime_ns]:digest=old['sha256']
 else:
  h=hashlib.sha256()
  with p.open('rb') as f:
   while chunk:=f.read(65536):h.update(chunk)
  digest=h.hexdigest();fresh+=1
 rows.append(f'`{digest}` `{key}`')
text='# S014 immutable recursive SHA256 inventory\n\nScope: every S014 session/evidence file recursively, all tools/s014* files, all research/S014*.md. Excluded exact basenames: '+', '.join(sorted(excluded))+'. Excluded working/checkpoint hashes and resumable cache/progress are historical or mutable administrative metadata, not final assurance. Actual bytes are independently rehashed by governance; the cache is not trusted by validation. Final validation log is included once written, followed by read-only validation.\n\n'+'\n'.join(rows)+'\n'
Path('evidence/S014/HASHES.md').write_text(text,encoding='utf-8',newline='\n')
print(f'S014 immutable manifest: {len(rows)} files; {fresh} new hashes, all require independent governance rehash.')
