#!/usr/bin/env python3
"""Fail-closed governance mirror/integrity checks (updated S006); not a mathematics or Lean test."""
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
assert state["last_completed_session"] == "S006"
assert state["recommended_next_session"] == "S007"
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
assert "S007" in next_prompt and "FUTURE, UNEXECUTED" in next_prompt
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
assert "S007" in next_prompt and "FUTURE, UNEXECUTED" in next_prompt
assert state["correspondence"]["authority"] == "AUTHOR_REPORTED_INTENDED_MEANING_NOT_PUBLISHED_ERRATUM"
assert state["correspondence"]["next_reply"] == "DRAFT_NOT_SENT"
assert any(x["id"] == "SRC-0010" and x["type"] == "PERSONAL_COMMUNICATION_OWNER_SUPPLIED" for x in sources)
assert all(any(x["id"] == claimid and x["status"] == "SOURCE_STATED" for x in claims) for claimid in ("CLM-0028", "CLM-0029"))
assert (ROOT / "sessions/S004/CLOSEOUT.md").exists()
print("Author correspondence provenance and unexecuted S007 handoff: PASS (administrative only).")

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
assert next_prompt in (ROOT/"sessions/S006/CLOSEOUT.md").read_text(encoding="utf-8")
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
for line in (ROOT/"evidence/S006/HASHES.md").read_text(encoding="utf-8").splitlines():
    m=re.fullmatch(r"`([0-9a-f]{64})`\s+`([^`]+)`",line.strip())
    if m:
        assert hashlib.sha256((ROOT/m.group(2)).read_bytes()).hexdigest()==m.group(1),m.group(2)
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
print(f"S006 mirrors, scope and {len(checked6)} hashes: PASS (universal ASH* OPEN; S007 FUTURE).")
