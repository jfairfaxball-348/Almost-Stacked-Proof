"""Synchronize current S011 mirrors; immutable S003-S010 evidence is untouched."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE='https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/main/'

def read(p):return (ROOT/p).read_text(encoding='utf-8')
def write(p,s):(ROOT/p).write_text(s,encoding='utf-8',newline='\n')
def load(p):return json.loads(read(p))
def save(p,x):write(p,json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def append(p,s):
    if s not in read(p):write(p,read(p).rstrip()+'\n\n'+s.rstrip()+'\n')

def main():
    sources=load('catalogue/sources.json');by={s['id']:s for s in sources}
    for sid in ['SRC-0001','SRC-0002','SRC-0003','SRC-0036','SRC-0037']:
        note=' S011 current selected PDF digest unchanged; precise proof scope/comparison in S011 primary report, no worldwide priority or final-stage assurance.'
        if note not in by[sid].get('note',''):by[sid]['note']=by[sid].get('note','')+note
    extra=[(41,'S011 exact terminal transport and universal bridge','research/S011_UNIVERSAL_RESEARCH.md','53-58 exact scopes/proofs; universal STACK/CLEAR OPEN; cold fresh-session challenge FUTURE S012.'),
           (42,'S011 selected primary and dependency comparison','research/S011_PRIMARY_AND_DEPENDENCY_COMPARISON.md','Known grammar/ancestry/signed3/+3/triangle primitives credited; exact refinements and equivalence uncertainty scoped.'),
           (43,'S011 registered root and terminal transport certificates','evidence/S011','Three prior-hashed campaigns with separately written complete validators; no universal/human/kernel assurance.')]
    for i,title,path,note in extra:
        url=BASE+path if not path.startswith('evidence/') else BASE.replace('/blob/','/tree/')+path
        existing=next((s for s in sources if s['id']==f'SRC-{i:04d}'),None)
        if existing:existing['url']=url
        else:sources.append({'id':f'SRC-{i:04d}','type':'LOCAL_RESEARCH_OR_EVIDENCE','title':title,'url':url,'access':'PROOF_INSPECTED','note':note})
    save('catalogue/sources.json',sources)
    write('catalogue/SOURCES.md','# Source catalogue \u2014 current after S011\n\nPer-proof access is scoped in the primary comparison reports; no unseen proof or kernel assurance inferred.\n\n'+'\n\n'.join(f"- **{s['id']}** {s['title']} \u2014 **{s['access']}**. {s.get('url','')} \u2014 {s.get('note','')}".rstrip() for s in sources)+'\n')
    claims=load('catalogue/claims.json');ids={c['id'] for c in claims}
    for c in claims:
        if c['id'] in {f'CLM-{i:04d}' for i in range(81,89)}:c['cold_audit']='PASS_S011_AT_STATED_SCOPES'
    new=[
      (93,'COMPUTED_EXACT','S011 cold challenge S01044-52 survives stated scopes; all25 unchanged check-only commands and historical manifests PASS. Fresh local review/replay is not independent human/kernel certification.',['SRC-0041','SRC-0043']),
      (94,'PROGRAMME_PROVED','S01153 prescribed nonempty terminal vector f: exact count chronology iff c=f+2out-in and every used label reaches supp(f). Direct known reverse-grammar arbitrary-pending specialization; no rootless forest.',['SRC-0041','SRC-0036']),
      (95,'PROGRAMME_PROVED','S01154 a3-output certificate re-roots to EVERY used label by simple positive path reversal, including empty transit sites; ANY positive used edge can be exposed as exact terminal2u+2v with all inputs consumed.',['SRC-0041','SRC-0036']),
      (96,'PROGRAMME_PROVED','S01155/55a: stackable CLEAR loser has all occupied deletions reaching2 at their sites and every3-witness avoids ambient triangular edges. If clear>=stack+2, critical heavy sites lie on no triangle; if every vertex lies on a triangle, clear<=stack+1. With<=1 nontriangular vertex and gap>=2 ASH*-CLEAR follows conditionally. Gap1/general target open.',['SRC-0041','SRC-0001']),
      (97,'PROGRAMME_PROVED','S01156 bipartite critical STACK insertion CLEAR roots lie in the insertion part, hence common CLEAR root over ALL sites impossible, including non-AS inputs/empty sites. Common STACK roots remain separate; no bipartite CLEAR threshold.',['SRC-0041','SRC-0002']),
      (98,'PROGRAMME_PROVED','S01157 d=c-ae_s+ae_t reaching k at donor s gives c->(k+a-3)s+(3-a)t for a1/2,k+a>=3 via exact path reversal. Adjacent STACK criterion excludes a1k1 and a2k2; donor2/changing terminal types handled conditionally, unrooted root coverage open.',['SRC-0041','SRC-0036']),
      (99,'PROGRAMME_PROVED','S01158 mass>=2 exact CLEAR roots=N(exactTWO roots), STACK roots=R1 unionR2 unionR3. Winning STACK-loser insertion has nonempty D_w=R2 excluding w,R3 empty,C_w=N(D_w),S_w=D_w unionC_w. Actual input compatibility not encoded by assigned root sets.',['SRC-0041','SRC-0001']),
      (100,'COMPUTED_EXACT','CAM-S011-01 all90 layers/97839 explicit inputs;3416 winning insertions/4418 occupied deletions;4883 literal traces/43286 moves/15 selected negative closures.884 noncritical own-root failures each goal,3 critical common CLEAR root failures,10 C5 nonbipartiteR3 CLEAR losers; no ASH* failure.',['SRC-0043']),
      (101,'COMPUTED_EXACT','CAM-S011-02 all116401 exact terminal transport certificates/507217 moves,65164 adjacent pair checks/6978 exceptional(1,1) outcomes,24894 triangle repairs/12 critical CLEAR cuts. Actual C5 odd-cycle3-support c=(4,1,1,1,1) has70-state closed CLEAR-negative reachability and all3 roots. Not critical ASH* failure.',['SRC-0043']),
      (102,'COMPUTED_EXACT','CAM-S011-03 all97798 mass>=2 root identities/120 critical STACK insertion root families/23 critical CLEAR cases(15 stackable)/10 bipartite checks. Explicit abstract C5 typed/self-root family has empty common STACK intersection, NOT claimed graph/configuration realization.',['SRC-0043'])]
    for i,status,claim,src in new:
        if f'CLM-{i:04d}' not in ids:
            row={'id':f'CLM-{i:04d}','status':status,'claim':claim,'sources':src}
            if status=='PROGRAMME_PROVED':row.update(cold_audit='FUTURE_S012',originality_assessment='KNOWN_PRIMITIVES_EXACT_REFINEMENT_EQUIVALENCE_UNRESOLVED_S011')
            claims.append(row)
    save('catalogue/claims.json',claims)
    write('catalogue/CLAIMS.md','# Claim catalogue - current after S011\n\nUniversal STACK/CLEAR remain OPEN. Programme proofs, bounded computation, source access and originality are separate.\n\n| ID | Status | Claim | Sources |\n|---|---|---|---|\n'+'\n'.join(f"| {c['id']} | {c['status']} | {c['claim'].replace('|',chr(92)+'|')} | {', '.join(c['sources'])} |" for c in claims)+'\n')
    detail={'research':'research/S011_UNIVERSAL_RESEARCH.md','prior_art':'research/S011_PRIMARY_AND_DEPENDENCY_COMPARISON.md',
        'universal_stack':'OPEN','universal_clear':'OPEN','cold_s010_audit':'PASS_S011_AT_STATED_SCOPES','cold_new_proofs':'FUTURE_S012','formal_status':'NOT_STARTED',
        'novelty':'KNOWN_PRIMITIVES_QUALIFIED_EXACT_REFINEMENTS_NO_WORLDWIDE_PRIORITY',
        'exact_terminal_transport':'PROGRAMME_PROVED nonempty arbitrary final forest;3-root/any-used-edge exposure;donor1/2 conditional terminal transport',
        'critical_tree_roots':'PROGRAMME_PROVED typed CLEAR/TWO roots and bipartite common-CLEAR obstruction; SAME-input compatibility/AS selection OPEN',
        'clear_extremizers':'PROGRAMME_PROVED deletion-to2/triangle-free3 histories;gap>=2 heavy-site restriction;gap1 and arbitrary triangle-free bridge OPEN',
        'finite_verification':{'tree_layers':90,'tree_configurations':97839,'winning_insertions':3416,'occupied_deletions':4418,'tree_literal_traces':4883,'tree_moves':43286,
          'negative_closures':15,'transport_certificates':116401,'transport_moves':507217,'adjacent_pairs':65164,'exceptional_terminal_pairs':6978,
          'triangular_repairs':24894,'critical_triangle_cuts':12,'root_identity_inputs':97798,'critical_root_insertions':120,'critical_clear_cases':23,'stackable_critical_clear':15,
          'symmetry':'none','new_threshold_claims':0,'inherited_cutoffs_unchanged':True}}
    for p in ['authoritative/STATE.json','research/ASH_SPEC.json']:
        data=load(p);data['s010']['cold_new_proofs']='PASS_S011_AT_STATED_SCOPES';data['s011']=detail
        if p.startswith('authoritative'):
            data.update(last_completed_session='S011',recommended_next_session='S012',as_of='2026-10-15',active_campaign=None)
            data['phases']['1']['note']='Universal STACK/CLEAR OPEN. S011 exact terminal transport/root typing and critical CLEAR triangle restrictions do not prove all-class AS selection; independent universal gate unpassed.'
            data['source_inspection']='S011 selected current April/October/TreeStack/grammar/Parikh PDF digests unchanged; exact proof scopes/comparisons retained, no final novelty or kernel assurance.'
            data['owner_addendum']='Explicit S011 invocation and implementation request executed exactly S011 across multiple milestones; S012 and all final stages remain unexecuted.'
            data['next_session_context']='S012 strictly FUTURE/UNEXECUTED: cold-audit53-58, then actual SAME-input insertion compatibility/integer-hole comparison and separate CLEAR gap1/triangle-free extremizers.'
            data['headline_detail']['assurance']='S011 fresh local hostile audit and three prior-hashed dual-validator campaigns; no independent human/kernel or universal-resolution assurance.'
            for key in ['critical_form_ASHstar_stack','critical_form_ASHstar_clear']:
                note='; S011 exact terminal transport/root typing/critical restrictions, universal comparison still OPEN'
                if note not in data['headline_detail'][key]:data['headline_detail'][key]+=note
            data['open_obligations']=['Cold-challenge S01153-58 and original ordering dependency before reuse; no independent human/kernel claim.',
                'Prove actual SAME-input compatibility beyond typed insertion root masks and57 exceptional donor-root/pile types; all sites/donor2/carries/three-mark reconstruction.',
                'Prove all-class arbitrary-buffer min-root integer-hole domination by maximal AS mass, retaining zero/support/positive representative/carry cases.',
                'Resolve separate CLEAR gap1/protected output and gap>=2 triangle-free used-component extremal comparison; stackable inputs are outside51.',
                'Prove true threshold/AS-preserving cyclic gluing or eligible simple quotient equality; representation/strict quotient drop alone is insufficient.',
                'Or certify exact-g general critical loser plus EVERY critical AS winner with two complete independent validators/certificates.',
                'S012 requires fresh owner invocation. All Lean, registration, publication and correspondence remain deferred.']
        save(p,data)
    update='''## Current S011 authority - 2026-10-15

Earlier current/future sections are historical. Last S011, next S012 strictly FUTURE/UNEXECUTED. Universal critical STACK/CLEAR OPEN, printed PASS separate. S01044-52 cold challenge and25 inherited check-only replays PASS at stated scopes with old bytes/cutoffs retained. New53 nonempty terminal-vector forest,54 three-output used-label re-root/edge exposure,55 stackable CLEAR deletion/triangle-free history and gap>=2 heavy-site restriction,56 bipartite common CLEAR root obstruction,57 donor1/2 exact terminal transport,58 CLEAR/TWO root typing are programme-proved at explicit scopes. They do NOT provide global AS selection. Actual C5 odd-cycle3-witness can still fail clearing; abstract typed/self-root families can lack common STACK roots and are NOT actual configuration counterexamples. Three registered dual-validator campaigns pass; no universal/human/kernel or priority assurance. Read S011 research/primary/AUDIT/MILESTONES. New proof cold challenge FUTURE S012; phases2-6 unchanged/deferred. Actual outgoing integration IDs/jobs/main reread belong in S011 PR metadata.'''
    for p in ['authoritative/START_HERE.md','research/PROBLEM_SPEC.md','research/ASH_SPEC.md','research/ROUTES.md','research/ASHSTAR_ATTACK_BRIEF.md','README.md']:append(p,update)
    append('research/TREESTACK_BRIDGE.md','## S011 boundary\n\nTreeStack currentv2 digest unchanged and earlier nontrivial-tree equality/registered package credited; no Lean/registry build. Known exact ancestry/scheduling/last-move/+3 primitives remain prior. S011 exact terminal/cyclic transport is not a new tree estimator or universal ASH* proof. Precise equivalence uncertainty remains in the S011 primary report.')
    append('docs/PHASE_GATE_LEDGER.md','S011 review (2026-10-15): Universal Phase1 IN_PROGRESS separately STACK/CLEAR; printed PASS unchanged. S010 cold challenge PASS;53-58 exact transport/root typing/critical CLEAR restrictions and three dual-validator campaigns do not resolve universal AS selection. Fresh local adversarial review/replay is not independent human/kernel assurance. New proof audit FUTURE S012; phases2-6 remain unchanged/deferred.')
    append('docs/SESSION_LEDGER.md','| S011 | 2026-10-15 | Sustained cold challenge, exact terminal/three-root/small-transfer reconstruction, typed insertion roots and separate CLEAR triangle restrictions; three registered dual-validator campaigns and synthesis | Universal STACK/CLEAR OPEN; no old cutoff expansion; complete S012 FUTURE/UNEXECUTED, no final-stage activity |')
    append('authoritative/DECISION_LOG.md','| 2026-10-15 S011 | Preserve exact terminal roots/piles: bipartite common CLEAR root impossible, assigned typed root masks insufficient; donor1/2 reconstruction remains conditional on root/pile and actual input compatibility | S01153-58, AUDIT/MILESTONES | Universal ASH* OPEN; no gate advance |\n| 2026-10-15 S011 | CLEAR stackable extremizers use deletion-to2/triangle-free3-witness and gap>=2 heavy-site restrictions; never import51 or solve gap1 by dropping its hypothesis | S01155/55a | Conditional tools only |\n| 2026-10-15 S011 | Actual invocation/hashed bounded plans and three exact precision campaigns; historical hashes/cutoffs unchanged; complete S012 strictly future | S011 INPUT/PLAN/CLOSEOUT | Stop before S012/final stages |')
    append('docs/FAILURE_AND_LESSON_LEDGER.md','## S011 retained failures and missing implications\n\nBipartite common CLEAR insertion root is impossible universally (signed0 plus singleton part). Dropping criticality produces884 occupied self-root failures in each goal in the registered box. C5 c=(1,1,1,2,2) and(4,1,1,1,1) have all3 roots but cannot clear; the latter has an actual whole odd-cycle3-certificate, so non-bipartite support is insufficient. Abstract C5 typed/self-root sets need not have common STACK root; they are not graph-realized counterexamples. Small-transfer a2,k2 leaves(1,1), and nonadjacent two-output paths cannot be treated as K2. None refutes ASH*. Invocation extractor initially assumed absent event_msg user records; repaired to read actual response_item text. A temporary primary-text console display hit Windows encoding; UTF-8 display repaired, source bytes unchanged. No mathematical campaign implementation/resource failure. Full logs/limits retained.')
    append('audit/SEARCH_LOG.md','## S011 - 2026-10-15\n\nCurrent primary Aprilv1/Octoberv1/TreeStackv2/grammarv3/Parikh selected digests refreshed unchanged, original ordering/collapse and source signed3/ancestry/triangle repair/monotonicity checked at stated scopes. Dated targeted queries and exact-result comparisons in research/S011_PRIMARY_AND_DEPENDENCY_COMPARISON.md; qualified refinements/equivalence only, no worldwide priority. Three separately prior-hashed precision campaigns, no atlas/old-cutoff expansion. No contact/final action.')
    append('campaigns/REGISTRY.md','## CAM-S011-01/02/03 - completed within exact registered scopes\n\nPLAN and Amendments1-3 hashed BEFORE computation, independent forward/reverse/count chronology validators, no symmetry,600s/300000-state/2GB caps.01 eight fixed graphs at inherited maximal masses:90 layers/97839 inputs/3416 winning insertions/4418 deletion checks,4883 traces/43286 moves/15 selected complete negative closures.02 frozen S010 count traces plus one explicit C5 cycle:116401 terminal certificates/507217 moves/65164 adjacent pair checks/6978 exceptional(1,1) outcomes/24894 triangle repairs/12 critical CLEAR cuts; C5 negative closure70 states.03 frozen01 layers:97798 mass>=2 root identities/120 critical insertions/23 CLEAR critical cases(15 stackable)/10 bipartite checks, assigned abstract C5 obstruction expressly NOT graph-realized. No new threshold/universal/human/kernel claim or old cutoff expansion. Exact plans/code/input/output/environment/log hashes in S011 immutable manifest.')
    append('tools/README.md','## S011\n\n`s011_entry.py` archives actual live authority/invocation and immutable history; `s011_replay.py` logs25 unchanged inherited checks. `s011_trees.py` / independent `s011_trees_verify.py` validate complete exact root masks/tree compatibility. `s011_transport.py` / independent `s011_transport_verify.py` validate prescribed terminal-vector transport via connected counts versus full chronological recursion and literal repairs/closures. `s011_root_types.py` / independent `s011_root_types_verify.py` validate exact root normalization and critical classifications. All SIX mathematical scripts support read-only `--check-only`. `s011_run.py` freezes per-campaign code/input preflights then logs bounded sequential execution; `s011_sources.py` fetches selected primary metadata with temporary text only. `s011_closeout.py` updates current mirrors, `s011_hashes.py` hashes immutable S011 without self-hash, `s011_checks.py` replays six new checks. No universal or kernel certification.')
    future=read('sessions/S011/FUTURE_S012.md');write('authoritative/NEXT_SESSION_PROMPT.md',future)
    close='''# S011 closeout - universal critical ASH* remains OPEN

Executed exactly S011 locally across substantial internal milestones, no delegation. STACK/CLEAR remain OPEN separately, printed-form PASS separate, phases2-6 unchanged/deferred. No Lean, registration, manuscript/publication or correspondence. Actual owner invocation/implementation request archived separately from the older prospective prompt, bounded plan and three campaign amendments hashed before computation.

Live S010 PR12/head/tree/parents and actual hosted jobs reconciled; all branch/PR/history/policy evidence archived, zero-context pending correctly distinguished from jobs. Old S003-S010 manifests pass with frozen S006/S007 indexes; no historical evidence bytes/hashes or cutoffs changed. Original grammar ordering dependency and44-52 survive fresh challenge at stated scopes, all25 inherited check-only replays PASS. Fresh local review/replay is not independent human/kernel certification.

Research continued through53 exact nonempty arbitrary terminal forest,54 three-output used-label root transport/ANY-edge exposure,55 stackable CLEAR deletion-to2/triangle-free witness and55a critical gap>=2 heavy-site restrictions,56 universal bipartite common CLEAR root obstruction,57 donor1/2 terminal transport and exact donor-root exceptions,58 CLEAR/TWO insertion-root typing. Conditional CLEAR AS scope with<=1 nontriangular vertex retains the threshold-gap>=2 hypothesis; gap1/general triangle-free graph bridge remains OPEN. Every result's complete proof/quantifiers/limits and dependency chain are in S011 research/AUDIT; primary mechanisms attributed and qualified equivalence uncertainty retained.

Three registered independent-validator campaigns complete:01 all90 layers/97839 inputs/4883 literal traces/43286 moves;02 all116401 terminal transport certificates/507217 moves,65164 adjacent pairs/6978 exceptional terminals/24894 triangular repairs/12 critical cuts;03 all97798 positive-layer root identities/120 critical insertions/23 critical CLEAR cases(15 already stackable)/10 bipartite checks. C5 actual odd-cycle3-support configuration has a70-state complete CLEAR-negative closure and all3 roots, rejecting auxiliary support sufficiency, not ASH*. An assigned abstract C5 root family satisfies exact typing/self-root rules but has no common STACK root; it is NOT a common-input graph realization. Exact scopes/failure classes/logs/hashes retained; no resource cutoff or mathematical campaign implementation failure.

Synthesis: exact transport handles full input/terminal demand but does not ensure a global extremal witness supplies the needed root/pile/counts. Root typing cannot replace SAME-input leaf compatibility; B's all-class integer-hole domination remains unproved, C needs protected-output gap1 and triangle-free-component extremal comparison, D needs genuine threshold/AS-preserving gluing/equal-threshold quotient. No universal proof or fully certified ASH* counterexample obtained, so Phase1 stays IN_PROGRESS. Strongest scopes/ranked next decisive tests in MILESTONES; new proof cold challenge is FUTURE S012.

All current authority/spec/catalogue/decision/failure/session/gate/search/campaign/tool mirrors and immutable S011 hashes updated, historical bytes preserved. One branch session/S011-critical-insertion-trees, ONE atomic authored commit and ordinary PR, non-force two-parent merge if permitted. Actual outgoing head/tree/parents/jobs/merge/main reread belong in PR metadata, not invented committed self-hashes. Full complete ambitious S012 is copied verbatim below and into the next mirror, strictly FUTURE/UNEXECUTED. Stop before S012 and every deferred final action.

## COMPLETE FUTURE handoff - NOT executed

'''
    write('sessions/S011/CLOSEOUT.md',close+future)
    print('S011 current mirrors synchronized; universal OPEN; S012 future only.')

if __name__=='__main__':main()
