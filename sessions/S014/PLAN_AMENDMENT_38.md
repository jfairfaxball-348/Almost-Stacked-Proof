# CAM-S014-38: sound input-stabilizer closure of the CEGIS constraints

2026-10-15 BEFORE execution. CAM37 C6 exclusion is independently DRUP-certified;
C9a/C9b/C10 each hit5000 iterations and remain UNKNOWN. Continue these exact
fixed-input classes using the frozen independently checked necessary clauses,
not a new arbitrary graph sample or promotion of a timeout.

All permutations sigma with c_sigma(v)=c_v form a finite input stabilizer.
For ANY necessary clause C, its edge-variable relabeling sigma(C) is also
necessary: the graph class and ALL-AS-tail predicate are invariant, and the
fixed general input stays identical. This ADDS valid clauses; it does not
restrict models by an unproved graph symmetry quotient. Explicitly enumerate
the group by products of permutations within each equal-count vertex class.
Group sizes C6=8,C9a=480,C9b=216,C10=1440; retain C6 as a proof/checker control.

Separate orbit-continuation folders/code. Import ALL original CAM37 base
clauses with immutable certificate provenance. Generate every distinct
stabilizer image until a cap; store each CNF clause's base-record/permutation
indices. Fresh SAT solver on the expanded CNF. If SAT, continue at most1000
new counterexample-guided iterations, with the SAME sound connectivity,
c-winning-trace and AS-negative-supergraph rules, closing every new base
clause under the same stabilizer. For new c-winning traces greedily minimize
their used edge support, retaining the final literal history; this only
strengthens the valid negative clause. Unknown oracle model halts the case.

Caps PRIOR:500000 distinct clauses/case,1000 new iterations,540s internal plus
600s/2GiB external per producer/checker,300000 legal states/tested graph;
same500000 DRUP lines/200000000 unit clause scans for proof checker. A partial
orbit closure remains sound but is NOT called complete; SAT/cap UNKNOWN.
An UNSAT proof from ANY subset of these necessary clauses can exclude only
the exact fixed-c graph class, after full independent validation. No universal
ASH* result inferred.

Independent validation: replay EVERY imported/new base clause from literal
winning moves or full AS-negative closure using the separate CAM37 checker;
verify each permutation is bijective and fixes c; independently expand EVERY
recorded CNF source pair and compare exact clause bytes/order. Then a FRESH
native proof-logging solve and pure-Python DRUP replay as CAM37. No bare UNSAT.
Any potential counterexample retains complete c-negative/ALL3-AS-layer
positive DAG and triggers separate threshold/cold audit before promotion.

Freeze exact old source digests, cases/groups, new code/plan/runtime metadata,
then derived base-validation/CNF/proof/certificates before checkers. Preserve
all CAM37 UNKNOWN files. At most2 mathematical children with CAM33 on16GiB,
one per campaign/2GiB each. No CLEAR, delegation, closeout, next session,
formalisation, phase/novelty promotion, publication or correspondence.
