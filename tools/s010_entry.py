"""Read-only remote authority and historical integrity; administrative only."""
import concurrent.futures
import hashlib
import json
import platform
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

OUT = Path('evidence/S010')
REPO = 'jfairfaxball-348/Almost-Stacked-Proof'
MAIN = 'a1a38d79003a7081b8e14b59003d4d4641fb05fb'
HEAD = '34d7e2e28925026db4dbd99e15f8007f4037ed68'
PARENT = '325f39d3448b6a0dfa092ea16196c56c3cc04673'
TREE = '9e80a3c538a233b3d320013a808635eff0edd8d6'

def write(name, value):
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8', newline='\n')

def api(path):
    p = subprocess.run(['gh', 'api', path], capture_output=True, text=True, encoding='utf-8')
    try: body = json.loads(p.stdout)
    except json.JSONDecodeError: body = p.stdout
    return {'exit_code': p.returncode, 'body': body, 'stderr': p.stderr}

def manifests():
    rows = {}
    for session in ('S003','S004','S005','S006','S007','S008','S009'):
        ip = {'S006':'evidence/S007/frozen_s006_index.json', 'S007':'evidence/S008/frozen_s007_index.json'}.get(session)
        index = json.loads(Path(ip).read_text(encoding='utf-8'))['files'] if ip else {}
        for info in index.values():
            assert hashlib.sha256(Path(info['snapshot']).read_bytes()).hexdigest() == info['sha256']
        count = 0
        for line in Path(f'evidence/{session}/HASHES.md').read_text(encoding='utf-8').splitlines():
            m = re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`.*', line.strip().lstrip('- '))
            if not m or m[2].startswith('scratch:'): continue
            path = Path(index[m[2]]['snapshot'] if m[2] in index else m[2])
            assert hashlib.sha256(path.read_bytes()).hexdigest() == m[1], (session,str(path))
            count += 1
        rows[session] = {'verified_entries':count,'frozen_index':ip}
    return rows

def main():
    root = f'repos/{REPO}'
    req = {'main_ref':f'{root}/git/ref/heads/main', 'main_commit':f'{root}/git/commits/{MAIN}',
           'head_commit':f'{root}/git/commits/{HEAD}', 'previous_pr':f'{root}/pulls/11',
           'previous_commits':f'{root}/pulls/11/commits', 'branches':f'{root}/branches?per_page=100',
           'prs':f'{root}/pulls?state=all&per_page=100', 'protection':f'{root}/branches/main/protection',
           'rulesets':f'{root}/rulesets?includes_parents=true', 'rules':f'{root}/rules/branches/main',
           'history':f'{root}/commits?sha=main&per_page=100', 'workflows':f'{root}/actions/workflows'}
    for label,sha in [('main',MAIN),('head',HEAD)]:
        for kind,suffix in [('runs',f'actions/runs?head_sha={sha}&per_page=100'),
                            ('checks',f'commits/{sha}/check-runs?per_page=100'),('status',f'commits/{sha}/status')]:
            req[f'{label}_{kind}'] = f'{root}/{suffix}'
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = dict(zip(req,pool.map(api,req.values())))
    for name,r in results.items(): write(f'entry_{name}.json',r)
    for label in ('main','head'):
        runs = results[f'{label}_runs']['body']['workflow_runs']
        write(f'entry_{label}_jobs.json',[{'run_id':r['id'],'response':api(f"{root}/actions/runs/{r['id']}/jobs?per_page=100")} for r in runs])
    assert results['main_ref']['body']['object']['sha'] == MAIN
    assert results['main_commit']['body']['tree']['sha'] == results['head_commit']['body']['tree']['sha'] == TREE
    assert [c['sha'] for c in results['main_commit']['body']['parents']] == [PARENT,HEAD]
    assert [c['sha'] for c in results['head_commit']['body']['parents']] == [PARENT]
    assert [c['sha'] for c in results['previous_commits']['body']] == [HEAD]
    assert results['previous_pr']['body']['merged'] and results['previous_pr']['body']['merge_commit_sha'] == MAIN
    assert not [p for p in results['prs']['body'] if p['state']=='open']
    refs = []
    for b in results['branches']['body']:
        sha = b['commit']['sha']
        p = subprocess.run(['git','merge-base','--is-ancestor',sha,MAIN],capture_output=True,text=True)
        refs.append({'name':b['name'],'sha':sha,'ancestor_of_main':p.returncode==0,'exit_code':p.returncode})
    write('entry_ref_reconciliation.json',refs)
    assert all(r['ancestor_of_main'] for r in refs)
    counts = manifests(); write('inherited_hashes.json',counts)
    write('environment.json', {'utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),
          'input_provenance':'Exact accessible user message extracted from the current local conversation event; UTF-8 LF, not transport-byte identity.',
          'input_sha256':hashlib.sha256(Path('sessions/S010/OWNER_INVOCATION.txt').read_bytes()).hexdigest(),
          'plan_sha256':hashlib.sha256(Path('sessions/S010/PLAN.md').read_bytes()).hexdigest()})
    print(json.dumps({'main':MAIN,'tree':TREE,'previous_pr':11,'all_remote_branches_ancestors':True,'manifests':counts}))

if __name__=='__main__': main()
