# S01496: even-pair mass extension fails at the actual zero-imbalance scope

Universal ASH*-STACK and critical no-two remain OPEN. This is a refutation
of one proposed auxiliary extension, not a new printed-ASH counterexample.
The earlier credited P4 printed witness and threshold retain their source
status; no novelty or human/kernel assurance is claimed.

Proposed E0: for every bipartite STACK loser x with signed I(x)=0 and at
least one even positive coordinate, some even-positive site s and some vertex
v make x-2e_s+3e_v lose. If true, it would give a larger-mass loser and rule
all even positive piles out at bipartite criticality. It is FALSE.

Use P4, labels0-1-2-3, x=(9,2,0,1). Its only even-positive site is s1 and
I(x)=9-2-1=6=0 modulo3. It is the label reversal of the already certified
printed witness(1,0,2,9). CAM49 v2 independently regenerates its complete
50-state negative closure and checks the coordinate BFS equality against the
old mirrored certificate. There are exactly FOUR eligible v, all winning:

| v | x-2e1+3ev | Complete consuming history |
|---|---|---|
|0|(12,0,0,1)|0->1 six times,1->2 twice,2->3,3->2,1->2|
|1|(9,3,0,1)|0->1 four times,1->2 three times,2->3,3->2,2->1,1->0|
|2|(9,0,3,1)|2->3,3->2,2->1,0->1 four times,1->0 twice,0->1,1->0|
|3|(9,0,0,4)|3->2 twice,2->1,0->1 four times,1->0 twice,0->1,1->0|

Each history has11 moves, ends in a positive pile2, and consumes its entire
mass13 input. The first ends at2, the other three at0. These are ALL sites,
not just neighbors or a failed choice of donor. The separate literal checker
replays all44 moves. The original CAM49 tuple/list membership implementation
failed before output and is preserved; separately frozen v2 makes only that
representation repair and passes both complete checks.

P4's already audited stack threshold is15, by earlier TreeStack/April7.4
and independent complete tables. x's mass12 is therefore BELOW critical14.
This does not refute a critical odd-heavy/no-two assertion. A proof of one
must use actual largest losing mass, or deliver a different larger loser;
signed zero, an even pile and global choice of receiver alone do not suffice.
Do not infer impossibility from an unsuccessful move search or replace the
universal comparison by the existence of a local extension family.
