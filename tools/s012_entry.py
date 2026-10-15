"""S012 entry authority, immutable history, invocation and read inventory."""
import concurrent.futures
import hashlib
import json
import lzma
import os
import platform
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from s010_entry import api, manifests

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'evidence/S012'
MAIN = 'ca4aad7abf25d396eed16c6e3d89179ea6215b60'
HEAD = '42961f1099f9389c32c26ea6a2d1fdacce3646b0'
PARENT = '6f0d63b023daa5b3424b2ef166e25786f477332a'
TREE = 'a9cb765956c74eac52e03666ccb43a7684222f0d'
REPO = 'repos/jfairfaxball-348/Almost-Stacked-Proof'

def write(path, value):
    path=ROOT/path;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(value if isinstance(value,str) else json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')

def main():
    requests={'main_ref':f'{REPO}/git/ref/heads/main','main_commit':f'{REPO}/git/commits/{MAIN}',
        'head_commit':f'{REPO}/git/commits/{HEAD}','previous_pr':f'{REPO}/pulls/13',
        'previous_commits':f'{REPO}/pulls/13/commits','previous_comments':f'{REPO}/issues/13/comments?per_page=100',
        'branches':f'{REPO}/branches?per_page=100','prs':f'{REPO}/pulls?state=all&per_page=100',
        'history':f'{REPO}/commits?sha=main&per_page=100','protection':f'{REPO}/branches/main/protection',
        'rulesets':f'{REPO}/rulesets?includes_parents=true','rules':f'{REPO}/rules/branches/main','workflows':f'{REPO}/actions/workflows'}
    for label,sha in [('main',MAIN),('head',HEAD)]:
        for kind,suffix in [('runs',f'actions/runs?head_sha={sha}&per_page=100'),('checks',f'commits/{sha}/check-runs?per_page=100'),('status',f'commits/{sha}/status')]:
            requests[f'{label}_{kind}']=f'{REPO}/{suffix}'
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results=dict(zip(requests,pool.map(api,requests.values())))
    assert results['main_ref']['body']['object']['sha']==MAIN
    assert results['main_commit']['body']['tree']['sha']==results['head_commit']['body']['tree']['sha']==TREE
    assert [p['sha'] for p in results['main_commit']['body']['parents']]==[PARENT,HEAD]
    assert [p['sha'] for p in results['head_commit']['body']['parents']]==[PARENT]
    assert [c['sha'] for c in results['previous_commits']['body']]==[HEAD]
    pr=results['previous_pr']['body'];assert pr['merged'] and pr['merge_commit_sha']==MAIN and pr['auto_merge'] is None
    assert not [p for p in results['prs']['body'] if p['state']=='open']
    refs=[]
    for b in results['branches']['body']:
        code=subprocess.run(['git','merge-base','--is-ancestor',b['commit']['sha'],MAIN],capture_output=True).returncode
        refs.append({'name':b['name'],'sha':b['commit']['sha'],'ancestor_exit_code':code})
    assert all(r['ancestor_exit_code']==0 for r in refs)
    assert subprocess.check_output(['git','ls-remote','origin','refs/heads/main'],text=True).split()[0]==MAIN
    hashes=manifests()
    import re
    for session in ('S010','S011'):
        count=0
        for line in (ROOT/f'evidence/{session}/HASHES.md').read_text(encoding='utf-8').splitlines():
            m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
            if m:
                assert hashlib.sha256((ROOT/m[2]).read_bytes()).hexdigest()==m[1],m[2];count+=1
        hashes[session]={'verified_entries':count,'frozen_index':None}
    # No writing until the authority and historical assertions above have passed.
    for key,value in results.items():write(f'evidence/S012/entry_{key}.json',value)
    for label in ('main','head'):
        jobs=[{'run_id':r['id'],'response':api(f"{REPO}/actions/runs/{r['id']}/jobs?per_page=100")} for r in results[f'{label}_runs']['body']['workflow_runs']]
        write(f'evidence/S012/entry_{label}_jobs.json',jobs)
    write('evidence/S012/entry_ref_reconciliation.json',refs);write('evidence/S012/inherited_hashes.json',hashes)
    write('sessions/S012/OWNER_INVOCATION.txt','Run the next session\n')
    write('sessions/S012/AUTHORISED_PROMPT.md',(ROOT/'sessions/S011/FUTURE_S012.md').read_text(encoding='utf-8'))
    write('sessions/S012/INPUT.md','# S012 invocation provenance\n\nActual current owner message: `Run the next session`. OWNER_INVOCATION.txt stores that complete accessible message normalized to UTF-8 LF; no transport-byte hash claimed. Live state and S011 future handoff identify S012. AUTHORISED_PROMPT.md preserves that prospective scope separately. Stop before S013 and all deferred final stages. No delegation.\n')
    inventory=[]
    folders=['authoritative','docs','research','catalogue','audit','campaigns','sessions/S011','evidence/S011','tools','validation','.github']
    for folder in folders:
        for p in sorted((ROOT/folder).rglob('*')):
            if not p.is_file() or '__pycache__' in str(p):continue
            raw=p.read_bytes();entry={'path':p.relative_to(ROOT).as_posix(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
            if p.suffix=='.xz':
                decoded=lzma.decompress(raw);obj=json.loads(decoded);entry.update(decoded_bytes=len(decoded),decoded_sha256=hashlib.sha256(decoded).hexdigest(),top_level_items=len(obj))
            elif p.suffix=='.json':json.loads(raw)
            elif p.suffix in ('.md','.py','.txt','.yml','.sha256','.cpp','.c'):raw.decode('utf-8')
            inventory.append(entry)
    write('evidence/S012/read_inventory.json',inventory)
    write('evidence/S012/environment.json',{'utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),
        'invocation_sha256':hashlib.sha256((ROOT/'sessions/S012/OWNER_INVOCATION.txt').read_bytes()).hexdigest(),
        'inventory_note':'Full byte/schema ingestion and provenance inventory; mathematical inspection is separately documented in AUDIT, not inferred from hashes.'})
    print(json.dumps({'main':MAIN,'tree':TREE,'manifests':hashes,'inventory_files':len(inventory),'invocation_archived':True}))

if __name__=='__main__':main()
