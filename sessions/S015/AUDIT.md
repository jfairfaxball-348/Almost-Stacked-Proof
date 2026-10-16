# S015 audit - adversarial self-review of the G9 counterexample and the atlases

This is a same-programme adversarial review, not an independent human or kernel audit.

## Could G9 be an artefact of definitions?

- Move: two pebbles off u, one onto a TRUE neighbour v. All tools generate moves only along the 14 listed edges in both directions; the certificate verifier rebuilds adjacency from the edge list as unordered pairs and rejects any other move.
- Stackable: some reachable configuration has exactly one occupied vertex. Mass never reaches 0 (a move needs two pebbles and leaves one). Every tool and certificate uses "at most one occupied vertex" as the win condition, which for positive mass equals "exactly one".
- AS: at most one vertex holds more than one pebble (ASH_SPEC; the authors' code `is_almost_stacked` uses the same predicate). AS coverage at masses 14-16 was enumerated independently by (pile vertex, 0/1 vector on the rest).
- Threshold: stack(G) = least t>=2 with every size-t configuration stackable (ASH_SPEC, October definition). For t<=9 the all-ones-type 0/1 configurations of size t lose; masses 10..14 have losers (brute force), mass 15 has none. Monotonicity above n (elementary: mass > n forces a legal move from a non-single-pile configuration) gives all masses >=15 stackable. Hence stack(G9)=15 under both the exact-layer and the at-least conventions, and S003 Thm 4's equivalence applies: ASH* needs an AS loser of size 14; there is none.
- Intended form: the authors confirmed (SRC-0010) that ASH* concerns the largest bad configurations; their own public code computes exactly the critical witness set and tests for an AS member. That code returns False on G9.

## Could it be a bug?

Seven computational routes agree: C++ hash-set recursion (v1/v2/v3/v4 lineage), separately written C sorted-array recursion (v1/v2/v3), the Python layer validator, the bare-definition brute force (no candidate lemma), explicit certificates with a separate replay verifier, the full mass-15 certificate (490,314 replays), and the authors' counter-based code. Graph identity is confirmed by nauty decoding and canonical labelling. The non-stackability of c* also has a human proof (research/S015_G9_COUNTEREXAMPLE.md section 5) depending only on S014-111/112/113, which were re-derived in S015.

Residual risks recorded: (a) the human proof is long case analysis and has not been read by an independent person; (b) all routes ran in one container session; (c) no Lean proof. These are exactly the pending gates.

## Atlases

Order <=8: complete, dual compiled with byte-identical critical layers; orders <=7 also Python set-validated; order 8 Python only on a 31-graph prefix (policy stop). Agreement with every frozen S003 threshold (no mismatches). Order 9: see evidence/S015/cam85/summary.json for the exact dual-verified count and any UNKNOWN graphs (trees possibly capped; trees satisfy ASH* by earlier credited TreeStack + S003 Thm 8).

## Scope discipline

No extrapolation: the infinite bridge family is a conjecture; bipartite critical ASH*-STACK remains open; CLEAR untouched. No novelty/priority claim (Phase 2 not started). Plans/amendments were hashed before each execution; deviations (aborted pilot, stopped runs, crash, restructure, naming corrections) are recorded in addenda rather than by editing hashed plans.
