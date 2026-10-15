# ASH source-indexed specification (updated S003)

**Source gate: PASS for statements (S003).**
- October arXiv:2610.09650v1 (submitted 2026-10-07, dated October 8, 23 pp): STATEMENT_INSPECTED, with PROOF_INSPECTED for Lemma 4.7 and Theorem 5.2.
- April arXiv:2604.22341v1: STATEMENT_INSPECTED.

Line-by-line comparison: `research/S003_SOURCE_RECONCILIATION.md`. The two printed hypotheses are identical in content.

**Model.** Finite simple graph G. A configuration is c: V→ℕ of exact size ‖c‖=t. A move u⇒v along an edge requires c(u)≥2 and does c(u)−=2, c(v)+=1. *Stacked*: |supp|=1. *Cleared*: ‖c‖=1.
- stack(G): connected G only; the least t≥2 such that every configuration of size t is stackable.
- clear(G): connected non-bipartite G only; the analogous least t for clearable.
- *Almost stacked*: ∃v0 ∀u≠v0, c(u)≤1.

**Printed (literal) ASH — October Hypothesis 3.2 = April Hypothesis 9.1.** For every finite connected G:
- (1) stack(G) is the least integer t≥2 such that every almost stacked configuration in Conf_t(G) is stackable;
- (2) if G is non-bipartite, clear(G) is the least integer t≥2 such that every almost stacked configuration in Conf_t(G) is clearable.

**S003 status: both (1) and (2) are FALSE as printed.** Certified finite counterexamples, Lean pending and independent cold audit pending:
- (1) fails on P4 at t=12, with stack(P4)=15;
- (2) fails on the bull graph at t=12, with clear=15.

**Critical (monotone) form ASH\*** — the form tested by the authors' public atlas code. For every finite connected G:
- stack(G) = least t₀≥2 such that every AS configuration of every size t≥t₀ is stackable;
- the same for clear when G is non-bipartite.

For n≥2, ASH\* ⇔ some AS configuration of size g(G)−1 is not g-able (S003 Theorem 4). **Status: OPEN.** It is true for:
- all trees, from the earlier TreeStack theorem plus October Theorem 5.2;
- complete bipartite graphs with ≥3 vertices (S003 Theorem 10, plus April Theorem 8.2);
- every graph with g(G)=n+1;
- every connected graph with ≤7 vertices whose threshold was found within t≤55, and every connected 8-vertex graph with threshold ≤26 (computed);
- the selected larger graphs computed.

**Boundaries.**
- K1: stack=2. Literal and critical forms both hold. K1 is bipartite, so clearing is excluded.
- t=0,1 are not threshold candidates. For n≥2 every t∈[2,n] has an AS terminal loser.
- Both thresholds are ≥ n+1.
- Monotonicity above n (October Lemma 4.7) holds for all configurations but not for AS configurations. This is exactly why the printed and critical forms differ.
- Simple graphs only; no claims for multigraphs or loops.

**Tree estimate.** estim(T) = max{2, 1 + max_r(ρ_T(r)+leaf_T(r))}, where ρ_T(r) = Σ_{v=r or deg v>1} deg(v)·2^{dist(r,v)} (October Def. 5.1). This equals April's max_r(σ_T(r)+leaf_T(r)) with σ=1+ρ, for |V|≥2.

The earlier TreeStack theorem `stack_eq_estim_of_two_le_card` (arXiv:2609.31811) proves stack(T)=estim(T) for |V|≥2. October Conjecture 5.6 states the same equality.

**Cycle conventions.**
- Under ASH\* (not only under the false literal form): stack(C₂ₙ) ≤ 2^{n+1}−1 and clear(C₂ₙ₊₁) ≤ 3·2ⁿ−2, because October Theorems 4.10 and 4.11 are "‖c‖≥" statements.
- Unconditional exact values computed in S003: stack(C6)=15, stack(C8)=31, stack(C7)=17, clear(C7)=22.

## 2026-10-13 author confirmation — provenance, NOT an arXiv amendment

In a reply provided by the recipient (sender Tamás Csernák, cc Lajos Soukup), Tamás confirms that the intended idea is an almost-stacked **largest bad configuration**, precisely **ASH\***. He acknowledges that the stronger *printed* least-exact-t form is false because a critical-layer witness does not force the corresponding statement for every smaller size. The algorithm he describes builds losing layers upward by testing legal moves; see `research/ASHSTAR_ATTACK_BRIEF.md` for the exact elementary recurrence and attempted proof directions.

The author reports successfully determining stacking and clearing thresholds for all graphs with up to 7 vertices (in the valid graph classes), and ASH* holding for that finite atlas. This is **SOURCE_STATED / AUTHOR_REPORTED** (SRC-0010), not a new independent computation: S003 independently resolved 845/853 seven-vertex stacking and 806/809 non-bipartite clearing graphs within t<=55, leaving 8/3 unresolved. The original source's 995/924 total count spans 2<=n<=7; preserve graph-order conventions.

No published correction, universal proof, author verification of our particular P4/bull certificates, permission to quote the entire email, or S004 audit is inferred. S003 is still the last executed research session. Our *target* is now unambiguously universal ASH*.

## Current S004 update (supersedes pending-audit/finite-cutoff prose above)

Printed stack/clear: FALSE, independently cold-audited PASS, Lean pending. Universal ASH* remains OPEN for both goals. Theorem12 supplies an AS non-stackable witness at mass3k for every independent set of size k>=2 on any simple graph. Consequently ASH* holds at g=3alpha+1 or n+1 and for all complete multipartite graphs using cited source threshold equalities.

Order-seven finite coverage is now complete: 853/853 stack and 809/809 eligible clear, by S003 plus S004 independent certificate replay; still finite only. C9 37/46, triangle-tail stack128 and two-triangles-path 36/36 exact. C10 through t16 only; triangle-tail clear>140 with no threshold. See research/S004_ASHSTAR_ATTACK.md and sessions/S004/AUDIT.md. Source PDFs freshly inspected, v1 only and hashes unchanged. Printed-form Phase1 PASS is scoped; universal Phase1 IN_PROGRESS.

## Current S005 update
Universal ASH* remains OPEN, both goals. Exact pure-pile clearing theorem19 uses h(r)=(odd(r,G)-1)/2: clearable iff N%3!=0 or N>=3*2^h(r), with bipartite multiples3 excluded. The rooted lower bound is prior April Theorem6.1; novelty unaudited. This gives ASH*-clear only when that lower bound is attained and supplies no stacking loser. S005 independently finishes C10 stack63 and triangle-tail5 clear190; see audit/campaign for full labelled finite scopes and cutoffs. Global square selection remains HEURISTIC. S006 future/unexecuted.

## Current S006 update

Universal critical ASH* remains OPEN for both goals; printed mathematics PASS and earlier TreeStack credit retained. S006 proves exact rooted pure-pile/buffer conductor interfaces using clearing trees versus stacking forests, with a separate zero-source bit; source pullback and +3 operations credited. Exact AS-ray largest-loser formula and a coarse finite rooted bound do not establish general-versus-binary extremal domination. No infinite triangle-tail threshold upper. See research/S006_ROOTED_CONDUCTORS_AND_EXTREMAL_GAP.md and S006 AUDIT for full proofs, certificate/finite scopes and cutoff. S007 FUTURE/UNEXECUTED; no phase promotion.

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

## Current S012 authority - 2026-10-15

Earlier current/future sections are historical. Last S012, next S013 strictly FUTURE/UNEXECUTED. Universal critical STACK/CLEAR OPEN, printed PASS separate. S01153-58 cold challenge and12 needed check-only replays PASS; historical hashes/cutoffs retained. New59 exact marked-input reciprocity/symmetric TWO insertion and zero-bit protected first move,60 exact donor1/2 languages,61 whole-history originalR3/triangular escape/fuel/componentwise conditional AS at gap>=2,62 distinguished-output occurrence permutation are programme-proved at stated scopes. They do NOT establish global AS selection/gluing. Symmetric assigned C6 masks are not realized inputs; actual critical C5 unit donor exception and double transfer winning only at other roots expose missing root availability, not ASH*. Three prior-hashed dual-validator campaigns pass; two fixed n6 exact threshold controls8/8 and12/12 are computed only. Draft zero-base/donor interpretation failures retained/corrected. Read S012 research/primary/AUDIT/MILESTONES. Fresh new-proof cold challenge FUTURE S013; phases2-6 unchanged/deferred, no human/kernel or worldwide priority assurance. Actual outgoing integration IDs/jobs/main reread belong in S012 PR metadata.

## Current S013 authority - 2026-10-15

Earlier current/future sections are historical. Last S013, next S014 strictly FUTURE/UNEXECUTED. Universal critical STACK/CLEAR OPEN; printed PASS separate. S01259-62 cold challenge and18 needed replays PASS with historical hashes/cutoffs retained. New63-70 prove exact open-neighborhood even concentration (zero/singleton receivers with precise mass3 STACK exception), GLOBAL Q/P minimal-heavy-neighborhood selection and an equivalent restriction of BOTH extremal maxima; conditional CLEAR comparable-component consequence/private-exit burden/all-root THREE exclusion retain explicit scopes. Incomparable minimal neighborhoods and general integer-hole/gluing comparison remain. Actual gap1 first-step shadow and threshold/GLOBAL-Q deletion-independence routes fail, not ASH*. Six registered dual-validator campaigns PASS, no universal/human/kernel/priority assurance. Read S013 research/primary/AUDIT/MILESTONES. Fresh proof cold challenge FUTURE S014; phases2-6 unchanged/deferred. Actual outgoing integration evidence is in S013 PR metadata.
