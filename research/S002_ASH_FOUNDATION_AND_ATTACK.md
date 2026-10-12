# S002 — ASH foundations and first universal attack (2026-10-12)

## Verdict and evidence boundary

**Universal ASH: UNRESOLVED.** Neither an unconditional proof nor a fully certified counterexample was found. The exact original April 2026 Hypothesis 9.1 was inspected directly. The October 2026 23-page paper (arXiv:2610.09650, 2026-10-07/08) remains **ABSTRACT_INSPECTED**, because direct PDF/HTML and several alternative retrieval attempts failed. Its exact internal numbered theorem and revised estimator cannot be asserted. The computations below test the fully source-verified **April** definition; they are not claimed as a source-gated certification of the unread October manuscript.

## Independently checked primary mathematics

Csernák–Soukup, arXiv:2604.22341v1 (submitted 2026-04-24, PDF dated April 27), PDF p.3: pebbling move c(u)≥2, c(u)−2, c(v)+1, changes total by −1; stacked means support singleton; cleared means mass exactly 1. Both invariants are **least exact** t≥2, not at-least thresholds. PDF p.20, **Hypothesis 9.1**: for each finite connected graph the least t≥2 for which every almost-stacked c of exact mass t is stackable equals stack(G); for each such **non-bipartite** graph, the analogous equality is clear(G). Almost stacked means ∃v0 ∀u≠v0: c(u)≤1. For |V|=1, stacking threshold is 2, not 1; clearing does not enter because K1 is bipartite. No empty vertex-set case is asserted. PDF pp.21–26 Theorems 9.4–9.7 establish almost-stacked even-cycle stacking and odd-cycle clearing, and only *conditionally* turn them into unrestricted equalities. Theorem 2.10 supplies finiteness for connected stack and connected non-bipartite clear. The October 2026 abstract independently reports the same broad ASH description and those conditional cycle implications; literal October theorem wording was NOT read.

## Exact reachability certificate theorem (elementary, checked separately)

For a finite undirected graph G, let Conf_m denote all nonnegative labeled configurations of exact mass m. Every legal move decreases mass by exactly one, so the reachability graph is a **finite acyclic directed graph graded by mass**. Let W^S_m be the set of configurations with some legal-move descendant of singleton support, and W^C_m the analogous set whose descendant has mass exactly one. Then for every m≥2,

- W^S_m equals the singleton-support configurations of mass m, together with every configuration having **one legal successor in W^S_(m−1)**.
- W^C_m equals every configuration having **one legal successor in W^C_(m−1)**, with W^C_1=Conf_1.

**Proof.** If a terminal is already a goal, the assertion holds (singleton support is a stack goal, and at mass m≥2 no clearing goal exists). Otherwise any witnessing finite move path has a first legal move into mass m−1, followed by a winning suffix. Conversely prefix that first legal move to the inductively certified winning suffix. The strict decrease proves termination and completeness of both backward sets. The forward recursive code implements the same recursion independently of the reverse-predecessor cold checker. The separate BFS enumerates actual reachable descendants without invoking either recursion.

**Least-threshold discipline:** Since `stack(G)` and `clear(G)` are defined by the **least exact t≥2**, simply compare every exact layer 2,...,T, without assuming a false pointwise monotonicity under adding pebbles to a winning configuration. A fixed winning configuration need not stay stackable or clearable after arbitrary extra pebbles when the terminal vertex is unspecified. Thus the finite thresholds below are proven as least t in the *fully enumerated* search interval; their equality to source thresholds is justified because their first successful layer is found. This is a general exact decision procedure for bounded configurations, **not** a global ASH proof.

## TreeStack reconciliation (not a new ASH theorem)

April source PDF p.26 defines
sigma_T(r)=1+sum_{v=r OR deg_T(v)>1} deg_T(v) 2^{dist(r,v)};
leaf_T(r)=number of degree-one vertices other than r;
estim(T)=max_r[sigma_T(r)+leaf_T(r)].
This matches exactly the inspected Lean definitions `TreeStack/Estimator.lean` (sigmaVertices, sigma, leafVertices, rootEstimate, estim), including the degree-one root. `TreeStack/Stacking.lean` defines least exact t≥2 and proves
`stack_eq_estim_of_two_le_card : 2 ≤ Fintype.card V → stack T = estim T`.
`RootScore.lean`, `UpperBound.lean` and `notes/defect-flow.md` use disjoint incident branches, exact rooted scores and a connected-partition weighted defect bound. ArXiv:2609.31811v1 was submitted 2026-09-25; project reports Palomar-2026-09-25-000010 v1. The October authors' abstract lists tree equality as conditional on ASH and the unconditional form as a conjecture; the earlier TreeStack record addresses that tree consequence independently, not universal ASH. No inference about awareness, plagiarism or formal peer-review status. October equation-by-equation comparison remains BLOCKED by PDF access.

## Mathematical attacks / failures

**Route A — mass-preserving pile compression.** The proposed universal claim that arbitrary redistribution/merging of heavy piles preserves nonstackability is FALSE, even on P4: on vertices 0–1–2–3, c=(2,0,0,2) is nonstackable. Either legal first move sends an endpoint's pair inward; after both possible moves the terminal state is (0,1,1,0), not stacked, and no other moves are possible. The same mass rearranged to (4,0,0,0) is already stacked. This invalidates arbitrary merging as a monotone operation, but **does not refute existential ASH reduction**, since a different almost-stacked losing witness might exist.

**Route B — TreeStack cyclic extension.** Disjoint incident branches are key to `incidentBranch_vertices_disjoint` and independent root-task execution; a cycle has two r-neighbours connected after removing r, so their branch interiors overlap. Applying a spanning tree's rooted scores to the full graph can fail even qualitatively: c=(2,0,0,2) is losing for P4 but winning when adding edge 0–3 (C4), via the move 0→3. A graph-wide cyclic correction or new dual certificate is needed.

**Route C — exact bounded counterexample hunt, CAM-S002-01.** The local preregistration file was fixed before execution (SHA-256 `a1403026ddc36fed628ac4e7ef6ce633c7d4dfbd240d87315e17509a2da115fd`), specifying six labeled connected simple eight-vertex graphs, every weak composition at each exact mass 2..14, without isomorphism reduction. Forward reachability uses exact recursion on a DAG because every move loses one pebble, with stackable terminal a singleton support and clearable terminal total 1. Exhaustive labeled inputs: **1,918,566** (=6·319,761). All six cases showed **no ASH threshold gap in the tested range**. Distinct queue-based forward BFS checked 420 deterministic states with zero disagreements. Independent **inverse-move predecessor dynamic programming** cold-checked all 13 exact-size layers (2..14) for W8 and K4-bridge-K4 and exactly reproduced the forward counts, not just sampled states.

| 8-vertex graph | Stack AS threshold | Unrestricted stack threshold | Clear AS threshold | Unrestricted clear threshold | Scope |
|---|---:|---:|---:|---:|---|
| W8 (hub + 7-cycle) | 11 | 11 | 11 | 11 | exact least t≥2 in tested 2..14 |
| K4—bridge—K4 | 13 | 13 | 13 | 13 | exact least t≥2 in tested 2..14 |
| C8 + chord 0–4 | >14 | >14 | n/a | n/a | graph is bipartite; clearing excluded |
| C8 + chords 0–2, 4–6 | >14 | >14 | >14 | >14 | cutoff only |
| K2,6 | >14 | >14 | n/a | n/a | bipartite; known source formula gives stack=19 |
| two triangles, bridge, two leaves | >14 | >14 | >14 | >14 | cutoff only |

On W8 at mass 10, AS and unrestricted each have 14/28 nonstackable and 14/28 nonclearable respectively; at mass 11 all 31,824 configurations pass both goals. On K4—bridge—K4 at mass 12, exactly 12/26 AS/general configurations lose for each goal; at mass 13 all 77,520 configurations pass both. These are machine-computed **finite exact results**, not a new universal theorem, nor full verification of the October manuscript. The 8-vertex family is beyond the authors' reported n≤7 baseline but no priority is asserted.

Computational reproducibility: Python 3.13.5 standard library, Linux x86_64; executed `python cam_s002_01.py --max-total 14 > cam_s002_01_output.txt 2>&1` then `python reverse_cold_check.py --input cam_s002_01_output.txt --max-total 14`. The original execution bundle, including preregistration, raw logs and both scripts, accompanies the session in chat as `S002_research_evidence.zip`. GitHub contains the full algorithms with instructions. Checksums of executed files: `cam_s002_01.py e91125db00bf5f816cc8505b69bb4ae1b262d929014e7649d8426499dfda8aa4`; `reverse_cold_check.py ee855ed3832be40b4ab826ce223691605e826d2f384c44b57821a79b6a89393e`; `cam_s002_01_output.txt a437a59259b0a3b28f883cd92405ee7d270823d95f5c59a0fc60815566017515`; `reverse_cold_check_output.txt 7f69aa07c2a837d56e1c558668ac3fd8aa0353dc0890b9c417b2b7de69cd4e1d`. Graphs are labeled 0..7; exact adjacency generated by the code. No unlabeled atlas completeness claimed.

## Frontier/source audit (bounded, NOT stage 2 novelty)

Sjöstrand, *The Cover Pebbling Theorem* (EJC 12(1), N22, 2005, DOI 10.37236/1989) settles a positive-demand **cover** objective by starting from stacked obstructions; it does not prove ASH for existential stacking/clearing terminal targets. The April 2026 foundational source identifies the 7-vertex atlas result as computational, reports the cycle theorem as conditional, and distinguishes the rooted tree conjecture. Targeted 2026-10-12 queries for 2610.09650, ASH counterexamples, and the TreeStack publication found no independently verified universal solution, but negative search is not a novelty audit. Source and claim catalogue statuses stay bounded by actual evidence.

## Decisions and remaining obstacle

1. **Universal stack ASH: unresolved. Universal clear ASH: unresolved.** No counterexample certificate or Lean theorem.
2. Certain graph families (complete and complete multipartite, paths/trees) have separate source-proved or TreeStack-proved exact stacking formulae; the tested W8 and bridge-of-K4s have newly independently cross-checked finite results. None establishes universal ASH.
3. Critical mathematical obstacle: find a mass-preserving *loss-witness* replacement whose one heavy pile does not accidentally become winning, or a dual characterization of nonstackability/clearability that remains necessary and sufficient in cyclic graphs. Tree-only disjoint branch methods fail at overlap.
4. Critical provenance obstacle: direct inspection of October 2026 PDF remains necessary before claiming its precise current theorem has been independently transcribed. S003 must reopen this gate, then aggressively pursue unrestricted proof/counterexample and broader exact search. No Phase 2, Lean, Palomar or arXiv action.

## S003 errata (appended 2026-10-12; original text above left unchanged)

1. **C8 + chord 0–4 is NOT bipartite.** The chord closes the 5-cycle 0-1-2-3-4-0, so the "n/a / graph is bipartite" entries in the clear columns of the table above are wrong. The S002 code computed both goals for every graph without a bipartiteness filter; the clearing counts were >14 at the cutoff. S003 computed exact values with three independent solvers: **stack = clear = 23** for this graph, with no AS-gap. See FL-0013.
2. The "no ASH threshold gap" statements above test the printed hypothesis on layers t≤14 only. In S003 the printed (literal) hypothesis was shown false on smaller graphs, e.g. P4 at t=12, and the substantive open target became the critical form ASH\*. See `research/S003_AS_GAP_AND_ATTACKS.md`.
3. Exact thresholds for the S002 graphs that were left ">14": C8+{0,2},{4,6}: stack=clear=19; K2,6: stack=19 (April Thm 8.2 formula); C8+{0,4}: 23/23. The triangular ladder with leaves exceeds the S003 cap (t≤40), so it is a cutoff only.
