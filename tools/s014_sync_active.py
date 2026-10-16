"""Idempotent ACTIVE checkpoint synchronization; never close or commit S014."""
import datetime,hashlib,json
from pathlib import Path
def read(p):return json.loads(Path(p).read_bytes())
def write(p,v):Path(p).write_text(v if isinstance(v,str) else json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def append(p,v):
    text=Path(p).read_text(encoding='utf-8')
    if v not in text:write(p,text.rstrip()+'\n\n'+v+'\n')
def main():
    s=read('authoritative/STATE.json');assert s['last_completed_session']=='S013' and s['active_session']['status']=='IN_PROGRESS'
    assert not Path('sessions/S014/CLOSEOUT.md').exists() and not Path('sessions/S014/FUTURE_S015.md').exists()
    s['s014'].update(campaigns_completed=list(range(1,33)),new_local_proofs=list(range(71,90)),critical_private_head='FALSE_CAM25_26_ACTUAL_CRITICAL_INPUT_EXISTENCE',H2='FALSE_CAM27_SOURCE_ZERO_ONLY',H2r='UNPROVED_SUFFICIENT_INDUCTION_CAM28_29_BOUNDED_SUPPORT',minimum_heavy_selection='PROGRAMME_PROVED_89_SCOPED_NOT_UNIVERSAL',research_record='research/S014_CRITICAL_HEAVY_ELIMINATION.md')
    s['s014']['new_proof_assurance']='LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING'
    s['s014']['owner_no_closeout_sha256']=hashlib.sha256(Path('sessions/S014/OWNER_KEEP_GOING.txt').read_bytes()).hexdigest()
    s['s014']['continuation_verification'].update(CAM25=read('evidence/S014/headcritical/verification.json'),CAM26=read('evidence/S014/criticalcert/verification.json'),CAM28=read('evidence/S014/eliminate_residual/verification.json'),CAM29={k:v for k,v in read('evidence/S014/regular_eliminate/verification.json').items() if k!='graphs_detail'},CAM30={k:v for k,v in read('evidence/S014/coupled/verification.json').items() if k!='selected_for_AS_rays'})
    s['active_session']['working_research']='research/S014_CRITICAL_HEAVY_ELIMINATION.md';s['active_session']['proof_reports']=[p.as_posix() for p in sorted(Path('research').glob('S014*.md'))]
    s['next_session_handoff']=None;s['recommended_next_session']='S014';s['headline_detail']['assurance']='S014 ACTIVE,71-89 local proofs and32 completed registered campaigns; universal STACK/CLEAR OPEN, independent human/kernel review pending. Owner prohibits closeout before proof/counterexample. No universal inference from finite comparisons.'
    s['s014']['active_campaign_note']='CAM32 COMPLETE: exact general STACK thresholds19/25 on selected coupled n12 graphs match exact unbounded AS maxima18/24; all critical losers AS. Continue proof/counterexample work.'
    write('authoritative/STATE.json',s);spec=read('research/ASH_SPEC.json');spec['s014']=s['s014'];write('research/ASH_SPEC.json',spec)
    current='S014 ACTIVE continuation:71-89 local exact-scope proofs;32 completed prior-hashed campaigns. CAM25/26 refute critical private-head input existence, not ASH*. H2r heavy-elimination with source residual0/1 and up to two new bits survives1457 critical non-AS inputs across fixed/new cases, but is UNPROVED. Minimum-heavy selection89 preserves70 residual neighborhoods and supplies all fewer-heavy winners, even Q-decreasing ones. CAM31/32 certify exact AS maxima18/24 and unrestricted thresholds19/25 on two selected coupled n12 graphs; all their critical losers AS. No closeout/commit/PR/future handoff. Universal STACK/CLEAR OPEN; CLEAR deferred.'
    for p in ['authoritative/START_HERE.md','authoritative/DECISION_LOG.md','research/ROUTES.md','research/PROBLEM_SPEC.md','research/ASH_SPEC.md','research/ASHSTAR_ATTACK_BRIEF.md','docs/SESSION_LEDGER.md','docs/PHASE_GATE_LEDGER.md','docs/FAILURE_AND_LESSON_LEDGER.md','tools/README.md','sessions/S014/CHECKPOINT.md','sessions/S014/AUDIT.md','sessions/S014/MILESTONES.md']:
        text=Path(p).read_text(encoding='utf-8').replace('S014 completed at a substantive mathematical review boundary: local proofs71-88 and24 preregistered campaigns.','Historical administrative closeout attempt REVERSED by explicit owner direction; S014 ACTIVE. Local proofs71-88 and24 campaigns preserved.').replace('S015 strictly FUTURE/UNEXECUTED. See sessions/S014/CLOSEOUT.md','No closeout or S015 handoff. See sessions/S014/CHECKPOINT.md')
        write(p,text);append(p,current)
    append('research/S014_TRIPLET_HEAD_AND_SIGNED_BARRIER.md','CURRENT CONTINUATION SUPERSEDES THE EARLIER REVIEW-BOUNDARY NARRATIVE: S014 remains ACTIVE, owner explicitly prohibits closeout before proof/counterexample. CAM25/26 now refute the critical private-head input-existence strengthening too; GLOBAL-Q-only remains unproved. Read research/S014_CRITICAL_HEAVY_ELIMINATION.md. All earlier scoped proofs/evidence preserved.')
    sources=read('catalogue/sources.json');newsrc=dict(id='SRC-0057',type='LOCAL_RESEARCH_OR_EVIDENCE',title='S014 critical heavy elimination and minimum-heavy selection89',url='../research/S014_CRITICAL_HEAVY_ELIMINATION.md',access='PROOF_INSPECTED',note='Active local proof89 and complete conditional induction H2r=>ASH*, H2r unproved; fresh exact critical auxiliary failures and bounded challenges. No universal/kernel or priority assurance.')
    if not any(x['id']==newsrc['id'] for x in sources):sources.append(newsrc)
    write('catalogue/sources.json',sources);append('catalogue/SOURCES.md',f"- **{newsrc['id']}** {newsrc['title']} - **PROOF_INSPECTED**. {newsrc['url']} - {newsrc['note']}")
    claims=read('catalogue/claims.json');new=[
    (166,'PROGRAMME_PROVED','S01489: minimize heavy count first, then maximize Q/minimize degree P on a losing layer M>=4; selected heavy neighborhoods are minimal and incomparable. Zero relocation uses the correct endomorphism direction d->c. Fewer-heavy same-mass candidates must win at a hypothetical counterexample; no universal AS selection proved.'),
    (167,'COMPUTED_EXACT','CAM25:252 full general threshold comparisons,508929 losing states;4 ordered-pair failures at2 actual critical inputs refute smaller odd private-head input existence. All graph AS comparisons hold; no non-AS global Q critical maximum.'),
    (168,'COMPUTED_EXACT','CAM26: fresh complete negative closures for2 critical inputs and2 AS critical witnesses,2556 states;52 literal transformed winning moves. Critical private-head failure is not ASH* failure.'),
    (169,'HEURISTIC','H2r: every critical non-AS STACK loser has a losing elimination to one fewer heavy site retaining source residual0/1 and adding at most2 binary bits at initially empty sites. Complete conditional induction would imply ASH*, but universal hypothesis remains UNPROVED.'),
    (170,'COMPUTED_EXACT','CAM27: entire-source H2 fails1124 of1230 critical non-AS inputs, already P3(3,3,0); source residual must not be silently forbidden. Failed H2 records retained.'),
    (171,'COMPUTED_EXACT','CAM28:444 fixed STACK cases/1230 non-AS critical inputs/45804 full residual H2r candidates, zero failures. Bounded support only.'),
    (172,'COMPUTED_EXACT','CAM29:72 new cycle/matching/chord graphs n8/9/10,1545176 complete losing states,227 non-AS critical inputs/11632 H2r candidates, zero failures. All AS comparisons hold; no universal extrapolation.'),
    (173,'COMPUTED_EXACT','CAM30:252 coupled n12 gadget inputs at mass16,108 lose/144 win;617212 state records/1799764 legal dependencies checked, no cap hit. Two strongest cross-edge survivors selected by prior rule; not ASH* counterexamples by themselves.'),
    (174,'COMPUTED_EXACT','CAM31: complete unbounded source/binary-buffer STACK rays on C00_51/C00_60; explicit automorphisms cover all12 sources using reps0/2/4. Exact L_AS18/24. Thus fixed mass16 holes do not refute ASH*. General thresholds tested separately in CAM32.'),
    (175,'COMPUTED_EXACT','CAM32: exact general STACK thresholds19/25 on C00_51/C00_60, independently compared348930/587258 full losing states; exact AS maxima18/24 match. Every critical loser is AS, H2r scope there vacuous. No unrestricted ASH* inference.')]
    for i,status,claim in new:
        ident=f'CLM-{i:04d}';row=dict(id=ident,status=status,sources=['SRC-0057'],claim=claim)
        if status=='PROGRAMME_PROVED':row['cold_audit']='LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING'
        if not any(c['id']==ident for c in claims):claims.append(row)
        append('catalogue/CLAIMS.md',f'| {ident} | {status} | {claim} | SRC-0057 |')
    write('catalogue/claims.json',claims)
    for i,status,claim in new[1:]:
        if status=='COMPUTED_EXACT':append('campaigns/REGISTRY.md',f'## S014 active CLM-{i:04d}\n\n{claim} Prior-hashed plan and independent complete code/certificates/logs under sessions/S014/evidence/S014. No session or phase promotion.')
    append('audit/SEARCH_LOG.md','S014 ongoing89/H2r: exact minimum-heavy choice and correct zero-relocation direction checked against63/66/67; H2r finite agreement is not proof and fails without criticality (printed P4 control). Original critical private-head strengthening now refuted by CAM25/26, no priority/kernel/universal claim.')
    p=Path('authoritative/NEXT_SESSION_PROMPT.md');text=p.read_text(encoding='utf-8');frozen=Path('sessions/S013/FUTURE_S014.md').read_text(encoding='utf-8');assert text.endswith(frozen)
    if current not in text:write(p,text[:-len(frozen)]+current+'\n\n'+frozen)
    files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for folder in ['sessions/S014','evidence/S014'] for p in Path(folder).rglob('*') if p.is_file() and p.name not in ['working_hashes.json','checkpoint_hashes.json','progress_checks.json','active_validation_checks.json']}
    files.update({p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('tools').glob('s014*.py')});files.update({p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('research').glob('S014*.md')})
    write('evidence/S014/working_hashes.json',dict(status='ACTIVE_MUTABLE_CHECKPOINT_NOT_CLOSEOUT',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),files=files))
    print(current)
if __name__=='__main__':main()
