"""Exactly23 independently bounded source/box optimizers and proof checkers."""
import hashlib,json,sys
from pathlib import Path
from s009_checks import run
B=Path('evidence/S014')
def main():
    inp=json.loads((B/'ray_inputs.json').read_bytes());ids=sys.argv[1:] or [r['id'] for r in inp['cases']]
    pre=json.loads((B/'ray_preflight.json').read_bytes())
    for p,h in pre['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    for ident in ids:
        assert ident in {r['id'] for r in inp['cases']}
        rows=[];suffix='_replay' if '--check-only' in sys.argv else '_checks'
        for script in ['s014_rays','s014_rays_verify']:
            result=run([sys.executable,'tools/'+script+'.py',ident]);rows.append(result)
            (B/(ident+suffix+'.json')).write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='\n')
            print(json.dumps({k:result[k] for k in ['command','exit_code','seconds','peak_working_set_bytes','resource_failure','stdout','stderr']}),flush=True)
            if result['exit_code'] or result['resource_failure']:sys.exit(1)
if __name__=='__main__':main()
