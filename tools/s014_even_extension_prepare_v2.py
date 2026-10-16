import hashlib,json
from pathlib import Path
B=Path('evidence/S014/even_extension_v2');B.mkdir(exist_ok=True);(B/'inputs.json').write_bytes(Path('evidence/S014/even_extension/inputs.json').read_bytes())
for name in ['s014_even_extension','s014_even_extension_verify','s014_even_extension_run']:
    t=Path('tools/'+name+'.py').read_text(encoding='utf-8').replace("B=Path('evidence/S014/even_extension')","B=Path('evidence/S014/even_extension_v2')")
    if name=='s014_even_extension':t=t.replace('assert [u,v] in arcs','assert (u,v) in arcs')
    if name=='s014_even_extension_run':t=t.replace("['s014_even_extension','s014_even_extension_verify']","['s014_even_extension_v2','s014_even_extension_verify_v2']").replace("script.endswith('_verify')","script.endswith('_verify_v2')")
    Path('tools/'+name+'_v2.py').write_text(t,encoding='utf-8',newline='\n')
files=json.loads(Path('evidence/S014/even_extension/preflight.json').read_bytes())['files'].copy()
for p in [Path('sessions/S014/REPAIR_49_1.md'),B/'inputs.json',*Path('tools').glob('s014_even_extension*v2.py')]:files[p.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
(B/'preflight.json').write_text(json.dumps(dict(files=files),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM49 repair frozen; mathematical inputs unchanged')
