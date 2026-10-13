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
