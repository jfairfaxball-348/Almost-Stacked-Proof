"""Independent stage-specific caps; derived inputs are frozen before stageB."""
import hashlib,json,lzma,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014/regular')
def main():
    mode=sys.argv[1];pre=json.loads((B/('ray_preflight.json' if mode=='rays' else 'threshold_preflight.json')).read_bytes())
    for p,h in pre['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    inp=json.loads((B/('ray_inputs.json' if mode=='rays' else 'threshold_inputs.json')).read_bytes())
    if mode!='rays':
        for p,h in inp['source_certificate_hashes'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    for case in inp['cases']:
        name=case['id'] if mode=='rays' else case['graph']['graph']+'_'+case['goal']+'_threshold';args=[case['id']] if mode=='rays' else [case['graph']['graph'],case['goal']];scripts=['s014_regular_rays','s014_regular_rays_verify'] if mode=='rays' else ['s014_regular_threshold','s014_regular_threshold_verify'];rows=[]
        for script in scripts:
            row=run([sys.executable,'tools/'+script+'.py']+args);rows.append(row);(B/(name+'_checks.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:row[k] for k in ['command','exit_code','seconds','peak_working_set_bytes','resource_failure','stderr']})+' '+(row['stdout'].splitlines()[-1] if row['stdout'] else ''),flush=True)
            if row['exit_code'] or row['resource_failure']:sys.exit(1)
if __name__=='__main__':main()
