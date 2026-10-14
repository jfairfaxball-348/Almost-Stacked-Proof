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
