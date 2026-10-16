"""Preserve pre-closeout validator and bound decoded-hash memory; no assertion removal."""
import ast, hashlib
from pathlib import Path

p=Path('validation/validate_governance.py'); raw=p.read_bytes()
digest=hashlib.sha256(raw).hexdigest()
archive=Path(f'evidence/S014/frozen_validate_governance_{digest}.py.txt')
if not archive.exists():archive.write_bytes(raw)
text=raw.decode();lines=text.splitlines(keepends=True);offset=[0]
for line in lines:offset.append(offset[-1]+len(line))
changes=[]
for node in ast.walk(ast.parse(text)):
    if not isinstance(node,ast.Call) or not isinstance(node.func,ast.Attribute) or node.func.attr!='hexdigest':continue
    h=node.func.value
    if not isinstance(h,ast.Call) or ast.unparse(h.func)!='hashlib.sha256' or len(h.args)!=1:continue
    d=h.args[0]
    if not isinstance(d,ast.Call) or ast.unparse(d.func)!='lzma.decompress' or len(d.args)!=1:continue
    r=d.args[0]
    if not isinstance(r,ast.Call) or not isinstance(r.func,ast.Attribute) or r.func.attr!='read_bytes':continue
    changes.append((offset[node.lineno-1]+node.col_offset,offset[node.end_lineno-1]+node.end_col_offset,'sha256_lzma('+ast.get_source_segment(text,r.func.value)+')'))
for a,b,replacement in sorted(changes,reverse=True):text=text[:a]+replacement+text[b:]
text=text.replace('stream.read(1048576)','stream.read(65536)')
helper='''def sha256_lzma(path):
    import lzma
    h = hashlib.sha256()
    with lzma.open(path, 'rb') as stream:
        while chunk := stream.read(65536):
            h.update(chunk)
    return h.hexdigest()

'''
text=text.replace('def load(rel):',helper+'def load(rel):')
p.write_text(text,encoding='utf-8',newline='\n')
print(f'Archived {digest}; streamed {len(changes)} decoded hashes without changing comparisons.')
