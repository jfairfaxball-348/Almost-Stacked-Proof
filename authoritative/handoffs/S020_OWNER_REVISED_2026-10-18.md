# S020 — Write the standalone counterexample paper (with prominent exact figures)

**FUTURE, UNEXECUTED.** Owner-authorised prospective handoff, installed administratively on 2026-10-18 after S019. S019 is the last completed research session. Execute S020 only when the owner separately invokes the next session; do not execute S021 in S020.

## Owner decision and changed release order

The owner reports that Palomar registration is stalling, and explicitly directs us to move ahead to **paper writing now**, retaining a clearly marked placeholder for the eventual Palomar link. This supersedes the S019 assumption that S020 must wait for successful registration. It authorises drafting and building a manuscript, **not** claiming Palomar acceptance, submitting to arXiv or a journal, contacting the hypothesis authors, or modifying the frozen Palomar submission snapshot. The original S019 CLOSEOUT and FUTURE_S020 remain historical and unchanged. Phases 2 and 4 novelty audits are OWNER_WAIVED (not passed); do not claim worldwide novelty/priority. Phase 1 and 3 PASS are still owner decisions, not implied by drafting. Phase 5 remains pending/unconfirmed.

## Entry and evidence

1. Read LIVE `main` and reconcile S019 PR #25, its actual merge commit and any intervening changes; read AGENTS.md, authoritative/{START_HERE.md,STATE.json}, docs/{SESSION_PROTOCOL.md,RELEASE_PROTOCOL.md,PHASE_GATE_LEDGER.md}, S014 local structural research when used, the decision, source, claim and session ledgers, research/ASH_SPEC.md, and sessions/S015–S019 research, audits, Lean assurance, packaging and closeouts. Check this S020 revision against the 2026-10-18 owner decision and confirm S020 not already executed.
2. Pin the **separate, immutable** Palomar snapshot `palomar/submission` at `34363e5222136c54b08e0c5550e2d49b9f23f5fd`. Its local fresh-clone preflight passed; do not present it as a Palomar-registered or sandbox-verified record, do not rewrite it, and do not assume an entry ID. Research `main` S019 merge was `5f0900c17995362155bff0e8aecd7fa67e0d8363` at this revision; repin it live at execution.
3. Create the S020 INPUT/PLAN/decisions and manuscript source tree on a research session branch. Preserve exact bibliographic attribution to Tamás Csernák and Lajos Soukup (arXiv:2610.09650, arXiv:2604.22341); independently check exact theorems/definitions against primary sources and Lean Challenge.lean before writing mathematical claims. Credit the earlier TreeStack paper (arXiv:2609.31811) only for its actual separate result. Owner is the sole named paper author unless the owner directs otherwise; do not fabricate endorsements, correspondence or priority.

## Primary objective and finished deliverables

Produce a polished, **standalone, self-contained, rigorous mathematical paper**, in a reproducible LaTeX source tree, including bibliography, high-quality vector figures, compiled PDF when the environment permits, and an exact-source build command. Aim at an arXiv-ready draft, not publication/submission. Give a serious exposition legible to graph theory and graph-pebbling readers: the mathematical surprise should be visible quickly while the finite certificate proof is transparent and auditable.

Proposed working title: **A Nine-Vertex Counterexample to the Critical Almost Stacked Hypothesis** (adjust only if accuracy/clarity improves). A possible structural outline:
- Abstract: refutation of **both** intended critical stacking and clearing clauses by the same nine-vertex graph, with precise quantitative gap; state computer-assisted/kernel-checked nature honestly.
- Introduction: the authors' conjecture and its motivation; careful distinction between the *printed pointwise* wording (separately false, acknowledged by an author as stronger than intended) and the intended **critical/monotone** ASH*. Do not insinuate an erratum or endorsement exists. Position the exact main theorem prominently.
- Definitions: graphs, configurations, pebbling moves, stackable vs clearable, almost stacked, `stack(G)`, `clear(G)`, critical thresholds and `L_all` vs `L_AS` with explicit "every size >= t" distinction, admissibility/nonbipartiteness, and finite versus universal quantifiers.
- Main theorem: graph `G9` on vertices 0..8, graph6 `HCQTaXi`, exactly the 14 undirected edges
  `03,05,06,14,17,18,26,28,35,36,47,48,57,68`.
  Connected and nonbipartite. `stack(G9)=clear(G9)=15`, `L_all(G9)=14`, `L_AS(G9)=13`; the sole size-14 losers (for each of stacking and clearing) are `(0,0,1,0,0,5,0,8,0)` and its graph-automorphic image, **not** almost stacked. Thus the intended critical ASH* fails in both clauses; in particular the proposed universal inequality `L_all(G) <= L_AS(G)` is **false** and must not appear as an asserted theorem.
- Proof: expose a readable mathematical explanation of why the critical configuration loses; distinguish a hand argument from any computational certificate. Give precise certified ingredients for upper bounds/all almost-stacked inputs, losing-layer recurrence, correctness proof, and how the Lean kernel checks untrusted finite data. For CLEAR, explain clearly what is independently verified and what follows from STACK; never skip a needed implication. Include fully specified computational completeness scopes and limitations, or move reproducibility/detail into an appendix.
- Context and discussion: minimal counterexample order 9 only at the scopes actually verified; avoid asserting uniqueness among all order-9 graphs if a sweep has UNKNOWN/unverified cases. Distinguish conjectural infinite PB(4,4,2j,1) family from established finite examples. Separate the printed-form P4/bull examples from the flagship claim if mentioned. Cite exact existing results; no unverified novelty assertion.
- Verification, declarations/acknowledgements, reproducible repository paths and references.

## Figures are required, not optional: prominent, accurate, reproducible

**At least FOUR useful vector diagrams/figures**, with accompanying explanatory captions and accessible monochrome printing. Store editable source (TikZ/PGF or equivalent deterministic script) alongside figure outputs and build instructions; avoid decorative AI renderings and manually imagined edges.

**Figure 1: G9 graph itself.** Place it conspicuously **on page 1 if the layout permits, otherwise at the very start of page 2**, immediately adjacent to the principal theorem or its introduction. Large enough to inspect vertex labels (0..8), exactly nine vertices and fourteen undirected edges; no phantom/missing edges. Use an elegant stable embedding with readable straight or deliberately routed edges; white-space and restrained visual hierarchy. Caption gives graph6 `HCQTaXi` and a reproducibility pointer. This is the paper's signature image, not a tiny late appendix figure.

**Figure 2: Critical losing configuration on G9.** Show the same verified graph with at-each-vertex pebble counts from `(0,0,1,0,0,5,0,8,0)` (one at vertex 2, five at vertex 5, eight at vertex 7, all others zero). Explicitly display the total 14, and visually distinguish the three occupied vertices using text/markers rather than colour alone. Put this adjacent to/soon after Figure 1. The second automorphic image may be shown in an inset only if its exact permutation is verified from source; never guess it.

**Figure 3: The sharp obstruction/gap.** A logically precise threshold illustration comparing all configurations vs almost-stacked configurations at mass 14 for both STACK and CLEAR: critical losers exist generally, but none are almost stacked; the respective guaranteed thresholds are 15 and 14. Specify whether plotted numbers are largest losing masses (`14,13`) or guaranteed thresholds (`15,14`), never conflate these measures or imply unsampled data. Prefer a compact conceptual/quantitative figure rather than an ungrounded statistical chart.

**Figure 4: Verification architecture.** A clean schematic for exact losing-layer recursion, certificate data, proved checker correctness, Lean kernel evaluation and independent cold re-check/comparator. Accurately distinguish what is a theorem, an untrusted input, local acceptance, and what awaits the Palomar service. Optional extra figure: a legal move example or appendix atlas diagram only if mathematically exact.

**Figure-integrity gate:** programmatically derive edges from the canonical list/graph6 and assert simple undirected graph, nine unique vertex labels, 14 exact edges and graph6 equality. For Figure 2 verify vertex-count mapping, total 14 and non-almost-stacked property. Verify every visual caption and numeric claim against source evidence/Lean; check compiled output visually for overlap, legibility and graph incidence (do not count crossings as extra vertices). Keep figure-generating code and checks in the repo. No figure may be used as proof of a completeness assertion.

## Palomar placeholder and release boundary

In the paper use a conspicuous but unobtrusive editorial placeholder, for example:
`Palomar verification: [registration pending; registry entry URL to be inserted after confirmation].`
If typesetting a hyperlink, define one named macro (e.g. `\\PalomarEntry`) to replace later; **no invented registry URL, ID, badge, date, or claim of acceptance**. Cite the exact available GitHub snapshot commit separately as reproducibility evidence. Owner reports registration is stalled, not proof of a service outcome; do not change the Palomar branch or submit on the owner's behalf.

Produce a `paper/` directory with `main.tex`, bibliography, vector figure sources/build tools, README/reproducibility instructions, generated PDF if possible, and S020 editorial audit / source-to-claim crosswalk. Make a genuine serious effort to produce the complete paper in this session: proof, captions, bibliography, rigorous limitations, not only a skeleton. Run available LaTeX compilation and tests; where tools are absent record exactly what was not checked, without calling it PASS. Include an author-review checklist and any remaining honest manuscript defects.

## Closeout

Follow the repo's normal numbered-session closeout for S020: one reviewable atomic session commit, ordinary PR and non-force merge (if permitted), main re-pin, accurate test and phase status, session ledger/decision/failure/source/claim mirror updates, and a **complete future S021 prompt** (likely editorial hostile audit, typesetting, reference checking, author approval and eventual release gates). Stop before S021. No journal/arXiv submission, Palomar registration attempt, claimed acceptance, or email to Csernák/Soukup without a fresh explicit owner instruction.
