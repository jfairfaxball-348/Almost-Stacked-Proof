"""Synchronize active research; never commit, close or advance a session."""
import datetime,hashlib,json
from pathlib import Path
def read(p):return json.loads(Path(p).read_bytes())
def write(p,v):Path(p).write_text(v if isinstance(v,str) else json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def append(p,v):
    text=Path(p).read_text(encoding='utf-8')
    if v not in text:write(p,text.rstrip()+'\n\n'+v+'\n')
PROOFS=[
('71','Protected capacitated multiple-donor reconstruction is equivalent to EVERY donor-subset Hall inequality on true heads, with a reserved simple root path. GLOBAL Q losers force deficiencies, not a universal contradiction.'),
('72','Every adjacent1/2 transfer from a stackable CLEAR loser CLEARs; its THREE roots remain absent. The proposed triangular loss-transfer shortcut is false.'),
('73','If retaining3 at an occupied triangular root leaves a whole input that STACKs, the original input CLEARs.'),
('74','Input on a complete-bipartite subgraph with all initial heavy sites ambient-triangular CLEARs at mass>=3alpha(occupied support)+4, by a complete all-input case proof.'),
('75','If every vertex is triangular and every nontrivial nontriangle-edge component is complete bipartite, CLEAR=STACK. A same-graph STACK AS witness transfers if available.'),
('76','Every input of mass>=10 on adjacent sites, at least one triangular, CLEARs, with all parities and zero-root cases covered.'),
('77','CLEAR=STACK when each nontrivial nontriangle-edge component satisfies75 or is K(a,b), b>=a+2, with an actual external common neighbor of B; A need not be triangular.'),
('78','K(k,3) plus one edge in the size-three part has both thresholds3k+1 and both ASH* for all k>=3, using the credited independent-set AS witness.'),
('79','For a,b>=1 the exact one-edge buffer join has STACK=max(3b+1,3a+5), CLEAR=max(3b+1,3a+7), both ASH*. Earlier F_a and known bounds/primitives retain credit.'),
('80','For a,b>=1,m>=2 the matching-buffer join has STACK=CLEAR=max(3b+1,3a+4m+1), with explicit all-target AS critical witnesses and both ASH*.'),
('81','An initially binary region U with I single arrivals/O pair exits satisfies theta(U)<=2I-O if emptied, and <=2I-O-1 for one terminal pile whose root starts empty or has incoming. Complete causal first-firing proof includes repeated/zero sites.'),
('82','For J(a,b,F), a,b>=1,F nonempty/no isolates, n=a+b+|F|,W=max_U(|U|+2theta(F[U])), STACK=S=max(n+1,3b+1,3a+W+1), CLEAR=max(S,3a+7). Both ASH* on this full arbitrary-buffer join class, not arbitrary graphs.'),
('83','For ANY finite simple graph of order>=2,N>=1, STACKability of N at r plus binary U implies N>=theta(G[U])+1. With UNIVERSAL r this is iff, giving rooted AS maximum max_U(|U|+theta(G[U])), not full graph threshold.'),
('84','Inside82, positive CLEAR-STACK gap occurs exactly for b<=a+1,F=K2 (gap2) or K3 (gap1); ALL critical CLEAR losers there have only nontriangular heavy sites. Universal gap1 C14 remains unproved.')]
FINITE=[
('CAM02','2087 matching cases/2210 reservations/114 complete reconstructions;127 of127 triangular loss-transfer tests fail, with independently checked selected negative closures. Proper-subset Hall obstructions retained.'),
('CAM03-04','Complete unbounded binary source rays plus independent full general losing layers certify theta334 STACK25/CLEAR27 and barbell55 STACK48/CLEAR48. All critical losers on these four cases AS; mixed source boxes remain limited.'),
('CAM05-06','Whole-pile swaps fail1846 of10240 tests, including71 GLOBAL-Q CLEAR cases; triangular split fails3 of176 tests. Selected complete negative closures and winning traces independently checked; weaker critical variants unproved.'),
('CAM07-10','Seven complete-bipartite triangular construction challenges, four book examples, seven balanced exact AS ray examples/ten general thresholds and7620 literal one-edge AS histories all pass at their fixed scopes.'),
('CAM11','Fourteen matching-buffer full threshold comparisons,66144 literal STACK histories/552534 moves and explicit AS witnesses pass independently.'),
('CAM12','Two full W/path-cover algorithms agree on50 prescribed labeled F graphs, giving146 join graphs/292 goal comparisons:146 exact STACK endpoints match82;286 goal endpoints exact, six CLEAR initially incomplete at STACK cutoff.'),
('CAM13','All66642 boundary cells/11625 terminal histories/10033 true path covers agree independently; six earlier CLEAR cutoffs separately completed with old layers unchanged;228 explicit STACK AS witnesses checked across146 graphs.'),
('CAM14','All198320 arbitrary-buffer literal STACK histories/2046597 moves pass independently, including180224 n16 histories with order bound17 strictly dominating both other lower terms16.'),
('CAM15','ALL26 source rays/six general comparisons certify Q3plus03 thresholds15/15, Wagner8 11/11, Petersen10 15/15; every open neighborhood minimal, every critical Q/Q-P maximum AS.'),
('CAM16','All256 parity-preserving AS candidates for32 non-AS Wagner goal/input pairs checked,1716 literal winning moves; every input has a related parity-class AS loser. Bounded positive pattern only.'),
('CAM17','Fixed343 goal cases/1043 non-AS critical inputs: two ALL-receiver fixed-parity failures and eight heavy-receiver failures. Original schema KeyError/code/log preserved; separate hashed v2 metadata-only repair passes.'),
('CAM18','Two exact critical parity obstructions independently recomputed through threshold9, every old layer preserved;161 complete negative states/12 same-parity AS winners/72 moves checked. Critical non-AS loser isolated under every unit redistribution; alpha2 blocks endomorphic AS lift.'),
('CAM19','Fixed343-case odd-shift diagnostic:34 true-head transforms/14 eligible critical inputs,28 losing outputs. Each input has some losing output; six ORDERED-pair variants fail. Smaller-donor22-pair filter is post-data finite support, not a universal theorem.')]
def main():
    s=read('authoritative/STATE.json');assert s['last_completed_session']=='S013' and s['active_session']['status']=='IN_PROGRESS'
    s['s014'].update(multiple_donor_argument='PROGRAMME_PROVED_71_NECESSARY_NOT_UNIVERSAL',new_local_proofs=list(range(71,87)),new_proof_assurance='LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING',arbitrary_buffer_join='PROGRAMME_PROVED_82_AT_EXACT_CLASS_SCOPE',rooted_path_cover='PROGRAMME_PROVED_81_83',clear_gap1_candidate='UNPROVED',campaigns_completed=list(range(1,20)),new_computed_controls=dict(theta334=[25,27],barbell55=[48,48],Q3plus03=[15,15],Wagner8=[11,11],Petersen10=[15,15]),historical_bytes_unchanged=True,parity_strengthening='FALSE_EVEN_AT_CRITICAL_SIZE',odd_shift_candidate='UNPROVED_BOUNDED_INPUT_EXISTENCE_SUPPORT_ORDERED_VERSION_FAILS',preserved_implementation_failure='CAM17_KEYERROR_N_REPAIRED_V2_NO_SCOPE_CHANGE')
    s['active_session']['working_research']='research/S014_PARITY_AND_TRUE_HEAD_FRONTIER.md'
    s['active_session']['proof_reports']=['research/S014_UNIVERSAL_RESEARCH.md','research/S014_TWIN_BLOWUP_COMPARISON.md','research/S014_MATCHING_BUFFER_COMPARISON.md','research/S014_ARBITRARY_BUFFER_JOIN.md','research/S014_LOCAL_PROOF_AUDIT.md','research/S014_PARITY_AND_TRUE_HEAD_FRONTIER.md']
    if 'research_focus' in s['s014']:
        focus=s['s014']['research_focus']
        assert hashlib.sha256(Path(focus['document']).read_bytes()).hexdigest()==focus['sha256']
        s['open_obligations'][-1]=focus['obligation']
    else:
        s['open_obligations'][-1]='Continue S014: critical fixed-parity compression, local unit-Q ascent and endomorphic AS lifting have actual counterexamples. Prove a suitable parity-changing true-head reconstruction or another SAME-GRAPH AS domination, keeping71/81 terminal/root constraints and nonadjacent/partial neighborhoods. Odd-shift input existence is UNPROVED; six ordered-pair failures remain. No S015/final-stage execution.'
    s['source_inspection']='S014 current October/April/earlier TreeStack/ordering digests unchanged; selected exact ordering, complete-bipartite8.4, Hamiltonian necessity October6.2/Aprilp27 and path-cover6.8 inspected. No worldwide priority/kernel assurance.'
    for goal in ['stack','clear']:
        key='critical_form_ASHstar_'+goal
        if 'S01471-84' not in s['headline_detail'][key]:s['headline_detail'][key]+='; S01471-84 prove Hall/causal path-cover necessity and full arbitrary-buffer join-class ASH*, not the unrestricted comparison.'
    s['headline_detail']['assurance']='S014 complete local proofs71-84 with14 prior-hashed distinct-validator campaigns and historical dependency replay. Independent human/kernel/new-session cold audit pending. Universal STACK/CLEAR OPEN.'
    write('authoritative/STATE.json',s);spec=read('research/ASH_SPEC.json');spec['s014']=s['s014'];write('research/ASH_SPEC.json',spec)
    claims=read('catalogue/claims.json');new=[]
    for number,text in PROOFS:new.append(dict(id=f'CLM-{131+int(number)-71:04d}',status='PROGRAMME_PROVED',sources=['SRC-0052'],claim=f'S014{number}: '+text,cold_audit='LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING'))
    for number,text in [(85,'Inside a fixed-parity losing layer of mass>=4, Q/P-selected heavies have incomparable open neighborhoods; any strictly nonminimal heavy must be ODD and every smaller-neighborhood site EMPTY. Global67 can change parity and cannot be silently reused in that simplex.'),(86,'An AS input pushed through any same-graph endomorphism has at most one coordinate>alpha(G), since all other fibers are independent binary sets. Thus the two alpha2 critical examples with two3-piles admit no endomorphic AS lift.')]:new.append(dict(id=f'CLM-{153+number-85:04d}',status='PROGRAMME_PROVED',sources=['SRC-0054'],claim=f'S014{number}: '+text,cold_audit='LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING'))
    for i,(campaign,text) in enumerate(FINITE):new.append(dict(id=f'CLM-{145+i if i<8 else 155+i-8:04d}',status='COMPUTED_EXACT',sources=['SRC-0053'] if i<8 else ['SRC-0054'],claim=campaign+': '+text+' No universal extrapolation.'))
    for c in new:
        if not any(old['id']==c['id'] for old in claims):claims.append(c)
        else:assert next(old for old in claims if old['id']==c['id'])==c
        append('catalogue/CLAIMS.md',f"| {c['id']} | {c['status']} | {c['claim']} | {', '.join(c['sources'])} |")
    write('catalogue/claims.json',claims);sources=read('catalogue/sources.json')
    for number,title,url,note in [(52,'S014 local proofs71-84 and exact scope adjudication','../research/S014_LOCAL_PROOF_AUDIT.md','LOCAL UNCOMMITTED ACTIVE research; complete join-class comparison/causal necessity, no universal ASH*, worldwide novelty or kernel assurance. Execution-time candidate labels/citation typo explicitly reconciled.'),(53,'S014 fourteen preregistered independent campaigns','../sessions/S014/MILESTONES.md','Complete bounded certificates/logs/input/code/plan hashes in evidence/S014. Six CAM12 CLEAR cutoffs preserved and separately completed in CAM13. No caps hit or universal extrapolation.')]:
        sid=f'SRC-{number:04d}'
        if not any(x['id']==sid for x in sources):sources.append(dict(id=sid,type='LOCAL_RESEARCH_OR_EVIDENCE',title=title,url=url,access='PROOF_INSPECTED',note=note))
        append('catalogue/SOURCES.md',f'- **{sid}** {title} - **PROOF_INSPECTED**. {note} See {url[3:]}.')
    write('catalogue/sources.json',sources)
    if not any(x['id']=='SRC-0054' for x in sources):
        sources.append(dict(id='SRC-0054',type='LOCAL_RESEARCH_OR_EVIDENCE',title='S014 partial-neighborhood/parity continuation85-86 and CAM15-19',url='../research/S014_PARITY_AND_TRUE_HEAD_FRONTIER.md',access='PROOF_INSPECTED',note='LOCAL UNCOMMITTED ACTIVE: exact critical parity/local-Q/endomorphism barriers, full negative closures and literal winners; odd-shift existence remains unproved. Initial CAM17 schema failure and v2 repair both retained.'))
        write('catalogue/sources.json',sources)
    append('catalogue/SOURCES.md','- **SRC-0054** S014 partial-neighborhood/parity continuation85-86 and CAM15-19 - **PROOF_INSPECTED**. Local active research/S014_PARITY_AND_TRUE_HEAD_FRONTIER.md; exact critical barriers, independent full certificates, preserved schema failure/repair, unproved odd-shift frontier. No universal/kernel assurance.')
    checkpoint='# S014 ACTIVE research checkpoint\n\nLast completed session S013; S014 remains IN_PROGRESS on session/S014-residual-universal-comparison, main/base8ea5db207a91ca917c3b94bc98b54ac65406e7a5. Live remote main re-read unchanged during this continuation. No authored session commit/PR/merge/closeout or S015 handoff. Universal STACK/CLEAR OPEN; later phases unchanged.\n\nRead research/S014_LOCAL_PROOF_AUDIT.md FIRST for current statuses/corrections; execution-time proof texts retain preflight bytes. Complete local proofs71-84 cover protected Hall reconstruction, triangular components, full arbitrary-buffer joins and causal first-firing/rooted-AS necessities.14 prior-hashed campaigns independently checked. These are tools toward the universal comparison.\n\nContinuing obligation: '+s['open_obligations'][-1]+'\n\nEnding an answer stops that turn; an ACTIVE label alone does not run research. This checkpoint preserves actual work and is not itself a stopping rule. No owner-action blocker is claimed.\n'
    write('sessions/S014/CHECKPOINT.md',checkpoint)
    write('sessions/S014/CHECKPOINT.md',checkpoint.replace('proofs71-84','proofs71-86').replace('14 prior-hashed','19 prior-hashed').replace('Read research/S014_LOCAL_PROOF_AUDIT.md FIRST','Read research/S014_PARITY_AND_TRUE_HEAD_FRONTIER.md, then research/S014_LOCAL_PROOF_AUDIT.md'))
    write('sessions/S014/MILESTONES.md','# S014 continuing milestones, not closeout\n\nCurrent frontier: research/S014_PARITY_AND_TRUE_HEAD_FRONTIER.md; foundation proof audit: research/S014_LOCAL_PROOF_AUDIT.md.\n\n'+'\n\n'.join(f'**{name}:** {text}' for name,text in FINITE)+'\n\nNo cap hit; original logs/certificates and registered cutoffs retained. CAM17 original schema failure and separate passing repair both retained. Universal STACK/CLEAR OPEN.\n')
    write('sessions/S014/AUDIT.md','# S014 active audit\n\nS01363-70 dependency cold challenge and24 unchanged historical replays PASS at stated scopes. Additional S008 dependency replay PASS. Current new-proof adjudication: research/S014_LOCAL_PROOF_AUDIT.md, including root/parity/zero/input/chronology boundaries, source6.2 correction and independent finite checks. New71-84 locally PROGRAMME_PROVED; independent human/kernel/session-external review pending. Universal STACK/CLEAR OPEN; not a final session audit or closeout.\n')
    old='Multiple-donor matching argument awaits adversarial checking and an extremal implication.'
    now='Multiple-donor reconstruction71 is locally proved as necessary Hall deficiency;81-84 add causal path-cover necessity and full arbitrary-buffer join-class comparisons. Universal comparison remains OPEN. Read research/S014_LOCAL_PROOF_AUDIT.md for current scopes.'
    for p in ['authoritative/START_HERE.md','research/ROUTES.md','research/ASH_SPEC.md','research/PROBLEM_SPEC.md','research/ASHSTAR_ATTACK_BRIEF.md']:write(p,Path(p).read_text(encoding='utf-8').replace(old,now))
    p=Path('authoritative/NEXT_SESSION_PROMPT.md');text=p.read_text(encoding='utf-8');needle='The following is the immutable prospective scope originally prepared by S013.';update='Current S014 progress: read research/S014_LOCAL_PROOF_AUDIT.md and sessions/S014/MILESTONES.md first.71-84 locally proved at exact scopes;14 prior-hashed campaigns complete. Universal STACK/CLEAR OPEN; continue the same session on true-head/weighted-region comparison.\n\n'
    replacement='Current S014 progress: read research/S014_PARITY_AND_TRUE_HEAD_FRONTIER.md and sessions/S014/MILESTONES.md first.71-86 locally proved at exact scopes;19 prior-hashed campaigns complete. Universal STACK/CLEAR OPEN; continue the same session on parity-changing true-head/weighted-region comparison.\n\n'
    text=text.replace(update,replacement)
    if replacement not in text:text=text.replace(needle,replacement+needle)
    write(p,text)
    append('authoritative/DECISION_LOG.md','| 2026-10-15 S014 continued | Accept71-84 at exact local scopes after causal/root/zero/parity challenge and14 registered independent campaigns;82 settles arbitrary buffer joins, not arbitrary graphs | research/S014_LOCAL_PROOF_AUDIT.md | S014 active; universal STACK/CLEAR OPEN; no phase/session promotion |')
    append('docs/SESSION_LEDGER.md','| S014 continued | 2026-10-15 |14 preregistered campaigns, complete local proofs71-84; universal true-head comparison remains | IN_PROGRESS; no authored session commit/PR/closeout/S015 |')
    append('docs/PHASE_GATE_LEDGER.md','S014 continuing update:71-84 complete local proofs and14 bounded independent campaigns. Exact class/necessity scopes only; universal STACK/CLEAR OPEN, Phase1 IN_PROGRESS; phases2-6 unchanged, new-proof independent cold assurance pending.')
    append('docs/FAILURE_AND_LESSON_LEDGER.md','- FL-S014-02: Ending a turn is an actual stop; ACTIVE state is not a running job. Followed renewed owner steering through multiple proofs and14 campaigns. Preserve failed triangular TR/whole-pile swap/triangle split. Path-cover sufficiency alone was insufficient for the buffer lower;81 supplies causal necessity. Retain separate order n+1 for dense buffers. Universal geometric/weighted comparison remains unproved.')
    for name,text in FINITE:append('campaigns/REGISTRY.md',f'## S014 {name} completed within ACTIVE session\n\n{text} Prior-hashed plans, frozen preflights, separate producer/checker logs and full certificates under sessions/S014/evidence/S014. No caps hit or universal/session promotion.')
    append('audit/SEARCH_LOG.md','S014 continued selected-primary comparison: original October6.2 Hamiltonian necessity and6.7/6.8 path cover, Aprilp27 Hamiltonian iff/8.4 complete bipartite proof freshly read.82 preflight text cites6.5 in error; canonical audit corrects to6.2 with execution bytes preserved. No worldwide novelty/equivalence conclusion, PDF mirroring or contact.')
    append('tools/README.md','## S014 continuing implementation\n\nCAM02 family/Hall; CAM03 rays; CAM04 full thresholds; CAM05 swap; CAM06 split; CAM07 biptri; CAM08 book; CAM09 balanced; CAM10 AS paths; CAM11 matching; CAM12 arbitrary buffers; CAM13 firstfires/boundaries; CAM14 joinpaths: each has separate fixed input/preflight/certificate/checker records. See sessions/S014/MILESTONES.md. `s014_progress.py`/`s014_checkpoint.py` synchronize ACTIVE state without committing/closing. Execution-time proof bytes remain pinned; current adjudication is research/S014_LOCAL_PROOF_AUDIT.md.')
    current='S014 latest continuing update:19 campaigns complete;71-86 locally proved at exact scopes. Read research/S014_PARITY_AND_TRUE_HEAD_FRONTIER.md. Critical parity compression/local unit-Q ascent/endomorphic AS lifting have exact barriers; suitable parity-changing true-head domination remains UNPROVED. One CAM17 metadata failure and its separate passing repair are retained. Universal STACK/CLEAR OPEN, S014 IN_PROGRESS; no closeout/S015/later gates.'
    for p in ['authoritative/START_HERE.md','research/ROUTES.md','research/ASH_SPEC.md','research/PROBLEM_SPEC.md','research/ASHSTAR_ATTACK_BRIEF.md','authoritative/DECISION_LOG.md','docs/SESSION_LEDGER.md','docs/PHASE_GATE_LEDGER.md','docs/FAILURE_AND_LESSON_LEDGER.md','tools/README.md']:append(p,current)
    p=Path('authoritative/NEXT_SESSION_PROMPT.md');text=p.read_text(encoding='utf-8');needle='The following is the immutable prospective scope originally prepared by S013.'
    if current not in text:write(p,text.replace(needle,current+'\n\n'+needle))
    append('sessions/S014/AUDIT.md','Current continuation:85-86 complete proofs and CAM15-19 independent checks in research/S014_PARITY_AND_TRUE_HEAD_FRONTIER.md. One original CAM17 schema-reader failure is preserved with a separately hashed successful v2 repair. No mathematical cap/failure hidden; no full-session audit/closeout.')
    append('sessions/S014/CHECKPOINT.md','Hash authority within the ACTIVE session: evidence/S014/checkpoint_hashes.json is the earlier nonfinal checkpoint snapshot; evidence/S014/working_hashes.json supersedes its working-file hashes. Preregistration preflights and historical S003-S013 manifests remain immutable and are checked separately. Neither working snapshot closes S014.')
    s=read('authoritative/STATE.json');s['headline_detail']['assurance']='S014 complete local proofs71-86 and19 prior-hashed distinct-validator campaigns; one preserved schema implementation failure, separate passing repair. Independent human/kernel cold review pending. Universal STACK/CLEAR OPEN.';write('authoritative/STATE.json',s)
    if 'research_focus' in s['s014']:
        focus=s['s014']['research_focus'];block=Path(focus['document']).read_text(encoding='utf-8').rstrip()
        p=Path('authoritative/NEXT_SESSION_PROMPT.md');text=p.read_text(encoding='utf-8')
        start='<!-- OWNER_STACK_BRIDGE_FOCUS_START -->';end='<!-- OWNER_STACK_BRIDGE_FOCUS_END -->'
        rendered=start+'\n'+block+'\n'+end+'\n\n'
        if start in text:
            before,rest=text.split(start,1);_,after=rest.split(end,1)
            text=before+rendered+after.lstrip('\n')
        else:
            heading,rest=text.split('\n\n',1);text=heading+'\n\n'+rendered+rest
        assert text.encode().endswith(Path('sessions/S013/FUTURE_S014.md').read_bytes())
        write(p,text)
        append('sessions/S014/CHECKPOINT.md','Owner-directed current priority: '+focus['obligation']+' Read '+focus['document']+'. Earlier broad two-goal work allocation is superseded; archived plans and evidence remain unchanged.')
    files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for folder in ['sessions/S014','evidence/S014'] for p in Path(folder).rglob('*') if p.is_file() and p.name not in ['working_hashes.json','checkpoint_hashes.json','progress_checks.json']}
    files.update({p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('tools').glob('s014*.py')});files.update({p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in Path('research').glob('S014*.md')})
    write('evidence/S014/working_hashes.json',dict(status='ACTIVE_MUTABLE_CHECKPOINT_NOT_CLOSEOUT',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),files=files))
    print('S014 ACTIVE synchronized:71-86 locally proved,19 campaigns; no closeout/commit/PR or universal promotion.')
if __name__=='__main__':main()
