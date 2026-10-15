"""Synchronize current S012 mirrors; preserve all historical immutable bytes."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE='https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/main/'
def read(p):return (ROOT/p).read_text(encoding='utf-8')
def write(p,s):(ROOT/p).write_text(s,encoding='utf-8',newline='\n')
def load(p):return json.loads(read(p))
def save(p,o):write(p,json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def append(p,s):
    if s not in read(p):write(p,read(p).rstrip()+'\n\n'+s.rstrip()+'\n')

def main():
    sources=load('catalogue/sources.json')
    for s in sources:
        if s['id'] in {'SRC-0001','SRC-0002','SRC-0003','SRC-0036','SRC-0037'}:
            note=' S012 selected current PDF digest unchanged; exact inspected proof scopes/qualified dependency comparison in S012 primary report, no final novelty/kernel assurance.'
            if note not in s.get('note',''):s['note']=s.get('note','')+note
    for i,title,path,note in [(44,'S012 reciprocal insertion and CLEAR escape proofs','research/S012_UNIVERSAL_RESEARCH.md','59-62 exact proofs and boundaries; universal STACK/CLEAR OPEN; fresh challenge FUTURE S013.'),
      (45,'S012 selected primary and dependency comparison','research/S012_PRIMARY_AND_DEPENDENCY_COMPARISON.md','Known reflection/ancestry/cancellation/last-move/triangle/transport credited; precise equivalence unresolved.'),
      (46,'S012 exact reciprocal, escape and donor campaigns','evidence/S012','Three prior-hashed dual-validator campaigns, fixed boxes and full closures; no human/kernel/universal assurance.')]:
        sid=f'SRC-{i:04d}'
        if not any(s['id']==sid for s in sources):sources.append({'id':sid,'type':'LOCAL_RESEARCH_OR_EVIDENCE','title':title,'url':BASE.replace('/blob/','/tree/')+path if path.startswith('evidence/') else BASE+path,'access':'PROOF_INSPECTED','note':note})
    save('catalogue/sources.json',sources)
    write('catalogue/SOURCES.md','# Source catalogue - current after S012\n\nPer-proof access/attribution and exact equivalence uncertainty are scoped in primary reports.\n\n'+'\n\n'.join(f"- **{s['id']}** {s['title']} \u2014 **{s['access']}**. {s.get('url','')} \u2014 {s.get('note','')}".rstrip() for s in sources)+'\n')
    claims=load('catalogue/claims.json')
    for c in claims:
        if c['id'] in {f'CLM-{i:04d}' for i in range(94,100)}:c['cold_audit']='PASS_S012_AT_STATED_SCOPES'
    additions=[
      (103,'COMPUTED_EXACT','S012 cold challenge S01153-58 and needed dependencies survives stated scopes;12 unchanged check-only replays and S003-S011 frozen manifests pass. Fresh local audit/replay is not human/kernel certification.',['SRC-0044','SRC-0046']),
      (104,'PROGRAMME_PROVED','S01259 exact marked-input reciprocity x->kq iff x-e_w+(3-k)e_q->2w, x(w)>=1,k1/2; SAME-base TWO insertion D is symmetric, critical STACK D loopless/nonempty. No AS selection.',['SRC-0044']),
      (105,'PROGRAMME_PROVED','S01259a for NONZERO c exact R2(c+2q)=union over z~q R2(c+z), realized by moving the TWO inserted q tokens first. c=0 has separate terminal{q}. Initial omitted zero bit corrected, failed run retained.',['SRC-0044']),
      (106,'PROGRAMME_PROVED','S01260 exact unit/double donor languages: d1->1s iff c+s->2t;d1->2s iff c->2t;d2->1s iff c->1t;d2->2s iff c-s->1t. No adjacency needed for these ROOTED identities; no unrooted donor availability.',['SRC-0044']),
      (107,'PROGRAMME_PROVED','S01261 stackable CLEAR-loser history using ambient triangular edge or landing outside ORIGINAL R3 immediately becomes nonstackable. At criticality gap<=shortest forbidden length; gap1 allowed first move lands at critical STACK loser.',['SRC-0044','SRC-0001']),
      (108,'PROGRAMME_PROVED','S01261a exact partial path fuel bounds gap<=2^(d+1)-1 toward triangular site or2^d-1 outside originalR3 under stated source-fuel hypotheses;61b if gap>=2 and each triangle-edge-deleted component has<=1 nontriangular vertex, EVERY critical CLEAR loser is AS. Gap1/general target OPEN.',['SRC-0044','SRC-0001']),
      (109,'PROGRAMME_PROVED','S01262 for base b and nonempty LIST l_i with repeated labels allowed, exact predicate b+sum_{j!=i}e_lj->2l_i is independent of distinguished index. Fixed-graph occurrence symmetry, NOT threshold/AS-preserving gluing.',['SRC-0044']),
      (110,'COMPUTED_EXACT','CAM-S012-01 ten fixed boxes/175359 full configurations/16394311 exact relations;714 traces/5484 moves/69 full critical negative closures. Fixed triangular prism stack=clear8 and bridged_triangles12 through mass14, both independently full-mask checked; no atlas/universal claim.',['SRC-0046']),
      (111,'COMPUTED_EXACT','CAM-S012-02 all435 one-step barriers/15 critical inputs/1177 closure states/78 partial-fuel witnesses/338 moves. BFS/full-DAG exact tau agree; C5/F2 tau3>gap2 and triangle_tail2 tau7>gap6, no equality inferred.',['SRC-0046']),
      (112,'COMPUTED_EXACT','CAM-S012-03 all42 concentrating transfers,18 donor traces/116 moves,26 complete control negative closures/1177 states and18 whole-layer extrema.4 transfers lose/38 win; actual critical C5 unit donor CLEAR but double wins at OTHER roots, no double donor TWO in this sample. All bounded Q maxima AS, not universal.',['SRC-0046']),
      (113,'PROGRAMME_PROVED','S01259b assigned abstract C6 matching D01,23,45 satisfies actual-style symmetry/typing/self-root rules but empty common STACK intersection. NOT a graph/configuration realization; no ASH* evidence.',['SRC-0044'])]
    existing={c['id'] for c in claims}
    for i,status,claim,ss in additions:
        if f'CLM-{i:04d}' in existing:continue
        c={'id':f'CLM-{i:04d}','status':status,'claim':claim,'sources':ss}
        if status=='PROGRAMME_PROVED':c.update(cold_audit='FUTURE_S013',originality_assessment='KNOWN_PRIMITIVES_EXACT_REFINEMENT_EQUIVALENCE_UNRESOLVED_S012')
        claims.append(c)
    save('catalogue/claims.json',claims)
    write('catalogue/CLAIMS.md','# Claim catalogue - current after S012\n\nUniversal STACK/CLEAR OPEN; proof, finite computation, source access and novelty assurance separate.\n\n| ID | Status | Claim | Sources |\n|---|---|---|---|\n'+'\n'.join(f"| {c['id']} | {c['status']} | {c['claim'].replace('|',chr(92)+'|')} | {', '.join(c['sources'])} |" for c in claims)+'\n')
    detail={'research':'research/S012_UNIVERSAL_RESEARCH.md','prior_art':'research/S012_PRIMARY_AND_DEPENDENCY_COMPARISON.md','universal_stack':'OPEN','universal_clear':'OPEN','cold_s011_audit':'PASS_S012_AT_STATED_SCOPES','cold_new_proofs':'FUTURE_S013','formal_status':'NOT_STARTED','novelty':'KNOWN_PRIMITIVES_QUALIFIED_EXACT_REFINEMENTS_EQUIVALENCE_UNRESOLVED',
      'reciprocity':'PROGRAMME_PROVED marked-input k1/2 equivalence, symmetric actual TWO insertions, protected first move with zero bit, occurrence permutation; no AS-selection/gluing theorem',
      'donor_languages':'PROGRAMME_PROVED four exact unit/double donor root identities; unrooted root availability OPEN',
      'clear_barriers':'PROGRAMME_PROVED originalR3/triangular-edge whole-history escape, exact fuel bounds and componentwise conditional AS at gap>=2; gap1 OPEN',
      'finite_verification':{'configurations':175359,'exact_relations':16394311,'root_traces':714,'root_moves':5484,'critical_negative_closures':69,'one_step_escape_barriers':435,'escape_critical_inputs':15,'escape_closure_states':1177,'fuel_witnesses':78,'fuel_moves':338,'transfers':42,'donor_traces':18,'donor_moves':116,'control_negative_closures':26,'control_closure_states':1177,'global_Q_cases':18,'nonAS_Qmax':0,'new_fixed_graph_thresholds':{'triangular_prism':{'stack':8,'clear':8},'bridged_triangles':{'stack':12,'clear':12}},'symmetry':'none','inherited_cutoffs_unchanged':True}}
    for path in ['authoritative/STATE.json','research/ASH_SPEC.json']:
        data=load(path);data['s011']['cold_new_proofs']='PASS_S012_AT_STATED_SCOPES';data['s012']=detail
        if path.startswith('authoritative'):
            data.update(last_completed_session='S012',recommended_next_session='S013',as_of='2026-10-15',active_campaign=None)
            data['phases']['1']['note']='Universal STACK/CLEAR OPEN. S012 exact SAME-input reciprocity/donor languages/CLEAR escape restrictions do not establish global AS extremal selection.'
            data['source_inspection']='S012 five selected current PDF digests unchanged; original ordering/source repair and exact proof scopes inspected; qualified equivalence, no final novelty/kernel assurance.'
            data['owner_addendum']='Actual owner Run the next session selected and executed exactly S012 from live state, multiple internal milestones, no delegation. S013 and all final stages unexecuted.'
            data['next_session_context']='S013 strictly FUTURE/UNEXECUTED: cold-audit59-62, pursue global maximality with cross-base input languages and arbitrary-buffer comparison; separate CLEAR gap1/originalR3 extremizers.'
            data['headline_detail']['assurance']='S012 local hostile audit and three prior-hashed dual-validator campaigns; no independent human/kernel or universal-resolution assurance.'
            for key in ['critical_form_ASHstar_stack','critical_form_ASHstar_clear']:
                note='; S012 reciprocal input languages/donor identities/escape barriers, universal extremal comparison still OPEN'
                if note not in data['headline_detail'][key]:data['headline_detail'][key]+=note
            data['open_obligations']=['Fresh cold challenge S01259-62 and their complete dependency DAG before reuse; no human/kernel claim.',
              'Exploit actual cross-base input/output occurrence compatibility at GLOBAL largest Q-maximal losers, beyond symmetric typed masks and donor exceptions; all sites/leaf partitions/carries.',
              'Prove all-class arbitrary-buffer min-root integer-hole domination by maximal AS mass, including support/zero bits/positive representatives/carries.',
              'Resolve CLEAR gap1 inverse-shadow/protected-output comparison and general originalR3 triangle-free extremal domination; escape inequality alone is not equality.',
              'Prove true threshold/AS-preserving gluing or eligible equal-threshold simple quotient comparison, retaining full terminal demands and disjoint input.',
              'Or certify exact-g general critical loser and EVERY critical AS winner with two complete independent validators/certificates.',
              'S013 requires fresh owner invocation; Lean, registration, publication and correspondence deferred.']
        save(path,data)
    update='''## Current S012 authority - 2026-10-15

Earlier current/future sections are historical. Last S012, next S013 strictly FUTURE/UNEXECUTED. Universal critical STACK/CLEAR OPEN, printed PASS separate. S01153-58 cold challenge and12 needed check-only replays PASS; historical hashes/cutoffs retained. New59 exact marked-input reciprocity/symmetric TWO insertion and zero-bit protected first move,60 exact donor1/2 languages,61 whole-history originalR3/triangular escape/fuel/componentwise conditional AS at gap>=2,62 distinguished-output occurrence permutation are programme-proved at stated scopes. They do NOT establish global AS selection/gluing. Symmetric assigned C6 masks are not realized inputs; actual critical C5 unit donor exception and double transfer winning only at other roots expose missing root availability, not ASH*. Three prior-hashed dual-validator campaigns pass; two fixed n6 exact threshold controls8/8 and12/12 are computed only. Draft zero-base/donor interpretation failures retained/corrected. Read S012 research/primary/AUDIT/MILESTONES. Fresh new-proof cold challenge FUTURE S013; phases2-6 unchanged/deferred, no human/kernel or worldwide priority assurance. Actual outgoing integration IDs/jobs/main reread belong in S012 PR metadata.'''
    for path in ['authoritative/START_HERE.md','research/PROBLEM_SPEC.md','research/ASH_SPEC.md','research/ROUTES.md','research/ASHSTAR_ATTACK_BRIEF.md','README.md']:append(path,update)
    append('research/TREESTACK_BRIDGE.md','## S012 boundary\n\nEarlier TreeStack2609.31811v2/registered package remains credited; selected current PDF digest unchanged, no new Lean/registry build.59-62 concern exact general-graph input language consequences and CLEAR restrictions, not a rediscovered tree estimator or universal ASH* proof. Precise equivalence uncertainty retained in S012 primary comparison.')
    append('docs/PHASE_GATE_LEDGER.md','S012 review (2026-10-15): Universal Phase1 IN_PROGRESS separately STACK/CLEAR, printed PASS unchanged. S011 cold challenge PASS;59-62 reciprocal insertion/donor/escape/occurrence laws and three bounded dual-validator campaigns do not resolve global AS selection. Gap1/general integer-hole/gluing obligations survive. Fresh local review is not human/kernel assurance; new cold challenge FUTURE S013, phases2-6 unchanged/deferred.')
    append('docs/SESSION_LEDGER.md','| S012 | 2026-10-15 | Sustained cold challenge, actual SAME-input reciprocity/donor languages, whole-history CLEAR escape/fuel/component restriction and port occurrence symmetry; three precision campaigns | Universal STACK/CLEAR OPEN; old cutoffs retained; complete S013 FUTURE/UNEXECUTED, no final-stage action |')
    append('authoritative/DECISION_LOG.md','| 2026-10-15 S012 | Exact reciprocal TWO/root languages require real SAME-base compatibility; zero-base protected terminal bit mandatory; symmetric assigned C6 still not actual inputs | S01259/59a/59b/62 | Universal AS selection OPEN |\n| 2026-10-15 S012 | Keep GLOBAL Q scope and donor-root availability: actual C5 double transfer wins only elsewhere, no claimed donor-TWO coexistence | S01260/CAM03/retained_failures | Draft corrected, no ASH* failure |\n| 2026-10-15 S012 | Original R3 whole-history escape costs at least gap; gap1 and arbitrary triangle-free extremizers unresolved; component conditional AS retains gap>=2 | S01261/61a/61b | No gate advance |\n| 2026-10-15 S012 | Exactly S012, one atomic authored PR/non-force integration, complete S013 future only | INPUT/PLAN/CLOSEOUT | No delegation/final actions |')
    append('docs/FAILURE_AND_LESSON_LEDGER.md','| FL-S012-01 | Draft protected-TWO normal form omitted zero-base terminal and failed at K2 | Add explicit c0 bit; retain failed log/preflight, amend/hash both independent implementations before rerun |\n| FL-S012-02 | Premature donor interpretation claimed C5 double reaches TWO at donor | Complete masks show no donor ONE/TWO/THREE; double wins elsewhere. Corrected report/user commentary, retained failure. Unrooted win gives no donor availability |\n| FL-S012-03 | Symmetric typed/self-root masks or shortest escape inequality treated as universal bridge | Abstract C6 still has no common root; tau exceeds actual gap in finite controls. Neither proves AS selection |\n| FL-S012-04 | Root authority-path lookup and cp1252 source display errors | Use authoritative/ canonical paths and UTF-8 source display; neither failure is mathematical/source proof evidence |')
    append('audit/SEARCH_LOG.md','## S012 - 2026-10-15\n\nFive current selected primary digests unchanged; original SRC0036 ordering2.7/2.8-2.10 and October repair/monotonicity/+3 portions read at precise scopes. Dated limited reflection/reciprocity queries in primary_queries.json; exact known mechanisms/qualified equivalence in S012 primary report, no worldwide priority or source upgrade from metadata. Three separately prior-hashed precision campaigns, no inherited cutoff expansion/contact/final action.')
    append('campaigns/REGISTRY.md','## CAM-S012-01/02/03 - complete at registered exact scopes\n\nPLAN and amendments1-5 frozen before dependent computation; no symmetry,600s/2GB/300000-state limits.01 original eight boxes plus FIXED prism/bridged triangles masses0..14:175359 configurations/16394311 exact relations,714 traces/5484 moves/69 complete critical closures; full independent forward/reverse masks, exact8/8 and12/12 controls only. Initial zero-base omission failed and was corrected under amendment3; original preflight/log retained.02 same boxes:435 one-step barriers/15 critical full closures1177 states/78 fuel witnesses338 moves, independent BFS/DAG tau.03 same critical layers:42 transfers/18 traces116 moves/26 negative closures1177 states/18 whole-layer Q extrema, no nonAS Q maximum in bounded sample. No resource cutoff, old cutoff expansion, universal/human/kernel assurance or ASH* counterexample. Actual C5 double donor output absent; no false exception claim retained as result.')
    append('tools/README.md','## S012\n\n`s012_entry.py` records exact entry authority/old manifests and actual invocation; `s012_replay.py` logs12 unchanged needed checks. `s012_reciprocity.py` / independent `_verify.py` compare complete full root masks, all reciprocal/donor identities and exact critical closures. `s012_escape.py` / independent `_verify.py` compare whole-history barriers/BFS versus finite-DAG shortest escape and literal fuel. `s012_exceptions.py` / independent `_verify.py` compare actual critical transfers, global extrema, literal donor histories and complete negative closures. All SIX mathematical scripts support read-only `--check-only`; `s012_checks.py` runs bounded final replays with historical-byte guards. `s012_sources.py` stores selected metadata/temporary text only. `s012_closeout.py` updates current mirrors; `s012_hashes.py` covers immutable S012 bytes without self-hash. No universal or kernel test.')
    future=read('sessions/S012/FUTURE_S013.md');write('authoritative/NEXT_SESSION_PROMPT.md',future)
    close='''# S012 closeout - universal critical ASH* remains OPEN

Executed exactly S012 across multiple substantial internal milestones from the actual owner message Run the next session and live S011 handoff. No delegation, Lean, registration, publication or correspondence. STACK/CLEAR remain OPEN separately, printed PASS separate, Phase1 IN_PROGRESS and phases2-6 unchanged/deferred. S013 is strictly FUTURE/UNEXECUTED.

Entry live S011 PR13/head/main/tree/parents/actual five-job head/main runs reconciled; all refs/PRs/history/policies archived, no authority conflict. S003-S011 manifests pass with frozen S006/S007 indexes, historical bytes/cutoffs preserved. Original ordering dependency and53-58 survive cold challenge;12 needed check-only replays pass. Actual accessible invocation is archived separately from prospective scope; bounded plan and five amendments hashed before dependent computations.

59 proves exact marked-input k1/2 reciprocity and actual SAME-base symmetric TWO insertions;59a supplies protected TWO first-move normal form with indispensable zero-base terminal bit.60 gives four exact unit/double donor root identities.61 supplies full-history triangular/originalR3 escape, explicit partial-fuel bounds and a componentwise conditional AS result retaining gap>=2.62 proves distinguished-output occurrence permutation in fixed-graph boundary languages. Complete proofs/quantifiers/boundaries/dependency DAG/distinct hostile pass in research/AUDIT; known primitives attributed, equivalence/novelty uncertainty retained.

Three prior-hashed distinct-validator campaigns pass:01 all175359 configurations/16394311 exact relations/714 traces5484 moves/69 full critical negative closures; fixed prism8/8 and bridged-triangles12/12 exact controls through14.02 all435 one-step barriers/15 critical inputs1177 closure states/78 fuel witnesses338 moves with exact BFS/DAG tau.03 all42 concentrating transfers/18 traces116 moves/26 negative closures1177 states/18 full critical-layer extrema. Four transfers lose,38 win; bounded Q maxima AS, no universal inference. No resource cap or old cutoff expansion. Failed zero-base formula, premature donor interpretation, source display and initial root-path lookups retained/corrected.

Universal synthesis: actual symmetric D excludes the old directed abstract C5 pattern, but symmetric typed/self-root C6 masks still permit empty common roots and are NOT realized common inputs. Actual critical C5 unit transfer clears at donor while double wins only elsewhere; criticality alone does not supply donor-root witnesses, and this cQ19 is below AS global Q27. Arbitrary-buffer integer-hole domination/global Q selection remain open. CLEAR originalR3 escape inequality is strict in named controls; gap1 and arbitrary triangle-free extremizers remain. Fixed-input occurrence symmetry does not prove threshold/AS-preserving gluing or equal-threshold quotient existence. No complete universal proof or certified ASH* disproof; no gate promotion. Fresh local audit/different code is not independent human/kernel certification.

All current state/spec/catalogue/decision/failure/session/gate/search/campaign/tool mirrors and immutable hashes synchronized. ONE branch session/S012-critical-extremal-bridge, ONE atomic authored session commit, ordinary PR and non-force two-parent merge if allowed. Actual outgoing head/tree/parents/jobs/checks/merge/main reread are recorded in PR metadata, never invented committed self-hashes. Stop before S013/all deferred final actions. Full self-contained next handoff copied identically below and into authoritative/NEXT_SESSION_PROMPT.md.

## COMPLETE FUTURE handoff - NOT executed

'''
    write('sessions/S012/CLOSEOUT.md',close+future)
    print('Current S012 mirrors synchronized; historical bytes untouched.')

if __name__=='__main__':main()
