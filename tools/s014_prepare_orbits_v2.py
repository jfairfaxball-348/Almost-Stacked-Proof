import hashlib,json
from pathlib import Path
B=Path('evidence/S014/cegis_orbits_v2');B.mkdir(exist_ok=True)
(B/'inputs.json').write_bytes(Path('evidence/S014/cegis_orbits/inputs.json').read_bytes())
for name in ['s014_cegis_orbits','s014_cegis_orbits_verify','s014_cegis_orbits_drup','s014_cegis_orbits_potential','s014_cegis_orbits_run']:
    t=Path('tools/'+name+'.py').read_text(encoding='utf-8').replace("B=Path('evidence/S014/cegis_orbits')","B=Path('evidence/S014/cegis_orbits_v2')").replace("checker.B=Path('evidence/S014/cegis_orbits')","checker.B=Path('evidence/S014/cegis_orbits_v2')")
    if name=='s014_cegis_orbits':t=t.replace('print(json.dumps(result),flush=True)',"print(json.dumps({**result,'case':case['id']}),flush=True)")
    if name=='s014_cegis_orbits_run':
        t=t.replace("['s014_cegis_orbits','s014_cegis_orbits_verify','s014_cegis_orbits_drup']","['s014_cegis_orbits_v2','s014_cegis_orbits_verify_v2','s014_cegis_orbits_drup_v2']").replace("script=='s014_cegis_orbits_verify'","script=='s014_cegis_orbits_verify_v2'").replace("'s014_cegis_orbits_potential.py'","'s014_cegis_orbits_potential_v2.py'")
        t=t.replace("['command','exit_code','seconds','resource_failure','stdout','stderr']","['command','exit_code','seconds','resource_failure']")
    Path('tools/'+name+'_v2.py').write_text(t,encoding='utf-8',newline='\n')
files=json.loads(Path('evidence/S014/cegis_orbits/preflight.json').read_bytes())['files'].copy()
for p in [Path('sessions/S014/REPAIR_38_1.md'),B/'inputs.json',*Path('tools').glob('*orbits*v2.py')]:files[p.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
(B/'preflight.json').write_text(json.dumps(dict(files=files),indent=2)+'\n',encoding='utf-8',newline='\n')
print('CAM38 repair frozen')
