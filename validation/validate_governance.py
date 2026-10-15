#!/usr/bin/env python3
"""Fail-closed governance mirror/integrity checks (updated S012); not a mathematics or Lean test."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

state = load("authoritative/STATE.json")
claims = load("catalogue/claims.json")
sources = load("catalogue/sources.json")
assert state["headline_status"] == "PRINTED_ASH_REFUTED_COLD_AUDIT_PASS_CRITICAL_FORM_OPEN"
assert state["last_completed_session"] == "S012"
assert state["recommended_next_session"] == "S013"
assert state["phases"]["0"]["status"] == "PASS"
assert state["phases"]["1"]["status"] == "IN_PROGRESS"
assert all(state["phases"][str(i)]["status"] != "PASS" for i in range(2, 7))
assert state["active_campaign"] is None
assert state["counterexample_status"] == "PRINTED_FORM_CERTIFIED_COLD_AUDIT_PASS_LEAN_PENDING"
assert state["lean_status"] == "NOT_STARTED"
assert state["palomar_status"] == "NOT_SUBMITTED"
assert state["arxiv_project_status"] == "NOT_SUBMITTED"
assert len({c["id"] for c in claims}) == len(claims)
assert len({s["id"] for s in sources}) == len(sources)
claim_status = {"SOURCE_STATED","PROGRAMME_PROVED","COMPUTED_EXACT",
                "HEURISTIC","FORMALLY_CERTIFIED","INHERITED_UNVERIFIED"}
source_status = {"METADATA_ONLY","ABSTRACT_INSPECTED","STATEMENT_INSPECTED",
                 "PROOF_INSPECTED","SECONDARY_ONLY"}
source_ids = {s["id"] for s in sources}
for s in sources:
    assert re.fullmatch(r"SRC-\d{4}", s["id"]) and s["access"] in source_status
for c in claims:
    assert re.fullmatch(r"CLM-\d{4}", c["id"]) and c["status"] in claim_status
    assert set(c["sources"]) <= source_ids
sources_md = (ROOT / "catalogue/SOURCES.md").read_text(encoding="utf-8")
claims_md = (ROOT / "catalogue/CLAIMS.md").read_text(encoding="utf-8")
for sid in source_ids:
    assert sid in sources_md
for c in claims:
    assert c["id"] in claims_md
next_prompt = (ROOT / "authoritative/NEXT_SESSION_PROMPT.md").read_text(encoding="utf-8")
assert "S013" in next_prompt and "FUTURE, UNEXECUTED" in next_prompt
for sess in ("S001", "S002", "S003", "S004"):
    assert (ROOT / f"sessions/{sess}/CLOSEOUT.md").exists()
print("Governance structure and mirrors: PASS (administrative only; no ASH or Lean verification).")

assert (ROOT / "research/ASH_SPEC.json").exists()
assert (ROOT / "sessions/S002/PLAN.md").exists()
assert (ROOT / "research/S002_ASH_FOUNDATION_AND_ATTACK.md").exists()

assert (ROOT / "sessions/S003/PLAN.md").exists()
assert (ROOT / "research/S003_AS_GAP_AND_ATTACKS.md").exists()
assert (ROOT / "research/S003_SOURCE_RECONCILIATION.md").exists()
# S003 evidence integrity: every hash line in evidence/S003/HASHES.md must match the file.
checked = 0
for line in (ROOT / "evidence/S003/HASHES.md").read_text(encoding="utf-8").splitlines():
    m = re.fullmatch(r"`([0-9a-f]{64})`\s+`([^`]+)`.*", line.strip().lstrip("- "))
    if m and not m.group(2).startswith("scratch:"):
        digest = hashlib.sha256((ROOT / m.group(2)).read_bytes()).hexdigest()
        assert digest == m.group(1), (m.group(2), digest)
        checked += 1
assert checked >= 10, checked
print(f"S003 evidence hashes: {checked} files match.")

# The earlier 2026-10-13 correspondence remains distinct from actual S004 execution.
assert (ROOT / "outreach/2026-10-csernak-soukup/2026-10-13_AUTHOR_REPLY.md").exists()
assert (ROOT / "outreach/2026-10-csernak-soukup/reply_draft_2026-10-13.txt").exists()
assert (ROOT / "research/ASHSTAR_ATTACK_BRIEF.md").exists()
assert "S013" in next_prompt and "FUTURE, UNEXECUTED" in next_prompt
assert state["correspondence"]["authority"] == "AUTHOR_REPORTED_INTENDED_MEANING_NOT_PUBLISHED_ERRATUM"
assert state["correspondence"]["next_reply"] == "DRAFT_NOT_SENT"
assert any(x["id"] == "SRC-0010" and x["type"] == "PERSONAL_COMMUNICATION_OWNER_SUPPLIED" for x in sources)
assert all(any(x["id"] == claimid and x["status"] == "SOURCE_STATED" for x in claims) for claimid in ("CLM-0028", "CLM-0029"))
assert (ROOT / "sessions/S004/CLOSEOUT.md").exists()
print("Author correspondence provenance and unexecuted S013 handoff: PASS (administrative only).")

# S004 scope and machine mirrors: printed PASS must never promote universal ASH*.
assert state["printed_form_phase1"]["status"] == "PASS"
spec=load("research/ASH_SPEC.json")
assert spec["literal_form"]["status"] == "FALSE_CERTIFIED_COLD_AUDIT_PASS_LEAN_PENDING"
assert spec["critical_form"]["status"] == "OPEN"
assert spec["s004"]["universal_stack"] == spec["s004"]["universal_clear"] == "OPEN"
assert state["independent_atlas_n7"]["stack"] == {"complete":853,"total":853}
assert state["independent_atlas_n7"]["clear"] == {"complete":809,"total":809}
plan=(ROOT/"sessions/S004/PLAN.md").read_bytes()
assert hashlib.sha256(plan).hexdigest() == (ROOT/"sessions/S004/PLAN.sha256").read_text(encoding="utf-8").split()[0]
for name in ("INPUT.md","PLAN.md","AUDIT.md","CLOSEOUT.md"):
    assert (ROOT/"sessions/S004"/name).is_file()
assert (ROOT/"sessions/S005/AUTHORISED_PROMPT.md").read_text(encoding="utf-8") in (ROOT/"sessions/S004/CLOSEOUT.md").read_text(encoding="utf-8")
checked4=0
for line in (ROOT/"evidence/S004/HASHES.md").read_text(encoding="utf-8").splitlines():
    m=re.fullmatch(r"`([0-9a-f]{64})`\s+`([^`]+)`",line.strip())
    if m:
        assert hashlib.sha256((ROOT/m.group(2)).read_bytes()).hexdigest()==m.group(1),m.group(2)
        checked4+=1
assert checked4>=50,checked4
rows=load("evidence/S004/frontier_summary.json")
verification=load("evidence/S004/frontier_verification.json")
assert len(rows)==len(verification)==21
byfile={r["file"]:r for r in verification}
import lzma
for r in rows:
    path=f"evidence/S004/{r['graph']}_{r['mode']}.json.xz"
    v=byfile[path]
    assert v["threshold"]==r["threshold"]
    assert v["layers"]==r["rows"][-1]["t"]
    data=json.loads(lzma.decompress((ROOT/path).read_bytes()))
    assert data["n"]==r["n"] and data["edges"]==r["edges"] and data["mode"]==r["mode"]
    assert hashlib.sha256(lzma.decompress((ROOT/path).read_bytes())).hexdigest()==r["layer_sha256"]
    if r["threshold"]:
        assert tuple(r["critical_as_witness"]) in {tuple(c) for c in data["layers"][-2]}
        assert sum(r["critical_as_witness"])==r["threshold"]-1
        assert sum(x>1 for x in r["critical_as_witness"])<=1
        assert not data["layers"][-1]
assert sum(r["scope"]=="EXACT_THRESHOLD" for r in rows)==19
assert sum(r["graph"].startswith("A7_") and r["mode"]=="stack" for r in rows)==8
assert sum(r["graph"].startswith("A7_") and r["mode"]=="clear" for r in rows)==3
assert all(r["all_agree"] for r in load("evidence/S004/base_verification.json"))
assert sum(r["independent_set_root_tests"] for r in load("evidence/S004/independent_witness_tests.json"))==233
print(f"S004 scope, complete certificate metadata and {checked4} hashes: PASS (no universal or Lean certification).")

# S005 precise completed scopes and full metadata closure.
assert spec["s005"]["universal_stack"] == spec["s005"]["universal_clear"] == "OPEN"
assert (ROOT/"sessions/S006/AUTHORISED_PROMPT.md").read_text(encoding="utf-8") in (ROOT/"sessions/S005/CLOSEOUT.md").read_text(encoding="utf-8")
for name in ("PLAN","PLAN_AMENDMENT_1","PLAN_AMENDMENT_2","PLAN_AMENDMENT_3","PLAN_AMENDMENT_4","PLAN_AMENDMENT_5","PLAN_AMENDMENT_6","PLAN_AMENDMENT_7"):
    assert hashlib.sha256((ROOT/f"sessions/S005/{name}.md").read_bytes()).hexdigest() == (ROOT/f"sessions/S005/{name}.sha256").read_text(encoding="utf-8").split()[0]
for name in ("INPUT.md","AUDIT.md","CLOSEOUT.md","CONTINUATION.md","AUTHORISED_PROMPT.md"):
    assert (ROOT/"sessions/S005"/name).exists()
rows5=load("evidence/S005/campaign_summary.json")
v5=load("evidence/S005/verification.json")
assert len(rows5)==len(v5)==len(load("evidence/S005/graphs.json"))
by5={r["file"]:r for r in v5}
for r in rows5:
    path=f"evidence/S005/{r['graph']}_{r['mode']}.bin.xz"
    v=by5[path];assert v["threshold"]==r["threshold"] and v["layers"]==r["last_layer"] and v["all_equal"]
    assert hashlib.sha256(lzma.decompress((ROOT/path).read_bytes())).hexdigest()==r["certificate_sha256"]
    if r["threshold"]:
        assert r["eligible"] and v["critical_AS_count"]>0 and v["nonAS_Qmax"]==0 and v["lex_max_is_AS"]
        c=v["critical_AS_witness"];assert sum(c)==r["threshold"]-1 and sum(x>1 for x in c)<=1
    if not r["eligible"]:
        assert r["graph"]=="C8_leaf" and r["mode"]=="clear" and r["threshold"] is None
assert sum(not r["eligible"] for r in rows5)==1
summary5=load("evidence/S005/analysis.json")
assert summary5["total_cases"]==len(rows5) and summary5["eligible_cases"]==len(rows5)-1
assert summary5["exact_threshold_cases"]==sum(r["threshold"] is not None for r in rows5)
assert summary5["Q_counterexamples"]==summary5["ASHstar_counterexamples"]==0
pure=load("evidence/S005/pure_theorem_tests.json")
assert pure["pure_tests"]==8619 and pure["root_graph_cases"]==665 and all(r["all_agree"] for r in pure["rows"])
checked5=0
for line in (ROOT/"evidence/S005/HASHES.md").read_text(encoding="utf-8").splitlines():
    m=re.fullmatch(r"`([0-9a-f]{64})`\s+`([^`]+)`",line.strip())
    if m:
        assert hashlib.sha256((ROOT/m.group(2)).read_bytes()).hexdigest()==m.group(1),m.group(2)
        checked5+=1
assert checked5>=2*len(rows5),checked5
assert not list((ROOT/"evidence/S005").glob("*.bin"))
print(f"S005 metadata, source scopes, {len(rows5)} certificates and {checked5} hashes: PASS (universal ASH* OPEN).")

# S006: exact interfaces must not be promoted to the missing ASH* comparison.
assert state["s006"] == spec["s006"]
assert state["s006"]["universal_stack"] == state["s006"]["universal_clear"] == "OPEN"
assert state["s006"]["novelty"] == "NOT_AUDITED"
assert state["s006"]["formal_status"] == "NOT_STARTED"
assert state["s006"]["finite_verification"]["new_global_threshold_claims"] == 0
for name in ("PLAN", "PLAN_AMENDMENT_1", "PLAN_AMENDMENT_2", "PLAN_AMENDMENT_3"):
    assert hashlib.sha256((ROOT/f"sessions/S006/{name}.md").read_bytes()).hexdigest() == (ROOT/f"sessions/S006/{name}.sha256").read_text(encoding="utf-8").split()[0]
for name in ("INPUT.md", "OWNER_INVOCATION.txt", "AUTHORISED_PROMPT.md", "AUDIT.md", "CLOSEOUT.md"):
    assert (ROOT/"sessions/S006"/name).is_file()
assert (ROOT/"sessions/S007/AUTHORISED_PROMPT.md").read_text(encoding="utf-8") in (ROOT/"sessions/S006/CLOSEOUT.md").read_text(encoding="utf-8")
assert (ROOT/"sessions/S006/AUTHORISED_PROMPT.md").read_text(encoding="utf-8") in (ROOT/"sessions/S005/CLOSEOUT.md").read_text(encoding="utf-8")
grammar=load("evidence/S006/grammar_verification.json")
assert len(grammar["cases"]) == 153 and grammar["all_grammar_bounds_and_legal_derivations"]
assert all(c["all_equal"] for c in grammar["cases"])
assert sum(c["finite_cells"] for c in grammar["cases"]) == 2145
assert sum(c["production_inequalities"] for c in grammar["cases"]) == 30347
assert hashlib.sha256(lzma.decompress((ROOT/"evidence/S006/grammar_certificates.json.xz").read_bytes())).hexdigest() == grammar["certificate_sha256"]
rooted=load("evidence/S006/rooted_challenges.json")
assert len(rooted["graphs"]) == 35
assert sum(len(g["layers"]) for g in rooted["graphs"]) == 531
assert sum(r["configurations"] for g in rooted["graphs"] for r in g["layers"]) == 3155536
assert all(r["full_forward_reverse_equal"] for g in rooted["graphs"] for r in g["layers"])
assert [(g["graph"],g["last_layer"]) for g in rooted["graphs"] if g["scope"] != "BOUNDED_COMPLETE"] == [("triangle_tail3",29)]
assert rooted["pure_source_target_tests"] == 11750 and rooted["buffer_source_target_tests"] == 1508
stack6=load("evidence/S006/stack_buffer_verification.json")
assert stack6["finite_forest_cells"] == 367 and stack6["concatenation_inequalities"] == 9161
assert stack6["buffer_source_target_tests"] == 1508 and stack6["all_legal_and_optimal"]
extrema6=load("evidence/S006/extremal_challenge.json")
assert len(extrema6["cases"]) == 257 and extrema6["failed_nonAS_class_maxima"] == 618
assert load("evidence/S006/obstruction_verification.json")["all_verified"]
checked6=set()
frozen_index=load('evidence/S007/frozen_s006_index.json')
assert frozen_index['base_commit']=='74feae2559af1ddc855febbd0da9693faf51ef22'
assert set(frozen_index['files'])=={'.github/workflows/governance.yml','authoritative/NEXT_SESSION_PROMPT.md','authoritative/STATE.json','catalogue/claims.json','catalogue/sources.json','research/ASH_SPEC.json','validation/validate_governance.py'}
frozen6={p:info['snapshot'] for p,info in frozen_index['files'].items()}
for p,info in frozen_index['files'].items():
    assert info['snapshot'].startswith('evidence/S007/frozen_s006_')
    assert hashlib.sha256((ROOT/info['snapshot']).read_bytes()).hexdigest()==info['sha256']
for line in (ROOT/"evidence/S006/HASHES.md").read_text(encoding="utf-8").splitlines():
    m=re.fullmatch(r"`([0-9a-f]{64})`\s+`([^`]+)`",line.strip())
    if m:
        historical=ROOT/frozen6.get(m.group(2),m.group(2))
        assert hashlib.sha256(historical.read_bytes()).hexdigest()==m.group(1),m.group(2)
        checked6.add(m.group(2))
required6={p.relative_to(ROOT).as_posix() for folder in ("sessions/S006","evidence/S006") for p in (ROOT/folder).glob("*") if p.is_file() and p.name != "HASHES.md"}
required6 |= {p.relative_to(ROOT).as_posix() for p in (ROOT/"tools").glob("s006*.py")}
assert required6 <= checked6 and len(checked6)>=40
for rel in required6:
    if not rel.endswith('.xz'):
        assert b'\r\n' not in (ROOT/rel).read_bytes(),rel
assert 'eol=lf' in (ROOT/'.gitattributes').read_text(encoding="utf-8")
local6=load('evidence/S006/local_checks.json')
effective6={r['command']:r['exit_code'] for r in local6}
assert len(effective6)>=15 and all(code==0 for code in effective6.values())
print(f"S006 mirrors, scope and {len(checked6)} historical hashes: PASS (cold audit S007; universal ASH* OPEN).")

# S007 full closure; family proof must never be promoted to universal ASH*.
assert state['s007']==spec['s007']
assert state['s007']['universal_stack']==state['s007']['universal_clear']=='OPEN'
assert state['s007']['novelty']=='NOT_AUDITED' and state['s007']['formal_status']=='NOT_STARTED'
assert state['s006']['cold_fresh_session_audit']=='PASS_S007'
assert (ROOT/'sessions/S008/AUTHORISED_PROMPT.md').read_text(encoding='utf-8')==(ROOT/'sessions/S007/FUTURE_S008.md').read_text(encoding='utf-8')
assert (ROOT/'sessions/S008/AUTHORISED_PROMPT.md').read_text(encoding='utf-8') in (ROOT/'sessions/S007/CLOSEOUT.md').read_text(encoding='utf-8')
assert (ROOT/'sessions/S007/OWNER_INVOCATION.txt').read_text(encoding='utf-8').strip()=='Run S007 locally using authoritative/NEXT_SESSION_PROMPT.md. Execute exactly S007 and stop before S008.'
for name in ('PLAN','PLAN_AMENDMENT_1','PLAN_AMENDMENT_2'):
    assert hashlib.sha256((ROOT/f'sessions/S007/{name}.md').read_bytes()).hexdigest()==(ROOT/f'sessions/S007/{name}.sha256').read_text().split()[0]
for stem,goal,counts in [('tail','clear',(36,81763,15251,316569,[4,10,22])),('stack_tail','stack',(28,20876,5025,73132,[4,8,16]))]:
    data=load(f'evidence/S007/{stem}_layers.json');verified=load(f'evidence/S007/{stem}_verification.json')
    layers,states,traces,moves,thresholds=counts
    assert [r['length'] for r in data['graphs']]==[0,1,2]
    assert [r['threshold'] for r in data['graphs']]==thresholds
    assert sum(len(r['layers']) for r in data['graphs'])==layers
    assert sum(t['configurations'] for r in data['graphs'] for t in r['layers'])==states
    assert verified['all_verified'] and verified['goal']==goal
    assert (verified['full_reverse_layer_matches'],verified['complete_configurations'],verified['independent_legal_traces'],verified['legal_moves'])==(layers,states,traces,moves)
    assert hashlib.sha256(lzma.decompress((ROOT/f'evidence/S007/{stem}_traces.json.xz').read_bytes())).hexdigest()==data['trace_raw_sha256']
for c in claims:
    if c['id'] in ('CLM-0055','CLM-0056','CLM-0057','CLM-0058','CLM-0059','CLM-0061'):
        assert c['status']=='PROGRAMME_PROVED'
    if c['id']=='CLM-0060': assert c['status']=='COMPUTED_EXACT'
frozen7_index=load('evidence/S008/frozen_s007_index.json')
assert frozen7_index['base_commit']=='a21ce4702f2d888bd5e6a417a17df0f2095f0b0a'
expected7={'.github/workflows/governance.yml','audit/SEARCH_LOG.md','authoritative/DECISION_LOG.md','authoritative/NEXT_SESSION_PROMPT.md','authoritative/START_HERE.md','authoritative/STATE.json','campaigns/REGISTRY.md','catalogue/claims.json','catalogue/CLAIMS.md','catalogue/sources.json','catalogue/SOURCES.md','docs/FAILURE_AND_LESSON_LEDGER.md','docs/PHASE_GATE_LEDGER.md','docs/SESSION_LEDGER.md','research/ASH_SPEC.json','research/ASH_SPEC.md','research/ASHSTAR_ATTACK_BRIEF.md','research/PROBLEM_SPEC.md','research/ROUTES.md','tools/README.md','validation/validate_governance.py'}
assert set(frozen7_index['files'])==expected7
frozen7={p:info['snapshot'] for p,info in frozen7_index['files'].items()}
for p,info in frozen7_index['files'].items():
    assert info['snapshot']=='evidence/S008/frozen_s007_'+p.replace('/','__')
    assert hashlib.sha256((ROOT/info['snapshot']).read_bytes()).hexdigest()==info['sha256']
checked7=set()
for line in (ROOT/'evidence/S007/HASHES.md').read_text(encoding='utf-8').splitlines():
    m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
    if m:
        assert hashlib.sha256((ROOT/frozen7.get(m[2],m[2])).read_bytes()).hexdigest()==m[1],m[2]
        checked7.add(m[2])
required7={p.relative_to(ROOT).as_posix() for folder in ('sessions/S007','evidence/S007') for p in (ROOT/folder).glob('*') if p.is_file() and p.name!='HASHES.md'}
required7|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s007*.py')}
assert required7<=checked7
for rel in required7:
    if not rel.endswith('.xz'): assert b'\r\n' not in (ROOT/rel).read_bytes(),rel
print(f'S007 scope and {len(checked7)} historical hashes: PASS (cold audit S008; universal ASH* OPEN).')

# S008 closure and exact scope boundaries, never a universal mathematical certificate.
assert state['s008']==spec['s008']
assert state['s008']['universal_stack']==state['s008']['universal_clear']=='OPEN'
assert state['s008']['novelty']=='NOT_AUDITED' and state['s008']['formal_status']=='NOT_STARTED'
assert state['s007']['cold_fresh_session_audit']=='PASS_S008'
assert state['s008']['cold_fresh_session_audit']=='PASS_S009_AT_STATED_SCOPES'
old_prompt=(ROOT/'sessions/S008/FUTURE_S009.md').read_text(encoding='utf-8')
assert old_prompt==(ROOT/'sessions/S009/AUTHORISED_PROMPT.md').read_text(encoding='utf-8')
assert old_prompt in (ROOT/'sessions/S008/CLOSEOUT.md').read_text(encoding='utf-8')
assert 'First substantive priority: deep primary-source prior art' in old_prompt
assert 'Do not impose a one-object' in old_prompt
for name in ('PLAN','PLAN_AMENDMENT_1','PLAN_AMENDMENT_2'):
    assert hashlib.sha256((ROOT/f'sessions/S008/{name}.md').read_bytes()).hexdigest()==(ROOT/f'sessions/S008/{name}.sha256').read_text().split()[0]
for name in ('INPUT.md','OWNER_ADDENDUM.md','AUTHORISED_PROMPT.md','AUDIT.md','CLOSEOUT.md','FUTURE_S009.md'):
    assert (ROOT/'sessions/S008'/name).is_file()
tip=load('evidence/S008/tip_verification.json')
assert tip['all_verified'] and len(tip['grammar'])==len(tip['forest'])==9
assert [r['length'] for r in tip['forest']]==list(range(9))
assert sum(r['forest_finite'] for r in tip['forest'])==774
assert [r['complete_reachable_states'] for r in tip['closures']]==[1,14,101,891]
assert all(r['stack_goals']==0 for r in tip['closures'])
symbolic=load('evidence/S008/symbolic_certificate.json')
assert symbolic['all_production_inequalities'] and symbolic['count']==len(symbolic['checks'])==4376 and symbolic['bases_checked']==5
for row in symbolic['checks']:
    a,b=row['difference_A_t'];ratio=row['domain_A_ge_ratio_t']
    assert ratio in (1,2) and a>=0 and a*ratio+b>=0
branch=load('evidence/S008/branch_layers.json');verified=load('evidence/S008/branch_verification.json')
assert [(r['k'],r['goal']) for r in branch['graphs']]==[(k,g) for k in (1,2,3) for g in ('stack','clear')]
assert sum(len(r['layers']) for r in branch['graphs'])==72
assert sum(t['configurations'] for r in branch['graphs'] for t in r['layers'])==127799
assert verified['all_verified'] and (verified['complete_layers'],verified['complete_configurations'],verified['independent_traces'],verified['legal_moves'])==(72,127799,36173,479591)
assert hashlib.sha256(lzma.decompress((ROOT/'evidence/S008/branch_traces.json.xz').read_bytes())).hexdigest()==branch['trace_raw_sha256']
for c in claims:
    if c['id'] in ('CLM-0062','CLM-0063','CLM-0064','CLM-0065'):assert c['status']=='PROGRAMME_PROVED'
    if c['id'] in ('CLM-0066','CLM-0067'):assert c['status']=='COMPUTED_EXACT'
checked8=set()
for line in (ROOT/'evidence/S008/HASHES.md').read_text(encoding='utf-8').splitlines():
    m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
    if m:
        assert hashlib.sha256((ROOT/m[2]).read_bytes()).hexdigest()==m[1],m[2]
        checked8.add(m[2])
required8={p.relative_to(ROOT).as_posix() for folder in ('sessions/S008','evidence/S008') for p in (ROOT/folder).glob('*') if p.is_file() and p.name!='HASHES.md'}
required8|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s008*.py')}
required8.add('research/S008_HOSTILE_AUDIT_AND_UNIVERSAL_ROUTES.md')
assert required8<=checked8
for rel in required8:
    if not rel.endswith('.xz'):assert b'\r\n' not in (ROOT/rel).read_bytes(),rel
for key in ('2610.09650','2604.22341'):
    assert load('evidence/S008/source_refresh.json')[key]['pdf_unchanged']
    assert load('evidence/S008/source_refresh.json')[key]['versions']==['1']
assert all(r['exit_code']==0 for r in load('evidence/S008/cold_checks.json'))
print(f'S008 scopes and {len(checked8)} immutable hashes: PASS (cold S009; universal ASH* OPEN).')

# S009 foundational assessment is within Phase1; final gates and universal goal stay open.
assert state['s009']==spec['s009']
assert state['s009']['universal_stack']==state['s009']['universal_clear']=='OPEN'
assert state['s009']['cold_new_proofs']=='PASS_S010_AT_STATED_SCOPES' and state['s009']['formal_status']=='NOT_STARTED'
assert state['phases']['2']['status']=='NOT_STARTED'
future10=(ROOT/'sessions/S009/FUTURE_S010.md').read_text(encoding='utf-8')
assert future10==(ROOT/'sessions/S010/AUTHORISED_PROMPT.md').read_text(encoding='utf-8')
assert future10 in (ROOT/'sessions/S009/CLOSEOUT.md').read_text(encoding='utf-8')
assert (ROOT/'sessions/S009/INPUT.md').read_text(encoding='utf-8')=='Run this session\n\n'+old_prompt
for name in ('PLAN','PLAN_AMENDMENT_1','PLAN_AMENDMENT_2'):
    assert hashlib.sha256((ROOT/f'sessions/S009/{name}.md').read_bytes()).hexdigest()==(ROOT/f'sessions/S009/{name}.sha256').read_text().split()[0]
for i,digest in ((1,'8d05ff6b0f972d23260571dd6881aa4a47c3458942ac8389bb63d15d4dbe370a'),(2,'cbe9d2c29a8b1776e751c0b9a953295421f3cb7a7d0ed0c47b2ce06aae8bf6c2')):
    assert hashlib.sha256((ROOT/f'sessions/S009/PLAN_AMENDMENT_{i}_INITIAL.md').read_bytes()).hexdigest()==digest
assert len(load('evidence/S009/cold_checks.json'))==15
assert all(r['exit_code']==0 and r['resource_failure'] is None for r in load('evidence/S009/cold_checks.json'))
pv=json.loads(lzma.decompress((ROOT/'evidence/S009/port_verification.json.xz').read_bytes()));pr=load('evidence/S009/port_results.json')
assert pv['all_verified'] and pv['complete_cases']==len(pv['cases'])==len(pr['cases'])==318
assert (pv['total_closure_states'],pv['maximum_closure_states'],pv['rooted_winning_traces'])==(53924,3409,1694)
assert pv['marked_forest']['affected_components']==3
assert hashlib.sha256((ROOT/'evidence/S009/port_inputs.json').read_bytes()).hexdigest()==pr['input_sha256']
for a,b in zip(pr['cases'],pv['cases']):
    assert (a['id'],a['clear_mask'],a['stack_mask'])==(b['id'],b['clear_mask'],b['stack_mask'])
cv=load('evidence/S009/credit_verification.json');cu=load('evidence/S009/credit_upper.json')
assert cv['all_verified'] and (cv['complete_layers'],cv['complete_configurations'],cv['upper_traces'],cv['literal_moves'],cv['protected_B3_trees'],cv['threshold_claims'])==(33,13088,3860,41800,795,0)
assert (cu['traces'],cu['moves'])==(3860,41800)
assert hashlib.sha256(lzma.decompress((ROOT/'evidence/S009/credit_traces.json.xz').read_bytes())).hexdigest()==cu['trace_raw_sha256']
for c in claims:
    if c['id'] in {'CLM-0071','CLM-0072','CLM-0073','CLM-0074','CLM-0075','CLM-0076','CLM-0077','CLM-0079'}:assert c['status']=='PROGRAMME_PROVED'
    if c['id'] in {'CLM-0070','CLM-0078'}:assert c['status']=='COMPUTED_EXACT'
refresh9=load('evidence/S009/source_refresh.json')
for ident in ('2604.22341','2610.09650'):
    assert refresh9[ident]['pdf_sha256']==load('evidence/S008/source_refresh.json')[ident]['pdf_sha256'] and refresh9[ident]['versions']==['1']
assert refresh9['2609.31811']['current_version']=='2'
local9=load('evidence/S009/local_checks.json')
assert len(local9)==4 and all(r['exit_code']==0 and r['resource_failure'] is None for r in local9)
for r in local9:
    assert hashlib.sha256((ROOT/r['command'][1]).read_bytes()).hexdigest()==r['code_sha256']
checked9=set()
for line in (ROOT/'evidence/S009/HASHES.md').read_text(encoding='utf-8').splitlines():
    m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
    if m:
        assert hashlib.sha256((ROOT/m[2]).read_bytes()).hexdigest()==m[1],m[2]
        checked9.add(m[2])
required9={p.relative_to(ROOT).as_posix() for folder in ('sessions/S009','evidence/S009') for p in (ROOT/folder).glob('*') if p.is_file() and p.name!='HASHES.md'}
required9|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s009*.py')}
required9|={'research/S009_PRIOR_ART_AND_DEPENDENCY_AUDIT.md','research/S009_UNIVERSAL_RESEARCH.md'}
assert required9<=checked9
for rel in required9:
    if not rel.endswith('.xz'):assert b'\r\n' not in (ROOT/rel).read_bytes(),rel
print(f'S009 primary/scopes/mirrors and {len(checked9)} immutable hashes: PASS (universal OPEN; historical S010 handoff retained).')

# S010 exact finite assurance, explicit universal and future boundaries.
assert state['s010']==spec['s010']
assert state['s010']['universal_stack']==state['s010']['universal_clear']=='OPEN'
assert state['s010']['formal_status']=='NOT_STARTED' and state['s010']['cold_new_proofs']=='PASS_S011_AT_STATED_SCOPES'
assert state['s009']['cold_new_proofs']=='PASS_S010_AT_STATED_SCOPES'
future11=(ROOT/'sessions/S010/FUTURE_S011.md').read_text(encoding='utf-8')
assert future11==(ROOT/'sessions/S011/AUTHORISED_PROMPT.md').read_text(encoding='utf-8') and future11 in (ROOT/'sessions/S010/CLOSEOUT.md').read_text(encoding='utf-8')
assert 'FUTURE, UNEXECUTED' in future11 and 'Stop before S012' in future11
actual10=(ROOT/'sessions/S010/OWNER_INVOCATION.txt').read_text(encoding='utf-8')
assert actual10.startswith('# Run S010 — Sustained universal ASH*') and 'Milestone 7' in actual10
assert actual10!=future10 and 'Stop before S011' in actual10
assert hashlib.sha256(actual10.encode()).hexdigest()==load('evidence/S010/environment.json')['input_sha256']
for name in ('PLAN','PLAN_AMENDMENT_1','PLAN_AMENDMENT_2','PLAN_AMENDMENT_3'):
    assert hashlib.sha256((ROOT/f'sessions/S010/{name}.md').read_bytes()).hexdigest()==(ROOT/f'sessions/S010/{name}.sha256').read_text().split()[0]
for filename in ('campaign_preflight','campaign2_preflight','campaign3_preflight'):
    preflight=load(f'evidence/S010/{filename}.json')
    assert preflight['execution']=='NOT_YET_RUN'
    for p,digest in preflight['files'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest,p
cold10=load('evidence/S010/cold_checks.json')
assert len(cold10)==19 and all(r['exit_code']==0 and r['resource_failure'] is None for r in cold10)
assert sum(r['seconds'] for r in cold10)<1800
for r in cold10:assert hashlib.sha256((ROOT/r['command'][1]).read_bytes()).hexdigest()==r['code_sha256']
count10=load('evidence/S010/count_summary.json');vcount10=load('evidence/S010/count_verification.json')
assert vcount10['all_verified'] and (count10['certificates'],count10['connected'],count10['weak_only'])==(37556,26274,3856)
assert (vcount10['certificates'],vcount10['legal_exact_count_traces'],vcount10['weak_failures'])==(37556,26274,3856)
for file,key in [('count_certificates','certificate_raw_sha256'),('count_traces','trace_raw_sha256'),('count_closures','closure_raw_sha256')]:
    owner=count10 if file=='count_certificates' else vcount10
    assert hashlib.sha256(lzma.decompress((ROOT/f'evidence/S010/{file}.json.xz').read_bytes())).hexdigest()==owner[key]
root10=load('evidence/S010/root_summary.json');vroot10=load('evidence/S010/root_verification.json')
assert vroot10['all_verified'] and (root10['case_count'],root10['complete_layers'],root10['complete_configurations'])==(14,136,125481)
assert (vroot10['complete_layers'],vroot10['complete_configurations'],vroot10['literal_insertion_root_traces'],vroot10['literal_moves'])==(136,125481,930,7703)
assert all(r['critical_empty_insertion_intersection']==r['occupied_self_failure_configs']==r['heavy_self_failure_configs']==0 for r in root10['cases'])
assert next(r for r in root10['cases'] if r['graph']=='C5' and r['goal']=='stack')['whole_threshold_common_roots']==0
for file,owner,key in [('root_tables',root10,'table_raw_sha256'),('root_traces',vroot10,'trace_raw_sha256')]:
    assert hashlib.sha256(lzma.decompress((ROOT/f'evidence/S010/{file}.json.xz').read_bytes())).hexdigest()==owner[key]
ref10=load('evidence/S010/reflection_summary.json');vref10=load('evidence/S010/reflection_verification.json')
assert vref10['all_verified'] and (ref10['original_three_pile_traces'],ref10['marked_cases'],ref10['reflected_moves'],ref10['empty_marked_paths'])==(7289,21707,98878,2642)
assert (vref10['marked_cases'],vref10['reflected_literal_moves'],vref10['distinct_deleted_inputs'],vref10['complete_closure_states'],vref10['maximum_closure_states'])==(21707,98878,1447,60868,122)
assert hashlib.sha256(lzma.decompress((ROOT/'evidence/S010/reflection_traces.json.xz').read_bytes())).hexdigest()==ref10['output_raw_sha256']
assert ref10['input_trace_raw_sha256']==vcount10['trace_raw_sha256']
for name in ('count','root','reflection'):
    for kind in ('producer','checker'):
        log=load(f'evidence/S010/{name}_{kind}_log.json')
        assert log['exit_code']==0 and log['resource_failure'] is None and log['seconds']<600 and log['peak_working_set_bytes']<=2*1024**3
        assert hashlib.sha256((ROOT/log['command'][1]).read_bytes()).hexdigest()==log['code_sha256']
for ident in ('2604.22341','2610.09650','2609.31811'):
    assert load('evidence/S010/source_refresh.json')[ident]['pdf_sha256']==refresh9[ident]['pdf_sha256']
checked10=set()
for line in (ROOT/'evidence/S010/HASHES.md').read_text(encoding='utf-8').splitlines():
    m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
    if m:
        assert hashlib.sha256((ROOT/m[2]).read_bytes()).hexdigest()==m[1],m[2]
        checked10.add(m[2])
required10={p.relative_to(ROOT).as_posix() for folder in ('sessions/S010','evidence/S010') for p in (ROOT/folder).glob('*') if p.is_file() and p.name!='HASHES.md'}
required10|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s010*.py')}
required10|={p.relative_to(ROOT).as_posix() for p in (ROOT/'research').glob('S010*.md')}
assert required10<=checked10
for rel in required10:
    if not rel.endswith('.xz'):assert b'\r\n' not in (ROOT/rel).read_bytes(),rel
local10=load('evidence/S010/local_checks.json')
assert len(local10)==6 and all(r['exit_code']==0 and r['resource_failure'] is None for r in local10)
for c in claims:
    if c['id'] in {f'CLM-{i:04d}' for i in range(81,89)}:assert c['status']=='PROGRAMME_PROVED'
    if c['id'] in {'CLM-0080','CLM-0089','CLM-0090','CLM-0091'}:assert c['status']=='COMPUTED_EXACT'
    if c['id']=='CLM-0092':assert c['status']=='HEURISTIC'
print(f'S010 historical scopes and {len(checked10)} immutable hashes: PASS (cold challenge S011 at stated scopes).')

# S011: exact certificate scope, immutable campaigns and current future boundary.
assert state['s011']==spec['s011']
s11=state['s011']
assert s11['universal_stack']==s11['universal_clear']=='OPEN'
assert s11['cold_s010_audit']=='PASS_S011_AT_STATED_SCOPES' and s11['cold_new_proofs']=='PASS_S012_AT_STATED_SCOPES'
assert s11['formal_status']=='NOT_STARTED' and state['phases']['1']['status']=='IN_PROGRESS'
future12=(ROOT/'sessions/S011/FUTURE_S012.md').read_text(encoding='utf-8')
assert (ROOT/'sessions/S012/AUTHORISED_PROMPT.md').read_text(encoding='utf-8')==future12 and future12 in (ROOT/'sessions/S011/CLOSEOUT.md').read_text(encoding='utf-8')
assert 'FUTURE, UNEXECUTED' in future12 and 'Stop before S013' in future12
actual11=(ROOT/'sessions/S011/OWNER_INVOCATION.txt').read_text(encoding='utf-8')
assert actual11.startswith('S011') and 'Resolve the universal critical ASH* bridge' in actual11
assert 'No delegated agent work' in actual11 and 'Stop before S012' in actual11 and actual11!=future11
assert hashlib.sha256(actual11.encode()).hexdigest()==load('evidence/S011/environment.json')['invocation_sha256']
assert (ROOT/'sessions/S011/IMPLEMENTATION_REQUEST.txt').read_text().strip()=='Implement the proposed plan.'
for name in ('PLAN','PLAN_AMENDMENT_1','PLAN_AMENDMENT_2','PLAN_AMENDMENT_3'):
    assert hashlib.sha256((ROOT/f'sessions/S011/{name}.md').read_bytes()).hexdigest()==(ROOT/f'sessions/S011/{name}.sha256').read_text().split()[0]
for number in (1,2,3):
    pre=load(f'evidence/S011/campaign{number}_preflight.json')
    assert pre['execution']=='NOT_YET_RUN' and pre['limits']=={'seconds_each':600,'states_per_layer':300000,'peak_bytes':2*1024**3}
    for p,digest in pre['files'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest,p
    assert f'sessions/S011/PLAN_AMENDMENT_{number}.md' in pre['files']
cold11=load('evidence/S011/cold_checks.json');local11=load('evidence/S011/local_checks.json')
assert len(cold11)==25 and len(local11)==6
for row in cold11+local11:
    assert row['exit_code']==0 and row['resource_failure'] is None and row['seconds']<600 and row['peak_working_set_bytes']<=2*1024**3
    assert hashlib.sha256((ROOT/row['command'][1]).read_bytes()).hexdigest()==row['code_sha256']
for tool in ['s011_trees','s011_trees_verify','s011_transport','s011_transport_verify','s011_root_types','s011_root_types_verify']:
    row=load(f'evidence/S011/{tool}_log.json')
    assert row['exit_code']==0 and row['resource_failure'] is None and row['seconds']<600 and row['peak_working_set_bytes']<=2*1024**3
    assert hashlib.sha256((ROOT/row['command'][1]).read_bytes()).hexdigest()==row['code_sha256']
t11=load('evidence/S011/tree_summary.json');vt11=load('evidence/S011/tree_verification.json')
assert (t11['layers'],t11['configurations'],t11['winning_insertions_checked'],t11['occupied_deletions_checked'])==(90,97839,3416,4418)
assert vt11['all_verified'] and (vt11['literal_traces'],vt11['literal_moves'],vt11['negative_closures'])==(4883,43286,15)
assert t11['failure_counts']=={'occupied_self_stack':884,'occupied_self_clear':884,'critical_common_clear':3,'critical_occupied_self_clear':0,'nonbipartite_ternary_clear_loser':10}
p11=load('evidence/S011/transport_summary.json');vp11=load('evidence/S011/transport_verification.json')
assert (p11['certificates'],p11['roots'],p11['edges'],p11['exchanges'])==(116401,25278,25959,65164)
assert vp11['all_verified'] and (vp11['certificates'],vp11['literal_moves'],vp11['exceptional_two_singletons'],vp11['triangular_repairs'],vp11['critical_clear_cuts'],vp11['C5_closure_states'])==(116401,507217,6978,24894,12,70)
r11=load('evidence/S011/root_types.json');vr11=load('evidence/S011/root_types_verification.json')
assert vr11['all_verified'] and (vr11['checked_inputs'],vr11['critical_insertions'],vr11['critical_clear_cases'],vr11['bipartite_insertion_checks'],vr11['already_stackable_critical_clear'])==(97798,120,23,10,15)
assert r11['model_is_graph_configuration'] is False
assert hashlib.sha256((ROOT/'evidence/S011/root_types.json').read_bytes()).hexdigest()==vr11['result_sha256']
odd11=load('evidence/S011/odd_cycle_failure.json')
assert odd11['c']==[4,1,1,1,1] and odd11['clear_mask']==0 and odd11['three_mask']==31 and len(odd11['closure'])==70
for file,owner,key in [('tree_tables',t11,'table_raw_sha256'),('tree_traces',vt11,'trace_raw_sha256'),('tree_negative_closures',vt11,'negative_raw_sha256'),('transport_certificates',p11,'table_raw_sha256'),('transport_traces',vp11,'trace_raw_sha256'),('triangle_repairs',vp11,'repair_raw_sha256')]:
    assert hashlib.sha256(lzma.decompress((ROOT/f'evidence/S011/{file}.json.xz').read_bytes())).hexdigest()==owner[key]
refresh11=load('evidence/S011/source_refresh.json')
for ident in ['2604.22341','2610.09650','2609.31811']:
    assert refresh11[ident]['pdf_sha256']==load('evidence/S010/source_refresh.json')[ident]['pdf_sha256']
assert refresh11['1501.04245']['current_version']=='3'
checked11=set()
for line in (ROOT/'evidence/S011/HASHES.md').read_text(encoding='utf-8').splitlines():
    m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
    if m:
        assert hashlib.sha256((ROOT/m[2]).read_bytes()).hexdigest()==m[1],m[2]
        checked11.add(m[2])
required11={p.relative_to(ROOT).as_posix() for folder in ['sessions/S011','evidence/S011'] for p in (ROOT/folder).glob('*') if p.is_file() and p.name!='HASHES.md'}
required11|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s011*.py')}
required11|={p.relative_to(ROOT).as_posix() for p in (ROOT/'research').glob('S011*.md')}
assert required11<=checked11
for rel in required11:
    if not rel.endswith('.xz'):assert b'\r\n' not in (ROOT/rel).read_bytes(),rel
for c in claims:
    if c['id'] in {f'CLM-{i:04d}' for i in range(94,100)}:assert c['status']=='PROGRAMME_PROVED' and c['cold_audit']=='PASS_S012_AT_STATED_SCOPES'
    if c['id'] in {'CLM-0093','CLM-0100','CLM-0101','CLM-0102'}:assert c['status']=='COMPUTED_EXACT'
print(f'S011 historical scopes and {len(checked11)} immutable hashes: PASS (cold challenge S012 at stated scopes).')

# S012: exact SAME-input identities and bounded history barriers, no universal promotion.
assert state['s012']==spec['s012']
s12=state['s012']
assert s12['universal_stack']==s12['universal_clear']=='OPEN'
assert s12['cold_s011_audit']=='PASS_S012_AT_STATED_SCOPES' and s12['cold_new_proofs']=='FUTURE_S013'
assert s12['formal_status']=='NOT_STARTED' and state['phases']['1']['status']=='IN_PROGRESS'
future13=(ROOT/'sessions/S012/FUTURE_S013.md').read_text(encoding='utf-8')
assert future13 in (ROOT/'sessions/S012/CLOSEOUT.md').read_text(encoding='utf-8')
# An owner-directed administrative revision supersedes only the prospective handoff.
# Frozen S012 closeout/prompt/hash bytes remain the original historical record.
revision_path=ROOT/'authoritative/HANDOFF_REVISION.json'
if revision_path.exists():
    revision=load('authoritative/HANDOFF_REVISION.json')
    assert revision['schema']==1 and revision['kind']=='OWNER_DIRECTED_FUTURE_HANDOFF_REVISION'
    assert revision['session']=='S013' and revision['status']=='FUTURE_UNEXECUTED'
    assert revision['prior_prompt']=='sessions/S012/FUTURE_S013.md'
    assert revision['closeout_addendum_for']=='sessions/S012/CLOSEOUT.md'
    assert hashlib.sha256((ROOT/revision['prior_prompt']).read_bytes()).hexdigest()==revision['prior_sha256']
    revised=(ROOT/revision['current_prompt']).read_bytes()
    request=(ROOT/revision['owner_request']).read_bytes()
    assert hashlib.sha256(revised).hexdigest()==revision['current_sha256']
    assert hashlib.sha256(request).hexdigest()==revision['owner_request_sha256']
    assert next_prompt==revised.decode('utf-8') and state['next_session_handoff']==revision
    assert b'\r\n' not in revised and b'\r\n' not in request
    assert "Don't stop at one or two milestones" in request.decode('utf-8')
    for requirement in ['L_all(G) <= L_AS(G)','Do not stop after one or two milestones',
                        'GLOBAL Q','delta0, delta1 and delta>=2','Local execution',
                        'PRIOR hashed bounded amendments','Stop before S014']:
        assert requirement in next_prompt,requirement
else:
    assert next_prompt==future13
assert 'FUTURE, UNEXECUTED' in future13 and 'Stop before S014' in future13
actual12=(ROOT/'sessions/S012/OWNER_INVOCATION.txt').read_text(encoding='utf-8')
assert actual12=='Run the next session\n'
assert hashlib.sha256(actual12.encode()).hexdigest()==load('evidence/S012/environment.json')['invocation_sha256']
for name in ['PLAN']+[f'PLAN_AMENDMENT_{i}' for i in range(1,6)]:
    assert hashlib.sha256((ROOT/f'sessions/S012/{name}.md').read_bytes()).hexdigest()==(ROOT/f'sessions/S012/{name}.sha256').read_text().split()[0]
for i in (1,2,3):
    pre=load(f'evidence/S012/campaign{i}_preflight.json')
    for p,digest in pre['files'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest,p
initial12=load('evidence/S012/campaign1_initial_preflight.json')
for suffix in ['reciprocity','reciprocity_verify']:
    assert hashlib.sha256((ROOT/f'evidence/S012/failed_initial_{suffix}.py').read_bytes()).hexdigest()==initial12['files'][f'tools/s012_{suffix}.py']
failed12=load('evidence/S012/failed_zero_base_normal_form_log.json')
assert failed12['exit_code']!=0 and 'AssertionError' in failed12['stderr'] and failed12['resource_failure'] is None
cold12=load('evidence/S012/cold_checks.json');local12=load('evidence/S012/local_checks.json')
assert len(cold12)==12 and len(local12)==6
for row in cold12+local12:
    assert row['exit_code']==0 and row['resource_failure'] is None and row['seconds']<600 and row['peak_working_set_bytes']<=2*1024**3
    assert hashlib.sha256((ROOT/row['command'][1]).read_bytes()).hexdigest()==row['code_sha256']
for tool in ['s012_reciprocity','s012_reciprocity_verify','s012_escape','s012_escape_verify','s012_exceptions','s012_exceptions_verify']:
    row=load(f'evidence/S012/{tool}_log.json')
    assert row['exit_code']==0 and row['resource_failure'] is None and row['seconds']<600 and row['peak_working_set_bytes']<=2*1024**3
    assert hashlib.sha256((ROOT/row['command'][1]).read_bytes()).hexdigest()==row['code_sha256']
v12=load('evidence/S012/verification.json');e12=load('evidence/S012/escape_verification.json');x12=load('evidence/S012/exceptions_verification.json')
assert v12=={'graphs':10,'configurations':175359,'relations':16394311,'literal_traces':714,'literal_moves':5484,'complete_negative_closures':69,'all_full_masks_and_relations_equal':True}
assert e12=={'one_step_barriers':435,'critical_inputs':15,'complete_closure_states':1177,'fuel_witnesses':78,'literal_moves':338,'finite_tau':15,'no_escape_after_complete_closure':0,'all_equal':True}
assert x12=={'pairs':42,'increasing_losing_transfers':4,'literal_traces':18,'literal_moves':116,'complete_negative_closures':26,'negative_closure_states':1177,'global_extrema':18,'nonAS_global_Qmax':0,'all_equal':True}
a12=load('evidence/S012/analysis.json')
assert len(a12['rows'])==10 and not a12['model_is_realized']
assert sum(r['configurations'] for r in a12['rows'])==v12['configurations']
assert sum(sum(r['relation_counts'].values()) for r in a12['rows'])==v12['relations']
for name,value in [('triangular_prism',8),('bridged_triangles',12)]:
    row=next(r for r in a12['rows'] if r['graph']==name)
    assert row['thresholds']=={'stack':value,'clear':value} and row['max_mass']==14
ex12=load('evidence/S012/exceptions.json')
diagnostic=[r for r in ex12['pairs'] if r['graph']=='C5' and r['c']==[0,1,0,3,3] and r['s']==3 and r['t']==4]
assert next(r for r in diagnostic if r['a']==1)['donor_1_2_3']==[True,False,False]
assert next(r for r in diagnostic if r['a']==2)['donor_1_2_3']==[False,False,False]
assert next(r for r in diagnostic if r['a']==2)['stackable']
for ident,result in load('evidence/S012/source_refresh.json').items():assert result['pdf_sha256']==refresh11[ident]['pdf_sha256']
checked12=set()
for line in (ROOT/'evidence/S012/HASHES.md').read_text(encoding='utf-8').splitlines():
    m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
    if m:
        assert hashlib.sha256((ROOT/m[2]).read_bytes()).hexdigest()==m[1],m[2]
        checked12.add(m[2])
required12={p.relative_to(ROOT).as_posix() for folder in ['sessions/S012','evidence/S012'] for p in (ROOT/folder).glob('*') if p.is_file() and p.name!='HASHES.md'}
required12|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s012*.py')}
required12|={p.relative_to(ROOT).as_posix() for p in (ROOT/'research').glob('S012*.md')}
assert required12<=checked12
for rel in required12:
    if not rel.endswith('.xz'):assert b'\r\n' not in (ROOT/rel).read_bytes(),rel
for c in claims:
    if c['id'] in {f'CLM-{i:04d}' for i in [104,105,106,107,108,109,113]}:assert c['status']=='PROGRAMME_PROVED' and c['cold_audit']=='FUTURE_S013'
    if c['id'] in {f'CLM-{i:04d}' for i in [103,110,111,112]}:assert c['status']=='COMPUTED_EXACT'
print(f'S012 current scopes/mirrors and {len(checked12)} immutable hashes: PASS (universal STACK/CLEAR OPEN; S013 FUTURE).')
