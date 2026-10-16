"""Keep governance checks identical while hashing files in bounded memory."""
import ast,hashlib,os
from pathlib import Path
p=Path('validation/validate_governance.py');raw=p.read_bytes();src=raw.decode('utf-8')
if 'def sha256_file(' in src:print('Streaming hash helper already installed');raise SystemExit
h=hashlib.sha256(raw).hexdigest();archive=Path(f'evidence/S014/frozen_validate_governance_{h}.py.txt')
assert not archive.exists() or archive.read_bytes()==raw
if not archive.exists():archive.write_bytes(raw)
offsets=[0]
for line in raw.splitlines(keepends=True):offsets.append(offsets[-1]+len(line))
edits=[]
for node in ast.walk(ast.parse(src)):
    if not(isinstance(node,ast.Call) and not node.args and isinstance(node.func,ast.Attribute) and node.func.attr=='hexdigest'):continue
    call=node.func.value
    if not(isinstance(call,ast.Call) and len(call.args)==1 and isinstance(call.func,ast.Attribute) and isinstance(call.func.value,ast.Name) and call.func.value.id=='hashlib' and call.func.attr=='sha256'):continue
    arg=call.args[0]
    if not(isinstance(arg,ast.Call) and not arg.args and isinstance(arg.func,ast.Attribute) and arg.func.attr=='read_bytes'):continue
    expression=ast.get_source_segment(src,arg.func.value);a=offsets[node.lineno-1]+node.col_offset;b=offsets[node.end_lineno-1]+node.end_col_offset;edits.append((a,b,('sha256_file('+expression+')').encode('utf-8')))
assert len(edits)>30
for a,b,replacement in sorted(edits,reverse=True):raw=raw[:a]+replacement+raw[b:]
helper='''
# Each real file is independently hashed from bytes once per validation run.
# Repeated preflight references reuse only an unchanged in-process stat key.
_FILE_HASH_CACHE = {}
def sha256_file(path):
    path = Path(path)
    before = path.stat()
    key = (str(path), before.st_size, before.st_mtime_ns)
    if key in _FILE_HASH_CACHE:
        return _FILE_HASH_CACHE[key]
    h = hashlib.sha256()
    with path.open('rb') as stream:
        while chunk := stream.read(1048576):
            h.update(chunk)
    after = path.stat()
    assert (before.st_size, before.st_mtime_ns) == (after.st_size, after.st_mtime_ns), str(path)
    digest = h.hexdigest()
    _FILE_HASH_CACHE[key] = digest
    return digest
'''
anchor=b'ROOT = Path(__file__).resolve().parents[1]\n';assert raw.count(anchor)==1;raw=raw.replace(anchor,anchor+helper.encode('utf-8'));ast.parse(raw.decode('utf-8'));tmp=p.with_name(p.name+'.stream.tmp');tmp.write_bytes(raw);os.replace(tmp,p);print(f'Archived {h}; replaced {len(edits)} whole-file hash expressions with streaming hashes; all comparisons retained')
