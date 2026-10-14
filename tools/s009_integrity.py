"""Entry reconciliation and immutable manifest validation; no research search."""
import concurrent.futures
import hashlib
import json
import platform
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

OUT = Path('evidence/S009')
REPO = 'jfairfaxball-348/Almost-Stacked-Proof'
MAIN = '325f39d3448b6a0dfa092ea16196c56c3cc04673'
HEAD = '8fe4ec3e09fcee3a80f6f0caa9eb97337f9ee061'

def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8', newline='\n')

def api(path):
    p = subprocess.run(['gh','api',path],capture_output=True,text=True,encoding='utf-8')
    try: body=json.loads(p.stdout)
    except json.JSONDecodeError: body=p.stdout
    return {'exit_code':p.returncode,'body':body,'stderr':p.stderr}

def manifests():
    results={}
    for session in ('S003','S004','S005','S006','S007','S008'):
        ip={'S006':'evidence/S007/frozen_s006_index.json','S007':'evidence/S008/frozen_s007_index.json'}.get(session)
        index=json.loads(Path(ip).read_text(encoding='utf-8'))['files'] if ip else {}
        count=0
        for line in Path(f'evidence/{session}/HASHES.md').read_text(encoding='utf-8').splitlines():
            m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`.*',line.strip().lstrip('- '))
            if not m or m[2].startswith('scratch:'): continue
            path=Path(index[m[2]]['snapshot'] if m[2] in index else m[2])
            assert hashlib.sha256(path.read_bytes()).hexdigest()==m[1],(session,str(path))
            count+=1
        results[session]={'verified_entries':count,'frozen_index':ip}
    return results

def main():
    root=f'repos/{REPO}'
    req={'main_ref':f'{root}/git/ref/heads/main','main_commit':f'{root}/git/commits/{MAIN}',
         'previous_pr':f'{root}/pulls/10','previous_commits':f'{root}/pulls/10/commits',
         'branches':f'{root}/branches?per_page=100','prs':f'{root}/pulls?state=all&per_page=100',
         'protection':f'{root}/branches/main/protection','rulesets':f'{root}/rulesets',
         'history':f'{root}/commits?sha=main&per_page=30'}
    for label,sha in [('main',MAIN),('head',HEAD)]:
        for kind,suffix in [('runs',f'actions/runs?head_sha={sha}&per_page=100'),('checks',f'commits/{sha}/check-runs?per_page=100'),('status',f'commits/{sha}/status')]:
            req[f'{label}_{kind}']=f'{root}/{suffix}'
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results=dict(zip(req,pool.map(api,req.values())))
    for name,r in results.items(): write(f'entry_{name}.json',r)
    for label in ('main','head'):
        runs=results[f'{label}_runs']['body']['workflow_runs']
        jobs=[{'run_id':r['id'],'response':api(f"{root}/actions/runs/{r['id']}/jobs?per_page=100")} for r in runs]
        write(f'entry_{label}_jobs.json',jobs)
    assert results['main_ref']['body']['object']['sha']==MAIN
    pr=results['previous_pr']['body']
    assert pr['merged'] and pr['head']['sha']==HEAD and pr['merge_commit_sha']==MAIN
    assert [c['sha'] for c in results['previous_commits']['body']]==[HEAD]
    assert [c['sha'] for c in results['main_commit']['body']['parents']]==['3f2aba35da0ac48b7d93ef0df7d84af5ef2475b4',HEAD]
    counts=manifests();write('inherited_hashes.json',counts)
    write('environment.json',{'utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),
        'research_execution':'local Windows','symmetry':'none','input_note':'INPUT.md preserves accessible message text as UTF-8 LF; no claim about raw chat transport bytes',
        'input_sha256':hashlib.sha256(Path('sessions/S009/INPUT.md').read_bytes()).hexdigest(),
        'plan_sha256':hashlib.sha256(Path('sessions/S009/PLAN.md').read_bytes()).hexdigest()})
    print(json.dumps({'entry_reconciled':True,'main':MAIN,'previous_pr':pr['number'],'manifests':counts}))

if __name__=='__main__':main()
