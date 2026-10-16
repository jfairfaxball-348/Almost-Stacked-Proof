import json,sys
from pathlib import Path
from s009_checks import run
r=run([sys.executable,'validation/validate_governance.py']);Path('evidence/S014/scope81_validation_checks.json').write_text(json.dumps([r],indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(r),flush=True)
if r['exit_code'] or r['resource_failure']:sys.exit(1)
