# ACTIVE S01491: critical-loser-preserving edge saturation

Universal STACK/CLEAR remain OPEN. STACK only; source graph monotonicity and
exact threshold conventions retain credit.

**Proposition91.** Let c be a globally largest STACK loser on finite connected
simple G,n>=2, M=|c|. If H adds edges on the SAME vertices and c still loses
on H, then stack(H)=stack(G)=M+1. If G is an ASH* counterexample, so is H.
One may further choose H where adding ANY missing edge makes this very c win.

Proof. Every G winning history remains legal on H, so stack(H)<=stack(G).
The mass-M loser c gives stack(H)>M. As stack(G)=M+1, equality follows.
If all AS mass-M inputs win on G, they still win on H while c loses, hence
the critical ASH* failure persists. Finitely many edges can be added while
preserving c's loss. At the end, any missing edge wins c. A one-pass greedy
order suffices: a successful history for an earlier skipped edge stays legal
after every later edge addition. QED.

For an arbitrary-layer loser c, only stack(H)>=|c|+1 follows; equality with
stack(G) is NOT asserted. No contraction, deletion or quotient is used.

A hypothetical counterexample may thus be edge-saturated while preserving its
critical loser. Adding edges can change which configurations minimize heavy
count: do NOT assert that old c remains selected after saturation. Reselect
a minimum-heavy critical loser on H using the preserved absence of AS critical
losers, then saturate that c if needed. Continue only when an edge can actually
be added. At most n(n-1)/2 additions occur, so this finite process ends with
a compatible pair(H,c): c is minimum-heavy critical, Q/P residual as in89,
and every missing edge makes c win. Every fewer-heavy same-mass input wins.
No contradiction among these constraints has yet been proved.

The computational follow-through greedily saturates known hole inputs, keeps
full negative closures and a positive history for every missing-edge addition,
then uses90's AS-tail screen. An AS loser at the same or higher mass rejects
the candidate; complete positive three-layer coverage triggers definitive
counterexample audits. All generation/adaptive selection is preregistered.
