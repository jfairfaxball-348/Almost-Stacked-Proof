#!/usr/bin/env python3
"""Fail-closed governance/mirror checks, including active S014; not a math test."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]

# Each real file is independently hashed from bytes once per validation run.
# Repeated preflight references reuse only an unchanged in-process stat key.
_FILE_HASH_CACHE = {}
def sha256_file(path):
    # Original Windows log arguments remain unchanged; resolve separators on CI.
    path = Path(str(path).replace('\\', '/'))
    before = path.stat()
    key = (str(path), before.st_size, before.st_mtime_ns)
    if key in _FILE_HASH_CACHE:
        return _FILE_HASH_CACHE[key]
    h = hashlib.sha256()
    with path.open('rb') as stream:
        while chunk := stream.read(65536):
            h.update(chunk)
    after = path.stat()
    assert (before.st_size, before.st_mtime_ns) == (after.st_size, after.st_mtime_ns), str(path)
    digest = h.hexdigest()
    _FILE_HASH_CACHE[key] = digest
    return digest
def sha256_lzma(path):
    import lzma
    h = hashlib.sha256()
    with lzma.open(path, 'rb') as stream:
        while chunk := stream.read(65536):
            h.update(chunk)
    return h.hexdigest()

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def versioned_tool_source(path,digest):
    # Frozen host paths are identities, not paths on the Linux checkout.
    path=path.replace('\\','/')
    if path.startswith('C:/Almost-Stacked-Proof/'):
        path=path[len('C:/Almost-Stacked-Proof/'):]
        assert '..' not in Path(path).parts
    if path=='C:/Users/johnf/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe':
        assert digest=='362a356ce7f0940ec74f73a8fc2c990a2cc24a38a11c90bbd8eca947110ad139'
        assert (ROOT/'evidence/S014/external_tool_archive/LICENSE.txt').is_file()
        return ROOT/'evidence/S014/external_tool_archive/pwsh.exe'
    assert not re.match(r'^[A-Za-z]:',path), ('Unregistered external preflight source',path)
    # Exact historical filename collision; never a generic preflight bypass.
    if path=='tools/s014_split_verify.py' and digest=='de2b450e5aafe604b591df5c14eac04c3687bc46442d265ecc8c17bad4908f29':
        aliases=load('evidence/S014/tool_version_aliases.json')['aliases']
        assert aliases==[dict(path=path,sha256=digest,archive='tools/s014_mass_split_verify.py',reason='Exact CAM56 source version archived after restoring frozen CAM06 source')]
        assert sha256_file(ROOT/'tools/s014_split_verify.py')=='73a042ac51e8f289a5976220e28601a21e6c03f68acabe3d33135299c25a0ad3'
        return ROOT/'tools/s014_mass_split_verify.py'
    return ROOT/path

state = load("authoritative/STATE.json")
active14 = state.get('active_session') is not None
closed19 = state.get('last_completed_session') == 'S019'
closed18 = state.get('last_completed_session') in ('S018', 'S019')
closed17 = state.get('last_completed_session') in ('S017', 'S018', 'S019')
closed16 = state.get('last_completed_session') in ('S016', 'S017', 'S018', 'S019')
closed15 = state.get('last_completed_session') in ('S015', 'S016', 'S017', 'S018', 'S019')
closed14 = state.get('last_completed_session') in ('S014', 'S015', 'S016', 'S017', 'S018', 'S019')
executed14 = active14 or closed14
if active14:
    assert state['active_session']['session']=='S014' and state['active_session']['status']=='IN_PROGRESS'
    assert state['active_session']['session_commit'] is None and state['active_session']['pull_request'] is None
claims = load("catalogue/claims.json")
sources = load("catalogue/sources.json")
assert state["headline_status"] == ("PRINTED_ASH_REFUTED_COLD_AUDIT_PASS_CRITICAL_STACK_AND_CLEAR_REFUTED_G9_LEAN_PALOMAR_SNAPSHOT_READY_FOR_OWNER_UPLOAD" if closed19 else "PRINTED_ASH_REFUTED_COLD_AUDIT_PASS_CRITICAL_STACK_AND_CLEAR_REFUTED_G9_COLD_RECHECK_PASS_LEAN_LOCAL_COMPARATOR_STATEMENT_PASS_INDEPENDENT_KERNELS_RECORDED" if closed18 else "PRINTED_ASH_REFUTED_COLD_AUDIT_PASS_CRITICAL_STACK_AND_CLEAR_REFUTED_G9_COLD_RECHECK_PASS_LEAN_LOCAL_KERNEL_PROOF_COMPARATOR_PENDING" if closed17 else "PRINTED_ASH_REFUTED_COLD_AUDIT_PASS_CRITICAL_STACK_REFUTED_COLD_RECHECK_PASS_LEAN_PENDING_CRITICAL_CLEAR_REFUTED_COMPUTED_COLD_RECHECK_AND_LEAN_PENDING" if closed16 else "PRINTED_ASH_REFUTED_COLD_AUDIT_PASS_CRITICAL_STACK_REFUTED_COMPUTED_COLD_RECHECK_AND_LEAN_PENDING_CRITICAL_CLEAR_OPEN" if closed15 else "PRINTED_ASH_REFUTED_COLD_AUDIT_PASS_CRITICAL_FORM_OPEN")
assert state["last_completed_session"] == ('S019' if closed19 else 'S018' if closed18 else 'S017' if closed17 else 'S016' if closed16 else 'S015' if closed15 else 'S014' if closed14 else 'S013')
assert state["recommended_next_session"] == ('S020' if closed19 else 'S019' if closed18 else 'S018' if closed17 else 'S017' if closed16 else 'S016' if closed15 else 'S015' if closed14 else 'S014')
assert state["phases"]["0"]["status"] == "PASS"
assert state["phases"]["1"]["status"] == "IN_PROGRESS"
assert all(state["phases"][str(i)]["status"] != "PASS" for i in range(2, 7))
assert state["active_campaign"] is None
assert state["counterexample_status"] == ("PRINTED_FORM_CERTIFIED_COLD_AUDIT_PASS_LEAN_PENDING; CRITICAL_STACK_G9_COLD_RECHECK_PASS_LEAN_LOCAL_KERNEL_PROOF; CRITICAL_CLEAR_G9_COLD_RECHECK_PASS_LEAN_LOCAL_KERNEL_PROOF" if closed17 else "PRINTED_FORM_CERTIFIED_COLD_AUDIT_PASS_LEAN_PENDING; CRITICAL_STACK_G9_COLD_RECHECK_PASS_LEAN_PENDING; CRITICAL_CLEAR_G9_COMPUTED_MULTI_CHECKER_COLD_RECHECK_PENDING_LEAN_PENDING" if closed16 else "PRINTED_FORM_CERTIFIED_COLD_AUDIT_PASS_LEAN_PENDING; CRITICAL_STACK_G9_COMPUTED_MULTI_CHECKER_COLD_RECHECK_PENDING_LEAN_PENDING" if closed15 else "PRINTED_FORM_CERTIFIED_COLD_AUDIT_PASS_LEAN_PENDING")
assert state["lean_status"] == ("G9_PALOMAR_SNAPSHOT_PREPARED_NOT_SUBMITTED" if closed19 else "IN_PROGRESS_G9_LOCAL_COMPARATOR_STATEMENT_PASS_UNSANDBOXED_INDEPENDENT_KERNELS_RECORDED" if closed18 else "IN_PROGRESS_G9_LOCAL_KERNEL_PROOF_COMPARATOR_PENDING" if closed17 else "NOT_STARTED")
assert state["phases"]["3"]["status"] == ("IN_PROGRESS" if closed17 else "NOT_STARTED")
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
assert "S014" in next_prompt and "FUTURE, UNEXECUTED" in next_prompt
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
        digest = sha256_file(ROOT / m.group(2))
        assert digest == m.group(1), (m.group(2), digest)
        checked += 1
assert checked >= 10, checked
print(f"S003 evidence hashes: {checked} files match.")

# The earlier 2026-10-13 correspondence remains distinct from actual S004 execution.
assert (ROOT / "outreach/2026-10-csernak-soukup/2026-10-13_AUTHOR_REPLY.md").exists()
assert (ROOT / "outreach/2026-10-csernak-soukup/reply_draft_2026-10-13.txt").exists()
assert (ROOT / "research/ASHSTAR_ATTACK_BRIEF.md").exists()
assert "S014" in next_prompt and "FUTURE, UNEXECUTED" in next_prompt
assert state["correspondence"]["authority"] == "AUTHOR_REPORTED_INTENDED_MEANING_NOT_PUBLISHED_ERRATUM"
assert state["correspondence"]["next_reply"] == "DRAFT_NOT_SENT"
assert any(x["id"] == "SRC-0010" and x["type"] == "PERSONAL_COMMUNICATION_OWNER_SUPPLIED" for x in sources)
assert all(any(x["id"] == claimid and x["status"] == "SOURCE_STATED" for x in claims) for claimid in ("CLM-0028", "CLM-0029"))
assert (ROOT / "sessions/S004/CLOSEOUT.md").exists()
print("Author correspondence provenance and current future handoff: PASS (administrative only).")

# S004 scope and machine mirrors: printed PASS must never promote universal ASH*.
assert state["printed_form_phase1"]["status"] == "PASS"
spec=load("research/ASH_SPEC.json")
assert spec["literal_form"]["status"] == "FALSE_CERTIFIED_COLD_AUDIT_PASS_LEAN_PENDING"
assert spec["critical_form"]["status"] == ("STACK_REFUTED_G9_COLD_RECHECK_PASS_LEAN_LOCAL_KERNEL_PROOF; CLEAR_REFUTED_G9_COLD_RECHECK_PASS_LEAN_LOCAL_KERNEL_PROOF" if closed17 else "STACK_REFUTED_G9_COLD_RECHECK_PASS_LEAN_PENDING; CLEAR_REFUTED_COMPUTED_G9_COLD_RECHECK_AND_LEAN_PENDING" if closed16 else "STACK_REFUTED_COMPUTED_G9_LEAN_AND_COLD_RECHECK_PENDING; CLEAR_OPEN" if closed15 else "OPEN")
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
        assert sha256_file(ROOT/m.group(2))==m.group(1),m.group(2)
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
    assert sha256_lzma(ROOT/path)==r["layer_sha256"]
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
    assert sha256_file(ROOT/f"sessions/S005/{name}.md") == (ROOT/f"sessions/S005/{name}.sha256").read_text(encoding="utf-8").split()[0]
for name in ("INPUT.md","AUDIT.md","CLOSEOUT.md","CONTINUATION.md","AUTHORISED_PROMPT.md"):
    assert (ROOT/"sessions/S005"/name).exists()
rows5=load("evidence/S005/campaign_summary.json")
v5=load("evidence/S005/verification.json")
assert len(rows5)==len(v5)==len(load("evidence/S005/graphs.json"))
by5={r["file"]:r for r in v5}
for r in rows5:
    path=f"evidence/S005/{r['graph']}_{r['mode']}.bin.xz"
    v=by5[path];assert v["threshold"]==r["threshold"] and v["layers"]==r["last_layer"] and v["all_equal"]
    assert sha256_lzma(ROOT/path)==r["certificate_sha256"]
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
        assert sha256_file(ROOT/m.group(2))==m.group(1),m.group(2)
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
    assert sha256_file(ROOT/f"sessions/S006/{name}.md") == (ROOT/f"sessions/S006/{name}.sha256").read_text(encoding="utf-8").split()[0]
for name in ("INPUT.md", "OWNER_INVOCATION.txt", "AUTHORISED_PROMPT.md", "AUDIT.md", "CLOSEOUT.md"):
    assert (ROOT/"sessions/S006"/name).is_file()
assert (ROOT/"sessions/S007/AUTHORISED_PROMPT.md").read_text(encoding="utf-8") in (ROOT/"sessions/S006/CLOSEOUT.md").read_text(encoding="utf-8")
assert (ROOT/"sessions/S006/AUTHORISED_PROMPT.md").read_text(encoding="utf-8") in (ROOT/"sessions/S005/CLOSEOUT.md").read_text(encoding="utf-8")
grammar=load("evidence/S006/grammar_verification.json")
assert len(grammar["cases"]) == 153 and grammar["all_grammar_bounds_and_legal_derivations"]
assert all(c["all_equal"] for c in grammar["cases"])
assert sum(c["finite_cells"] for c in grammar["cases"]) == 2145
assert sum(c["production_inequalities"] for c in grammar["cases"]) == 30347
assert sha256_lzma(ROOT/"evidence/S006/grammar_certificates.json.xz") == grammar["certificate_sha256"]
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
    assert sha256_file(ROOT/info['snapshot'])==info['sha256']
for line in (ROOT/"evidence/S006/HASHES.md").read_text(encoding="utf-8").splitlines():
    m=re.fullmatch(r"`([0-9a-f]{64})`\s+`([^`]+)`",line.strip())
    if m:
        historical=ROOT/frozen6.get(m.group(2),m.group(2))
        if executed14 and m.group(2)=='.gitattributes':
            assert m.group(1)=='7a49bb6909edb009cdeae26a1fe0c24997695a097bffbb416e97ce838ade111e'
            historical=ROOT/('evidence/S014/frozen_gitattributes_'+m.group(1)+'.txt')
        assert sha256_file(historical)==m.group(1),m.group(2)
        checked6.add(m.group(2))
required6={p.relative_to(ROOT).as_posix() for folder in ("sessions/S006","evidence/S006") for p in (ROOT/folder).glob("*") if p.is_file() and p.name != "HASHES.md"}
required6 |= {p.relative_to(ROOT).as_posix() for p in (ROOT/"tools").glob("s006*.py")}
assert required6 <= checked6 and len(checked6)>=40
for rel in required6:
    if not rel.endswith('.xz'):
        assert b'\r\n' not in (ROOT/rel).read_bytes(),rel
assert 'eol=lf' in (ROOT/'.gitattributes').read_text(encoding="utf-8")
if executed14:
    current_attributes=(ROOT/'.gitattributes').read_text(encoding='utf-8')
    for frozen_scope in ['evidence/S014/** -text','sessions/S014/** -text','tools/s014* -text','research/S014*.md -text']:
        assert frozen_scope in current_attributes
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
    assert sha256_file(ROOT/f'sessions/S007/{name}.md')==(ROOT/f'sessions/S007/{name}.sha256').read_text().split()[0]
for stem,goal,counts in [('tail','clear',(36,81763,15251,316569,[4,10,22])),('stack_tail','stack',(28,20876,5025,73132,[4,8,16]))]:
    data=load(f'evidence/S007/{stem}_layers.json');verified=load(f'evidence/S007/{stem}_verification.json')
    layers,states,traces,moves,thresholds=counts
    assert [r['length'] for r in data['graphs']]==[0,1,2]
    assert [r['threshold'] for r in data['graphs']]==thresholds
    assert sum(len(r['layers']) for r in data['graphs'])==layers
    assert sum(t['configurations'] for r in data['graphs'] for t in r['layers'])==states
    assert verified['all_verified'] and verified['goal']==goal
    assert (verified['full_reverse_layer_matches'],verified['complete_configurations'],verified['independent_legal_traces'],verified['legal_moves'])==(layers,states,traces,moves)
    assert sha256_lzma(ROOT/f'evidence/S007/{stem}_traces.json.xz')==data['trace_raw_sha256']
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
    assert sha256_file(ROOT/info['snapshot'])==info['sha256']
checked7=set()
for line in (ROOT/'evidence/S007/HASHES.md').read_text(encoding='utf-8').splitlines():
    m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
    if m:
        assert sha256_file(ROOT/frozen7.get(m[2],m[2]))==m[1],m[2]
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
    assert sha256_file(ROOT/f'sessions/S008/{name}.md')==(ROOT/f'sessions/S008/{name}.sha256').read_text().split()[0]
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
assert sha256_lzma(ROOT/'evidence/S008/branch_traces.json.xz')==branch['trace_raw_sha256']
for c in claims:
    if c['id'] in ('CLM-0062','CLM-0063','CLM-0064','CLM-0065'):assert c['status']=='PROGRAMME_PROVED'
    if c['id'] in ('CLM-0066','CLM-0067'):assert c['status']=='COMPUTED_EXACT'
checked8=set()
for line in (ROOT/'evidence/S008/HASHES.md').read_text(encoding='utf-8').splitlines():
    m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
    if m:
        assert sha256_file(ROOT/m[2])==m[1],m[2]
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
assert state['phases']['2']['status']==('OWNER_WAIVED' if (ROOT/'authoritative/HANDOFF_REVISION_S019.json').exists() else 'NOT_STARTED')
future10=(ROOT/'sessions/S009/FUTURE_S010.md').read_text(encoding='utf-8')
assert future10==(ROOT/'sessions/S010/AUTHORISED_PROMPT.md').read_text(encoding='utf-8')
assert future10 in (ROOT/'sessions/S009/CLOSEOUT.md').read_text(encoding='utf-8')
assert (ROOT/'sessions/S009/INPUT.md').read_text(encoding='utf-8')=='Run this session\n\n'+old_prompt
for name in ('PLAN','PLAN_AMENDMENT_1','PLAN_AMENDMENT_2'):
    assert sha256_file(ROOT/f'sessions/S009/{name}.md')==(ROOT/f'sessions/S009/{name}.sha256').read_text().split()[0]
for i,digest in ((1,'8d05ff6b0f972d23260571dd6881aa4a47c3458942ac8389bb63d15d4dbe370a'),(2,'cbe9d2c29a8b1776e751c0b9a953295421f3cb7a7d0ed0c47b2ce06aae8bf6c2')):
    assert sha256_file(ROOT/f'sessions/S009/PLAN_AMENDMENT_{i}_INITIAL.md')==digest
assert len(load('evidence/S009/cold_checks.json'))==15
assert all(r['exit_code']==0 and r['resource_failure'] is None for r in load('evidence/S009/cold_checks.json'))
pv=json.loads(lzma.decompress((ROOT/'evidence/S009/port_verification.json.xz').read_bytes()));pr=load('evidence/S009/port_results.json')
assert pv['all_verified'] and pv['complete_cases']==len(pv['cases'])==len(pr['cases'])==318
assert (pv['total_closure_states'],pv['maximum_closure_states'],pv['rooted_winning_traces'])==(53924,3409,1694)
assert pv['marked_forest']['affected_components']==3
assert sha256_file(ROOT/'evidence/S009/port_inputs.json')==pr['input_sha256']
for a,b in zip(pr['cases'],pv['cases']):
    assert (a['id'],a['clear_mask'],a['stack_mask'])==(b['id'],b['clear_mask'],b['stack_mask'])
cv=load('evidence/S009/credit_verification.json');cu=load('evidence/S009/credit_upper.json')
assert cv['all_verified'] and (cv['complete_layers'],cv['complete_configurations'],cv['upper_traces'],cv['literal_moves'],cv['protected_B3_trees'],cv['threshold_claims'])==(33,13088,3860,41800,795,0)
assert (cu['traces'],cu['moves'])==(3860,41800)
assert sha256_lzma(ROOT/'evidence/S009/credit_traces.json.xz')==cu['trace_raw_sha256']
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
    assert sha256_file(ROOT/r['command'][1])==r['code_sha256']
checked9=set()
for line in (ROOT/'evidence/S009/HASHES.md').read_text(encoding='utf-8').splitlines():
    m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
    if m:
        assert sha256_file(ROOT/m[2])==m[1],m[2]
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
    assert sha256_file(ROOT/f'sessions/S010/{name}.md')==(ROOT/f'sessions/S010/{name}.sha256').read_text().split()[0]
for filename in ('campaign_preflight','campaign2_preflight','campaign3_preflight'):
    preflight=load(f'evidence/S010/{filename}.json')
    assert preflight['execution']=='NOT_YET_RUN'
    for p,digest in preflight['files'].items():assert sha256_file(ROOT/p)==digest,p
cold10=load('evidence/S010/cold_checks.json')
assert len(cold10)==19 and all(r['exit_code']==0 and r['resource_failure'] is None for r in cold10)
assert sum(r['seconds'] for r in cold10)<1800
for r in cold10:assert sha256_file(ROOT/r['command'][1])==r['code_sha256']
count10=load('evidence/S010/count_summary.json');vcount10=load('evidence/S010/count_verification.json')
assert vcount10['all_verified'] and (count10['certificates'],count10['connected'],count10['weak_only'])==(37556,26274,3856)
assert (vcount10['certificates'],vcount10['legal_exact_count_traces'],vcount10['weak_failures'])==(37556,26274,3856)
for file,key in [('count_certificates','certificate_raw_sha256'),('count_traces','trace_raw_sha256'),('count_closures','closure_raw_sha256')]:
    owner=count10 if file=='count_certificates' else vcount10
    assert sha256_lzma(ROOT/f'evidence/S010/{file}.json.xz')==owner[key]
root10=load('evidence/S010/root_summary.json');vroot10=load('evidence/S010/root_verification.json')
assert vroot10['all_verified'] and (root10['case_count'],root10['complete_layers'],root10['complete_configurations'])==(14,136,125481)
assert (vroot10['complete_layers'],vroot10['complete_configurations'],vroot10['literal_insertion_root_traces'],vroot10['literal_moves'])==(136,125481,930,7703)
assert all(r['critical_empty_insertion_intersection']==r['occupied_self_failure_configs']==r['heavy_self_failure_configs']==0 for r in root10['cases'])
assert next(r for r in root10['cases'] if r['graph']=='C5' and r['goal']=='stack')['whole_threshold_common_roots']==0
for file,owner,key in [('root_tables',root10,'table_raw_sha256'),('root_traces',vroot10,'trace_raw_sha256')]:
    assert sha256_lzma(ROOT/f'evidence/S010/{file}.json.xz')==owner[key]
ref10=load('evidence/S010/reflection_summary.json');vref10=load('evidence/S010/reflection_verification.json')
assert vref10['all_verified'] and (ref10['original_three_pile_traces'],ref10['marked_cases'],ref10['reflected_moves'],ref10['empty_marked_paths'])==(7289,21707,98878,2642)
assert (vref10['marked_cases'],vref10['reflected_literal_moves'],vref10['distinct_deleted_inputs'],vref10['complete_closure_states'],vref10['maximum_closure_states'])==(21707,98878,1447,60868,122)
assert sha256_lzma(ROOT/'evidence/S010/reflection_traces.json.xz')==ref10['output_raw_sha256']
assert ref10['input_trace_raw_sha256']==vcount10['trace_raw_sha256']
for name in ('count','root','reflection'):
    for kind in ('producer','checker'):
        log=load(f'evidence/S010/{name}_{kind}_log.json')
        assert log['exit_code']==0 and log['resource_failure'] is None and log['seconds']<600 and log['peak_working_set_bytes']<=2*1024**3
        assert sha256_file(ROOT/log['command'][1])==log['code_sha256']
for ident in ('2604.22341','2610.09650','2609.31811'):
    assert load('evidence/S010/source_refresh.json')[ident]['pdf_sha256']==refresh9[ident]['pdf_sha256']
checked10=set()
for line in (ROOT/'evidence/S010/HASHES.md').read_text(encoding='utf-8').splitlines():
    m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
    if m:
        assert sha256_file(ROOT/m[2])==m[1],m[2]
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
    assert sha256_file(ROOT/f'sessions/S011/{name}.md')==(ROOT/f'sessions/S011/{name}.sha256').read_text().split()[0]
for number in (1,2,3):
    pre=load(f'evidence/S011/campaign{number}_preflight.json')
    assert pre['execution']=='NOT_YET_RUN' and pre['limits']=={'seconds_each':600,'states_per_layer':300000,'peak_bytes':2*1024**3}
    for p,digest in pre['files'].items():assert sha256_file(ROOT/p)==digest,p
    assert f'sessions/S011/PLAN_AMENDMENT_{number}.md' in pre['files']
cold11=load('evidence/S011/cold_checks.json');local11=load('evidence/S011/local_checks.json')
assert len(cold11)==25 and len(local11)==6
for row in cold11+local11:
    assert row['exit_code']==0 and row['resource_failure'] is None and row['seconds']<600 and row['peak_working_set_bytes']<=2*1024**3
    assert sha256_file(ROOT/row['command'][1])==row['code_sha256']
for tool in ['s011_trees','s011_trees_verify','s011_transport','s011_transport_verify','s011_root_types','s011_root_types_verify']:
    row=load(f'evidence/S011/{tool}_log.json')
    assert row['exit_code']==0 and row['resource_failure'] is None and row['seconds']<600 and row['peak_working_set_bytes']<=2*1024**3
    assert sha256_file(ROOT/row['command'][1])==row['code_sha256']
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
assert sha256_file(ROOT/'evidence/S011/root_types.json')==vr11['result_sha256']
odd11=load('evidence/S011/odd_cycle_failure.json')
assert odd11['c']==[4,1,1,1,1] and odd11['clear_mask']==0 and odd11['three_mask']==31 and len(odd11['closure'])==70
for file,owner,key in [('tree_tables',t11,'table_raw_sha256'),('tree_traces',vt11,'trace_raw_sha256'),('tree_negative_closures',vt11,'negative_raw_sha256'),('transport_certificates',p11,'table_raw_sha256'),('transport_traces',vp11,'trace_raw_sha256'),('triangle_repairs',vp11,'repair_raw_sha256')]:
    assert sha256_lzma(ROOT/f'evidence/S011/{file}.json.xz')==owner[key]
refresh11=load('evidence/S011/source_refresh.json')
for ident in ['2604.22341','2610.09650','2609.31811']:
    assert refresh11[ident]['pdf_sha256']==load('evidence/S010/source_refresh.json')[ident]['pdf_sha256']
assert refresh11['1501.04245']['current_version']=='3'
checked11=set()
for line in (ROOT/'evidence/S011/HASHES.md').read_text(encoding='utf-8').splitlines():
    m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
    if m:
        assert sha256_file(ROOT/m[2])==m[1],m[2]
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
assert s12['cold_s011_audit']=='PASS_S012_AT_STATED_SCOPES' and s12['cold_new_proofs']=='PASS_S013_AT_STATED_SCOPES'
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
    assert sha256_file(ROOT/revision['prior_prompt'])==revision['prior_sha256']
    revised=(ROOT/revision['current_prompt']).read_bytes()
    request=(ROOT/revision['owner_request']).read_bytes()
    assert hashlib.sha256(revised).hexdigest()==revision['current_sha256']
    assert hashlib.sha256(request).hexdigest()==revision['owner_request_sha256']
    assert (ROOT/'sessions/S013/AUTHORISED_PROMPT.md').read_bytes()==revised and state['entry_handoff_revision']==revision
    assert b'\r\n' not in revised and b'\r\n' not in request
    assert "Don't stop at one or two milestones" in request.decode('utf-8')
    for requirement in ['L_all(G) <= L_AS(G)','Do not stop after one or two milestones',
                        'GLOBAL Q','delta0, delta1 and delta>=2','Local execution',
                        'PRIOR hashed bounded amendments','Stop before S014']:
        assert requirement in revised.decode('utf-8'),requirement
else:
    assert next_prompt==future13
assert 'FUTURE, UNEXECUTED' in future13 and 'Stop before S014' in future13
actual12=(ROOT/'sessions/S012/OWNER_INVOCATION.txt').read_text(encoding='utf-8')
assert actual12=='Run the next session\n'
assert hashlib.sha256(actual12.encode()).hexdigest()==load('evidence/S012/environment.json')['invocation_sha256']
for name in ['PLAN']+[f'PLAN_AMENDMENT_{i}' for i in range(1,6)]:
    assert sha256_file(ROOT/f'sessions/S012/{name}.md')==(ROOT/f'sessions/S012/{name}.sha256').read_text().split()[0]
for i in (1,2,3):
    pre=load(f'evidence/S012/campaign{i}_preflight.json')
    for p,digest in pre['files'].items():assert sha256_file(ROOT/p)==digest,p
initial12=load('evidence/S012/campaign1_initial_preflight.json')
for suffix in ['reciprocity','reciprocity_verify']:
    assert sha256_file(ROOT/f'evidence/S012/failed_initial_{suffix}.py')==initial12['files'][f'tools/s012_{suffix}.py']
failed12=load('evidence/S012/failed_zero_base_normal_form_log.json')
assert failed12['exit_code']!=0 and 'AssertionError' in failed12['stderr'] and failed12['resource_failure'] is None
cold12=load('evidence/S012/cold_checks.json');local12=load('evidence/S012/local_checks.json')
assert len(cold12)==12 and len(local12)==6
for row in cold12+local12:
    assert row['exit_code']==0 and row['resource_failure'] is None and row['seconds']<600 and row['peak_working_set_bytes']<=2*1024**3
    assert sha256_file(ROOT/row['command'][1])==row['code_sha256']
for tool in ['s012_reciprocity','s012_reciprocity_verify','s012_escape','s012_escape_verify','s012_exceptions','s012_exceptions_verify']:
    row=load(f'evidence/S012/{tool}_log.json')
    assert row['exit_code']==0 and row['resource_failure'] is None and row['seconds']<600 and row['peak_working_set_bytes']<=2*1024**3
    assert sha256_file(ROOT/row['command'][1])==row['code_sha256']
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
        assert sha256_file(ROOT/m[2])==m[1],m[2]
        checked12.add(m[2])
required12={p.relative_to(ROOT).as_posix() for folder in ['sessions/S012','evidence/S012'] for p in (ROOT/folder).glob('*') if p.is_file() and p.name!='HASHES.md'}
required12|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s012*.py')}
required12|={p.relative_to(ROOT).as_posix() for p in (ROOT/'research').glob('S012*.md')}
assert required12<=checked12
for rel in required12:
    if not rel.endswith('.xz'):assert b'\r\n' not in (ROOT/rel).read_bytes(),rel
for c in claims:
    if c['id'] in {f'CLM-{i:04d}' for i in [104,105,106,107,108,109,113]}:assert c['status']=='PROGRAMME_PROVED' and c['cold_audit']=='PASS_S013_AT_STATED_SCOPES'
    if c['id'] in {f'CLM-{i:04d}' for i in [103,110,111,112]}:assert c['status']=='COMPUTED_EXACT'
print(f'S012 historical scopes and {len(checked12)} immutable hashes: PASS (cold challenge S013 at stated scopes).')

# S013 exact configuration reduction, not a universal or kernel theorem.
assert state['s013']==spec['s013']
s13=state['s013']
assert s13['universal_stack']==s13['universal_clear']=='OPEN'
assert s13['cold_s012_audit']=='PASS_S013_AT_STATED_SCOPES'
assert s13['cold_new_proofs']==('PASS_S014_AT_STATED_SCOPES' if executed14 else 'FUTURE_S014')
assert s13['formal_status']=='NOT_STARTED' and s13['inherited_cutoffs_unchanged']
future14=(ROOT/'sessions/S013/FUTURE_S014.md').read_bytes()
assert future14.decode() in (ROOT/'sessions/S013/CLOSEOUT.md').read_text(encoding='utf-8')
prior14=dict(session='S014',status='FUTURE_UNEXECUTED',path='sessions/S013/FUTURE_S014.md',sha256=hashlib.sha256(future14).hexdigest())
if active14:
    assert next_prompt.startswith('# S014 ACTIVE continuation') and next_prompt.encode().endswith(future14)
    assert state['next_session_handoff'] is None and state['consumed_prospective_handoff']==prior14
elif closed15:
    future15=(ROOT/'sessions/S014/FUTURE_S015.md').read_bytes()
    assert future15.decode() in (ROOT/'sessions/S014/CLOSEOUT.md').read_text(encoding='utf-8')
    assert (ROOT/'sessions/S015/AUTHORISED_PROMPT.md').read_bytes()==future15
    prior15=dict(session='S015',status='FUTURE_UNEXECUTED',path='sessions/S014/FUTURE_S015.md',sha256=hashlib.sha256(future15).hexdigest())
    future16=(ROOT/'sessions/S015/FUTURE_S016.md').read_bytes()
    assert future16.decode() in (ROOT/'sessions/S015/CLOSEOUT.md').read_text(encoding='utf-8')
    rev16_path=ROOT/'authoritative/HANDOFF_REVISION_S016.json'
    if rev16_path.exists():
        # Owner-directed administrative revision of the prospective S016 handoff; S015 bytes unchanged.
        rev16=load('authoritative/HANDOFF_REVISION_S016.json')
        assert rev16['schema']==1 and rev16['kind']=='OWNER_DIRECTED_FUTURE_HANDOFF_REVISION' and rev16['session']=='S016' and rev16['status']=='FUTURE_UNEXECUTED'
        assert rev16['prior_prompt']=='sessions/S015/FUTURE_S016.md' and rev16['prior_sha256']==hashlib.sha256(future16).hexdigest()
        revised16=(ROOT/rev16['current_prompt']).read_bytes(); request16=(ROOT/rev16['owner_request']).read_bytes()
        assert hashlib.sha256(revised16).hexdigest()==rev16['current_sha256'] and hashlib.sha256(request16).hexdigest()==rev16['owner_request_sha256']
        assert request16==b'Rewrite the next session to first recheck stack and then move on to clear if it survives.\n'
        assert state['handoff_revision_s016']==rev16
        if closed16:
            # S016 executed the owner-revised prompt; its frozen copy is AUTHORISED_PROMPT.md.
            assert (ROOT/'sessions/S016/AUTHORISED_PROMPT.md').read_bytes()==revised16
            prior16=dict(session='S016',status='FUTURE_UNEXECUTED',path=rev16['current_prompt'],sha256=rev16['current_sha256'])
        else:
            assert next_prompt.encode()==revised16
            assert state['next_session_handoff']==dict(session='S016',status='FUTURE_UNEXECUTED',path=rev16['current_prompt'],sha256=rev16['current_sha256'])
        for requirement in ['Gate 1','Gate 2','only if Gate 1 passes','do NOT proceed to CLEAR','critical ASH*-CLEAR']:
            assert requirement in revised16.decode('utf-8'),requirement
    else:
        assert next_prompt.encode()==future16
        assert state['next_session_handoff']==dict(session='S016',status='FUTURE_UNEXECUTED',path='sessions/S015/FUTURE_S016.md',sha256=hashlib.sha256(future16).hexdigest())
    assert state['active_session'] is None
    if closed16:
        future17=(ROOT/'sessions/S016/FUTURE_S017.md').read_bytes()
        assert future17.decode() in (ROOT/'sessions/S016/CLOSEOUT.md').read_text(encoding='utf-8')
        assert closed17 or state['consumed_prospective_handoff']==prior16
        rev17_path=ROOT/'authoritative/HANDOFF_REVISION_S017.json'
        if rev17_path.exists():
            # Owner-directed administrative revision of the prospective S017 handoff; S016 bytes unchanged.
            rev17=load('authoritative/HANDOFF_REVISION_S017.json')
            assert rev17['schema']==1 and rev17['kind']=='OWNER_DIRECTED_FUTURE_HANDOFF_REVISION' and rev17['session']=='S017' and rev17['status']=='FUTURE_UNEXECUTED'
            assert rev17['prior_prompt']=='sessions/S016/FUTURE_S017.md' and rev17['prior_sha256']==hashlib.sha256(future17).hexdigest()
            revised17=(ROOT/rev17['current_prompt']).read_bytes(); request17=(ROOT/rev17['owner_request']).read_bytes()
            assert hashlib.sha256(revised17).hexdigest()==rev17['current_sha256'] and hashlib.sha256(request17).hexdigest()==rev17['owner_request_sha256']
            assert request17.startswith(b'Write the next session prompt as being a long ambitious session;\n') and b'palomar register' in request17
            assert state['handoff_revision_s017']==rev17
            if closed17:
                # S017 executed the owner-revised prompt; its frozen copy is AUTHORISED_PROMPT.md.
                assert (ROOT/'sessions/S017/AUTHORISED_PROMPT.md').read_bytes()==revised17
                assert closed18 or state['consumed_prospective_handoff']==dict(session='S017',status='FUTURE_UNEXECUTED',path=rev17['current_prompt'],sha256=rev17['current_sha256'])
            else:
                assert next_prompt.encode()==revised17
                assert state['next_session_handoff']==dict(session='S017',status='FUTURE_UNEXECUTED',path=rev17['current_prompt'],sha256=rev17['current_sha256'])
                assert state['phases']['3']['status']=='NOT_STARTED' and state['lean_status']=='NOT_STARTED'
            for requirement in ['Milestone 1','cold re-check of the G9 CLEAR counterexample','Palomar','lean-toolchain','Freeze green modules','full `lake build`','BEGIN Lean formalisation']:
                assert requirement in revised17.decode('utf-8'),requirement
        else:
            assert not closed17
            assert next_prompt.encode()==future17
            assert state['next_session_handoff']==dict(session='S017',status='FUTURE_UNEXECUTED',path='sessions/S016/FUTURE_S017.md',sha256=hashlib.sha256(future17).hexdigest())
        assert 'FUTURE, UNEXECUTED' in next_prompt and (('Stop before S021' if closed19 else 'Stop before S020' if closed18 else 'Stop before S019') if closed17 else 'Stop before S018') in next_prompt
        assert (ROOT/'sessions/S016/OWNER_INVOCATION.txt').read_bytes()==b'run next session\n'
        if closed17:
            future18=(ROOT/'sessions/S017/FUTURE_S018.md').read_bytes()
            assert future18.decode() in (ROOT/'sessions/S017/CLOSEOUT.md').read_text(encoding='utf-8')
            assert (ROOT/'sessions/S017/OWNER_INVOCATION.txt').read_bytes()==b'run next session\n'
            if closed18:
                # S018 executed the S017 prospective handoff unchanged; its frozen copy is AUTHORISED_PROMPT.md.
                assert (ROOT/'sessions/S018/AUTHORISED_PROMPT.md').read_bytes()==future18
                assert closed19 or state['consumed_prospective_handoff']==dict(session='S018',status='FUTURE_UNEXECUTED',path='sessions/S017/FUTURE_S018.md',sha256=hashlib.sha256(future18).hexdigest())
                assert (ROOT/'sessions/S018/OWNER_INVOCATION.txt').read_bytes()==b'run next session\n'
                future19=(ROOT/'sessions/S018/FUTURE_S019.md').read_bytes()
                assert future19.decode() in (ROOT/'sessions/S018/CLOSEOUT.md').read_text(encoding='utf-8')
                rev19_path=ROOT/'authoritative/HANDOFF_REVISION_S019.json'
                if rev19_path.exists():
                    # Owner-directed administrative revision of the prospective S019 handoff; S018 bytes unchanged.
                    rev19=load('authoritative/HANDOFF_REVISION_S019.json')
                    assert rev19['schema']==1 and rev19['kind']=='OWNER_DIRECTED_FUTURE_HANDOFF_REVISION' and rev19['session']=='S019' and rev19['status']=='FUTURE_UNEXECUTED'
                    assert rev19['prior_prompt']=='sessions/S018/FUTURE_S019.md' and rev19['prior_sha256']==hashlib.sha256(future19).hexdigest()
                    revised19=(ROOT/rev19['current_prompt']).read_bytes(); request19=(ROOT/rev19['owner_request']).read_bytes()
                    assert hashlib.sha256(revised19).hexdigest()==rev19['current_sha256'] and hashlib.sha256(request19).hexdigest()==rev19['owner_request_sha256']
                    assert request19.startswith(b'License can be apache, ai name can be claude and codex.') and b'Skip novelty audit' in request19 and b'palomar packing' in request19
                    assert state['handoff_revision_s019']==rev19 and rev19['owner_decisions']['license']=='Apache-2.0'
                    if closed19:
                        # S019 executed the owner-revised prompt; its frozen copy is AUTHORISED_PROMPT.md.
                        assert (ROOT/'sessions/S019/AUTHORISED_PROMPT.md').read_bytes()==revised19
                        assert (ROOT/'sessions/S019/OWNER_INVOCATION.txt').read_bytes()==b'Run next session\n'
                        assert state['consumed_prospective_handoff']==dict(session='S019',status='FUTURE_UNEXECUTED',path=rev19['current_prompt'],sha256=rev19['current_sha256'])
                        future20=(ROOT/'sessions/S019/FUTURE_S020.md').read_bytes()
                        assert future20.decode() in (ROOT/'sessions/S019/CLOSEOUT.md').read_text(encoding='utf-8')
                        assert next_prompt.encode()==future20 and b'owner will dictate' in future20
                        assert state['next_session_handoff']==dict(session='S020',status='FUTURE_UNEXECUTED',path='sessions/S019/FUTURE_S020.md',sha256=hashlib.sha256(future20).hexdigest())
                        assert not (ROOT/'sessions/S020').exists(), 'S020 remains unexecuted'
                    else:
                        assert next_prompt.encode()==revised19
                        assert state['next_session_handoff']==dict(session='S019',status='FUTURE_UNEXECUTED',path=rev19['current_prompt'],sha256=rev19['current_sha256'])
                    assert state['phases']['2']['status']==state['phases']['4']['status']=='OWNER_WAIVED'
                    for requirement in ['Apache-2.0','Claude','Codex','OWNER_WAIVED','500 MiB','module system','plain `lake build`','un-freeze','the owner uploads','No submission, registration, publication or contact']:
                        assert requirement in revised19.decode('utf-8'),requirement
                else:
                    assert next_prompt.encode()==future19
                    assert state['next_session_handoff']==dict(session='S019',status='FUTURE_UNEXECUTED',path='sessions/S018/FUTURE_S019.md',sha256=hashlib.sha256(future19).hexdigest())
                assert closed19 or not (ROOT/'sessions/S019').exists(), 'S019 remains unexecuted'
            else:
                assert next_prompt.encode()==future18
                assert state['next_session_handoff']==dict(session='S018',status='FUTURE_UNEXECUTED',path='sessions/S017/FUTURE_S018.md',sha256=hashlib.sha256(future18).hexdigest())
                assert not (ROOT/'sessions/S018').exists(), 'S018 remains unexecuted'
        else:
            assert not (ROOT/'sessions/S017').exists(), 'S017 remains unexecuted'
    else:
        assert state['consumed_prospective_handoff']==prior15
        assert 'FUTURE, UNEXECUTED' in next_prompt and 'Stop before S017' in next_prompt
    assert (ROOT/'sessions/S014/OWNER_CLOSEOUT.txt').read_bytes()==b'Can you commit and close out this session\n'
    assert (ROOT/'sessions/S015/OWNER_INVOCATION.txt').read_bytes()==b'Run a sustained attack on the next session, aim to resolve a major obligation or proof\n'
    assert closed16 or not (ROOT/'sessions/S016').exists(), 'S016 remains unexecuted'
elif closed14:
    future15=(ROOT/'sessions/S014/FUTURE_S015.md').read_bytes()
    assert next_prompt.encode()==future15
    assert future15.decode() in (ROOT/'sessions/S014/CLOSEOUT.md').read_text(encoding='utf-8')
    assert state['next_session_handoff']==dict(session='S015',status='FUTURE_UNEXECUTED',path='sessions/S014/FUTURE_S015.md',sha256=hashlib.sha256(future15).hexdigest())
    assert state['consumed_prospective_handoff']==prior14 and state['active_session'] is None
    assert 'FUTURE, UNEXECUTED' in next_prompt and 'Stop before S016' in next_prompt
    assert (ROOT/'sessions/S014/OWNER_CLOSEOUT.txt').read_bytes()==b'Can you commit and close out this session\n'
    assert state['s014']['owner_no_closeout_superseded'] is True
    assert sha256_file(ROOT/state['s014']['owner_closeout'])==state['s014']['owner_closeout_sha256']
    assert not (ROOT/'sessions/S015').exists(), 'S015 remains unexecuted'
else:
    assert next_prompt.encode()==future14 and state['next_session_handoff']==prior14
assert ('Stop before S021' if closed19 else 'Stop before S020' if closed18 else 'Stop before S019' if closed17 else 'Stop before S018' if closed16 else 'Stop before S017' if closed15 else 'Stop before S016' if closed14 else 'Stop before S015') in next_prompt and 'L_all(G) <= L_AS(G)' in next_prompt
assert (ROOT/'sessions/S013/OWNER_INVOCATION.txt').read_bytes()==b'Run the next session\n'
assert (ROOT/'sessions/S013/OWNER_CONTINUATION.txt').read_bytes()==b'Continue\n'
assert load('evidence/S013/environment.json')['invocation_sha256']==hashlib.sha256(b'Run the next session\n').hexdigest()
for name in ['PLAN']+[f'PLAN_AMENDMENT_{i}' for i in range(1,7)]:
    assert sha256_file(ROOT/f'sessions/S013/{name}.md')==(ROOT/f'sessions/S013/{name}.sha256').read_text().split()[0]
names13=['gap_scan','precision','concentration','full_exchange','residual','synthesis']
for i,name in enumerate(names13,1):
    pre=load(f'evidence/S013/{i}_preflight.json')
    for path,digest in pre['files'].items():assert sha256_file(ROOT/path)==digest,path
    for suffix in ('','_verify'):
        row=load(f'evidence/S013/s013_{name}{suffix}_log.json')
        assert row['exit_code']==0 and row['resource_failure'] is None and row['seconds']<600 and row['peak_working_set_bytes']<=2*1024**3
        assert sha256_file(ROOT/row['command'][1])==row['code_sha256']
for fname,total in [('cold_checks.json',18),('local_checks.json',12)]:
    rows=load('evidence/S013/'+fname);assert len(rows)==total
    for row in rows:
        assert row['exit_code']==0 and row['resource_failure'] is None and row['seconds']<600 and row['peak_working_set_bytes']<=2*1024**3
        assert sha256_file(ROOT/row['command'][1])==row['code_sha256']
v13=load('evidence/S013/precision_verification.json')
assert v13['configurations']==291639 and v13['graphs']==11 and v13['all_full_masks_and_diagnostics_equal']
c13=load('evidence/S013/concentration_verification.json');f13=load('evidence/S013/full_exchange_verification.json')
assert c13['open_implications']==313052 and c13['reconstructed_counts']==3437 and c13['gap1_first_successors']==20
assert f13['implications']==370252 and f13['small_STACK_exceptions']==13 and f13['CLEAR_exceptions']==0 and f13['count_reconstructions']==12239
r13=load('evidence/S013/residual_verification.json');z13=load('evidence/S013/synthesis_verification.json')
assert r13['archive_graphs']==189 and r13['archive_critical_losers']==1028 and r13['archive_adjacent_pairs']==8 and r13['archive_unknown']==0
assert r13['private_certificates']==12345 and r13['adjacent_small_transfer_tests']==85604
assert z13['full_losing_layers']==134 and z13['selected_extremizers']==614 and z13['restricted_comparisons']==17
for ident,result in load('evidence/S013/source_refresh.json').items():assert result['pdf_sha256']==load('evidence/S012/source_refresh.json')[ident]['pdf_sha256']
assert next(s for s in sources if s['id']=='SRC-0050')['pdf_sha256']==load('evidence/S013/additional_source.json')['pdf_sha256']
for c in claims:
    if c['id'] in {f'CLM-{i:04d}' for i in range(115,123)}:assert c['status']=='PROGRAMME_PROVED' and c['cold_audit']==('PASS_S014_AT_STATED_SCOPES' if executed14 else 'FUTURE_S014')
    if c['id'] in {f'CLM-{i:04d}' for i in [114,123,124,125,126,127,128]}:assert c['status']=='COMPUTED_EXACT'
checked13=set()
for line in (ROOT/'evidence/S013/HASHES.md').read_text(encoding='utf-8').splitlines():
    m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
    if m:
        assert sha256_file(ROOT/m[2])==m[1],m[2];checked13.add(m[2])
required13={p.relative_to(ROOT).as_posix() for folder in ['sessions/S013','evidence/S013'] for p in (ROOT/folder).glob('*') if p.is_file() and p.name!='HASHES.md'}
required13|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s013*.py')}
required13|={p.relative_to(ROOT).as_posix() for p in (ROOT/'research').glob('S013*.md')}
assert required13<=checked13
for p in required13:
    if not p.endswith('.xz'):assert b'\r\n' not in (ROOT/p).read_bytes(),p
print(f'S013 current scopes/mirrors and {len(checked13)} immutable hashes: PASS; universal STACK/CLEAR OPEN.')
if executed14:
    import lzma
    assert state['s014']['status']==('COMPLETED' if closed14 else 'IN_PROGRESS') and state['s014']['universal_stack']==state['s014']['universal_clear']=='OPEN'
    assert state['s014']['multiple_donor_argument']=='PROGRAMME_PROVED_71_NECESSARY_NOT_UNIVERSAL'
    assert state['s014']['new_local_proofs']==list(range(71,122))
    assert state['s014']['campaigns_completed']==list(range(1,82))
    assert state['s014']['campaigns_registered']==list(range(1,82))
    assert state['s014']['new_proof_assurance']=='LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING'
    assert state['s014']==load('research/ASH_SPEC.json')['s014']
    assert state['s014']['clear_gap1_candidate']=='UNPROVED'
    if active14:
        assert not (ROOT/'sessions/S014/CLOSEOUT.md').exists() and not (ROOT/'sessions/S014/FUTURE_S015.md').exists()
    assert (ROOT/'sessions/S014/AUTHORISED_PROMPT.md').read_bytes()==future14
    for name in ['PLAN']+[f'PLAN_AMENDMENT_{i}' for i in range(1,82)]:
        assert sha256_file(ROOT/f'sessions/S014/{name}.md')==(ROOT/f'sessions/S014/{name}.sha256').read_text().split()[0]
    cold14=load('evidence/S014/cold_checks.json');gap14=load('evidence/S014/gap_checks.json')
    assert len(cold14)==24 and len(gap14)==2
    for row in cold14+gap14:
        assert row['exit_code']==0 and row['resource_failure'] is None and row['seconds']<600 and row['peak_working_set_bytes']<=2*1024**3
        assert sha256_file(ROOT/row['command'][1])==row['code_sha256']
    diag=json.loads(lzma.decompress((ROOT/'evidence/S014/gap_extrema.json.xz').read_bytes()))
    assert len(diag['archive'])==44 and len(diag['precision'])==4 and diag['threshold_claims']==0
    assert not diag['negative_witnesses'] and all(all(r['predicates'].values()) for r in diag['archive']+diag['precision'])
    del diag
    for c in claims:
        if c['id'] in ['CLM-0129','CLM-0130']:assert c['status']=='COMPUTED_EXACT'
    for ident,result in load('evidence/S014/source_refresh.json').items():
        assert result['pdf_sha256']==load('evidence/S013/source_refresh.json')[ident]['pdf_sha256']
    print('S014 bounded plans and initial metadata: PASS; independently hashing all preflight references.', flush=True)
    for preflight in (ROOT/'evidence/S014').rglob('*preflight.json'):
        for path,digest in json.loads(preflight.read_bytes())['files'].items():
            assert sha256_file(versioned_tool_source(path,digest))==digest,(str(preflight),path)
    print('S014 all preflight references: PASS; validating preserved execution rows.', flush=True)
    execution_rows=0;preserved_failures=0
    for log in (ROOT/'evidence/S014').rglob('*checks.json'):
        rows=json.loads(log.read_bytes())
        if not isinstance(rows,list):
            assert log.name in ['entry_head_checks.json','entry_main_checks.json'];continue
        for row in rows:
            if log.relative_to(ROOT).as_posix()=='evidence/S014/parity_archive/checks.json':
                assert len(rows)==1 and row['exit_code']==1 and row['resource_failure'] is None and "KeyError: 'n'" in row['stderr']
                assert sha256_file(ROOT/row['command'][1])==row['code_sha256']
                assert (ROOT/'sessions/S014/REPAIR_17_1.md').exists()
                repair=load('evidence/S014/parity_archive/repair_checks.json');assert len(repair)==2 and all(r['exit_code']==0 for r in repair)
                preserved_failures+=1;continue
            if log.relative_to(ROOT).as_posix()=='evidence/S014/oddlarge/checks.json':
                assert len(rows)==1 and row['exit_code']==4294967295 and row['resource_failure'] is None
                assert sha256_file(ROOT/row['command'][1])==row['code_sha256']
                assert (ROOT/'sessions/S014/REPAIR_21_1.md').exists()
                assert not (ROOT/'evidence/S014/oddlarge/results.json.xz').exists()
                repaired=load('evidence/S014/oddlarge_v2/checks.json');assert len(repaired)==2 and all(r['exit_code']==0 for r in repaired)
                preserved_failures+=1;continue
            if log.relative_to(ROOT).as_posix()=='evidence/S014/cegis_orbits/C9a/checks.json':
                assert len(rows)==1 and row['exit_code']==4294967295 and row['resource_failure'] is None
                assert sha256_file(ROOT/row['command'][1])==row['code_sha256']
                assert (ROOT/'sessions/S014/REPAIR_38_1.md').exists()
                repaired=load('evidence/S014/cegis_orbits_v2/C9a/checks.json');assert len(repaired)==3 and all(r['exit_code']==0 for r in repaired)
                preserved_failures+=1;continue
            if log.relative_to(ROOT).as_posix()=='evidence/S014/even_extension/checks.json':
                assert len(rows)==1 and row['exit_code']==1 and row['resource_failure'] is None and 'AssertionError' in row['stderr']
                assert sha256_file(ROOT/row['command'][1])==row['code_sha256']
                assert (ROOT/'sessions/S014/REPAIR_49_1.md').exists()
                repaired=load('evidence/S014/even_extension_v2/checks.json');assert len(repaired)==2 and all(r['exit_code']==0 for r in repaired)
                preserved_failures+=1;continue
            if log.relative_to(ROOT).as_posix()=='evidence/S014/cube_dag/checks.json' and row['exit_code']!=0:
                assert len(rows)==2 and rows[0]['exit_code']==0 and row==rows[1] and row['exit_code']==1 and row['resource_failure'] is None and 'negative shift count' in row['stderr']
                assert sha256_file(ROOT/row['command'][1])==row['code_sha256']
                assert (ROOT/'sessions/S014/REPAIR_58_1.md').exists()
                repaired=load('evidence/S014/cube_dag/repair_checks.json');assert len(repaired)==1 and repaired[0]['exit_code']==0
                assert load('evidence/S014/cube_dag/verification_v2.json')['complete_AS_tail_upper31']
                preserved_failures+=1;continue
            if log.relative_to(ROOT).as_posix()=='evidence/S014/fano_AS/checks.json':
                assert len(rows)==1 and row['exit_code']==1 and row['resource_failure'] is None and 'AssertionError' in row['stderr']
                assert sha256_file(ROOT/row['command'][1])==row['code_sha256']
                assert (ROOT/'sessions/S014/REPAIR_65_1.md').exists()
                repaired=load('evidence/S014/fano_AS/repair_checks.json');assert len(repaired)==2 and all(r['exit_code']==0 for r in repaired)
                assert load('evidence/S014/fano_AS/verification.json')['exact_L_AS']==29
                preserved_failures+=1;continue
            if log.relative_to(ROOT).as_posix()=='evidence/S014/scope62_validation_checks.json':
                assert len(rows)==1 and row['exit_code']==1 and row['resource_failure'] is None and "split_preflight.json" in row['stderr'] and "tools/s014_split_verify.py" in row['stderr']
                assert row['code_sha256']=='6814b9918ae76442a142108712c1f54ee00aebb92c47b61f62f0e280d1a648f4'
                frozen=ROOT/('evidence/S014/frozen_validate_governance_'+row['code_sha256']+'.py.txt');assert sha256_file(frozen)==row['code_sha256']
                recovery=load('evidence/S014/split_source_recovery/verification.json');assert recovery['replayed_checks']==33 and recovery['all_output_bytes_unchanged']
                preserved_failures+=1;continue
            assert row['exit_code']==0 and row['resource_failure'] is None and row['seconds']<600 and row['peak_working_set_bytes']<=2*1024**3,str(log)
            source=versioned_tool_source(row['command'][1],row['code_sha256'])
            if log.relative_to(ROOT).as_posix() in ['evidence/S014/focus_governance_checks.json','evidence/S014/progress_checks.json']:
                assert row['command'][1]=='validation/validate_governance.py' and row['code_sha256']=='73f39438d20d5832a52c88f6bfb8af2cf1f6a2f3c74de7bd57222c5feba65feb'
                source=ROOT/'evidence/S014/frozen_pre_continuation_validate_governance.py.txt'
            elif row['command'][1]=='validation/validate_governance.py' and sha256_file(source)!=row['code_sha256']:
                source=ROOT/('evidence/S014/frozen_validate_governance_'+row['code_sha256']+'.py.txt')
            assert sha256_file(source)==row['code_sha256'],str(log)
            execution_rows+=1
    assert execution_rows>=2000 and preserved_failures==7
    for c in claims:
        if c['id'] in {f'CLM-{i:04d}' for i in list(range(131,145))+[153,154]}:
            assert c['status']=='PROGRAMME_PROVED' and c['cold_audit']=='LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING'
        if c['id'] in {f'CLM-{i:04d}' for i in range(145,153)}:assert c['status']=='COMPUTED_EXACT'
        if c['id'] in {f'CLM-{i:04d}' for i in range(155,160)}:assert c['status']=='COMPUTED_EXACT'
    assert load('evidence/S014/family_verification.json')['all_generated_keys_and_certificates_equal']
    assert load('evidence/S014/swap_verification.json')['failures']==1846
    assert load('evidence/S014/split_verification.json')['failures']==3
    for name,thresholds in [('theta334',[25,27]),('barbell55',[48,48])]:
        for goal,target in zip(['stack','clear'],thresholds):
            r=load(f'evidence/S014/{name}_{goal}_threshold_verification.json')
            assert r['threshold']==target and r['all_full_losing_layers_equal']
    buffers=load('evidence/S014/buffers/summary.json')
    assert len(buffers)==292 and sum(r['threshold'] is not None for r in buffers)==286
    assert all(r['threshold']==r['proposed_L_AS']+1 for r in buffers if r['goal']=='stack')
    assert sum(r['threshold'] is None for r in buffers)==6
    first=load('evidence/S014/firstfires/verification.json')
    assert sum(r['all_cells'] for r in first)==66642 and sum(r['true_extracted_path_covers'] for r in first)==10033
    witnesses=load('evidence/S014/firstfires/witnesses_verification.json')
    assert witnesses['explicit_STACK_AS_witnesses']==228 and witnesses['completed_CLEAR_boundaries']==6 and witnesses['old_full_losing_layers_preserved']
    paths=load('evidence/S014/joinpaths/verification.json')
    assert sum(r['traces'] for r in paths)==198320 and sum(r['literal_moves'] for r in paths)==2046597
    regular=load('evidence/S014/regular/extrema.json')
    assert [r['graph'] for r in regular]==['Q3plus03','Wagner8','Petersen10']
    assert [[r['goals'][goal]['threshold'] for goal in ['stack','clear']] for r in regular]==[[15,15],[11,11],[15,15]]
    parity=load('evidence/S014/parity/verification.json');assert parity['cases']==256 and parity['complete_parity_class_failures']==0
    archive=load('evidence/S014/parity_archive/verification.json');assert archive['cases']==343 and archive['nonAS_critical_inputs']==1043 and archive['all_receiver_failures']==2 and archive['heavy_receiver_failures']==8
    obstruction=load('evidence/S014/obstruction/verification.json')
    assert len(obstruction)==2 and sum(r['complete_negative_states'] for r in obstruction)==161 and sum(r['literal_moves'] for r in obstruction)==72
    assert all(r['threshold']==9 and r['all_parity_AS_winners']==6 and r['alpha']==2 and not r['increasing_Q_losing_unit_neighbors'] for r in obstruction)
    odd=load('evidence/S014/oddshift/verification.json')
    assert odd['tests']==34 and odd['losing_transforms']==28 and odd['eligible_critical_inputs']==14 and odd['all_transformations_win_failures']==0 and odd['ordered_pair_failures']==6
    assert state['s014']['owner_no_closeout']=='sessions/S014/OWNER_KEEP_GOING.txt'
    assert sha256_file(ROOT/state['s014']['owner_no_closeout'])==state['s014']['owner_no_closeout_sha256']
    headcrit=load('evidence/S014/headcritical/verification.json')
    assert headcrit['complete_thresholds']==252 and headcrit['failed_input_existence']==2 and headcrit['nonAS_global_Q_critical_inputs']==0
    assert load('evidence/S014/criticalcert/verification.json')['complete_negative_states']==2556
    assert load('evidence/S014/eliminate/verification.json')['failed_H2_inputs']==1124
    er=load('evidence/S014/eliminate_residual/verification.json');assert er['nonAS_critical_inputs']==1230 and er['failed_H2r_inputs']==0
    regular_elimination=load('evidence/S014/regular_eliminate/verification.json');assert regular_elimination['complete']==72 and regular_elimination['nonAS_critical_inputs']==227 and regular_elimination['H2r_failures']==0
    cp=load('evidence/S014/coupled/verification.json');assert cp['complete_inputs']==252 and cp['losing_inputs']==108 and cp['unknown']==0
    for name,T in [('C00_51',19),('C00_60',25)]:
        r=load(f'evidence/S014/coupled_threshold/{name}_stack_threshold_verification.json')
        assert r['threshold']==T and r['L_AS_grammar']==T-1 and r['all_full_losing_layers_equal']
    assert load('evidence/S014/coupled_threshold/eliminate/verification.json')['nonAS_critical_inputs']==0
    circ=load('evidence/S014/circulant/summary.json');assert len(circ)==120
    assert all(r['scope']=='EXACT_THRESHOLD' and r['all_full_losing_layers_equal'] and r['L_AS_exact']==r['threshold']-1 for r in circ)
    tails=[load(f'evidence/S014/tail_screen/shard{i}_verification.json') for i in range(8)]
    assert sum(r['cases'] for r in tails)==7510 and all(r['unknown']==0 and not r['potential_counterexamples'] for r in tails)
    assert load('evidence/S014/singleton/verification.json')['failures']==90
    sat=load('evidence/S014/saturate/verification.json');assert sat['complete_saturations']==120 and sat['all_greedy_decisions_and_saturation_certificates_checked']
    for name in ['C6','C9a','C9b']:
        r=load(f'evidence/S014/lrat/{name}/verification.json');assert r['fixed_input_class_exclusion_certified']
        assert load(f'evidence/S014/cegis_orbits_v2/{name}/clause_verification.json')['all_clauses_necessary_for_fixed_input_counterexample']
    for name in ['E8','M9']:assert load(f'evidence/S014/watched_drup/{name}/verification.json')['fixed_input_class_exclusion_certified']
    assert not load('evidence/S014/watched_drup/core_C9b/verification.json')['fixed_input_class_exclusion_certified']
    assert load('evidence/S014/trace_cegis/C10/result.json')['status']=='ITERATION_BOUND_UNKNOWN'
    ev=load('evidence/S014/critical_even/verification.json');assert ev['cases']==638 and ev['critical']==20231 and ev['nonAS']==17940 and ev['nonAS_with2']==0 and ev['even_heavy_inputs']==4 and ev['bipartite_even_heavy_inputs']==0
    assert state['s014']['universal_no2']=='UNPROVED_FINITE_AGREEMENT_CAM44'
    for c in claims:
        if c['id']=='CLM-0166':assert c['status']=='PROGRAMME_PROVED' and c['cold_audit']=='LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING'
        if c['id']=='CLM-0169':assert c['status']=='HEURISTIC'
    for folder,name in [('continued','F9'),('lex','E9')]:
        assert load(f'evidence/S014/{folder}_lrat/{name}/verification.json')['fixed_input_class_exclusion_certified']
    for name,patterns in [('N9_M11',45),('N10_M12',65),('N10_M17',257),('N12_M13',88),('N12_M16',212)]:
        r=load(f'evidence/S014/master_cegis/{name}/result.json');assert r['status'].endswith('UNKNOWN') and r['patterns']==patterns
        assert load(f'evidence/S014/master_cegis/{name}/clause_verification.json')['counterexample_exists_implies_formula_satisfiable']
    cm=load('evidence/S014/coordinate_maximal/verification.json')
    assert cm['full_negative_states']==56 and cm['literal_witnesses']==18 and cm['literal_moves']==202 and cm['thresholds']==[15,8,7,8] and cm['complete_selected_sets_equal']
    assert load('evidence/S014/fair_lrat/N2_M4/verification.json')['fixed_mass_graph_class_exclusion_certified']
    for name in ['N8_M10','N9_M11','N10_M12','N10_M17','N12_M13','N12_M16']:
        assert load(f'evidence/S014/fair_cegis/{name}/result.json')['status']=='ITERATION_BOUND_UNKNOWN'
        assert load(f'evidence/S014/fair_cegis/{name}/clause_verification.json')['counterexample_exists_implies_formula_satisfiable']
    ob=[load(f'evidence/S014/onebit/shard{i}/verification.json') for i in range(2)]
    assert sum(r['ordered_pairs'] for r in ob)==654 and sum(r['queries'] for r in ob)==5260 and sum(r['states'] for r in ob)==44991 and all(r['all_queries_match_exact_residue_cutoffs'] for r in ob)
    rt=load('evidence/S014/retract_trees/trees_verification.json');assert rt['isometric_trees']==2279 and rt['crown_maxima']==[15,16,19] and rt['all_retractions_true_loopless_edge_maps']
    cr=load('evidence/S014/retract_trees/crown5_stack_threshold_verification.json');assert cr['threshold']==16 and cr['L_AS_exact']==15 and cr['certified_losing_states']==28880
    combined=[load(f'evidence/S014/combined_bound/shard{i}/verification.json') for i in range(2)];assert sum(r['cases'] for r in combined)==49 and sum(r['full_isometric_tree_sets'] for r in combined)==6415
    gaps=[g for r in combined for g in r['strict_gaps']];assert len(gaps)==1 and gaps[0]['source']=='A182' and gaps[0]['threshold']==42 and gaps[0]['bound']==40
    mg=load('evidence/S014/metric_gap/negative_verification.json');assert mg['states']==10988 and mg['complete_legal_dependencies']==50423 and mg['negative_closures_equal']
    mt=load('evidence/S014/metric_gap/A182fresh_stack_threshold_verification.json');assert mt['threshold']==42 and mt['L_AS_exact']==41 and mt['all_full_losing_layers_equal']
    assert state['s014']['combined_tree_independence_ceiling']=='FALSE_CAM54_55_A182_THRESHOLD42_VS40'
    split=load('evidence/S014/split_cegis/summary.json');assert split['patterns']==split['certified']==32 and split['complete_mass10_order8_exclusion']
    for i in range(32):assert load(f'evidence/S014/split_lrat/P{i:02d}/verification.json')['fixed_input_class_exclusion_certified']
    direct=load('evidence/S014/cube_tail/verification.json');assert direct['status']=='STATE_CAP_UNKNOWN' and direct['completed_queries']==16931 and direct['verified_states']==2000000 and not direct['complete_AS_tail_upper31']
    dag=load('evidence/S014/cube_dag/verification_v2.json');assert dag['verified_nodes']==1572864 and dag['queries_examined']==98304 and dag['complete_AS_tail_upper31'] and dag['exact_L_AS']==30
    lower=load('evidence/S014/cube_lower/verification.json');assert lower['exact_binary_buffer_AS_oracle_certified'] and lower['full_inequalities']==803538796 and lower['exact_L_AS']==30 and len(lower['source0_critical_AS'])==1
    general=load('evidence/S014/cube_general/verification.json');assert general['status']=='GLOBAL_STATE_CAP_UNKNOWN' and general['winning_inputs']==2157 and general['unknown']==1 and not general['potential']
    point=[load(f'evidence/S014/cube_pointwise/shard{i}/verification.json') for i in range(2)];assert sum(r['literal_full_input_winners'] for r in point)==2393 and sum(r['unknown'] for r in point)==2 and all(r['all_positive_histories_verified'] and not r['potential'] for r in point)
    orbit=load('evidence/S014/cube_orbits/verification.json');assert orbit['status']=='COMPLETE_REGISTERED_CASES' and orbit['winning_inputs']==orbit['candidates_checked']==9783 and orbit['unknown']==0 and orbit['verified_states']==872261 and not orbit['potential']
    controls=load('evidence/S014/cube_layers/control_summary.json');assert controls['both_controls_pass'] and [r['threshold'] for r in controls['controls']]==[3,15]
    for d,M in [(1,3),(3,15)]:
        for m in range(1,M+1):assert load(f'evidence/S014/cube_layers/d{d}/mass{m}_verification.json')['all_full_orbit_losing_sets_equal']
    for m in range(1,14):assert load(f'evidence/S014/cube_layers/d4/mass{m}_verification.json')['all_full_orbit_losing_sets_equal']
    layer=load('evidence/S014/cube_layers/d4_summary.json');assert layer['status']=='CANDIDATE_CAP_UNKNOWN' and layer['threshold'] is None and layer['last_verified_mass']==13
    import gzip,struct
    for base,case,M,n in [('cube_layers_full','d4',31,16),('fano_layers','FanoInc14',30,14)]:
        summary=load(f'evidence/S014/{base}/{case}_summary.json');assert summary['status']=='EXACT_THRESHOLD' and summary['threshold']==summary['last_verified_mass']==M
        for m in range(1,M+1):
            row=load(f'evidence/S014/{base}/{case}/mass{m}_verification.json');assert row['all_full_orbit_losing_sets_equal'] and row['mass']==m and row['status']=='COMPLETE_LAYER_VERIFIED'
            if m==M:assert row['loser_orbits']==0 and M>n
        raw=gzip.decompress((ROOT/f'evidence/S014/{base}/{case}/mass{M-1}.bin.gz').read_bytes());assert struct.unpack('<IQ',raw[:12])==(M-1,1) and len(raw)==28
        c=list(raw[12:12+n]);assert sum(c)==M-1 and sum(a>=2 for a in c)==1
    for base in ['cube_layers_full','fano_layers']:
        controls=load(f'evidence/S014/{base}/control_summary.json');assert controls['both_controls_pass'] and [r['threshold'] for r in controls['controls']]==[3,15]
    fa=load('evidence/S014/fano_AS/verification.json');assert fa['exact_binary_buffer_AS_oracle_certified'] and fa['exact_L_AS']==29 and len(fa['source0_critical_AS'])==1
    shell=load('evidence/S014/shell_witness/verification.json');assert shell['all_shell_hypotheses_verified'] and shell['shell_rows']==501 and shell['complete_negative_queries']==350 and shell['states']==22920 and shell['unknown_queries']==0
    mass11=load('evidence/S014/mass11_cegis/summary.json');assert mass11['complete_mass11_order8_exclusion'] and mass11['patterns']==mass11['certified']==44 and mass11['verified_RUP_additions']==64781
    for i in range(44):assert load(f'evidence/S014/mass11_lrat/P{i:03d}/verification.json')['fixed_input_class_exclusion_certified']
    high=load('evidence/S014/highpile_cegis/summary.json');assert high['all_registered_patterns_independently_excluded'] and high['certified']==8 and high['verified_RUP_additions']==33677
    for row in high['cases']:assert load(f"evidence/S014/highpile_lrat/{row['case']}/verification.json")['fixed_input_class_exclusion_certified']
    slack=load('evidence/S014/mass_slack/verification.json');assert slack['complete_tested_prefix_verified'] and slack['inputs']==2946 and slack['cases']==18 and slack['failed_inputs']==1 and slack['independently_checked_failed_candidates']==12
    pool=load('evidence/S014/two_pool/verification.json');assert pool['complete_tested_prefix_verified'] and pool['inputs']==3097 and pool['cases']==21 and pool['failed_inputs']==1 and pool['independently_checked_failed_candidates']==60
    for c in claims:
        if c['id'] in ['CLM-0223','CLM-0228']:assert c['status']=='PROGRAMME_PROVED' and c['cold_audit']=='LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING'
    for c in claims:
        if c['id'] in {f'CLM-{i:04d}' for i in range(188,194)}:assert c['status']=='PROGRAMME_PROVED' and c['cold_audit']=='LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING'
    parity72=load('evidence/S014/bip_parity/verification.json');assert parity72['complete_all_candidate_memberships_equal'] and parity72['nonAS_inputs']==14814 and parity72['candidates']==203673 and parity72['all_source_failures']==parity72['heavy_source_failures']==0
    odd73=load('evidence/S014/bip_odd_slack/verification.json');assert odd73['complete_tested_prefix_verified'] and odd73['cases']==142 and odd73['bipartite_cases']==27 and odd73['inputs']==13297 and odd73['failed_inputs']==0
    odd74=load('evidence/S014/bip_odd_larger/summary.json');assert odd74['independently_completed_cases']==18 and odd74['prior_scope_unknown_cases']==3 and odd74['inputs']==1598711 and odd74['maximum_order']==14 and odd74['failed_inputs']==0
    assert {r['case'] for r in odd74['unknown']}=={'A171','A181','A184'} and all(r['status']=='PRIOR_SCOPE_CUTOFF_UNKNOWN' for r in odd74['unknown'])
    for r in odd74['completed']:
        q=load(f"evidence/S014/bip_odd_larger/{r['case']}/verification.json");assert q['status']=='COMPLETE_REGISTERED_CASES' and q['complete_tested_prefix_verified'] and q['failed_inputs']==0 and q['inputs']==r['inputs']
    leaf75=load('evidence/S014/leaf_ascent/verification.json');assert leaf75['all_input_leaf_extension_memberships_equal'] and leaf75['extensions']==33188 and leaf75['initially_empty_leaf_extensions']==3104 and leaf75['failures']==0
    neighbor76=load('evidence/S014/neighbor_ascent/verification.json');assert neighbor76['all_input_neighbor_inventories_and_memberships_equal'] and neighbor76['records']==83376 and neighbor76['extensions']==145073 and neighbor76['failed_input_vertex_pairs']==515 and neighbor76['failures_at_pile2']==74 and neighbor76['failures_at_actual_critical_mass']==0
    for c in claims:
        if c['id'] in {f'CLM-{i:04d}' for i in [230,234,235,236,239]}:assert c['status']=='PROGRAMME_PROVED' and c['cold_audit']=='LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING'
    twofuel=load('evidence/S014/twofuel_cegis/summary.json');assert twofuel['certified']==1 and twofuel['unknown']==3 and twofuel['control_pass'] and twofuel['verified_F8_RUP_additions']==1365
    assert [r['status'] for r in twofuel['cases']]==['INDEPENDENTLY_EXCLUDED','ITERATION_BOUND_UNKNOWN','ITERATION_BOUND_UNKNOWN','TIME_BOUND_UNKNOWN']
    assert load('evidence/S014/twofuel_lrat/F8/verification.json')['fixed_input_class_exclusion_certified']
    fullleaf=load('evidence/S014/full_leaf_ascent/verification.json');assert fullleaf['all_input_leaf_extension_memberships_equal'] and fullleaf['states']==167713 and fullleaf['extensions']==160579 and fullleaf['initially_empty_leaf_extensions']==22440 and fullleaf['failures']==0
    sourcefirst=load('evidence/S014/source_first/verification.json');assert sourcefirst['complete_predecessor_inventory_and_all_child_masks_equal'] and sourcefirst['predecessors']==598867 and sourcefirst['winning_multioccupied_inputs']==437350 and sourcefirst['heavy_sources']==1211093 and sourcefirst['child_tests']==2538712 and sourcefirst['failed_sources']==0
    oddleaf=load('evidence/S014/odd_leaf_contraction/verification.json');assert oddleaf['complete_both_direction_inventories_and_memberships_equal'] and oddleaf['records']==164058 and oddleaf['odd_leaf_down']==oddleaf['even_leaf_parent_up']==oddleaf['even_heavy_leaf_plus3']==54686 and oddleaf['failed_memberships']==oddleaf['critical_even_leafs']==0
    exchange=load('evidence/S014/sector_exchange/verification.json');assert exchange['complete_tested_prefix_and_all_exchange_options_equal'] and exchange['status']=='COMPLETE_REGISTERED_SCOPE' and exchange['registered_groups']==exchange['executed_groups']==2490 and exchange['unexecuted_groups']==0 and exchange['membership_queries']==57060 and exchange['pair_source_checks']==560 and not exchange['first_failure']
    for c in claims:
        if c['id'] in {f'CLM-{i:04d}' for i in [240,241,243,245,246,248]}:assert c['status']=='PROGRAMME_PROVED' and c['cold_audit']=='LOCAL_ADVERSARIAL_PASS_INDEPENDENT_REVIEW_PENDING'
    if closed14:
        print('S014 exact bounded summaries: PASS; independently hashing recursive final manifest.', flush=True)
        checked14=set()
        for line in (ROOT/'evidence/S014/HASHES.md').read_text(encoding='utf-8').splitlines():
            m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
            if m:
                assert sha256_file(ROOT/m[2])==m[1],m[2];checked14.add(m[2])
        excluded14={'HASHES.md','working_hashes.json','checkpoint_hashes.json','scope81_hash_cache.json','scope81_hash_progress.json'}
        required14={p.relative_to(ROOT).as_posix() for folder in ['sessions/S014','evidence/S014'] for p in (ROOT/folder).rglob('*') if p.is_file() and p.name not in excluded14}
        required14|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s014*') if p.is_file()}
        required14|={p.relative_to(ROOT).as_posix() for p in (ROOT/'research').glob('S014*.md')}
        assert required14==checked14, (sorted(required14-checked14)[:5],sorted(checked14-required14)[:5])
        print(f'S014 CLOSED scopes/preflights/{execution_rows} successful bounded rows, {preserved_failures} preserved failed attempts, {len(checked14)} immutable hashes: PASS; S015 FUTURE; universal STACK/CLEAR OPEN.')
    else:
        for p,digest in load('evidence/S014/working_hashes.json')['files'].items():assert sha256_file(ROOT/p)==digest,p
        print(f'S014 ACTIVE scopes/preflights/{execution_rows} successful bounded rows, {preserved_failures} preserved failed schema attempt: PASS; no closeout/S015/universal proof inferred.')

if closed15:
    s15=state['s015']
    assert s15==spec['s015'] and s15['status']=='COMPLETED'
    assert s15['universal_stack']=='REFUTED_COMPUTED_G9_COLD_RECHECK_AND_LEAN_PENDING' and s15['universal_clear']=='OPEN'
    assert s15['counterexample']['graph6']=='HCQTaXi' and s15['counterexample']['L_all']==14 and s15['counterexample']['L_AS']==13
    for name in ['PLAN']+[f'PLAN_AMENDMENT_{i}' for i in range(1,s15['amendments']+1)]:
        assert sha256_file(ROOT/f'sessions/S015/{name}.md')==(ROOT/f'sessions/S015/{name}.sha256').read_text().split()[0],name
    g9=load('evidence/S015/counterexample/summary.json')
    assert g9['K1'] and g9['K2'] and g9['K3'] and g9['K4'] and g9['author_code_critical_AS'] is False
    brute=load('evidence/S015/counterexample/brute_truth_table.json')
    assert brute['per_mass']['14']['losers']==2 and brute['per_mass']['14']['AS_losers']==0
    assert brute['per_mass']['15']['losers']==0 and brute['per_mass']['16']['losers']==0
    a8=load('evidence/S015/cam83/summary_order8.json');assert a8['graphs_listed']==a8['ASH_OK_DUAL']==11117 and a8['all_crit_identical']
    a9=load('evidence/S015/cam85/summary.json');assert a9['graphs_listed']==261080 and 'HCQTaXi' in a9['ASH_FAIL']
    for c in claims:
        if c['id'] in s15['claims_programme_proved']:assert c['status']=='PROGRAMME_PROVED'
        if c['id'] in s15['claims_computed']:assert c['status']=='COMPUTED_EXACT'
    checked15=set()
    for line in (ROOT/'evidence/S015/HASHES.md').read_text(encoding='utf-8').splitlines():
        m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
        if m:
            assert sha256_file(ROOT/m[2])==m[1],m[2];checked15.add(m[2])
    required15={p.relative_to(ROOT).as_posix() for folder in ['sessions/S015','evidence/S015'] for p in (ROOT/folder).rglob('*') if p.is_file() and p.name!='HASHES.md'}
    required15|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s015*') if p.is_file()}
    required15|={p.relative_to(ROOT).as_posix() for p in (ROOT/'research').glob('S015*.md')}
    assert required15==checked15,(sorted(required15-checked15)[:5],sorted(checked15-required15)[:5])
    print(f'S015 CLOSED: G9 critical STACK counterexample records, order<=8 dual atlas, order-9 atlas summary and {len(checked15)} immutable hashes: PASS; cold re-check/Lean pending; CLEAR OPEN; S016 FUTURE.')

if closed16:
    s16=state['s016']
    assert s16==spec['s016'] and s16['status']=='COMPLETED'
    assert s16['gate1']=='COLD_RECHECK_PASS' and s16['universal_stack']=='REFUTED_G9_COLD_RECHECK_PASS_LEAN_PENDING'
    assert s16['universal_clear']=='REFUTED_COMPUTED_G9_COLD_RECHECK_AND_LEAN_PENDING'
    for name in ['PLAN']+[f'PLAN_AMENDMENT_{i}' for i in range(1,s16['amendments']+1)]:
        assert sha256_file(ROOT/f'sessions/S016/{name}.md')==(ROOT/f'sessions/S016/{name}.sha256').read_text().split()[0],name
    g9c=load('evidence/S016/gate2/cam04/summary.json')
    assert g9c['K1c'] and g9c['K2c'] and g9c['K3c'] and g9c['K4c'] and g9c['L_all']==14 and g9c['L_AS']==13 and g9c['clear']==15
    a=load('evidence/S016/gate2/cam03/compare_8.json');assert a['graphs']==11117 and a['ASH_OK_count']==10935 and a['BIPARTITE_SKIP']==182 and not a['UNKNOWN'] and not a['DISAGREE'] and a['ASH_FAIL_count']==0
    a=load('evidence/S016/gate2/cam05/summary.json');assert a['graphs']==261080 and a['bipartite_skip']==730 and a['ash_fail']==['HCQTaXi']
    for c in claims:
        if c['id'] in s16['claims_programme_proved']:assert c['status']=='PROGRAMME_PROVED'
        if c['id'] in s16['claims_computed']:assert c['status']=='COMPUTED_EXACT'
    checked16=set()
    for line in (ROOT/'evidence/S016/HASHES.md').read_text(encoding='utf-8').splitlines():
        m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
        if m:
            assert sha256_file(ROOT/m[2])==m[1],m[2];checked16.add(m[2])
    required16={p.relative_to(ROOT).as_posix() for folder in ['sessions/S016','evidence/S016'] for p in (ROOT/folder).rglob('*') if p.is_file() and p.name!='HASHES.md'}
    required16|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s016*') if p.is_file()}
    required16|={p.relative_to(ROOT).as_posix() for p in (ROOT/'research').glob('S016*.md')}
    assert required16==checked16,(sorted(required16-checked16)[:5],sorted(checked16-required16)[:5])
    print(f'S016 CLOSED: G9 STACK cold re-check PASS, G9 CLEAR counterexample records, order<=9 CLEAR atlas and {len(checked16)} immutable hashes: PASS; Lean pending; CLEAR cold re-check S017 FUTURE.')

if closed17:
    s17=state['s017']
    assert s17==spec['s017'] and s17['status']=='COMPLETED'
    assert s17['milestone1']=='CLEAR_COLD_RECHECK_PASS' and s17['lean']['status']=='G9_LOCAL_KERNEL_PROOF_COMPARATOR_PENDING'
    for name in ['PLAN']+[f'PLAN_AMENDMENT_{i}' for i in range(1,s17['amendments']+1)]:
        assert sha256_file(ROOT/f'sessions/S017/{name}.md')==(ROOT/f'sessions/S017/{name}.sha256').read_text().split()[0],name
    assert (ROOT/'formal/lean-toolchain').read_text()=='leanprover/lean4:v4.35.0\n'
    assert '56a005855ea17e0b0958f73ec801ae140b0a1679' in (ROOT/'formal/lakefile.toml').read_text()
    manifest=json.loads((ROOT/'formal/lake-manifest.json').read_text())
    assert any(p['name']=='mathlib' and p['rev']=='56a005855ea17e0b0958f73ec801ae140b0a1679' for p in manifest['packages'])
    comp=json.loads((ROOT/'formal/comparator.json').read_text())
    assert comp['permitted_axioms']==['propext','Quot.sound','Classical.choice'] and len(comp['theorem_names'])==s17['lean']['compared_theorems']
    # Forbidden placeholders and module headers in every formal source.
    for p in (ROOT/'formal').rglob('*.lean'):
        if '.lake' in p.parts: continue
        code=re.sub(r'/-.*?-/','',p.read_text(encoding='utf-8'),flags=re.S)
        code=re.sub(r'--[^\n]*','',code)
        toks=set(re.findall(r'\b(sorry|admit|native_decide|axiom|ofReduceBool|implemented_by|extern)\b',code))
        if p==ROOT/'formal/Challenge.lean': toks-={'sorry'}
        assert not toks,(p,toks)
        assert next((l for l in code.splitlines() if l.strip()),'').strip()=='module',p
        assert len(p.read_text(encoding='utf-8').splitlines())<=10000,p
    frozen=0
    for line in (ROOT/'formal/FROZEN_MODULES.md').read_text(encoding='utf-8').splitlines():
        m=re.match(r'\| `([A-Za-z.0-9]+)` \| `([0-9a-f]{64})` \|',line)
        if m:
            assert sha256_file(ROOT/'formal'/(m[1].replace('.','/')+'.lean'))==m[2],m[1];frozen+=1
    assert frozen==s17['lean']['frozen_modules'],frozen
    for c in claims:
        if c['id'] in s17['claims_formal']:assert c['status']=='FORMALLY_CERTIFIED'
        if c['id'] in s17['claims_computed']:assert c['status']=='COMPUTED_EXACT'
    checked17=set()
    superseded17=dict(state['s018']['superseded_s017_hashes']) if closed18 else {}
    if closed19: superseded17.update(state['s019']['superseded_s017_hashes'])
    for line in (ROOT/'evidence/S017/HASHES.md').read_text(encoding='utf-8').splitlines():
        m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
        if m:
            if m[2] in superseded17:
                # S018 supersession: S017 bytes recorded; current bytes hashed in evidence/S018/HASHES.md.
                assert superseded17[m[2]]==m[1],m[2]
            else:
                assert sha256_file(ROOT/m[2])==m[1],m[2]
            checked17.add(m[2])
    required17={p.relative_to(ROOT).as_posix() for folder in ['sessions/S017','evidence/S017'] for p in (ROOT/folder).rglob('*') if p.is_file() and p.name!='HASHES.md'}
    required17|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s017*') if p.is_file()}
    required17|={p.relative_to(ROOT).as_posix() for p in (ROOT/'research').glob('S017*.md')}
    required17|={p.relative_to(ROOT).as_posix() for p in (ROOT/'formal').rglob('*') if p.is_file() and '.lake' not in p.relative_to(ROOT).parts}
    if closed18: required17-=set(state['s018']['new_formal_files'])
    assert required17==checked17,(sorted(required17-checked17)[:5],sorted(checked17-required17)[:5])
    print(f'S017 CLOSED: G9 CLEAR cold re-check PASS, Lean G9 STACK+CLEAR local kernel proof, {frozen} frozen modules and {len(checked17)} immutable hashes: PASS; Comparator/independent replay pending; S018 FUTURE.')

if closed18:
    s18=state['s018']
    assert s18==spec['s018'] and s18['status']=='COMPLETED'
    assert s18['milestone1']=='S017_BUILD_REPRODUCED' and s18['milestone3']=='LEAN_STATEMENT_COLD_RECHECK_PASS_AFTER_F1_FIX'
    assert s18['comparator']['statement_and_axiom_check']=='PASS_LOCAL_UNSANDBOXED' and s18['comparator']['lean_kernel']=='ACCEPT'
    for name in ['PLAN']+[f'PLAN_AMENDMENT_{i}' for i in range(1,s18['amendments']+1)]:
        assert sha256_file(ROOT/f'sessions/S018/{name}.md')==(ROOT/f'sessions/S018/{name}.sha256').read_text().split()[0],name
    # S018 superseded S017-hashed formal files only through recorded entries, and froze nothing new.
    for path,old in s18['superseded_s017_hashes'].items():
        assert path.startswith('formal/') and sha256_file(ROOT/path)!=old,path
    for path in s18['new_formal_files']:
        assert (ROOT/path).is_file() and path.startswith('formal/'),path
    if closed19:
        assert "license: \"Apache-2.0\"" in (ROOT/'formal/formalization.yaml').read_text(encoding='utf-8')
    else:
        assert '(no LICENSE file in the repository yet)' in (ROOT/'formal/formalization.yaml').read_text(encoding='utf-8') or (ROOT/'LICENSE').exists()
        assert 'NOT SUBMITTED' in (ROOT/'formal/formalization.yaml').read_text(encoding='utf-8')
    for c in claims:
        if c['id'] in s18['claims_formal']:assert c['status']=='FORMALLY_CERTIFIED'
    checked18=set()
    superseded18=state['s019']['superseded_s018_hashes'] if closed19 else {}
    for line in (ROOT/'evidence/S018/HASHES.md').read_text(encoding='utf-8').splitlines():
        m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
        if m:
            if m[2] in superseded18:
                assert superseded18[m[2]]==m[1],m[2]
            else:
                assert sha256_file(ROOT/m[2])==m[1],m[2]
            checked18.add(m[2])
    required18={p.relative_to(ROOT).as_posix() for folder in ['sessions/S018','evidence/S018'] for p in (ROOT/folder).rglob('*') if p.is_file() and p.name!='HASHES.md'}
    required18|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s018*') if p.is_file()}
    required18|=set(s18['superseded_s017_hashes'])|set(s18['new_formal_files'])
    assert required18==checked18,(sorted(required18-checked18)[:5],sorted(checked18-required18)[:5])
    print(f'S018 CLOSED: S017 Lean build reproduced, local lake comparator statement/axiom check PASS (unsandboxed), Lean kernel accept, external kernels recorded, statement cold re-check PASS after F1 fix, {len(checked18)} immutable hashes: PASS; S019 FUTURE.')

if closed19:
    s19=state['s019']
    assert s19==spec['s019'] and s19['status']=='COMPLETED' and s19['submitted'] is False
    for name in ['PLAN']+[f'PLAN_AMENDMENT_{i}' for i in range(1,s19['amendments']+1)]:
        assert sha256_file(ROOT/f'sessions/S019/{name}.md')==(ROOT/f'sessions/S019/{name}.sha256').read_text().split()[0],name
    for d in (s19['superseded_s017_hashes'],s19['superseded_s018_hashes']):
        for path,old in d.items():
            assert path.startswith('formal/') and sha256_file(ROOT/path)!=old,path
    # Snapshot files that come from formal/ are byte-identical to the current research copies.
    snap=0
    for line in (ROOT/'evidence/S019/snapshot_manifest.txt').read_text(encoding='utf-8').splitlines():
        m=re.fullmatch(r'([0-9a-f]{64})  (\S+)',line.strip())
        if not m: continue
        if m[2] in ('LICENSE','README.md','.gitignore'):
            continue
        assert sha256_file(ROOT/'formal'/m[2])==m[1],m[2]; snap+=1
    assert snap==s19['snapshot']['files_from_formal'],snap
    assert re.fullmatch(r'[0-9a-f]{40}',s19['snapshot']['commit']) and s19['snapshot']['branch']=='palomar/submission'
    checked19=set()
    for line in (ROOT/'evidence/S019/HASHES.md').read_text(encoding='utf-8').splitlines():
        m=re.fullmatch(r'`([0-9a-f]{64})`\s+`([^`]+)`',line.strip())
        if m:
            assert sha256_file(ROOT/m[2])==m[1],m[2];checked19.add(m[2])
    required19={p.relative_to(ROOT).as_posix() for folder in ['sessions/S019','evidence/S019'] for p in (ROOT/folder).rglob('*') if p.is_file() and p.name!='HASHES.md'}
    required19|={p.relative_to(ROOT).as_posix() for p in (ROOT/'tools').glob('s019*') if p.is_file()}
    required19|=set(s19['superseded_s017_hashes'])|set(s19['superseded_s018_hashes'])
    assert required19==checked19,(sorted(required19-checked19)[:5],sorted(checked19-required19)[:5])
    print(f"S019 CLOSED: Palomar snapshot {s19['snapshot']['branch']}@{s19['snapshot']['commit'][:12]} prepared ({snap} files byte-identical to formal/), memory-safe plain build, {len(checked19)} immutable hashes: PASS; NOT submitted (owner uploads); S020 placeholder.")
