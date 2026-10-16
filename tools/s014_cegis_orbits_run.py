import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/cegis_orbits')
def main():
    for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    for case in json.loads((B/'inputs.json').read_bytes())['cases']:
        D=B/case['id'];D.mkdir(exist_ok=True);rows=[]
        for script in ['s014_cegis_orbits','s014_cegis_orbits_verify','s014_cegis_orbits_drup']:
            if script=='s014_cegis_orbits_verify':
                files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in D.rglob('*') if p.is_file() and p.name!='checks.json'}
                (D/'derived_preflight.json').write_text(json.dumps(dict(files=files),indent=2)+'\n',encoding='utf-8',newline='\n')
            row=run([sys.executable,'tools/'+script+'.py',case['id']]);rows.append(row);(D/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','resource_failure','stdout','stderr']}),flush=True)
            if row['exit_code'] or row['resource_failure']:sys.exit(1)
        if json.loads((D/'result.json').read_bytes())['status']=='POTENTIAL_ACTUAL_COUNTEREXAMPLE':
            row=run([sys.executable,'tools/s014_cegis_orbits_potential.py',case['id']]);rows.append(row);(D/'checks.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(row),flush=True);break
if __name__=='__main__':main()
