import hashlib,json,re,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/fano_AS');old=Path('tools/s014_c065_produce.py');new=Path('tools/s014_c065_produce_v2.py');source=old.read_text(encoding='utf-8');fixed=re.sub(r'\b16\b','n',source);assert fixed!=source
if new.exists():assert new.read_text(encoding='utf-8')==fixed
else:new.write_text(fixed,encoding='utf-8',newline='\n')
rows0=json.loads((B/'checks.json').read_bytes());assert len(rows0)==1 and rows0[0]['exit_code']==1 and 'AssertionError' in rows0[0]['stderr'];assert not (B/'nodes.bin.xz').exists() and not (B/'result.json').exists();files=[new,old,Path('tools/s014_c065_repair.py'),Path('tools/s014_c065_verify.py'),Path('sessions/S014/REPAIR_65_1.md'),B/'inputs.json',B/'preflight.json',B/'checks.json'];(B/'repair_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');rows=[]
for script in [new,Path('tools/s014_c065_verify.py')]:
    if script.name.endswith('_verify.py'):
        files=[B/'nodes.bin.xz',B/'choices.json',B/'result.json'];(B/'derived_preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n')
    r=run([sys.executable,script.as_posix()]);rows.append(r);(B/'repair_checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:r[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
    if r['exit_code'] or r['resource_failure']:sys.exit(1)
