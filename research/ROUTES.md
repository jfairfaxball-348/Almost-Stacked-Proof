# Proof-first / counterexample-first exploration routes (all PROPOSED)

The **headline** is universal ASH. No route has been proved viable in S001.

| Route | Candidate | First falsifiable gate | Danger |
|---|---|---|---|
| R-A | Generalize TreeStack rooted transfer/defect certificates to graphs using rooted spanning trees or cycle corrections | Derive a sound graph-wide invariant that handles cycles and changing roots | A tree-only monotonicity/cancellation step may fail on cycles |
| R-B | Minimal-counterexample structural reduction: select a worst configuration and compress all >1 piles into one | Rigorous potential/uncrossing argument preserving nonreachability at fixed size | Such compression may consume a pebble and change outcome |
| R-C | Graph decomposition / block-cut tree, ear or cycle induction | Establish ASH under graph sums or small cycle extensions | Stacking and clearing behave differently across blocks |
| R-D | Dual certificates / integer potentials for unreachable terminal sets | Necessity and sufficiency of a computable invariant in one nontrivial cyclic family | Weighted invariant may be sufficient only |
| R-E | Exact finite counterexample hunt on connected small cyclic non-bipartite and bipartite graphs | Independent complete state reachability and symmetry-quotient check | Incomplete state exploration gives false negatives |
| R-F | Split stack vs clear formulations; demonstrate one follows the other or isolate potential failure | Proved logical reduction or explicit separating example | Two source quantifiers may differ |

R-A through R-F can be reprioritized after transcribing the primary 2026 statement and checking source atlas reports. Mathematically ambitious work is welcome inside a numbered session: do not spend sessions on local lemmas merely to satisfy process. Before any heavy computation register a bounded CAM plan with a precise certificate and independent validator.

## 2026-10-13 reprioritisation (preparatory, NOT an executed mathematics session)

The exact open headline is **universal ASH\***, not the disproved printed form. Tamás Csernák confirms that his intended conjecture concerns almost-stacked configurations in the **largest bad layer**; his algorithm builds losing configurations upward by considering every legal successor (SRC-0010). The leading route is now **R-G: bad-layer predecessor/shadow structure**. Define `B_t` (all goal-losing exact size-t configurations), and for t>=2 use the precise recurrence `c ∈ B_t iff c is not a goal and M(c)⊆B_(t−1)`. Prove an **existential** AS member of `B_(g(G)-1)` or construct a threshold-complete counterexample; no unproved monotonicity or compression shortcut. See `research/ASHSTAR_ATTACK_BRIEF.md`.

Keep R-A/R-C/R-D/R-E as competing strategies. **R-B's naive within-critical-layer compression is false (FL-0015), not a live lemma.** Stage-1 printed-form audit remains a separate S004 obligation. Do not mark a route proved, selected by theorem, or experimentally passed based on this correspondence alone.

## S004 outcomes

R-G complete sparse recurrence produces certifiable thresholds but does not force an AS last-layer witness. R-A weighted budget succeeds for every independent set, settling bound-saturation/complete multipartite classes; arbitrary non-bipartite mod3 invariant impossible. R-B minimum support/local convexity fails on P3; global square extrema survive finite checks and remain HEURISTIC. R-C block list alone fails, rooted interface theorem still open. R-D exact ancestry grammar proved, extremal-hole theorem missing. R-F stack/clear pointwise equivalent at mass>=4 on edge-triangulated graphs (credited source argument). R-E completes n7 coverage and selected larger thresholds; two explicit cutoff cases, no counterexample. Universal headline OPEN. S005 handoff prioritizes graphs above both independence and singleton bounds.

## S005 outcomes
R-A/R-D: exact pure-pile clearing classification via rooted odd-walk height and ancestry, with prior lower bound credited; no general threshold upper. R-C signed leaf normalization needs deferred legal debt. The stronger two-site geodesic stack witness is refuted on triangle-tail n5. R-D/C acyclic balance schedules legally but K3 pure6 proves exact clearing may require cycles. Support/residue +3 lower sets give an exact extremal-hole formulation; general lower-set axis arguments fail abstractly. R-B global Q and lexicographic pile extrema survive the complete finite sample, no proof. R-E exact C10 and five-tail clearing frontiers completed; larger explicit cutoffs retained. S006 targets universal cross-class hole selection and genuine rooted interfaces.
