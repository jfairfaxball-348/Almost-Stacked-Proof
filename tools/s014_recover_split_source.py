"""Read original source as data; exact original digest required before restore."""
import hashlib,json,re
from pathlib import Path
B=Path('evidence/S014');old=Path('tools/s014_split_verify.py');archive=Path('tools/s014_mass_split_verify.py');current=old.read_bytes();archive.write_bytes(current);expected=json.loads((B/'split_preflight.json').read_bytes())['files'][old.as_posix()];rollout=Path('C:/Users/johnf/.codex/sessions/2026/10/15/rollout-2026-10-15T09-58-39-01a13ec8-f48b-7b41-af3f-5298d8c04ce5.jsonl');record=json.loads(next(l for i,l in enumerate(rollout.open(encoding='utf-8'),1) if i==1209));text=record['payload']['input'];candidates=[]
for quoted in re.findall(r'tools\.apply_patch\(("(?:[^"\\]|\\.)*")\)',text):
    patch=json.loads(quoted);lines=patch.splitlines();collect=False;body=[]
    for line in lines:
        if line.startswith('*** Add File: '):
            if collect:break
            collect=line.endswith('/tools/s014_split_verify.py');continue
        if collect:
            if line.startswith('*** '):break
            assert line.startswith('+');body.append(line[1:])
    if collect:candidates.append(('\n'.join(body)+'\n').encode('utf-8'))
assert len(candidates)==1;candidate=candidates[0];(B/'recovered_split_initial.py.txt').write_bytes(candidate);digest=hashlib.sha256(candidate).hexdigest();print(json.dumps(dict(expected=expected,initial_patch_hash=digest,current_mass_split_hash=hashlib.sha256(current).hexdigest(),initial_bytes=len(candidate))))
if digest!=expected:
    # Original file writer inserts one blank line between top-level definitions.
    options=[candidate,candidate.replace(b"B=Path('evidence/S014')\ndef read",b"B=Path('evidence/S014')\n\ndef read").replace(b'else p.read_bytes())\ndef main',b'else p.read_bytes())\n\ndef main')]
    matches=[v for v in options if hashlib.sha256(v).hexdigest()==expected]
    assert len(matches)==1,'Exact original digest not recovered; old filename not restored'
    candidate=matches[0]
assert hashlib.sha256(candidate).hexdigest()==expected;old.write_bytes(candidate);aliases=[dict(path=old.as_posix(),sha256=hashlib.sha256(current).hexdigest(),archive=archive.as_posix(),reason='Exact CAM56 source version archived after restoring frozen CAM06 source')];(B/'tool_version_aliases.json').write_text(json.dumps(dict(aliases=aliases,recovery=dict(original_sha256=expected,original_bytes=len(candidate),source_rollout_id='01a13ec8-f48b-7b41-af3f-5298d8c04ce5',source_ordinal=1208,source_timestamp=record['timestamp'])),indent=2)+'\n',encoding='utf-8',newline='\n');print('Original CAM06 checker restored to exact frozen digest; CAM56 bytes separately preserved')
