"""Prior preflight and supervised campaign runner; no implicit campaign scope."""
import hashlib,json,sys
from pathlib import Path
from s009_checks import run

def main():
    campaign=sys.argv[1];names=sys.argv[2:]
    pre=Path(f'evidence/S013/{campaign}_preflight.json')
    if not pre.exists():
        inputs=['sessions/S013/PLAN.md',f'sessions/S013/PLAN_AMENDMENT_{campaign}.md','evidence/S013/environment.json']+[f'tools/{n}.py' for n in names]
        if campaign=='1':inputs+=['evidence/S003/T2b_analysis.json','evidence/S003/A3_n8_analysis.json.xz']
        elif campaign=='2':inputs+=['evidence/S013/precision_inputs.json']
        elif campaign=='3':inputs+=['evidence/S013/precision_inputs.json','evidence/S013/precision_tables.json.xz','evidence/S013/precision.json']
        elif campaign=='4':inputs+=['evidence/S013/precision_inputs.json','evidence/S013/precision_tables.json.xz','evidence/S013/precision.json']
        elif campaign=='5':inputs+=['evidence/S013/precision_inputs.json','evidence/S013/precision_tables.json.xz','evidence/S013/precision.json','evidence/S013/archive_inputs.json']
        elif campaign=='6':inputs+=['evidence/S013/precision_inputs.json','evidence/S013/precision_tables.json.xz','evidence/S013/precision.json']
        pre.write_text(json.dumps({'files':{p:hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in inputs}},indent=2)+'\n',encoding='utf-8',newline='\n')
    else:
        for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    for n in names:
        row=run([sys.executable,f'tools/{n}.py'])
        Path(f'evidence/S013/{n}_log.json').write_text(json.dumps(row,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(json.dumps(row),flush=True)
        assert row['exit_code']==0 and row['resource_failure'] is None

if __name__=='__main__':main()
