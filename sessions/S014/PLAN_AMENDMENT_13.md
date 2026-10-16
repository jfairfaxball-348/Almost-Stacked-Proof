# CAM-S014-13: first-firing necessity and the six CLEAR boundaries

2026-10-15, BEFORE computation. Test81's necessary path cover against ALL
reachable auxiliary boundary states, and complete the six CAM12 CLEAR cases
that reached their STACK cutoff. No silent cutoff expansion or oldfile writes.

Boundary graphs: P3,K3,2K2,K1,3,C4,K4,P5,C5,K1,4,K5, with explicitly frozen
labeled edges. EVERY initial0/1 subset U, arrivals I<=3, every legal internal
2u->v move, arbitrary external+1 arrivals, arbitrary external-2 exits. Every
reachable (configuration,I,O) cell, no histories sampled, n<=5, mass<=|U|+3.
Producer breadth-first state exploration retains one history per cell and
all terminal empty/single-pile cells. Checker independently enumerates the
whole finite coordinate box by I ascending and mass descending, using ALL
possible predecessors, and compares the complete state sets. Independently
checks theta via every acyclic degree<=2 edge subset. For each terminal
history record first incoming parents/firing counts and extract a TRUE path
cover with the proved bound. Untouched initial singleton terminal is excluded
only from the strict root conclusion; it stays in the complete reachable set.
300000 cells per initial subset,600s/2GiB per process; any cap UNKNOWN.

Six CLEAR cases exactly as CAM12 summary's incomplete list: F2_1 with A1B1,
A1B2,A2B2; F3_7 with A1B1,A1B2,A2B2. New full losing-layer certificates in a
new directory through C=max(S,3a+7), not modification of old certificates.
Reuse unchanged independent packed/tuple algorithms with equality expectation
now explicitly tested at C. Keep all masses/AS/root completeness and prior
resource caps. Compare each earlier full losing layer byte-for-byte in decoded
coordinates, and record both the prior incomplete status and new exact status.

Additionally check theorem82's explicit W-maximizing AS STACK witnesses in
every CAM12 full critical losing set, and its pure-leaf AS CLEAR witness in
the six new critical sets. No extrapolation from finite agreement;82 remains
dependent on its written all-parameter proof and hostile case audit.
Freeze plan/input/code/import/runtime hashes before execution. No session
closeout, novelty priority, later phase or universal headline promotion.
