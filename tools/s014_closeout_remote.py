"""Read-only live reconciliation before S014 integration; preserve actual API outcomes."""
import concurrent.futures, datetime, json, subprocess
from pathlib import Path
from s010_entry import api

repo='repos/jfairfaxball-348/Almost-Stacked-Proof'
main=subprocess.check_output(['git','ls-remote','origin','refs/heads/main'],text=True).split()[0]
assert main=='8ea5db207a91ca917c3b94bc98b54ac65406e7a5'
requests={
 'main_ref':f'{repo}/git/ref/heads/main','main_commit':f'{repo}/git/commits/{main}',
 'previous_pr':f'{repo}/pulls/16','branches':f'{repo}/branches?per_page=100',
 'prs':f'{repo}/pulls?state=all&per_page=100','history':f'{repo}/commits?sha=main&per_page=100',
 'protection':f'{repo}/branches/main/protection','rulesets':f'{repo}/rulesets?includes_parents=true',
 'rules':f'{repo}/rules/branches/main','workflows':f'{repo}/actions/workflows',
 'workflow_file':f'{repo}/contents/.github/workflows/governance.yml?ref={main}',
}
for label,sha in [('main',main),('previous_head','ccfbdd7194c6571b5b9cbd780941777494f03073')]:
 for kind,path in [('runs',f'actions/runs?head_sha={sha}&per_page=100'),('check_runs',f'commits/{sha}/check-runs?per_page=100'),('statuses',f'commits/{sha}/status')]:requests[label+'_'+kind]=f'{repo}/{path}'
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 results=dict(zip(requests,pool.map(api,requests.values())))
assert results['main_ref']['body']['object']['sha']==main
c=results['main_commit']['body'];assert c['tree']['sha']=='b9811bdbf667c9e93df9a5001ebf30a036adb73b'
assert [p['sha'] for p in c['parents']]==['1e28259f6e35849723bbe5e5fd545630498d45a9','ccfbdd7194c6571b5b9cbd780941777494f03073']
assert results['previous_pr']['body']['merged'] and results['previous_pr']['body']['merge_commit_sha']==main
assert not [p for p in results['prs']['body'] if p['state']=='open']
for label in ['main','previous_head']:
 runs=results[label+'_runs']['body']['workflow_runs'];assert runs
 results[label+'_jobs']=[api(f"{repo}/actions/runs/{run['id']}/jobs?per_page=100") for run in runs]
 jobs=[j for result in results[label+'_jobs'] for j in result['body']['jobs']]
 assert len(jobs)==5 and all(j['status']=='completed' and j['conclusion']=='success' for j in jobs)
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),main=main,results=results,scope='Pre-commit read-only reconciliation; outgoing commit/PR/merge/jobs do not yet exist. Inaccessible protection endpoints retain actual error responses, not an invented policy.')
Path('evidence/S014/closeout_remote_snapshot.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
print('Live main, S013 merge/parents/tree and both actual five-job runs reconciled; policies and all requested API outcomes archived.')
