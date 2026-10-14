# Source catalogue — current after S007

Per-material access levels retained; inspection of selected proofs is not a full-paper audit.

- **SRC-0001** The Almost Stacked Hypothesis: A Conjectural Analogue of Sjöstrand's Cover Pebbling Theorem — **STATEMENT_INSPECTED**. https://arxiv.org/abs/2610.09650 — S003: full v1 PDF read (sha256 cbc9877b...); Hypothesis 3.2, Defs 2.1/3.1/5.1, Lemma 4.7 and Thm 5.2 proofs checked (PROOF_INSPECTED for those two); see research/S003_SOURCE_RECONCILIATION.md S004 2026-10-13 fresh current version list v1 only and PDF digest unchanged; statements re-inspected. No posted revised hypothesis in fetched text. S005 same v1 PDF hash; equation4.10 proof operation freshly inspected. S006 current v1 list and PDF digest freshly verified unchanged; relevant proof portions re-inspected.

- **SRC-0002** Stacking and clearing in graph pebbling — **STATEMENT_INSPECTED**. https://arxiv.org/abs/2604.22341 — April v1 full PDF (sha256 ab34962a...) definitions p3, Hypothesis 9.1 p20, Thms 2.1, 2.10, 3.1, 5.1, 6.1, 7.3, 7.4, 8.1-8.3, 9.4-9.7, 10.1-10.3, s11 read; not a full proof audit S004 2026-10-13 fresh current version list v1 only and PDF digest unchanged; statements re-inspected. No posted revised hypothesis in fetched text. S005 continuation freshly inspects full Theorem6.1 proof/internal rooted claim; root odd-walk bound is prior source work. S006 current v1 list and PDF digest freshly verified unchanged; relevant proof portions re-inspected.

- **SRC-0003** The stacking number of a tree — **STATEMENT_INSPECTED**. https://arxiv.org/abs/2609.31811 — Exact Lean Stacking/Estimator/RootScore/UpperBound and defect-flow proof notes inspected; no new kernel build in S002

- **SRC-0004** TreeStack Palomar entry — **METADATA_ONLY**. https://palomar-registry.org/entry.html?id=PALOMAR-2026-09-25-000010&version=1 — 

- **SRC-0005** Davenport-Counterexample-Hunt — **STATEMENT_INSPECTED**. https://github.com/jfairfaxball-348/Davenport-Counterexample-Hunt — 

- **SRC-0006** Sjöstrand cover pebbling — **ABSTRACT_INSPECTED**. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v12i1n22 — Sjöstrand 2005 EJC 12(1) N22, DOI 10.37236/1989, publisher abstract inspected

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

- **SRC-0017** S007 selected ancestry credit, sharp triangle-tail clearing and leaf extensions — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/main/research/S007_LEAF_CREDIT_AND_TRIANGLE_TAILS.md — Complete symbolic proofs, prior odd-walk lower credited; universal ASH* OPEN; no novelty or Lean.

- **SRC-0018** S007 full forward/reverse triangle-tail layers and independent constructive trace replay — **PROOF_INSPECTED**. https://github.com/jfairfaxball-348/Almost-Stacked-Proof/tree/main/evidence/S007 — Exact labelled l=0,1,2 only, complete full set hashes/counts, all constructive winning traces independently replayed; no universal certification.

S007 source refresh: SRC-0001/0002 remain current v1 with unchanged PDF digests; selected April6.1 and October4.7/pullback/+3 proofs re-inspected. No public correction or novelty claim.
