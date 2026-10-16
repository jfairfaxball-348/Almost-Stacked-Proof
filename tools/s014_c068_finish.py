import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/mass11_cegis');V=Path('evidence/S014/mass11_lrat');assert not (B/'summary_preflight.json').exists();files=[B/'inputs.json',B/'inventory_verification.json',Path('tools/s014_c068_summary.py'),Path('tools/s014_c068_finish.py')]
for case in json.loads((B/'inputs.json').read_bytes())['cases']:
    files.extend([B/case['id']/p for p in ['result.json','clause_verification.json','derived_preflight.json','checks.json']]);files.extend([V/case['id']/p for p in ['verification.json','derived_preflight.json']])
(B/'summary_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');r=run([sys.executable,'tools/s014_c068_summary.py']);(B/'summary_checks.json').write_text(json.dumps([r],indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(r))
