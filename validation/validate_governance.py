#!/usr/bin/env python3
"""Fail-closed governance mirror/integrity checks (updated S003); not a mathematics or Lean test."""
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
assert state["headline_status"] == "PRINTED_ASH_REFUTED_PENDING_INDEPENDENT_AUDIT_CRITICAL_FORM_OPEN"
assert state["last_completed_session"] == "S003"
assert state["recommended_next_session"] == "S004"
assert state["phases"]["0"]["status"] == "PASS"
assert state["phases"]["1"]["status"] == "IN_PROGRESS"
assert all(state["phases"][str(i)]["status"] != "PASS" for i in range(2, 7))
assert state["active_campaign"] is None
assert state["counterexample_status"] == "PRINTED_FORM_CERTIFIED_LEAN_AND_COLD_AUDIT_PENDING"
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
assert "S004" in next_prompt and "FUTURE, UNEXECUTED" in next_prompt
for sess in ("S001", "S002", "S003"):
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

# The 2026-10-13 update is CORRESPONDENCE ONLY, never S004 execution.
assert (ROOT / "outreach/2026-10-csernak-soukup/2026-10-13_AUTHOR_REPLY.md").exists()
assert (ROOT / "outreach/2026-10-csernak-soukup/reply_draft_2026-10-13.txt").exists()
assert (ROOT / "research/ASHSTAR_ATTACK_BRIEF.md").exists()
assert "S004" in next_prompt and "FUTURE, UNEXECUTED" in next_prompt
assert state["correspondence"]["authority"] == "AUTHOR_REPORTED_INTENDED_MEANING_NOT_PUBLISHED_ERRATUM"
assert state["correspondence"]["next_reply"] == "DRAFT_NOT_SENT"
assert any(x["id"] == "SRC-0010" and x["type"] == "PERSONAL_COMMUNICATION_OWNER_SUPPLIED" for x in sources)
assert all(any(x["id"] == claimid and x["status"] == "SOURCE_STATED" for x in claims) for claimid in ("CLM-0028", "CLM-0029"))
assert not (ROOT / "sessions/S004/CLOSEOUT.md").exists()
print("Author correspondence provenance and unexecuted S004 handoff: PASS (administrative only).")
