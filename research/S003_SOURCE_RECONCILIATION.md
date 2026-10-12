# S003 primary-source reconciliation (October 2610.09650v1 vs April 2604.22341v1)

**Access (2026-10-12).** `https://arxiv.org/pdf/2610.09650` returned HTTP 200 in S003. The PDF was read in full from local scratch: 23 pp, 390,157 bytes, SHA-256 `cbc9877b3ce37e720f2305333a21d0078ac2e31f57991c03baedcb4683c27313`.
- arXiv abstract page: v1 only, submitted Wed 7 Oct 2026 08:23:38 UTC; header "arXiv:2610.09650v1 [math.CO] 7 Oct 2026", dated "October 8, 2026" in the paper.
- April PDF re-fetched: SHA-256 `ab34962a77a7caa4126d07430e48ba47b04c57f5ef71c21f85803cf959cbabed`.
- No PDF is mirrored in this repository (no redistribution right asserted).

Access levels:
- **October: STATEMENT_INSPECTED overall.** Definitions 2.1, 3.1, Hypothesis 3.2, Lemma 4.7, Theorems 4.10–4.13, 5.2–5.4, Conjecture 5.6, Lemma 6.4, Theorem 6.9 and 6.11/6.13 were read. **PROOF_INSPECTED** for Lemma 4.7 and Theorem 5.2: both proofs were checked line by line.
- **April: STATEMENT_INSPECTED** (re-read: Thm 2.1, 2.10, 3.1, 5.1, 6.1, 7.3, 7.4, 8.1–8.3, Hyp 9.1, §10–11).

| Item | April v1 | October v1 | Verdict |
|---|---|---|---|
| Graph class | finite simple; stack for connected, clear for connected non-bipartite (Thm 2.10) | same (Def. 2.1, "following [4]") | identical |
| Move, size, stacked, cleared | p.3 | §2, Def. 2.1 | identical |
| stack/clear | least t≥2, every config in Conf_t | least t≥2, every config in Conf_t | identical (exact size, pointwise least) |
| Almost stacked | ∃v0 ∀u≠v0 c(u)≤1 | Def. 3.1, same | identical |
| ASH | Hypothesis 9.1 (1),(2) | Hypothesis 3.2 (1),(2) | **identical wording up to "The stack(G)"→"stack(G)"**; (2) restricted to non-bipartite |
| Monotonicity | (implicit) | Lemma 4.7, for all configurations, t>\|V\| | proof checked; does **not** apply to AS configurations alone |
| Even/odd cycles | Thms 9.4–9.7 | Thms 4.10–4.13 | same statements; AS bounds are "‖c‖ ≥ …" |
| Tree estimate | σ_T(r)=1+Σ deg·2^dist, estim=max_r(σ+leaf) (p.26) | ρ_T(r)=Σ deg·2^dist, estim=max{2, 1+max_r(ρ+leaf)} (Def. 5.1) | **equal for \|V\|≥2** (σ=1+ρ); October adds the K1 value 2. Matches TreeStack `Estimator.lean` for \|V\|≥2 |
| Tree lower bound | — | Thm 5.2, unconditional, witness AS at r of size estim−1 | proof checked (S003) |
| Tree upper bound | Thm 10.1/10.2 (under ASH) | Thm 5.3 (AS, ‖c‖≥ρ_S+leaf_S+1), Thm 5.4 (under ASH) | same structure |
| Tree conjecture | Conj. 10.3 | Conj. 5.6 | already proved by the earlier TreeStack theorem (arXiv:2609.31811, 2026-09-25); the October paper does not cite it — **no inference about awareness** |
| Atlas | §11: atlas_ash_report, trees ≤7 | §1.1 ref [12]: ASH verified for connected n≤7, clearing for non-bipartite n≤7 | provenance below |
| New in October | — | §6 perfectly pebblable graphs (Def. 6.1, Prop. 6.2, Lemma 6.4, Thms 6.9, 6.11, 6.13 under ASH) | depend on AS stackability at size n+1 only (see S003 report §4) |

**Atlas provenance (ref [12]).** Public repository `https://github.com/lajossoukup/pebbling` was read-only shallow-cloned to local scratch (not mirrored): HEAD `701cdd93dd19869a9b90947edd6361efd81cfc1f`, 2026-04-01, "Revised and renamed reports".
- `pebbling.py::Pebbling.stacking_number` computes the non-stackable sets layer by layer.
- `is_critical_stacked_almost_stacked` returns `any(is_almost_stacked(c) for c in witness_set)`, where witness_set is the non-stackable configurations at level stack(G)−1.
- `atlas_ash_report.tex` reports 995/995 (stack) and 924/924 (clear) successes over NetworkX atlas graphs with 2≤n≤7.

**This tests the critical form ASH\*, not the printed Hypothesis.** By S003 Theorem 4, ASH\* is equivalent to an AS witness existing at level g(G)−1. The printed statement is refuted at n=4 (stack) and n=5 (clear); see `research/S003_AS_GAP_AND_ATTACKS.md`.

**Chronology (unchanged, no priority adjudication).**
1. April 2604.22341v1: 2026-04-24.
2. TreeStack arXiv:2609.31811v1: 2026-09-25.
3. October 2610.09650v1: 2026-10-07.

The October tree Conjecture 5.6 coincides with the earlier TreeStack theorem for |V|≥2. The October K1 convention estim=2=stack(K1) is consistent with it.
