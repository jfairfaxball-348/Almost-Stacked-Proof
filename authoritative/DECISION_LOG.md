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
