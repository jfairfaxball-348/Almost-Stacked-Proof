# CAM-S014-60: direct Q4 universal-counterexample search above exact L_AS30

2026-10-16 BEFORE execution. Fixed Q4 labels0..15, XOR-popcount1 edges.
CAM58 v2/59 fully certify exact L_AS30, positive attaining nodes and ALL
lower-production inequalities; original57 cap and58 checker failure retained.
Only launch if both independent exact-AS checks PASS and hashes match.

Frozen candidate matrix, no adaptive selection: masses31/32/33; at each mass
2048 distinct uniform weak-composition draws with >=2 heavies, >=4 occupied
sites and signed imbalance0, plus1024 two-heavy/binary-buffer draws with
heavy sites0 and one of1/3/7/15, >=2 occupied binary sites, signed0. Seed
14060, canonicalize by XOR with the lowest labeled maximum-pile site; retain
exact draws before execution, deduplicate identical full inputs. Include
ALL signed0 ways to add M-28 binary singletons outside{0,3,5,6}, whose four
counts are7, and33 elementary controls all2, all2 minus/plus one token.
Controls first, structured next, then deterministic interleaved draws. At
most9799 candidates, all full labeled vectors frozen before producer.

Forward consuming STACK DFS with exact AS positive/negative shortcuts ONLY
from the completed59 oracle. Positive AS shortcuts expand105's checked DAG
to literal full-input legal move histories, replayed independently. Negative
AS shortcuts require exact source/buffer/residue conductor after the literal
XOR map, backed by59's complete lower proof. All other negative states check
EVERY true legal successor. Triple-removal positive macros allowed only at
source>=4, with explicit3 true moves restoring the neighbor and reducing
source3. Positive edge order may favor occupied receivers; no heuristic
answer is accepted as loss. Whole original configurations are consumed.

Max2000000 total completed memo states and300000 NEW states/candidate,
producer540seconds/external600seconds/2GiB. Per-query cap marks that query
UNKNOWN and may continue within global cap/time; global cap stops remaining
candidates. Central insertion checks prevent recursion unwinding from
exceeding caps. New uint16 tags distinguish goal65535, ordinary loss65534,
literal AS win65533, exact AS loss65532; ordinary arcs0..255, triple macros
256..271. Literal anchor histories <=100 moves each, stored separately.

Independent tuple checker imports no producer/optimizer, verifies all memo
states, all literal positive histories, all negative AS oracle calls, all
ordinary negative successors, actual frozen candidate/result indices and
every completed yes/no answer. Any actual non-AS loser above30 is STOPPED
for a separately registered fresh cold negative/AS audit; never promote
from an unverified DFS outcome, cap, missing witness or SAT assertion.
Winning samples cannot prove the full general threshold or universal ASH*.

Freeze input graph/candidates, all code/plan, exact AS proof chain, literal
ancestry table and choices before producer; derived outputs frozen before
checker. Independent checker540seconds/600seconds/2GiB, maxTWO math children.
No CLEAR/delegation/Lean/phase/closeout/future session/contact/publication.
