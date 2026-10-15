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
