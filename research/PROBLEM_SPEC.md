# ASH precise problem specification — SOURCE-TRANSCRIPTION GATE

**Authority:** Csernák & Soukup, [arXiv:2610.09650](https://arxiv.org/pdf/2610.09650) (October 2026), plus [arXiv:2604.22341](https://arxiv.org/abs/2604.22341). As of S001 the October **abstract** was inspected; full original 23-page PDF could not be read directly. **This file is a working synopsis, not a verbatim audited formal statement.** S002 must transcribe exact original hypothesis numbering, wordings, threshold conventions and relevant definitions with page citations.

Working finite-graph pebbling model:
- Graph finite, simple unless the source states otherwise; graph class and connectivity need primary verification.
- A configuration `c : V(G) -> Nat`; total mass `|c| = Σ_v c(v)`.
- Legal move along `u ~ v`: if `c(u)>=2`, replace `c(u)` by `c(u)-2` and `c(v)` by `c(v)+1`; all other entries unchanged.
- *Stackable*: there is a finite legal move sequence ending with all surviving pebbles on one vertex. Note total pebbles decrease under moves; distinguish 'stackable at a specified root' and 'some root'.
- *Clearable*: under source convention, legal moves achieve a configuration with one surviving pebble; check whether zero-pebble configurations, trivial graphs and exact target conventions are excluded.
- *Almost stacked*: some `v0` exists with `c(u)<=1` for each `u≠v0`.
- Working `AS_stack(G)`: testing almost-stacked `t`-configurations is sufficient to identify the universal stack threshold. `AS_clear(G)` similarly for connected non-bipartite graphs. **Do not use this paraphrase to justify proofs or novelty until source theorem checked.**

Important logical boundaries:
1. `stack(T)=estim(T)` on finite nontrivial trees is established in the separate TreeStack project, but **does not imply general ASH**, and should not be used as its converse without proof.
2. The source proves almost-stacked even-cycle and odd-cycle cases; ASH would promote these to general statements. The paper's *conditional* cycle formula is not itself an ASH proof.
3. Universal stacking on all finite connected graphs and clearing on all finite connected non-bipartite graphs may be independent or have reductions. Test any proposed implication with explicit proof; do not assume equivalence.
4. Exact-size thresholds `t`, `t>=2`, graph `|V|=1`, bipartite clearability, and how zero pebbles are handled can reverse edge cases. Read the text, not only abstracts.
5. A counterexample to the threshold equality must establish both the almost-stacked threshold `t` and existence of a non-stackable/non-clearable *general* configuration of that same `t`, or another logically equivalent precise witness in the paper's convention; a lone hard configuration is insufficient.

## S002 expected definitive deliverables

A page/theorem-number indexed transcription table, a machine-readable `research/ASH_SPEC.json`, two precise statement families with all quantified graph assumptions, explicit edge-case verdicts, and independent equivalence proofs between the exact theorem and any computational formulation. If primary source access fails, retain unverified status and do not certify a counterexample.


**S002 2026-10-12 source status update:** The exact original **April Hypothesis 9.1**, arXiv:2604.22341v1, PDF p20 and definitions p3, was independently inspected. It specifies finite connected G for stack, additionally non-bipartite G for clear, exact sizes t≥2, and at most one vertex carrying more than one pebble. See `research/ASH_SPEC.md` and JSON. **The October arXiv:2610.09650 full PDF is still inaccessible**; its numbering/rewritten details are not transcribed and the October gate is not PASS. No contradiction to original April source asserted. S002 exact eight-vertex survey is bounded to those verified original definitions and is not a proof/counterexample to universal ASH.

**S003 2026-10-12 status update.**
- The October full text was read. Its Hypothesis 3.2 has the same content as April 9.1; see `research/ASH_SPEC.md`.
- That printed form is refuted (P4 stack, bull clear, t=12). The working open target is the critical form ASH\*: for n≥2, an AS non-g-able configuration of size g(G)−1 exists. See `research/S003_AS_GAP_AND_ATTACKS.md`.

**2026-10-13 intended-form clarification (private author correspondence).** The author confirms the intended conjecture is ASH*, not the refuted pointwise single-layer minimum. The definitive definitions, literal failure, and critical-form target are in `research/ASH_SPEC.md` (v1 paper) and `research/ASHSTAR_ATTACK_BRIEF.md`. The 2026-10-13 letter is author testimony, not a revised public PDF. Source-version recheck remains mandatory in S004.
