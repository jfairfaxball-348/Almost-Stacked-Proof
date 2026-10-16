# CAM-S014-36: edge-saturate actual holes before AS-tail screening

2026-10-15 BEFORE execution. Use91's exact normal form toward a counterexample
or structural proof. Select completed CAM34 AS_LOSER_FOUND seeds: first12
in lexical graph-id order and first12 in(-input mass,graph-id) order;
deduplicate IDs. Add G0/G1 with c=(3,3,1,1,0,0), both CAM25 critical failure
graphs/exact c, and both CAM30 selected coupled graphs/exact c. Expected30
seeds, at most30. Freeze the actual complete list before any saturation.

For EACH seed take four orders of ALL missing edges: start lexical, shuffle
with random.Random(141036) continuing in seed/restart order. Greedily add
iff c still LOSES by complete legal recursion; skip iff it wins and retain
a literal winning history. Cap makes the case UNKNOWN, never saturated.
One pass suffices by monotonicity. A fresh complete negative closure on the
final graph proves all accepted intermediate subgraphs losing. Positive
histories for final graph+EVERY missing edge prove saturation; independent
checker also replays each actual earlier skip on its exact prefix graph.
Do not infer criticality for an arbitrary seed;91 needs an actual largest
loser for threshold equality.

On each completed saturated graph screen AS masses T,T+1,T+2, T=|c|>n,
source/mask order as CAM34. First AS loser rejects this candidate. All
positive layers flag a potential actual ASH* counterexample for fresh exact
threshold/cold audit. Retain full negative DAGs, positive dependencies,
missing-edge histories, original/final labeled adjacency and every log.

Bounds600seconds/2GiB per producer/checker,300000 memo states per tested
graph including final graph's shared AS screen; at most120 saturation cases.
Separate stages/preflights: freeze seeds/orders/code/plan BEFORE producer,
derived final graph/tail inputs and certificates BEFORE independent checker.
Independent coordinate DAG checker plus separate edge-order/history validator,
no producer imports. At most2 mathematical children concurrently with CAM33,
4GiB combined ceiling on16GiB host. No CLEAR, delegation, closeout, future
session, later-gate or correspondence action. No universal claim from a sample.
