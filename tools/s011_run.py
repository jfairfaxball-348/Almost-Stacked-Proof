"""Bounded sequential campaign invocation after immutable input preflight."""
import hashlib,json,sys
from pathlib import Path
from s009_checks import run

def main():
    number=sys.argv[1]
    preflight=Path(f'evidence/S011/campaign{number}_preflight.json')
    if sys.argv[2]=='freeze':
        names=sys.argv[3:]
        files={p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in names}
        data={'execution':'NOT_YET_RUN','files':files,'limits':{'seconds_each':600,'states_per_layer':300000,'peak_bytes':2*1024**3}}
        assert not preflight.exists();preflight.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8',newline='\n')
        print('Frozen preflight',number);return
    data=json.loads(preflight.read_text(encoding='utf-8'))
    for p,h in data['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    for script in sys.argv[2:]:
        cmd=[sys.executable,script];row=run(cmd)
        name=Path(script).stem
        dest=Path(f'evidence/S011/{name}_log.json');assert not dest.exists()
        dest.write_text(json.dumps(row,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(json.dumps(row),flush=True)
        if row['exit_code'] or row['resource_failure']:sys.exit(1)

if __name__=='__main__':main()
