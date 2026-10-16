"""Integrity repair only: recheck both historically distinct checker versions."""
import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/split_source_recovery');B.mkdir(exist_ok=True);paths=[Path('tools/s014_split_verify.py'),Path('tools/s014_mass_split_verify.py'),Path('tools/s014_mass_split_replay.py'),Path('tools/s014_recover_split_source.py'),Path('sessions/S014/REPAIR_56_1.md'),Path('evidence/S014/tool_version_aliases.json'),Path('evidence/S014/split_preflight.json'),Path('evidence/S014/split_inputs.json'),Path('evidence/S014/split.json.xz'),Path('evidence/S014/split_verification.json')];before={}
for name in [f'P{i:02d}' for i in range(32)]:
    paths.extend([Path(f'evidence/S014/split_cegis/{name}/clause_verification.json'),Path(f'evidence/S014/split_cegis/{name}/base/{name}/clause_verification.json')])
for p in paths:
    if p.name.endswith('verification.json'):before[p.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}),indent=2)+'\n',encoding='utf-8',newline='\n');rows=[]
commands=[[sys.executable,'tools/s014_split_verify.py']]+[[sys.executable,'tools/s014_mass_split_verify.py',f'P{i:02d}'] for i in range(32)]
for cmd in commands:
    r=run(cmd);rows.append(r);(B/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(command=cmd,exit_code=r['exit_code'],seconds=r['seconds'],resource_failure=r['resource_failure'])),flush=True)
    if r['exit_code'] or r['resource_failure']:print(r['stderr']);sys.exit(1)
for p,h in before.items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
out=dict(original_CAM06_checker_sha256=hashlib.sha256(Path('tools/s014_split_verify.py').read_bytes()).hexdigest(),archived_CAM56_checker_sha256=hashlib.sha256(Path('tools/s014_mass_split_verify.py').read_bytes()).hexdigest(),replayed_checks=len(rows),all_output_bytes_unchanged=True,scope='Source-version recovery and same-scope replay only; no new mathematics')
(B/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
