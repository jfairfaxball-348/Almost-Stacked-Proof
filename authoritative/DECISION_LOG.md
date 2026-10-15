# Decision log

| Date | Decision | Evidence / rationale | Status |
|---|---|---|---|
| 2026-10-12 | Start independent ASH research project; target either unconditional universal proof or certified counterexample | Owner objective; Csernák–Soukup 2026 arXiv:2610.09650 | BINDING |
| 2026-10-12 | Inherit Davenport's session/claim/source/phase discipline; adapt phases to proof, preliminary novelty, Lean, final novelty, Palomar, arXiv | Davenport repository procedures inspected | IMPLEMENTED S001 |
| 2026-10-12 | Do not treat tree estimator equality as unproved or as ASH itself | TreeStack repo README, Lean declaration, arXiv:2609.31811, Palomar entry | BINDING |
| 2026-10-12 | Primary October PDF unavailable for direct full-text inspection in S001; no fabricated theorem numbering, quantifiers or proof inspection | arXiv abstract available, PDF direct fetch failed | SOURCE-TRANSCRIPTION GATE |
| 2026-10-12 | No computational campaigns, Lean development, Palomar, arXiv submission or third-party outreach during bootstrap | Owner authorises scaffold + future prompt | BINDING |
| 2026-10-12 | Phase 0 governance PASS; Phase 1 IN_PROGRESS; other stages gated | Required bootstrap files created | GATE S001 |

| 2026-10-12 S002 | April primary Hypothesis 9.1 independently inspected; October full PDF still unread | April PDF p20; October abstract only | SOURCE GATE PARTIAL |
| 2026-10-12 S002 | Original TreeStack estimator equation and exact t≥2 match April source; not universal ASH | April p26; TreeStack/Estimator.lean and Stacking.lean | PRECEDENCE VERIFIED FOR APRIL |
| 2026-10-12 S002 | Pre-registered finite eight-vertex exact survey; no ASH gap through cutoff | 1,918,566 configs, 420 BFS, independent inverse-DP on two graphs | COMPUTED EXACT / BOUNDED |
| 2026-10-12 S002 | Do not advance beyond Mathematics Phase 1 or execute S003 | No proof/certified counterexample; October full source gate incomplete | BINDING |
| 2026-10-12 S003 | October 2610.09650v1 full text read; Hypothesis 3.2 identical in content to April 9.1; estim equal for \|V\|≥2 | PDF sha256 cbc9877b…; research/S003_SOURCE_RECONCILIATION.md | SOURCE GATE PASS (statements) |
| 2026-10-12 S003 | Printed (literal) ASH is false for stacking (P4, t=12) and clearing (bull, t=12) | Finite certificates checked by five (P4) / four (bull) independent tools; research/S003_AS_GAP_AND_ATTACKS.md | CERTIFIED (Lean pending; cold audit pending) |
| 2026-10-12 S003 | Authors' public atlas code tests the critical form ASH*, not the printed statement | lajossoukup/pebbling@701cdd93 `is_critical_stacked_almost_stacked` | PROVENANCE RECORDED; no contact |
| 2026-10-12 S003 | Substantive open target becomes ASH* (critical/monotone form); trees settled by TreeStack + October Thm 5.2 | S003 Thm 4, Thm 8 | BINDING FOR S004 |
| 2026-10-12 S003 | Phase 1 not silently advanced: literal-form counterexample needs independent cold audit (S004) before any Phase 1 PASS; no Phase 2/Lean/Palomar/arXiv action | AGENTS rules 7, 10 | BINDING |
| 2026-10-12 S003 | Work on the harness-designated development branch (name recorded by the PR) instead of a `session/S003-*` name | Execution environment requirement | RECORDED DEVIATION |
| 2026-10-12 (correspondence, not a research session) | Owner authorised correspondence; prepared, not sent by the agent. The email to Csernák and Soukup was audited and corrected; the attachments are the two printed-form certificates, a fresh standalone checker and a readme. No phase, headline or claim status changed | outreach/2026-10-csernak-soukup/AUDIT.md; fresh verifier and spot-checks in outreach/2026-10-csernak-soukup/audit/; the S004 independent cold audit is still pending | OWNER-AUTHORISED; NOT SENT BY AGENT |

| 2026-10-13 (correspondence, not S004) | Owner reported outgoing email sent and supplied a response from Tamás Csernák, cc Lajos Soukup; author confirms **ASH\*** is intended and acknowledges stronger printed statement is false; algorithm propagates bad sets by size | outreach/2026-10-csernak-soukup/2026-10-13_AUTHOR_REPLY.md; SRC-0010; no raw SMTP headers | AUTHOR_REPORTED; PREPUBLICATION / NOT AN ERRATUM |
| 2026-10-13 (handoff-only) | Retain S004 FUTURE; elevate universal ASH* as headline, add bad-layer recurrence as direct proof route; keep printed-form independent cold audit and Phase 1 gate; no numerical results or claim statuses promoted | research/ASHSTAR_ATTACK_BRIEF.md; authoritative/NEXT_SESSION_PROMPT.md | BINDING FOR S004; NOT_EXECUTED |

| 2026-10-13 S004 | Cold audit independently rechecks P4/bull and smallest-order boundaries; printed mathematics PASS only | sessions/S004/AUDIT.md | SCOPED PASS |
| 2026-10-13 S004 | Prove independent-set AS witness despite outside-I cycle edges; derive complete multipartite ASH* using source thresholds | S004 Thm12, Cor13-14; 233 finite challenges | PROGRAMME_PROVED; NOVELTY UNAUDITED |
| 2026-10-13 S004 | Complete missing n7 8/3 thresholds using complete losing-layer certificates, independent canonical-parent replay and base full-DP | evidence/S004 | COMPUTED_EXACT; FINITE ONLY |
| 2026-10-13 S004 | Keep universal ASH* OPEN; no Phase2/Lean/contact; S005 is strictly future | no universal theorem or counterexample | BINDING |
| 2026-10-13/14 S005 | Universal ASH* remains headline; exact pure-pile classification is a source-credited synthesis, not a new universal threshold | S005 Theorem19; April6.1/October4.10 | NO GATE/Priority promotion |
| 2026-10-14 S005 | Continue same interrupted session; regenerate missing executable, exclude incomplete outputs, independently replay every retained layer | CONTINUATION.md; evidence/S005 | NUMERICAL CLAIMS REQUIRE REPLAY |
| 2026-10-14 S005 | Retire geodesic and acyclic-exact shortcuts; retain global residue-hole/cyclic debt routes | S005 report and legal traces | BINDING FOR S006 |
| 2026-10-14 S005 | Next prompt is S006 FUTURE/UNEXECUTED; no Lean/contact/manuscript | authoritative/NEXT_SESSION_PROMPT.md | STOP BEFORE S006 |
| 2026-10-14 S005 | Correct C8-leaf clearing eligibility before run; retain only n+1 bipartite reachability sanity check, exclude from threshold/ASH* counts | PLAN_AMENDMENT_5/6 | CLEAR THRESHOLD UNDEFINED |
| 2026-10-14 S005 | Add independent streamed array-state canonical replay for large retained cutoff layers; full set equality and reverse bases retained | PLAN_AMENDMENT_7; tools/s005_stream_check.cpp | VALIDATION CHANGE, NO NEW SCIENTIFIC SEARCH |

| 2026-10-14 S006 | Prove exact rooted pure/buffer tree/forest conductors and constructive finite bounds; retain zero-source/target/consumption distinctions | S006 Theorems23-27, independent grammar/forest certificates | PROGRAMME_PROVED; novelty unaudited |
| 2026-10-14 S006 | Reject scalar leaf/core rule and fixed-residue extremal concentration with exact obstructions; preserve universal ASH* OPEN | S006 report/closures/extrema | NO UNIVERSAL GATE PROMOTION |
| 2026-10-14 S006 | Enforce canonical LF text/evidence bytes on local Windows and hosted checkouts | .gitattributes; old hash reconciliation | PORTABILITY FIX, NO HISTORICAL CONTENT CHANGE |
| 2026-10-14 S006 | Last session S006, next strictly FUTURE S007; ordinary atomic PR/merge closeout only | S006 INPUT/PLAN/AUDIT/CLOSEOUT | STOP BEFORE S007 |

| 2026-10-14 S007 | Cold S006 audit PASS; selected ancestry credit proves exact infinite triangle-tail clearing and conditional sharp-core path extension; prior odd lower credited | S007 Lemmas28-29/Theorems30/33 | PROGRAMME_PROVED, novelty unaudited |
| 2026-10-14 S007 | Keep stacking upper separate from unproved matching AS lower and universal conductor comparison; scalar dual fails K3 pure3 | S007 Lemma31/Cor32/routes | Universal ASH* OPEN; no gate promotion |
| 2026-10-14 S007 | Preserve historical S006 mutable-mirror hash bytes as frozen snapshots; no historical manifest rewrite | evidence/S007/frozen_s006_* | LF evidence integrity |
| 2026-10-14 S007 | Complete S008 handoff future/unexecuted; ordinary atomic PR/merge only | S007 CLOSEOUT | STOP BEFORE S008 |

| 2026-10-14 S008 | Hostile S007 audit PASS; exact all-length triangle-tail stacking and common-root leaf thresholds proved; universal ASH* OPEN | S008 report/Theorems35-36, AUDIT | No universal gate promotion |
| 2026-10-14 S008 | Owner requires S009 deep primary-source originality/dependency investigation before continued universal research | S008 INPUT/addendum; S009 FUTURE prompt | Foundational Phase1 work, no Lean/publication trigger |
| 2026-10-14 S008 | Preserve21 S007 mutable mirror bytes in explicit frozen index; old manifests unchanged | evidence/S008/frozen_s007_index.json | Integrity PASS, no history rewrite |
| 2026-10-14 S008 | Complete S009 handoff; stop before S009 and all final-stage actions | S008 CLOSEOUT/FUTURE_S009 | FUTURE/UNEXECUTED |

| 2026-10-14 S009 | Foundational prior-art comparison first, exact source semantics/slips and earlier mechanisms attributed, possible novelty bounded | S009 prior-art report/SRC0001–0033 | NO PRIORITY OR PHASE2 PROMOTION |
| 2026-10-14 S009 | Hostile S008 challenge and all old manifests/check-only scopes PASS; frozen indexes retained | S009 AUDIT/cold_checks | NO HISTORICAL HASH REWRITE |
| 2026-10-14 S009 | Exact first-return languages and marked input frontiers; three-component shortcut refuted; continued path-cover/protected triangle upper | S00938–43 and CAM01/02 | UNIVERSAL ASH* OPEN |
| 2026-10-14 S009 | Stop before complete future S010 and all final-stage activity; one atomic authored PR/non-force merge only | S009 CLOSEOUT/FUTURE_S010 | BINDING |

| 2026-10-14 S010 | Reconcile actual S009 head/merge/jobs and expanded invocation, plan hashed first, historical frozen indexes unchanged | entry/INPUT/PLAN/AUDIT | PASS |
| 2026-10-14 S010 | Exact reverse grammar counts/finite ports/cuts/quotients, then full reflection/critical insertion trees/zero-I extension | 44-52 and three registered campaigns | PROGRAMME_PROVED scoped, universal OPEN |
| 2026-10-14 S010 | Keep CLEAR stackable critical losers and roots/donor2/three-mark bridge separate; S011 future only | MILESTONES/FUTURE_S011 | No gate/final-stage advance |

| 2026-10-15 S011 | Preserve exact terminal roots/piles: bipartite common CLEAR root impossible, assigned typed root masks insufficient; donor1/2 reconstruction remains conditional on root/pile and actual input compatibility | S01153-58, AUDIT/MILESTONES | Universal ASH* OPEN; no gate advance |
| 2026-10-15 S011 | CLEAR stackable extremizers use deletion-to2/triangle-free3-witness and gap>=2 heavy-site restrictions; never import51 or solve gap1 by dropping its hypothesis | S01155/55a | Conditional tools only |
| 2026-10-15 S011 | Actual invocation/hashed bounded plans and three exact precision campaigns; historical hashes/cutoffs unchanged; complete S012 strictly future | S011 INPUT/PLAN/CLOSEOUT | Stop before S012/final stages |

| 2026-10-15 S012 | Exact reciprocal TWO/root languages require real SAME-base compatibility; zero-base protected terminal bit mandatory; symmetric assigned C6 still not actual inputs | S01259/59a/59b/62 | Universal AS selection OPEN |
| 2026-10-15 S012 | Keep GLOBAL Q scope and donor-root availability: actual C5 double transfer wins only elsewhere, no claimed donor-TWO coexistence | S01260/CAM03/retained_failures | Draft corrected, no ASH* failure |
| 2026-10-15 S012 | Original R3 whole-history escape costs at least gap; gap1 and arbitrary triangle-free extremizers unresolved; component conditional AS retains gap>=2 | S01261/61a/61b | No gate advance |
| 2026-10-15 S012 | Exactly S012, one atomic authored PR/non-force integration, complete S013 future only | INPUT/PLAN/CLOSEOUT | No delegation/final actions |
