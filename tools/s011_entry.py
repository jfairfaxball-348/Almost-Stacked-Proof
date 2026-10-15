"""S011 entry authority, immutable history, invocation and read inventory."""
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
OUT = ROOT/'evidence/S011'
MAIN = '6f0d63b023daa5b3424b2ef166e25786f477332a'
HEAD = '243e563aa2b17042409833002b520165fdc3b69f'
PARENT = 'a1a38d79003a7081b8e14b59003d4d4641fb05fb'
TREE = '36f4bf59f91afcb2753fa58725d02c772b5c8522'
REPO = 'repos/jfairfaxball-348/Almost-Stacked-Proof'

def write(path, value):
    path=ROOT/path;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(value if isinstance(value,str) else json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')

def main():
    requests={'main_ref':f'{REPO}/git/ref/heads/main','main_commit':f'{REPO}/git/commits/{MAIN}',
        'head_commit':f'{REPO}/git/commits/{HEAD}','previous_pr':f'{REPO}/pulls/12',
        'previous_commits':f'{REPO}/pulls/12/commits','previous_comments':f'{REPO}/issues/12/comments?per_page=100',
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
    hashes=manifests();count=0
    import re
    for line in (ROOT/'evidence/S010/HASHES.md').read_text(encoding='utf-8').splitlines():
        m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
        if m:
            assert hashlib.sha256((ROOT/m[2]).read_bytes()).hexdigest()==m[1],m[2];count+=1
    hashes['S010']={'verified_entries':count,'frozen_index':None}
    # No writing until the authority and historical assertions above have passed.
    for key,value in results.items():write(f'evidence/S011/entry_{key}.json',value)
    for label in ('main','head'):
        jobs=[{'run_id':r['id'],'response':api(f"{REPO}/actions/runs/{r['id']}/jobs?per_page=100")} for r in results[f'{label}_runs']['body']['workflow_runs']]
        write(f'evidence/S011/entry_{label}_jobs.json',jobs)
    write('evidence/S011/entry_ref_reconciliation.json',refs);write('evidence/S011/inherited_hashes.json',hashes)
    thread=os.environ['CODEX_THREAD_ID'];sessiondir=Path(os.environ['USERPROFILE'])/'.codex/sessions/2026/10/15'
    files=list(sessiondir.glob(f'*{thread}.jsonl'));assert len(files)==1
    messages=[]
    for line in files[0].read_text(encoding='utf-8').splitlines():
        event=json.loads(line)
        if event.get('type')=='event_msg' and event.get('payload',{}).get('type')=='user_message':messages.append(event['payload']['message'])
        if event.get('type')=='response_item' and event.get('payload',{}).get('role')=='user':
            messages.append(''.join(c.get('text','') for c in event['payload'].get('content',[]) if c.get('type') in ('input_text','text')))
    invocation=next(m for m in messages if 'Resolve the universal critical ASH* bridge using exact critical insertion trees' in m)
    if not invocation.startswith('S011'):
        start=invocation.index('S011')
        invocation=invocation[start:]
    assert 'Prepare ONE COMPLETE' in invocation and 'No delegated agent work' in invocation
    write('sessions/S011/OWNER_INVOCATION.txt',invocation.rstrip()+'\n')
    write('sessions/S011/IMPLEMENTATION_REQUEST.txt',next(m for m in reversed(messages) if m.strip()=='Implement the proposed plan.').strip()+'\n')
    write('sessions/S011/AUTHORISED_PROMPT.md',(ROOT/'sessions/S010/FUTURE_S011.md').read_text(encoding='utf-8'))
    write('sessions/S011/INPUT.md','# S011 invocation provenance\n\nOWNER_INVOCATION.txt preserves the accessible full owner research invocation, normalized to UTF-8 LF, extracted from this conversation event. IMPLEMENTATION_REQUEST.txt records the subsequent implementation instruction. AUTHORISED_PROMPT.md preserves the older prospective S011 separately. No transport-byte identity or implicit permission for S012 is claimed.\n')
    inventory=[]
    folders=['authoritative','docs','research','catalogue','audit','campaigns','sessions/S010','evidence/S010','tools','validation','.github']
    for folder in folders:
        for p in sorted((ROOT/folder).rglob('*')):
            if not p.is_file() or '__pycache__' in str(p):continue
            raw=p.read_bytes();entry={'path':p.relative_to(ROOT).as_posix(),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}
            if p.suffix=='.xz':
                decoded=lzma.decompress(raw);obj=json.loads(decoded);entry.update(decoded_bytes=len(decoded),decoded_sha256=hashlib.sha256(decoded).hexdigest(),top_level_items=len(obj))
            elif p.suffix=='.json':json.loads(raw)
            elif p.suffix in ('.md','.py','.txt','.yml','.sha256','.cpp','.c'):raw.decode('utf-8')
            inventory.append(entry)
    write('evidence/S011/read_inventory.json',inventory)
    write('evidence/S011/environment.json',{'utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),
        'invocation_sha256':hashlib.sha256((ROOT/'sessions/S011/OWNER_INVOCATION.txt').read_bytes()).hexdigest(),
        'inventory_note':'Full byte/schema ingestion and provenance inventory; mathematical inspection is separately documented in AUDIT, not inferred from hashes.'})
    print(json.dumps({'main':MAIN,'tree':TREE,'manifests':hashes,'inventory_files':len(inventory),'invocation_archived':True}))

if __name__=='__main__':main()
