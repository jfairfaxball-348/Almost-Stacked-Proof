"""Continuing checkpoint, all81 bounded campaigns finished; no closeout."""
import datetime,hashlib,json,os
from pathlib import Path
def read(p):return json.loads(Path(p).read_bytes())
def write(p,v):
    p=Path(p);t=v if isinstance(v,str) else json.dumps(v,indent=2,ensure_ascii=False)+'\n'
    if p.exists() and p.read_text(encoding='utf-8')==t:return
    tmp=p.with_name(p.name+'.s01481.tmp');tmp.write_text(t,encoding='utf-8',newline='\n');os.replace(tmp,p)
def append(p,t):
    old=Path(p).read_text(encoding='utf-8')
    if t not in old:write(p,old.rstrip()+'\n\n'+t+'\n')
def digest(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        while chunk:=f.read(1048576):h.update(chunk)
    return h.hexdigest()
s=read('authoritative/STATE.json');v=s['s014'];assert s['last_completed_session']=='S013' and s['active_session']['status']=='IN_PROGRESS';sat=read('evidence/S014/twofuel_cegis/summary.json');ex=read('evidence/S014/sector_exchange/verification.json');assert sat['certified']==1 and sat['unknown']==3 and ex['status']=='COMPLETE_REGISTERED_SCOPE' and not ex['first_failure']
v.update(campaigns_completed=list(range(1,82)),campaigns_registered=list(range(1,82)),campaign77_status='COMPLETE_F8_EXCLUDED_F9_F10_F12_UNKNOWN',campaign81_status='COMPLETE_FINITE_RESCALED_SECTOR_EXCHANGE_AGREEMENT',research_record='research/S014_ELEMENTARY_SOURCE_AND_ODD_LEAF_CONTRACTION.md');v['continuation_verification'].update(CAM77=sat,CAM81=ex)
current='CURRENT S014 ACTIVE through completed/registeredCAM81, local proofs71-121. CAM77 independently excludes ONLY full-buffer two-pile3 order8/mass12 class F8 (1365 RUP additions/40162 hints); order9/10 iteration caps and order12 time cap remain UNKNOWN. CAM81 all30 fixed graphs through order5, bipartite filter,2490 mod3-residue groups/57060 memberships/560 nontrivial pair-source exchange checks complete with no failure; rescaled-sector M-convexity remains UNPROVED globally.116/118 prescribed-source theorem,117 critical graph-leaf neighbor zeros,119 odd-leaf contraction and120 even-leaf +3 ascent/critical leaf oddness remain complete scoped proofs with finite independent challenges78-80.121 refutes direct unit exchange of THREE by charge, not rescaled exchange or ASH*. Universal SAME-GRAPH STACK comparison OPEN; arbitrary buffers/graph cores remain. Continue S014; no closeout/commit/PR/S015/Lean/phase/contact, CLEAR deferred.'
v['active_campaign_note']=current;s['headline_detail']['assurance']=current;s['as_of']='2026-10-16';write('authoritative/STATE.json',s);spec=read('research/ASH_SPEC.json');spec['s014']=v;write('research/ASH_SPEC.json',spec)
for path in ['authoritative/START_HERE.md','authoritative/DECISION_LOG.md','research/ROUTES.md','research/PROBLEM_SPEC.md','research/ASH_SPEC.md','research/ASHSTAR_ATTACK_BRIEF.md','docs/SESSION_LEDGER.md','docs/PHASE_GATE_LEDGER.md','docs/FAILURE_AND_LESSON_LEDGER.md','tools/README.md','sessions/S014/CHECKPOINT.md','sessions/S014/AUDIT.md','sessions/S014/MILESTONES.md','audit/SEARCH_LOG.md','campaigns/REGISTRY.md','research/S014_COUNTEREXAMPLE_SEARCH.md']:append(path,current)
p=Path('authoritative/NEXT_SESSION_PROMPT.md');old=p.read_text(encoding='utf-8');frozen=Path('sessions/S013/FUTURE_S014.md').read_text(encoding='utf-8');assert old.endswith(frozen)
if current not in old:write(p,old[:-len(frozen)]+current+'\n\n'+frozen)
claims=read('catalogue/claims.json');rows=[(249,'CAM77 ONLY specified F8 c=(1,1,1,1,1,1,3,3),mass12 on order8 independently excluded across ALL connected graphs with full necessary-CNF/LRAT chain. F9/F10 iteration bounds and F12 time bound UNKNOWN; no larger-pattern inference.'),(250,'CAM81 finite complete charge-sector exchange challenge on bipartite fixed graphs through order5:2490 residue/fuel groups,57060 membership queries,560 nontrivial ordered pair/source checks, all matched independently. Rescaled-sector M-convexity remains UNPROVED universally; direct unscaled W_p exchange stays false by121.')]
for i,claim in rows:
    row=dict(id=f'CLM-{i:04d}',status='COMPUTED_EXACT',sources=['SRC-0072'],claim=claim)
    if not any(x['id']==row['id'] for x in claims):claims.append(row)
    append('catalogue/CLAIMS.md',f"| {row['id']} | COMPUTED_EXACT | {claim} | SRC-0072 |")
write('catalogue/claims.json',claims);print(current,flush=True)
exclude={'working_hashes.json','checkpoint_hashes.json','progress_checks.json','active_validation_checks.json'};files={}
for folder in ['sessions/S014','evidence/S014']:
    for p in Path(folder).rglob('*'):
        if p.is_file() and p.name not in exclude and not p.name.endswith('_validation_checks.json'):
            files[p.as_posix()]=digest(p)
for p in [*Path('tools').glob('s014*'),*Path('research').glob('S014*.md')]:
    if p.is_file():files[p.as_posix()]=digest(p)
write('evidence/S014/working_hashes.json',dict(status='ACTIVE_MUTABLE_CHECKPOINT_NOT_CLOSEOUT',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),hash_method='SHA256 streaming 1MiB chunks to bound memory',files=files));print(f'Active scope81 stable files hashed: {len(files)}',flush=True)
