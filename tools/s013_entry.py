"""S013 live authority, historical integrity and invocation provenance."""
import concurrent.futures,hashlib,json,lzma,platform,re,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
from s010_entry import api,manifests

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'evidence/S013'
REPO='repos/jfairfaxball-348/Almost-Stacked-Proof'
MAIN='1e28259f6e35849723bbe5e5fd545630498d45a9'

def write(p,v):
    p=ROOT/p;p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(v if isinstance(v,str) else json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')

def main():
    req={'main_ref':f'{REPO}/git/ref/heads/main','branches':f'{REPO}/branches?per_page=100','prs':f'{REPO}/pulls?state=all&per_page=100','history':f'{REPO}/commits?sha=main&per_page=100','protection':f'{REPO}/branches/main/protection','rulesets':f'{REPO}/rulesets?includes_parents=true','rules':f'{REPO}/rules/branches/main','workflows':f'{REPO}/actions/workflows'}
    points={'s012_main':'1505c1b8437973aa23bd09b6040a3ad39852f311','s012_head':'a201eeb0db60dfd68386ff76450a19ac4bb91c0a','admin_main':MAIN,'admin_head':'f831bce6a40a868b4a78c11dd5e74c995626edf5'}
    for tag,sha in points.items():
        req[tag+'_commit']=f'{REPO}/git/commits/{sha}'
        for kind,suffix in [('runs',f'actions/runs?head_sha={sha}&per_page=100'),('checks',f'commits/{sha}/check-runs?per_page=100'),('status',f'commits/{sha}/status')]:req[tag+'_'+kind]=f'{REPO}/{suffix}'
    for num in (14,15):
        for kind,path in [('pr',f'pulls/{num}'),('commits',f'pulls/{num}/commits'),('comments',f'issues/{num}/comments?per_page=100')]:req[f'pr{num}_{kind}']=f'{REPO}/{path}'
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:results=dict(zip(req,pool.map(api,req.values())))
    assert results['main_ref']['body']['object']['sha']==MAIN
    assert subprocess.check_output(['git','ls-remote','origin','refs/heads/main'],text=True).split()[0]==MAIN
    for num,tag,parent in [(14,'s012','ca4aad7abf25d396eed16c6e3d89179ea6215b60'),(15,'admin',points['s012_main'])]:
        m=results[tag+'_main_commit']['body'];h=results[tag+'_head_commit']['body'];pr=results[f'pr{num}_pr']['body']
        assert [p['sha'] for p in m['parents']]==[parent,points[tag+'_head']]
        assert [p['sha'] for p in h['parents']]==[parent] and m['tree']==h['tree']
        assert [c['sha'] for c in results[f'pr{num}_commits']['body']]==[points[tag+'_head']]
        assert pr['merged'] and pr['merge_commit_sha']==points[tag+'_main'] and pr['auto_merge'] is None
    assert not [p for p in results['prs']['body'] if p['state']=='open']
    refs=[]
    for b in results['branches']['body']:
        code=subprocess.run(['git','merge-base','--is-ancestor',b['commit']['sha'],MAIN],capture_output=True).returncode
        refs.append({'branch':b['name'],'sha':b['commit']['sha'],'ancestor_exit':code});assert code==0
    hashes=manifests()
    for s in ('S010','S011','S012'):
        count=0
        for line in (ROOT/f'evidence/{s}/HASHES.md').read_text(encoding='utf-8').splitlines():
            m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
            if m:assert hashlib.sha256((ROOT/m[2]).read_bytes()).hexdigest()==m[1],m[2];count+=1
        hashes[s]={'verified_entries':count,'frozen_index':None}
    revision=json.loads((ROOT/'authoritative/HANDOFF_REVISION.json').read_bytes())
    for key,pkey in [('current_sha256','current_prompt'),('owner_request_sha256','owner_request'),('prior_sha256','prior_prompt')]:assert hashlib.sha256((ROOT/revision[pkey]).read_bytes()).hexdigest()==revision[key]
    assert (ROOT/'authoritative/NEXT_SESSION_PROMPT.md').read_bytes()==(ROOT/revision['current_prompt']).read_bytes()
    for k,v in results.items():write(f'evidence/S013/entry_{k}.json',v)
    for tag in points:
        jobs=[{'run_id':r['id'],'response':api(f"{REPO}/actions/runs/{r['id']}/jobs?per_page=100")} for r in results[tag+'_runs']['body']['workflow_runs']]
        write(f'evidence/S013/entry_{tag}_jobs.json',jobs)
    write('evidence/S013/inherited_hashes.json',hashes);write('evidence/S013/entry_refs.json',refs)
    write('sessions/S013/OWNER_INVOCATION.txt','Run the next session\n')
    write('sessions/S013/AUTHORISED_PROMPT.md',(ROOT/'authoritative/NEXT_SESSION_PROMPT.md').read_text(encoding='utf-8'))
    write('sessions/S013/INPUT.md','# S013 actual invocation and scope\n\nActual complete accessible owner message: `Run the next session`. Archived normalized UTF-8 LF, no transport-byte identity claimed. Live main and owner-revised prompt select exactly S013; administrative revision provenance verified separately from original frozen S012 handoff. No delegation, S014 or deferred final action.\n')
    inv=[]
    for folder in ['authoritative','docs','research','catalogue','audit','campaigns','sessions/S012','evidence/S012','tools','validation','.github']:
        for p in sorted((ROOT/folder).rglob('*')):
            if not p.is_file() or '__pycache__' in str(p):continue
            b=p.read_bytes();item={'path':p.relative_to(ROOT).as_posix(),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
            if p.suffix=='.xz':d=lzma.decompress(b);json.loads(d);item['decoded_sha256']=hashlib.sha256(d).hexdigest()
            elif p.suffix=='.json':json.loads(b)
            inv.append(item)
    write('evidence/S013/read_inventory.json',inv)
    write('evidence/S013/environment.json',{'utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,'platform':platform.platform(),'invocation_sha256':hashlib.sha256(b'Run the next session\n').hexdigest(),'plan_sha256':hashlib.sha256((ROOT/'sessions/S013/PLAN.md').read_bytes()).hexdigest(),'machine':'16 logical processors,16866881536 physical bytes; leave operating headroom','note':'Byte/schema ingestion is not proof inspection.'})
    print(json.dumps({'main':MAIN,'manifests':hashes,'inventory_files':len(inv)}))

if __name__=='__main__':main()
