# S015 invocation and entry record

Owner invocation (complete accessible text, normalized UTF-8 LF, archived in OWNER_INVOCATION.txt; no transport-byte identity claimed): "Run a sustained attack on the next session, aim to resolve a major obligation or proof". This selects exactly S015 per the frozen prospective handoff sessions/S014/FUTURE_S015.md, archived byte-identically as AUTHORISED_PROMPT.md. No S016 execution, Lean, registration, publication or author contact is implied.

Entry pin (local fetch of origin/main at session start): 4200dc84be0bfd54e8573e7aa02dacea7ff8513c, tree 4f83e4b58baf55cc300aa6094d8c43b8ce556b2d, ordered parents 8ea5db207a91ca917c3b94bc98b54ac65406e7a5 (S013 merge, first parent) and cafa2f9a9e69d6f271583ee76a2f5fbe9a3840c4 (owner-authorized S014 CI repair, whose parent is the S014 research commit 44a89726). Branches visible at entry: main and the harness-designated session branch ccr-a9fdff28-6mqxx0 (used for S015 in place of a session/S015-* name, because the execution environment fixes the branch). Hosted job records for the S014 merge were not re-queried through the API in this session; their recorded status in S014 PR metadata is not re-asserted here (UNVERIFIED in S015).

Environment: Linux cloud container, 4 cores, 15 GiB RAM, no swap; g++/gcc 13.3.0, Python 3.13.16, nauty 2.8.8 (Debian package `nauty`, installed at session start). This differs from the Windows host of S003-S014; the Windows-specific resource notes did not apply, but explicit per-process caps were still used.

Baseline: authoritative/STATE.json last_completed_session S014; validation/validate_governance.py passes on main until the S015 directory exists (it then fails by design: "S015 remains unexecuted"), and is updated in the S015 commit to the S015-closed state.

## Final S015 authority

S015 closes with universal critical ASH*-STACK REFUTED at COMPUTED_EXACT level (graph G9 = `HCQTaXi`, research/S015_G9_COUNTEREXAMPLE.md), pending the independent cold re-check and Lean gates; universal critical ASH*-CLEAR remains OPEN. See CLOSEOUT.md.
