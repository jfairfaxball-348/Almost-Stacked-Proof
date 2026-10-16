"""S014 fresh authority, exact owner steering and historical integrity."""
import concurrent.futures,hashlib,json,lzma,platform,re,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
from s010_entry import api,manifests
R=Path(__file__).resolve().parents[1]
REPO='repos/jfairfaxball-348/Almost-Stacked-Proof'
MAIN='8ea5db207a91ca917c3b94bc98b54ac65406e7a5'
HEAD='ccfbdd7194c6571b5b9cbd780941777494f03073'
PARENT='1e28259f6e35849723bbe5e5fd545630498d45a9'
TREE='b9811bdbf667c9e93df9a5001ebf30a036adb73b'
OWNER='What stopped you continuing with the jobs in s014 here? Lets keep going\n'
STEER='I more meant why did you close s013 and not keep going\n'
def write(p,x):
    p=R/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(x if isinstance(x,str) else json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def main():
    req={'main_ref':f'{REPO}/git/ref/heads/main','main_commit':f'{REPO}/git/commits/{MAIN}','head_commit':f'{REPO}/git/commits/{HEAD}','previous_pr':f'{REPO}/pulls/16','previous_commits':f'{REPO}/pulls/16/commits','previous_comments':f'{REPO}/issues/16/comments?per_page=100','branches':f'{REPO}/branches?per_page=100','prs':f'{REPO}/pulls?state=all&per_page=100','history':f'{REPO}/commits?sha=main&per_page=100','protection':f'{REPO}/branches/main/protection','rulesets':f'{REPO}/rulesets?includes_parents=true','rules':f'{REPO}/rules/branches/main','workflows':f'{REPO}/actions/workflows'}
    for label,sha in [('main',MAIN),('head',HEAD)]:
        for kind,path in [('runs',f'actions/runs?head_sha={sha}&per_page=100'),('checks',f'commits/{sha}/check-runs?per_page=100'),('status',f'commits/{sha}/status')]:req[label+'_'+kind]=f'{REPO}/{path}'
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=dict(zip(req,pool.map(api,req.values())))
    assert results['main_ref']['body']['object']['sha']==MAIN
    m=results['main_commit']['body'];h=results['head_commit']['body'];pr=results['previous_pr']['body']
    assert m['tree']['sha']==h['tree']['sha']==TREE and [p['sha'] for p in m['parents']]==[PARENT,HEAD]
    assert [p['sha'] for p in h['parents']]==[PARENT] and [c['sha'] for c in results['previous_commits']['body']]==[HEAD]
    assert pr['merged'] and pr['merge_commit_sha']==MAIN and pr['auto_merge'] is None
    assert not [p for p in results['prs']['body'] if p['state']=='open']
    refs=[]
    for b in results['branches']['body']:
        code=subprocess.run(['git','merge-base','--is-ancestor',b['commit']['sha'],MAIN],capture_output=True).returncode
        refs.append(dict(branch=b['name'],sha=b['commit']['sha'],ancestor_exit=code));assert code==0
    assert subprocess.check_output(['git','ls-remote','origin','refs/heads/main'],text=True).split()[0]==MAIN
    hashes=manifests()
    for s in ['S010','S011','S012','S013']:
        count=0
        for line in (R/f'evidence/{s}/HASHES.md').read_text(encoding='utf-8').splitlines():
            z=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
            if z:assert hashlib.sha256((R/z[2]).read_bytes()).hexdigest()==z[1],z[2];count+=1
        hashes[s]=dict(verified_entries=count,frozen_index=None)
    assert (R/'authoritative/NEXT_SESSION_PROMPT.md').read_bytes()==(R/'sessions/S013/FUTURE_S014.md').read_bytes()
    for key,value in results.items():write(f'evidence/S014/entry_{key}.json',value)
    for label in ['main','head']:
        jobs=[dict(run_id=x['id'],response=api(f"{REPO}/actions/runs/{x['id']}/jobs?per_page=100")) for x in results[label+'_runs']['body']['workflow_runs']]
        jj=[j for run in jobs for j in run['response']['body']['jobs']];assert len(jj)==5 and all(j['status']=='completed' and j['conclusion']=='success' for j in jj)
        write(f'evidence/S014/entry_{label}_jobs.json',jobs)
    write('evidence/S014/inherited_hashes.json',hashes);write('evidence/S014/entry_refs.json',refs)
    write('sessions/S014/OWNER_INVOCATION.txt',OWNER);write('sessions/S014/OWNER_STEERING.txt',STEER)
    write('sessions/S014/AUTHORISED_PROMPT.md',(R/'authoritative/NEXT_SESSION_PROMPT.md').read_text(encoding='utf-8'))
    write('sessions/S014/INPUT.md','# S014 invocation and continued research\n\nActual complete accessible invocation/steering archived separately, normalized UTF-8 LF, no transport-byte identity claimed. Owner clarified that ending S013 after intermediate progress was premature; fresh invocation authorizes continuation of the same universal objective as S014 after S013 was already merged. The session-boundary rule did not require closing S013 at that mathematical point. Preserve that history; do not impose a lemma/campaign/audit stopping quota. Exactly S014, no delegation/S015/final stages.\n')
    inv=[]
    for folder in ['authoritative','docs','research','catalogue','audit','campaigns','sessions/S013','evidence/S013','tools','validation','.github']:
        for p in sorted((R/folder).rglob('*')):
            if not p.is_file() or '__pycache__' in str(p):continue
            b=p.read_bytes();row=dict(path=p.relative_to(R).as_posix(),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
            if p.suffix=='.xz':raw=lzma.decompress(b);json.loads(raw);row['decoded_sha256']=hashlib.sha256(raw).hexdigest()
            elif p.suffix=='.json':json.loads(b)
            inv.append(row)
    write('evidence/S014/read_inventory.json',inv)
    write('evidence/S014/environment.json',dict(utc=datetime.now(timezone.utc).isoformat(),python=sys.version,platform=platform.platform(),invocation_sha256=hashlib.sha256(OWNER.encode()).hexdigest(),steering_sha256=hashlib.sha256(STEER.encode()).hexdigest(),plan_sha256=hashlib.sha256((R/'sessions/S014/PLAN.md').read_bytes()).hexdigest(),machine='16 logical processors,16866881536 physical bytes; starting per-process2GiB cap',note='Byte/schema ingestion is not proof inspection.'))
    print(json.dumps(dict(main=MAIN,tree=TREE,manifests=hashes,inventory_files=len(inv))))
if __name__=='__main__':main()
