# CAM-S014-37: certified constraint search over whole fixed-input graph classes

2026-10-15 BEFORE execution. Directly search for c losing and L_AS<|c| with
90's complete three-layer AS tail. ALL connected simple labeled graphs on
the selected vertices are permitted; no fixed seed edges, symmetry quotient,
heuristic exclusion, degree constraint beyond necessary connectedness.

Four fixed cases, in order:
C6: c=(3,3,1,1,0,0),n6,T8 (known negative control for ASH* failure).
C9a: c=(3,3,1,1,0,0,1,1,1),n9,T11.
C9b: c=(3,3,3,1,1,1,0,0,0),n9,T12.
C10: c=(1,0,0,0,0,0,7,7,1,1),n10,T17.
Each has T>n. Boolean variables are ALL unordered vertex pairs in lex order.

Counterexample-guided CNF with ONLY necessary clauses:
- Connectedness cuts: at least one edge across a proper nonempty subset.
  Begin with singleton cuts; add a cut for any disconnected proposed model.
- If c WINS on a proposed graph, retain its literal winning history with
  used edge set P and add the negative clause omitting at least one edge of P.
- If c LOSES, screen ALL AS inputs of masses T,T+1,T+2 in fixed source/mask
  order. At first AS loser d, greedily enlarge its graph while d still loses,
  then save its complete negative closure on the enlarged graph H. Add the
  positive clause requiring some edge outside H: any subgraph of H also
  loses d and cannot be an AS-tail-winning counterexample. A partially
  saturated H remains valid; do not claim maximality if a trial cap interrupts.
- If c loses and every AS tail input wins, flag potential actual counterexample
  with full negative/positive DAG certificates and exhaustive tail coverage;
  stop for fresh threshold/general/AS cold audit before promotion.

All clauses are necessary for a graph in this fixed-input counterexample
class. UNSAT means nothing mathematically unless independently certified.
If the incremental solver reports UNSAT, freeze exact CNF, run a FRESH proof-
logging Glucose3 instance on that CNF, and save its DRUP proof. Independent
checker A rederives every clause from its connectivity cut, literal c history,
or complete AS-negative closure. Checker B verifies every proof addition by
reverse unit propagation and every deletion against the frozen CNF, ending
in the empty clause. Unsupported/non-RUP proof or cap UNKNOWN. A valid proof
excludes ONLY that exact fixed-c labeled graph class, not universal ASH*.

Runtime: isolated temporary python-sat1.9.dev16/six1.17.0 installation, actual
native binary/wrapper digests recorded (not mirrored vendor artifacts).
Official PySAT solver API inspected; no bare solver-status promotion.
Maximum5000 iterations/case, internal wall540s plus external600s/2GiB per
producer/checker,300000 legal-recursion states per tested input/graph,
500000 DRUP lines and200000000 unit-propagation clause scans per proof.
One mathematical child in this campaign; at most2 including existing CAM33.
Persist each constraint/certificate before next solve, save UNKNOWN on bounds.
All code/input/plan/environment/output/log hashes. Any unknown oracle model
halts the case; never block an unverified model. No CLEAR, delegation, session
closeout, next invocation, Lean, phase/novelty promotion or external contact.
