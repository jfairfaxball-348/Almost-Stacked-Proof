# Source catalogue — current after S009

Per-material proof access is scoped in the S009 foundational report; no unseen original proof is inferred.

- **SRC-0001** The Almost Stacked Hypothesis: A Conjectural Analogue of Sjöstrand's Cover Pebbling Theorem — **PROOF_INSPECTED**. https://arxiv.org/abs/2610.09650 — S003: full v1 PDF read (sha256 cbc9877b...); Hypothesis 3.2, Defs 2.1/3.1/5.1, Lemma 4.7 and Thm 5.2 proofs checked (PROOF_INSPECTED for those two); see research/S003_SOURCE_RECONCILIATION.md S004 2026-10-13 fresh current version list v1 only and PDF digest unchanged; statements re-inspected. No posted revised hypothesis in fetched text. S005 same v1 PDF hash; equation4.10 proof operation freshly inspected. S006 current v1 list and PDF digest freshly verified unchanged; relevant proof portions re-inspected. S007 current v1/PDF digest unchanged; April6.1 and October4.7/pullback/+3 selected proof portions re-inspected. S008 current v1/PDF digest unchanged; selected definitions, monotonicity/pullback/+3 and April6.1 proofs re-inspected, no comprehensive novelty audit. S009 foundational comparison: full primary material and named proofs inspected; precise per-proof scope/slips in research/S009_PRIOR_ART_AND_DEPENDENCY_AUDIT.md, no kernel/priority claim.

- **SRC-0002** Stacking and clearing in graph pebbling — **PROOF_INSPECTED**. https://arxiv.org/abs/2604.22341 — April v1 full PDF (sha256 ab34962a...) definitions p3, Hypothesis 9.1 p20, Thms 2.1, 2.10, 3.1, 5.1, 6.1, 7.3, 7.4, 8.1-8.3, 9.4-9.7, 10.1-10.3, s11 read; not a full proof audit S004 2026-10-13 fresh current version list v1 only and PDF digest unchanged; statements re-inspected. No posted revised hypothesis in fetched text. S005 continuation freshly inspects full Theorem6.1 proof/internal rooted claim; root odd-walk bound is prior source work. S006 current v1 list and PDF digest freshly verified unchanged; relevant proof portions re-inspected. S007 current v1/PDF digest unchanged; April6.1 and October4.7/pullback/+3 selected proof portions re-inspected. S008 current v1/PDF digest unchanged; selected definitions, monotonicity/pullback/+3 and April6.1 proofs re-inspected, no comprehensive novelty audit. S009 foundational comparison: full primary material and named proofs inspected; precise per-proof scope/slips in research/S009_PRIOR_ART_AND_DEPENDENCY_AUDIT.md, no kernel/priority claim.

- **SRC-0003** The stacking number of a tree — **PROOF_INSPECTED**. https://arxiv.org/abs/2609.31811 — Exact Lean Stacking/Estimator/RootScore/UpperBound and defect-flow proof notes inspected; no new kernel build in S002 S009 foundational comparison: full primary material and named proofs inspected; precise per-proof scope/slips in research/S009_PRIOR_ART_AND_DEPENDENCY_AUDIT.md, no kernel/priority claim.

- **SRC-0004** TreeStack Palomar entry — **METADATA_ONLY**. https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-25-000010&version=1 —

- **SRC-0005** Davenport-Counterexample-Hunt — **STATEMENT_INSPECTED**. https://github.com/jfairfaxball-348/Davenport-Counterexample-Hunt —

- **SRC-0006** Sjöstrand cover pebbling — **PROOF_INSPECTED**. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v12i1n22 — Sjöstrand 2005 EJC 12(1) N22, DOI 10.37236/1989, publisher abstract inspected S009 foundational comparison: full primary material and named proofs inspected; precise per-proof scope/slips in research/S009_PRIOR_ART_AND_DEPENDENCY_AUDIT.md, no kernel/priority claim.

- **SRC-0007** Soukup, Computational data and reports for graph pebbling (atlas code and reports) — **STATEMENT_INSPECTED**. https://github.com/lajossoukup/pebbling — S003 read-only shallow clone at 701cdd93dd19869a9b90947edd6361efd81cfc1f (2026-04-01): is_critical_stacked_almost_stacked tests the critical form (AS witness at level stack-1), not the printed least-t equality; atlas_ash_report.tex 995/995 stack, 924/924 clear for 2<=n<=7

- **SRC-0008** S002 CAM-S002-01 six eight-vertex exhaustive exact search and reverse cold checker — **STATEMENT_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/tree/main/tools — Locally executed full forward recursion plus 420 BFS checks and reverse full W8/bridge-K4 layers; raw output hash in S002 report/attached bundle

- **SRC-0009** S003 CAM-S003-01 exact layered solvers, atlas n<=7, trees n<=9, literal-gap certificates — **STATEMENT_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/tree/main/evidence/S003 — Forward C DP, independent reverse C solver, Python reverse fixpoint, AS memo solver, independent certificate checker; hashes in evidence/S003/HASHES.md

- **SRC-0010** Tamás Csernák reply to John Fairfax-Ball, cc Lajos Soukup (2026-10-13) — **STATEMENT_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/main/outreach/2026-10-csernak-soukup/2026-10-13_AUTHOR_REPLY.md — Owner supplied the full message text in chat, displayed received 2:59 PM, exact headers/timezone unverified; public record is attributed summary only, not verbatim message or published correction; author reports intended ASH*, printed false, all n<=7 tested.

- **SRC-0011** S004 cold audit, sparse frontier layers, packed canonical-parent replay, structural atlas — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/tree/main/evidence/S004 — Fresh cold reverse-winning DP, independent packed-state complete sparse certificate replay, base layer cross-check; full scope and cutoffs in S004 PLAN/AUDIT/report; no Lean.

- **SRC-0012** S004 independent-set almost-stacked obstruction and structural proof attacks — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/main/research/S004_ASHSTAR_ATTACK.md — Complete symbolic proofs; lower-bound witness and complete multipartite consequence; universally unresolved. Novelty not audited; source exact thresholds credited.

- **SRC-0013** S005 exact pure-pile clearing, ancestry lower proof and structural failures — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/main/research/S005_ASHSTAR_EXTREMA_AND_ROOTED_CLEARING.md — Exact classification with prior odd-walk lower bound and +3 operation credited; no novelty or Lean claim. Universal target OPEN.

- **SRC-0014** S005 all-parent binary layers, canonical-parent replay and auxiliary legal traces — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/tree/main/evidence/S005 — Explicit graph scopes, complete/cutoff layers and independent set replay; Q and pure-pile challenge; no universal or kernel certification.

- **SRC-0015** S006 exact rooted pure/buffer conductors, stacking forests and finite bounds — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/main/research/S006_ROOTED_CONDUCTORS_AND_EXTREMAL_GAP.md — Complete tree/forest/interface/finiteness proofs; universal ASH* comparison remains OPEN, novelty unaudited, no Lean.

- **SRC-0016** S006 independent grammar optimality/legality certificates and dual rooted DP challenges — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/tree/main/evidence/S006 — All production inequalities/infinities and attaining derivations checked; complete bounded forward/reverse mask equality, explicit state cutoff and auxiliary closures. No universal ASH* certificate.

- **SRC-0017** S007 selected ancestry credit, sharp triangle-tail clearing and leaf extensions — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/main/research/S007_LEAF_CREDIT_AND_TRIANGLE_TAILS.md — Complete symbolic proofs, prior odd-walk lower credited; universal ASH* OPEN; no novelty or Lean. S008 hostile audit PASS at exact stated scopes; Theorem33 remains explicitly conditional.

- **SRC-0018** S007 full forward/reverse triangle-tail layers and independent constructive trace replay — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/tree/main/evidence/S007 — Exact labelled l=0,1,2 only, complete full set hashes/counts, all constructive winning traces independently replayed; no universal certification.

- **SRC-0019** S008 hostile audit, symbolic ancestry dual, exact triangle-tail stacking and common-root leaf thresholds — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/main/research/S008_HOSTILE_AUDIT_AND_UNIVERSAL_ROUTES.md — Complete scopes/dependencies/production case proofs and universal ideal/tightness reformulation; universal comparison OPEN, novelty unaudited, no Lean.

- **SRC-0020** S008 exact buffer certificates, universal symbolic inequalities and independent branch layer/trace checks — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/tree/main/evidence/S008 — Registered l0..8 named buffer/l0..3 closures and F_k k1..3 layers;4376 universal symbolic differences; precise counts/scopes in AUDIT, no universal/kernel certification.

- **SRC-0021** General graph pebbling — **PROOF_INSPECTED**. https://glennhurlbert.github.io/Papers/GGPpub.pdf — Hurlbert 2013; exact >=D semantics, no-cycle/balance, block/target definitions; selected proofs only.

- **SRC-0022** A Graph Pebbling Algorithm on Weighted Graphs — **PROOF_INSPECTED**. https://jgaa.info/index.php/jgaa/article/download/paper205/2754 — Sieben 2010; publisher web text Props3.1/3.3/7.3/8.1 inspected. Direct403/glyph failures retained; no usable local published digest claimed.

- **SRC-0023** The cover pebbling number of graphs — **PROOF_INSPECTED**. https://glennhurlbert.github.io/Papers/CPNGpub.pdf — Crull et al. 2005 Thms6/7 and leaf demand/supply/cycle-removal proofs inspected.

- **SRC-0024** Cover Rubbling and Stacking — **PROOF_INSPECTED**. https://faculty.etsu.edu/keatonr/documents/CoverRubbling.pdf — Haynes-Keaton 2020; initial simple-pile cover cost, extra rubbling move. Lemma5/Thm2 proof inspected,3/4 statements only.

- **SRC-0025** Target pebbling in trees — **PROOF_INSPECTED**. https://glennhurlbert.github.io/Papers/TPITpub.pdf — Adauto et al. 2026 Thm13/11/Lemma18/Cor19 proof comparison; fixed demand/leftovers and lex no-merging, not exact forests.

- **SRC-0026** Pebbling graphs by their blocks — **STATEMENT_INSPECTED**. https://arxiv.org/abs/0811.3238 — Curtis-Hines-Hurlbert-Moyer 2009; rooted block-cost and clique-block statements; imperfect published extraction, no full proof audit.

- **SRC-0027** Pebbling in hypercubes — **ABSTRACT_INSPECTED**. https://epubs.siam.org/doi/abs/10.1137/0402041 — Chung 1989 official primary metadata/abstract; original proof retrieval unsuccessful, no full proof access claimed.

- **SRC-0028** Pebbling graphs — **ABSTRACT_INSPECTED**. https://www.sciencedirect.com/science/article/pii/009589569290043W — Moews 1992 primary abstract; original proof access unresolved.

- **SRC-0029** On pebbling graphs — **METADATA_ONLY**. https://arxiv.org/abs/2604.22341 — Pachter-Snevily-Voxman 1995 Congressus Numerantium107:65-80, primary reference-list trail only; URL is citing primary paper, not full original.

- **SRC-0030** Lollipop and cubic weight functions for graph pebbling — **PROOF_INSPECTED**. https://arxiv.org/abs/2310.00580 — Yang-Yerger-Zhou v2, selected Thm3 proof; root reachability allows leftovers, not exact triangle-tail stacking.

- **SRC-0031** Modified Linear Programming and Class 0 Bounds for Graph Pebbling — **STATEMENT_INSPECTED**. https://arxiv.org/abs/1508.07299 — Cranston et al.; lollipop/weight Lemmas1-3 statements and selected Lemma3 proof, no comprehensive proof audit.

- **SRC-0032** Stacking and Clearing in Directed Graph Pebbling — **STATEMENT_INSPECTED**. https://arxiv.org/abs/2606.04659 — Csernak-Soukup June2026v1, directed-cycle/existence conditions compared; not universal undirected ASH*.

- **SRC-0033** S009 foundational primary-source and dependency audit — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/main/research/S009_PRIOR_ART_AND_DEPENDENCY_AUDIT.md — Dated bounded queries and every substantial S004-S008 dependency comparison; foundational Phase1, no worldwide priority/gate promotion.

- **SRC-0034** S009 exact excursions, marked frontiers and dominated credit — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/main/research/S009_UNIVERSAL_RESEARCH.md — Complete Thm38/Lemmas39-40/Props41,43/Cor42 proofs; universal ASH* OPEN, new results cold challenge futureS010.

- **SRC-0035** S009 independent port closures and protected credit validation — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/tree/main/evidence/S009 — Two preregistered campaigns,318 named inputs and3860 upper traces, complete independent finite scopes; retained failed attempts; no universal/kernel certificate.
