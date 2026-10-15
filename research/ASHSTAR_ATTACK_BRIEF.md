# ASH* direct attack — mathematical handoff after author clarification (2026-10-13)

**Scope.** This is a **research preparation note**, not an executed S004 mathematics session, new theorem about ASH*, or claim of an authorship/priority agreement. Tamás Csernák's owner-supplied correspondence establishes intended meaning (see `outreach/2026-10-csernak-soukup/2026-10-13_AUTHOR_REPLY.md`), not universal truth.

## Exact target

For a finite connected simple graph `G`, `n=|V(G)|>=2`, and goal `g = stack`, put `s=stack(G)`. Prove **there exists an almost-stacked non-stackable configuration of exact mass `s-1`**, or refute it with a finite certified graph and winning/losing witnesses. Repeat *separately* for `g=clear` when `G` is connected and non-bipartite, with `s=clear(G)`. Equivalently (S003 Thm 4), `s` is the least threshold from which **all** almost-stacked configurations at **every larger mass** win. This is ASH*. K1 is separately trivial under the threshold formulation; the `s-1` equivalence is restricted to `n>=2`.

The printed single-layer minimum statement is false (S003 P4 and bull certificates) and **is not** the target to solve anew. Do not conflate the two.

## Exact losing-layer recurrence to exploit (elementary definition-level identity)

Fix one goal (stack or clear), and define `B_t(G)` to be the set of all size-`t` configurations from which **no finite legal pebbling sequence** reaches that goal. Let `M(c)` be the **complete** set of immediate legal successor configurations, each of size `t-1`. For `t>=2`,

`c in B_t  <=>  c is not already a goal and every d in M(c) belongs to B_(t-1).`

Reason: reachability holds exactly when the current configuration is a goal or has *some* legal first move to a configuration from which the goal is reachable. Therefore a configuration is losing if and only if neither possibility exists. This is merely the Bellman recursion, **not** a proof of ASH*. A configuration with no moves is losing unless already at a goal. At `t>n` there must be a heavy vertex, hence a legal move in any connected graph with `n>=2`. Thus for `t>n` the losing set is a subset of the inverse one-step shadow of `B_(t-1)`; for `t<=n` terminal 0/1 cases require special care.

For each `t`, define `A_t=B_t ∩ AS_t`; `s` is the first mass with `B_s=∅`, using the source's monotonicity only where its hypotheses apply. ASH* is exactly `A_(s-1) ≠ ∅`. There is **no** general inference that `A_t=∅` implies `A_(t+1)=∅`: P4 supplies a counterexample to this tempting false statement.

## Priority proof/counterexample strategies, with explicit falsification

**P1 — Structure of the last losing layer / inverse shadows (new lead from authors' explanation).** Work with `B_(s-1)` and its descent to smaller losing layers. Search for an extremal `c in B_(s-1)` with constrained support, heavy-vertex count, parity, or graph-distance potential; prove the existence of an AS choice *among all losers* without claiming every loser can be mass-preservingly compressed. Analyse the full universal quantifier over legal moves. A proposed theorem must explain why its extremal choice is preserved under its operations, and why the process terminates. Gate: an independently checked tiny graph must falsify or support each proposed invariant.

**P2 — Bad-configuration frontier as a combinatorial shadow/operator.** Regard `B_(t+1)` as the non-goal configurations whose entire out-neighbourhood lies in `B_t`. Is there an extremal-shadow, injection, potential, closure, or duality theorem that forces an AS member when `B_(t+1)` is the *final* nonempty layer? Formulate an exact lemma with all quantifiers and test it against the known n<=6 data. Do not substitute "the density of bad configurations is small" for a proof.

**P3 — Loss certificates and cycle corrections.** Generalise TreeStack rooted transfer/defect or mod-3 weights to cycles; find *necessary* obstruction certificates (not merely sufficient ones) strong enough to produce AS witnesses. Check explicitly where cycles break independence of rooted subtrees, and preserve the separate stack/clear goals.

**P4 — Minimal non-tree counterexample / blocks.** Suppose ASH* is false and choose a minimal connected counterexample. Try to rule out cut vertices, bridges, pendant trees, unicyclic or cactus structures by a rigorous reduction preserving the critical level and the goal predicate. Gate: every reduction must be tested on the known smallest cycle/bridge counterexamples to naive compression.

**P5 — Precision counterexample search rather than unlimited census.** If a structural attack stalls, preregister a **bounded** exact campaign on unexplored threshold-complete graphs (especially S003's eight unresolved seven-vertex stack cases, three unresolved non-bipartite clear cases, sparse n=8+ graphs). Demand independent implementations, no assumptions about symmetry without proof, complete maximum bad mass and full AS enumeration at `s-1`, and reproducible winning certificates for *every* AS critical configuration plus a non-AS loser and proof of threshold. A failed individual sequence is not a counterexample.

## Known obstructions / safeguards

- S003/FL-0015: a losing configuration on C5 at mass 7 cannot be turned into an almost-stacked loser by the proposed same-layer pair transfers; *arbitrary critical-layer compression is false*. An **existential** extremal-selection theorem might still work.
- Arbitrary adding graph edges can turn losers into winners (FL-0010). A spanning-tree witness need not survive extra cycle moves.
- The author reports complete n<=7 checks; our independent evidence reaches 845/853 stack and 806/809 clear at n=7 (cutoff 55). Do not report the author's full coverage as independently verified.
- No universal conclusion follows from a finite atlas; maintain separate source-stated, exact-computed and proved statuses.
- For all finite t and graph size, distinguish `Conf_t`, `B_t`, `AS_t`, goal-at-current-mass and move-to-`t-1`. Clearing is only targeted on connected non-bipartite graphs.
- Earlier TreeStack result is cited as prior work. Printed-form counterexamples still need S004's independent cold audit, then the separate Phase 1 decision.
- No author contact, Lean, Palomar or publication from this preparatory brief.

## S004 success criterion

**Preferred:** an unconditional universal ASH* proof with complete self-contained lemmas and independent challenge, or a certified finite counterexample with exact threshold and two independent solvers. **Second best:** a genuine non-tree infinite-family theorem that materially constrains universal counterexamples, not a sequence of minor lemmas. **Honest fallback:** one structural route eliminated by its minimal concrete counterexample, a precise remaining obstruction, preserved reproducible tests, and a complete strictly future S005 handoff. The owner must explicitly invoke S004 separately.

## Current S007 update

Universal ASH* remains OPEN, both goals. S007 proves clear(G_l)=6*2^l-2 for every triangle-tail l>=0, with prior April6.1 pure AS lower and a complete legal selected-ancestry credit upper. Proves stack(G_l)<=4*2^l only; no infinite stacking equality/AS lower. Theorem33 extends sharp odd-bound cores under explicit rooted-tree hypotheses, not arbitrary cactus composition. S006 cold audit PASS; all inherited finite cutoffs retained. See research/S007_LEAF_CREDIT_AND_TRIANGLE_TAILS.md and S007 AUDIT. No novelty/Lean/later promotion; S008 strictly FUTURE/UNEXECUTED.

## Current S008 update (2026-10-14)

Universal ASH* remains OPEN, both goals. S008 hostile audit of S007 PASS at stated scopes (Theorem33 conditional). New exact all-length triangle-tail stacking4*2^l with AS lower, and triangle with k common-root leaves stack3k+5/clear3k+7 with separate AS witnesses. Exact support/residue ideal and simultaneous conductor tightness do not close the global comparison. Independent registered certificates/layers/traces passed; all old cutoffs retained. Novelty NOT_AUDITED, Lean NOT_STARTED, all final activities deferred. S009 strictly FUTURE/UNEXECUTED, first deep prior-art/dependency investigation then sustained universal research.

See research/S008_HOSTILE_AUDIT_AND_UNIVERSAL_ROUTES.md and sessions/S008/AUDIT.md. Historical session/future paragraphs above are superseded by this section and STATE.

## Current S009 authority — 2026-10-14

Earlier current/future-session paragraphs are historical and superseded. Last completed S009; next S010 strictly FUTURE/UNEXECUTED. Universal ASH* OPEN for both goals, printed mathematics PASS separate. Read STATE, research/S009_PRIOR_ART_AND_DEPENDENCY_AUDIT.md, research/S009_UNIVERSAL_RESEARCH.md and sessions/S009/AUDIT.md. Foundational primary-source/dependency comparisons completed within Phase1; known ancestry/reductions/algebra credited, possible-new/equivalence uncertainty scoped, no worldwide priority or Phase2 promotion. S008 hostile audit PASS. New exact first-return excursion interfaces, insertion/deletion frontiers, path-cover credit and dominated stacking/clearing bounds are proved at stated scopes; new cold challenge FUTURE S010. Registered independent finite checks pass; all old cutoffs unchanged. TreeStack currentv2/earlier registered package remains prior work. No Lean, Palomar, manuscript, arXiv/journal or correspondence.

## Current S010 authority — 2026-10-14

Earlier current/future sections are historical. Last S010, next S011 strictly FUTURE/UNEXECUTED. Universal ASH* OPEN separately STACK/CLEAR; printed PASS separate. Read STATE and S010 research/primary/AUDIT/MILESTONES. S00938-43 cold challenge PASS at stated scopes. Exact connected counts/finite ports and full forest cancellation/reversal proved; three-pile reflection supplies consuming TREE witnesses for EVERY critical STACK one-insertion and signed0 necessity for bipartite critical STACK losers. Roots/donor2/carries/three-mark/CLEAR bridge remain; no AS maximum theorem. Three prior-hashed precision campaigns pass, auxiliary weak connectivity/graph-wide root quantifiers refuted, old cutoffs unchanged. Known grammar/ancestry/+3/signed invariants and earlier TreeStack credited; qualified refinements/equivalence only. No universal gate promotion, Lean, Palomar, manuscript/arXiv/journal/contact. Outgoing actual integration IDs/jobs/main reread are in S010 PR metadata.

## Current S011 authority - 2026-10-15

Earlier current/future sections are historical. Last S011, next S012 strictly FUTURE/UNEXECUTED. Universal critical STACK/CLEAR OPEN, printed PASS separate. S01044-52 cold challenge and25 inherited check-only replays PASS at stated scopes with old bytes/cutoffs retained. New53 nonempty terminal-vector forest,54 three-output used-label re-root/edge exposure,55 stackable CLEAR deletion/triangle-free history and gap>=2 heavy-site restriction,56 bipartite common CLEAR root obstruction,57 donor1/2 exact terminal transport,58 CLEAR/TWO root typing are programme-proved at explicit scopes. They do NOT provide global AS selection. Actual C5 odd-cycle3-witness can still fail clearing; abstract typed/self-root families can lack common STACK roots and are NOT actual configuration counterexamples. Three registered dual-validator campaigns pass; no universal/human/kernel or priority assurance. Read S011 research/primary/AUDIT/MILESTONES. New proof cold challenge FUTURE S012; phases2-6 unchanged/deferred. Actual outgoing integration IDs/jobs/main reread belong in S011 PR metadata.
