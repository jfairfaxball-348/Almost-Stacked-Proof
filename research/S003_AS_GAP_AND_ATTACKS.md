# S003 — The AS-gap reformulation, a certified counterexample to the literal ASH, and the critical form

**Status summary (2026-10-12).**
- **Literal ASH, both halves: FALSE (certified finite counterexamples; Lean pending, independent cold audit pending).** This is the hypothesis exactly as printed in October Hypothesis 3.2 and April Hypothesis 9.1.
  - Stacking fails on the path P4 at t=12.
  - Clearing fails on the 5-vertex non-bipartite bull graph at t=12.
- **Critical (monotone) form ASH\*: OPEN.** This is the form the authors' public atlas code actually tests.
  - It holds on every connected graph with at most 7 vertices whose threshold was found, and on every connected 8-vertex graph with threshold ≤26 (independent exhaustive computation), as well as on the selected larger graphs computed.
  - It holds for every finite tree with ≥2 vertices, by combining two earlier theorems (§5).
  - Its universal truth remains unresolved.

No contact with the authors, no novelty or priority claim and no Lean work were done. The counterexample is to the *printed* statement. §6 explains why this is plausibly a formulation slip relative to the authors' intent. It is not described as "ASH is disproved" without that qualification.

## 1. Model and notation (verbatim conventions of October Def. 2.1, 3.1; April p.3)

G is a finite simple connected graph, n=|V(G)|. A configuration is c: V→ℕ with size ‖c‖=Σc(v). A move u⇒v along an edge requires c(u)≥2 and replaces c(u),c(v) by c(u)−2, c(v)+1.
- *Stacked*: |supp c|=1. *Cleared*: ‖c‖=1. Goal g∈{S,C}; C is used only for non-bipartite G.
- *Almost stacked (AS)*: ∃v0 ∀u≠v0, c(u)≤1.
- Lose_g(t) = {c∈Conf_t : c not g-able}, ASLose_g(t) = Lose_g(t) ∩ AS.
- g(G) = stack(G) or clear(G) = least t≥2 with Lose_g(t)=∅. This exists by April Thm 2.10.

Two readings of the hypothesis:
- **Literal (printed) ASH_g(G):** g(G) = a_g(G), where a_g(G) := least t≥2 with ASLose_g(t)=∅.
- **Critical / monotone ASH\*_g(G):** g(G) = a\*_g(G), where a\*_g(G) := least t₀≥2 with ASLose_g(t)=∅ for **every** t≥t₀.

## 2. Elementary structure (PROGRAMME_PROVED; complete proofs)

**Lemma 1 (terminal singletons).** If n≥2 and 2≤t≤n, then ASLose_g(t)≠∅. Hence g(G)≥n+1 and a_g(G)≥n+1.

*Proof.* A 0/1 configuration with t ones is AS and terminal (no vertex has 2 pebbles). It has support t≥2 and size t≥2, so it is neither stacked nor cleared. ∎

**Lemma 2 (monotonicity above the order; independent re-proof of October Lemma 4.7).** Let n≥2 and t>n. If Lose_g(t)=∅, then Lose_g(t')=∅ for all t'≥t.

*Proof.* Let ‖c‖=t'>t>n. By pigeonhole some vertex holds ≥2 pebbles. G is connected with n≥2, so that vertex has a neighbour and a legal move exists, lowering the size by exactly 1. Repeat until size t. The result is g-able, hence so is c. ∎

**Proposition 3.** For n≥2: Lose_g(t)≠∅ for 2≤t<g(G), and Lose_g(t)=∅ for t≥g(G).

*Proof.* For t≤n use Lemma 1. For n<t<g(G): if Lose_g(t)=∅, Lemma 2 makes every size ≥t empty, so g(G)≤t, a contradiction. For t≥g(G) use g(G)≥n+1 and Lemma 2. ∎

**Theorem 4 (AS-gap reformulation).** Let n≥2.
- (i) ASH_g(G) ⇔ ASLose_g(t)≠∅ for every t with n<t<g(G).
- (ii) ASH\*_g(G) ⇔ ASLose_g(g(G)−1)≠∅. Equivalently, the largest size of a non-g-able configuration is attained by an AS configuration.
- (iii) ASH ⇒ ASH\*, and a_g ≤ a\*_g ≤ g(G).

*Proof.* ASLose_g(t) ⊆ Lose_g(t) = ∅ for t≥g(G), so a_g ≤ g(G) and a\*_g ≤ g(G).
- (i) a_g = g(G) iff ASLose_g(t)≠∅ for all 2≤t<g(G). Lemma 1 covers t≤n.
- (ii) Let M = max{t≥2 : ASLose_g(t)≠∅}. M is well defined because t=2 qualifies, and M ≤ g(G)−1. Then a\*_g = M+1, so a\*_g = g(G) iff M = g(G)−1.
- (iii) follows from (i) and (ii). ∎

For n=1 (K1): stack(K1)=2=a=a\*. K1 is bipartite, so clearing does not apply.

**Corollary 5 (counterexample certificate shape).** Suppose t>n, every AS configuration of size t is g-able, and some configuration of size t is not g-able. Then ASH_g(G) fails, because a_g(G) ≤ t < g(G) by Proposition 3. The certificate needs no knowledge of g(G).

## 3. Literal ASH is false — certified examples

**Theorem 6 (stacking).** Let P4 have vertices 0–1–2–3, n=4.
- (W) All 32 AS configurations of size 12 are stackable. Each has an explicit replayed move sequence in `evidence/S003/cert_P4_stack_t12.json`.
- (L) c=(1,0,2,9) is not stackable. Its reachable set has 50 configurations; it is closed under legal moves and contains no stacked configuration (same file).

By Corollary 5, a_S(P4) ≤ 12 < stack(P4). In fact a_S(P4)=12 and stack(P4)=15 = 2⁴−1:
- April Thm 7.4;
- TreeStack estim(P4)=15;
- our exhaustive three-solver computation.

So the printed Hypothesis 3.2(1) / 9.1(1) fails on the path P4.

**Theorem 7 (clearing).** The bull graph B has V={0,…,4} and E={2-3, 3-4, 4-2, 1-3, 0-4}: a triangle 2,3,4 with pendant vertices 1 at 3 and 0 at 4. It is non-bipartite.
- (W) All 80 AS configurations of size 12 are clearable (replayed sequences).
- (L) (1,9,0,2,0) has a closed, goal-free reachable set of 96 configurations.

Hence a_C(B) ≤ 12 < clear(B) = 15 (exact, three solvers). So the printed Hypothesis 3.2(2) / 9.1(2) fails. The same data also give a stacking counterexample on B: stack(B)=15, with a gap at 12.

**Minimality (exhaustive, COMPUTED_EXACT).**
- No connected graph with ≤3 vertices violates either literal half.
- Among connected 4-vertex graphs only P4 violates literal stacking.
- No non-bipartite graph with ≤4 vertices violates literal clearing.
- Exactly three 5-vertex non-bipartite graphs violate literal clearing:
  - the bull, gap 12, clear 15;
  - the diamond with a pendant vertex, gap 12, clear 15;
  - the triangle with a pendant path of length 2, gaps 16 and 19, clear 22.

**Independence of evidence.** P4 is checked by all five tools (a)–(e) below. The bull graph B is checked by (a), (b), (c) and (e); (d) handles stacking on trees only.
- (a) the forward C DP `tools/cam_s003_fwd.c`;
- (b) the independently written reverse C solver `tools/cam_s003_rev.c`, which uses a different ranking;
- (c) the Python reverse fixpoint (run on P4 and B for t≤16, and on the T1/T4 graphs);
- (d) the per-configuration memo solver `tools/cam_s003_as.c`;
- (e) the certificate builder/checker `tools/cam_s003_cert.py`. It shares no code with (a)–(d); it replays every winning sequence and recomputes the loser's full reachable set.

The certificates themselves are finite, human-checkable proofs (32 short move sequences and a 50-element closed set for P4). AGENTS rule 7 additionally requires a later Lean kernel proof and a cold re-check. Both are pending: Phase 3, and S004 respectively.

**Prevalence (COMPUTED_EXACT; atlas n≤6).** Literal stacking fails on 21 of 143 connected graphs, and literal clearing on 19 of 115 non-bipartite ones. In trees (T3; stack(T)=estim(T) by the earlier TreeStack theorem, cross-checked exhaustively for n≤6), 77 of the 88 completed trees with 2≤n≤9 violate the printed form. Every observed gap lies in {estim−6, estim−3}, and estim−3 is a gap whenever any gap occurs. The gap-free trees are stars and a few spiders. Paths P4–P8 have gaps exactly at 2ⁿ−7 (n≥5) and 2ⁿ−4 (conjecture CLM-0024). Full lists are in `evidence/S003/`.

## 4. Consequences for the source's conditional theorems

The applications in October §4–5 survive if ASH is replaced by ASH\*, because their AS inputs are stated for all sizes at or above the threshold:
- Theorems 4.10, 4.11: ‖c‖ ≥ 2^{n+1}−1 and ‖c‖ ≥ 3·2ⁿ−2 respectively.
- Theorem 5.3: ‖c‖ ≥ ρ_S(r)+leaf_S(r)+1. Note that ρ_S(r)+leaf_S(r) ≤ ρ_T(r)+leaf_T(r) for every subtree S∋r, because a vertex that is a leaf of S but internal in T contributes 1 to leaf_S and at least 4 to ρ_T.

So ASH\*_g on the relevant graphs still gives:
- stack(C₂ₙ) ≤ 2^{n+1}−1;
- clear(C₂ₙ₊₁) ≤ 3·2ⁿ−2;
- stack(T) ≤ estim(T).

The perfectly-pebblable results (October Cor. 6.6, Thms 6.9, 6.11, 6.13) use only AS stackability at the single size n+1. Literal ASH would be enough for them, but literal ASH is false in general. Under ASH\* they would additionally need AS stackability at every size >n+1. **Their conclusions are therefore currently unsupported by any true form of ASH known here.** They are not shown false. This is recorded as an open dependency, not as a refutation.

## 5. Critical form ASH\*: what is proved, computed and refuted

**Theorem 8 (ASH\* for trees; PROGRAMME_PROVED relative to two cited theorems).** Every finite tree T with |V|≥2 satisfies ASH\*_S. The proof combines:
- (a) the earlier TreeStack theorem stack(T)=estim(T) (arXiv:2609.31811; formally certified in its own repository by `TreeStack.stack_eq_estim_of_two_le_card`; INHERITED, not re-built here);
- (b) October Theorem 5.2's witness ρ_T(r)·e_r + Σ_{leaves ℓ≠r} e_ℓ, of size estim(T)−1. This witness is AS at r, and the proof that it is non-stackable was read and checked line by line in S003 (mod-3 weight R=2^{dist}, forced upward moves out of every off-path subtree).

Then ASLose_S(stack(T)−1) ≠ ∅ and Theorem 4(ii) applies. T3 confirms an AS loser at estim−1 for all 87 completed trees with 3≤n≤9. There are 94 trees with 2≤n≤9. For K2, size estim−1=2≤n is covered by Lemma 1. Six trees of order 9 with estim≥163 exceeded the 3 GiB per-tree limit and are reported incomplete. This credits the earlier tree theorem; it is not a new tree result.

**Theorem 9 (trivial cases).** If g(G)=n+1, then the all-ones configuration on n vertices is an AS loser of size g(G)−1. So ASH\*_g holds, e.g. for K_n (n≥3) and for every perfectly pebblable graph for clearing.

**Theorem 10 (ASH\* for complete bipartite graphs; PROGRAMME_PROVED relative to April Thm 8.2).** Let G=K_{a,b} with bipartition (A,B), |B|=α=max(a,b)≥|A| and a+b≥3, so α≥2. Fix w∈B and put B′=B∖{w}. Define

c = (2α+1)·e_w + Σ_{x∈B′} e_x.

Then c is AS at w, has size 3α, and is not stackable. With April Thm 8.2 (stack(K_{a,b})=3α+1; SOURCE_STATED, proof not inspected here, and computed exactly for 7 small cases in S003), Theorem 4(ii) gives ASH\*_S(K_{a,b}).

*Proof of non-stackability.* Let R(v)=2^{dist(w,v)}: R=1 on w, 2 on A, 4 on B′. Write w_R(d)=Σ d(v)R(v). A move x⇒y changes w_R by −ℓ(x⇒y), where ℓ(x⇒y)=2R(x)−R(y). The losses are:

| move | w⇒A | A⇒w | A⇒B′ | B′⇒A |
|---|---|---|---|---|
| loss ℓ | 0 | 3 | 0 | 6 |

All losses are non-negative and divisible by 3. Initially w_R(c)=(2α+1)+4(α−1)=6α−3≡0 (mod 3).

Suppose some sequence reaches k·e_s. Then w_R(final)=k·R(s)≡0 (mod 3) with R(s) a power of 2, so 3∣k and w_R(final)≥3R(s). Every x∈B′∖{s} starts with one pebble and ends with none. Pebbles leave x only by moves x⇒A, so each such x forces a loss of at least 6.
- **s∈A:** w_R(final) ≤ 6α−3−6(α−1) = 3 < 6 ≤ 3R(s). Contradiction.
- **s∈B′:** w_R(final) ≤ 6α−3−6(α−2) = 9 < 12 = 3R(s). Contradiction.
- **s=w:** the bound gives k=w_R(final)=3 and total loss exactly 6(α−1). Hence:
  - each x∈B′ fires exactly once (one move x⇒A);
  - no move A⇒w occurs;
  - each x∈B′ receives exactly one pebble (net change −1 with one firing), necessarily by a move A⇒x before its firing, since x needs two pebbles to fire.

  Let x\* be the vertex of B′ that fires last (B′≠∅ since α≥2), say at time T, sending a pebble into A. After T, any move leaving A is some A⇒y with y∈B′, and y must fire later still. That contradicts the choice of x\*, because x\*'s only arrival precedes T. So A is non-empty at the end, contradicting stacked at w. ∎

Exhaustive check (S003): this c is non-stackable on all 24 graphs K_{a,b} with 1≤a≤5, a≤b≤7, a+b≥3. **Limitation:** the weight argument does not extend verbatim to complete k-partite graphs with k≥3, because moves between two non-B parts lose 2. That case (April Thm 8.3) is left open where 3α>n.

**Computed (COMPUTED_EXACT, exact thresholds):**
- ASH\*_S and ASH\*_C hold on every connected graph with ≤6 vertices: 143 for stack, 115 for clear.
- n=7, all 853 connected graphs with t≤55: ASH\* holds on every graph whose threshold was found (845 stack; 806 of 809 non-bipartite clear). The printed form fails on 112 (stack) and 123 (clear). This independently replicates the authors' n≤7 claim under its critical reading, with code that shares nothing with theirs.
- n=8, all 11117 connected graphs with cap t≤26: ASH\* holds on all 10225 graphs with stack≤26 and all 10052 non-bipartite graphs with clear≤26. The printed form fails on 613 / 612 of these, and literal gaps also appear inside 166 / 169 cutoff graphs. The 892 / 883 graphs with thresholds above 26 carry no ASH\* verdict.
- They hold on C6, C7, C8, C8+{0,4}, C8+{0,2},{4,6}, K2,6, W8, W9 and the Petersen graph (stack=clear=15). The triangular ladder with leaves (t≤40) and C9+{0,4} (t≤30) exceed their caps.
- Exact values computed include stack(C8)=31 (an unconditional finite value, equal to the conditional October formula at n=4), stack(C7)=17, clear(C7)=22, and stack=clear=23 for C8+{0,4}.

**Failed auxiliary statements (smallest counterexamples; none refutes ASH\*):**
- (A) "AS-loss is downward closed on t>n". False: P4, AS-loss at 13 but not 12. Equivalent to literal ASH failing.
- (C) "Every critical loser (size g(G)−1) is AS". False: smallest is the 5-cycle (labels 0-3-2-1-4-0) at t=7 with loser (0,0,3,3,1). W8 at t=10 has 28 critical losers, of which 14 are AS.
- (B′) "Same-mass pair transfers c ↦ c+2e_u−2e_w inside the critical loser set connect every critical loser to an AS one" (route B, existential form). False: same 5-cycle example. Fails for 7 of 134 graphs (stack) and 3 of 112 (clear) on the n≤6 atlas (layers ≤ 2·10⁵).
- (B″) "Moving the whole even part of one heavy pile onto another heavy vertex preserves critical loss for some choice". False: same 5-cycle example.

Critical losers on n≤6 carry up to 5 heavy piles (stack) or 4 (clear). So a proof of ASH\* cannot proceed by compressing critical losers within the critical layer.

## 6. Interpretation and provenance (no wrongdoing asserted)

The printed equality "stack(G) is the least t≥2 such that every AS configuration in Conf_t(G) is stackable" is a pointwise statement. October Lemma 4.7 makes the analogous statement for all configurations automatically monotone above n. For AS configurations it is not, because a move from an AS configuration generally destroys the AS property.

The authors' public code (`lajossoukup/pebbling`, commit `701cdd93…`, 2026-04-01; `pebbling.py`, `Pebbling.is_critical_stacked_almost_stacked`) checks only whether the non-stackable witnesses at level stack(G)−1 include an AS configuration. That is exactly ASH\* by Theorem 4(ii). Its report (`atlas_ash_report.tex`) records 995/995 and 924/924 passes for 2≤n≤7, consistent with our n≤6 replication of ASH\* and with the literal failures (which that code does not test).

The verbal gloss in both papers ("thresholds can be determined by testing only almost stacked configurations") is compatible with ASH\*. This is reported as a discrepancy between the printed statement and the tested statement. It is not reported as an error in the authors' computations.

## 7. Remaining obstruction (for S004)

Prove or refute ASH\*: "the largest size of a non-stackable (non-clearable, G non-bipartite) configuration is attained by an almost-stacked configuration".

Known ingredients:
- trees (Theorem 8);
- complete bipartite graphs (Theorem 10);
- g(G)=n+1 (Theorem 9);
- cycles C₂ₙ, which hold iff stack(C₂ₙ)=2^{n+1}−1 and an AS loser of size 2^{n+1}−2 exists. Computed true for n≤4.

Dead ends: critical-layer compression (§5). Promising directions:
- a *global* certificate of non-stackability (weight/mod-3 invariants as in October Thm 5.2 and April Lemma 2.5) whose extremal configurations can be taken AS;
- block/bridge decomposition, where trees are already settled;
- search for an ASH\* counterexample among graphs whose g(G) is computable but large (n=8 sparse non-tree graphs beyond the S003 cap).

## Dependency DAG

```
Lemma 1 ─┐
Lemma 2 ─┴─> Prop 3 ─> Thm 4 ─┬─> Cor 5 ─> Thm 6, Thm 7   [+ certificates; Lean pending]
                              ├─> Thm 8   [+ TreeStack theorem (cited) + October Thm 5.2 (proof read)]
                              ├─> Thm 9
                              └─> Thm 10  [+ mod-3 weight/ordering argument + April Thm 8.2 (cited)]
```
