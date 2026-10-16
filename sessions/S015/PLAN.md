# S015 plan - sustained attack on the universal STACK bridge

2026-10-16. Fresh owner invocation (OWNER_INVOCATION.txt): "Run a sustained attack on the next session, aim to resolve a major obligation or proof". This selects exactly S015 per authoritative/NEXT_SESSION_PROMPT.md. No S016, delegation of research judgement, Lean, registration, publication or contact.

Entry pin: live origin/main 4200dc84be0bfd54e8573e7aa02dacea7ff8513c, tree 4f83e4b58baf55cc300aa6094d8c43b8ce556b2d, ordered parents 8ea5db207a91ca917c3b94bc98b54ac65406e7a5 (S013 merge) then cafa2f9a9e69d6f271583ee76a2f5fbe9a3840c4 (S014 CI repair, child of S014 research commit 44a89726). Session branch: ccr-a9fdff28-6mqxx0 (harness-designated; recorded instead of a session/S015-* name).

Environment change: S015 runs in a Linux cloud container (4 cores, 15 GiB, no swap), not the Windows host of S003-S014. Windows-specific memory/CaDiCaL notes do not apply; each child process still gets an explicit wall/memory cap.

## Target

Binding target unchanged: for every finite connected simple G with n>=2, L_all^STACK(G) <= L_AS^STACK(G) (critical ASH*-STACK). CLEAR deferred.

## M1 - CAM-S015-82: complete order-8 STACK atlas (counterexample hunt / exhaustive finite verification)

The complete independently verified critical-ASH* atlas currently ends at order 7 (853 STACK graphs, S003+S004). No complete order-8 computation exists; S014 SAT campaigns excluded only all non-AS order-8 patterns of masses 10, 11 and selected heavy patterns. CAM82 asks, for EVERY connected graph of order 8 (11117 isomorphism classes) and, as a control, every order 2..7 connected graph: exact L_all, exact L_AS, and whether L_all=L_AS.

Graph generation: nauty-geng 2.8.8 (`nauty-geng -c N`) graph6, decoded by tools/s015_graphs.py. Independent cross-check of the isomorphism-class set against the repository's own S003 generator (tools/cam_s003_graphs.py, count asserted against OEIS A001349) by its canonical form, for N<=8. Symmetry: one representative per isomorphism class is sound because L_all, L_AS are isomorphism invariants; within a graph NO symmetry reduction (all labelled inputs).

Method (both checkers): exact loser-layer recursion. L_1 empty. For m>=2, c of mass m loses iff it has >=2 occupied sites and EVERY legal successor is in L_{m-1}. Candidate completeness lemma: a loser without legal move is a 0/1 vector; a loser with a move u->v has a losing successor s with c=s+2e_u-e_v. Termination lemma: if L_m is empty and m>=n then all L_{m'}, m'>m, are empty. L_all = last nonempty layer; L_AS = largest mass carrying an AS loser.

Producer: tools/s015_layers.cpp (sha256 cf49874dfd9cfbc6bee00971479554a0493f31fd07db07e1295499217e767e61), g++ 13.3.0 -O2, hash-set of packed 16-bit coordinates. Independent validator: tools/s015_validate.py (sha256 3d91e4f6d538ac44adba96e8d9d5e703c283cab7a036712c7cbfa3bb8b107285), Python 3.13, tuple frozensets, separately written candidate generation, plus an explicit closed forward reachable-set re-proof of every critical non-AS loser and one AS critical witness per graph. Graph decoder tools/s015_graphs.py (sha256 5c45d90d3310559262e3e19c136022d2d9938150e71bb3da0128b341657e163d).

Controls before the order-8 run: P4 must give L_all=14 (stack 15) and the order-7 run must reproduce the frozen S003/S004 statement that all 853 order-7 graphs satisfy L_all=L_AS; order<=7 per-graph thresholds are compared against frozen S003 evidence where machine-readable.

Caps: producer state cap 30,000,000 losers per layer per graph; each child process <=4 GiB address space and 3600 s wall per batch of graphs; at most 3 concurrent children. A capped graph is UNKNOWN, never ASH_OK. Validator: same per-graph semantics; graphs whose largest producer layer exceeds 2,000,000 states may be validated only by the compiled producer plus forward re-proofs, and are then reported separately as SINGLE_IMPLEMENTATION (not dual-verified). Trees are included (earlier TreeStack already covers trees; their inclusion here is a control, not a new result).

Completeness scope: exactly the geng order-8 connected list (and controls). Outcome classes: ASH_OK (dual verified), ASH_FAIL (candidate counterexample: requires full dual verification, explicit labelled adjacency, critical loser, closed forward reachable sets, and every AS input of mass L_all and above checked; later Lean and cold re-check separately gated), UNKNOWN (cap). No extrapolation beyond order 8.

Artefacts: evidence/S015/cam82/{graphs,producer,validator}_N.txt plus summary JSON and SHA256 manifest.

## M2 - symbolic attack

Use the per-graph critical-layer data to guide symbolic work on the residual comparison: (i) which critical losers are non-AS, and which structure they share; (ii) attempt a proof of a mass-preserving AS-witness construction for the observed non-AS critical families, stated with full quantifiers; (iii) if M1 finds an order-8 ASH_FAIL, switch entirely to certification of that counterexample. Every new lemma records assumptions, proof, dependencies and hostile challenge. Any further computation needs a prior hashed amendment.

## M3 - closeout

Per AGENTS.md: one atomic authored session commit, ordinary PR, non-force merge if permitted, ledgers/state/catalogue synchronisation, complete FUTURE S016 handoff. Phase 1 stays IN_PROGRESS unless the universal gate genuinely passes.
