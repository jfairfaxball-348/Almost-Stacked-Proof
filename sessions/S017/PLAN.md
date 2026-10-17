# S017 plan - Milestone 1: independent cold re-check of the G9 CLEAR counterexample

2026-10-16. Fresh owner invocation (OWNER_INVOCATION.txt, complete accessible text normalized UTF-8 LF, no transport-byte identity claimed): "run next session". This selects exactly S017 under the owner-revised handoff authoritative/NEXT_SESSION_PROMPT.md (sha256 5416dd68f1b619925ce802b9d2f21c0a62fcee719be6fc1481eef96d68b9b7dc = authoritative/handoffs/S017_OWNER_REVISED_2026-10-16.md), archived byte-identically as AUTHORISED_PROMPT.md. Stop before S018. No Palomar submission/registration, publication, arXiv or author contact.

Entry pin: live origin/main 77001a1315c52bda70fb81ff06aa5ee8270e9b92 (tree 7dad299239664cae5c45575dc06f1c39bf93c964), ordered parents 378652c76f6543f4f30e75e4113550865f2032c6 (S016 merge of PR #20, head 19537a9e26c11a0e2326722f3612c9c5d2da9ae4) and 8dd5a32ff3ec1b936a9d5c5a8744a49cfd0aceb0 (S017 handoff revision, PR #21, merged 2026-10-16T22:36:52Z). Branch session/S017-clear-recheck-and-lean.

## Claims under test (research/S016_CLEAR.md section 5)

On G9 = graph6 HCQTaXi, edges 0-3,0-5,0-6,1-4,1-7,1-8,2-6,2-8,3-5,3-6,4-7,4-8,5-7,6-8, with moves u->v (uv an edge, c_u>=2: c_u-=2, c_v+=1), clearable = some legal sequence reaches total mass exactly 1:
- K1c: c*=(0,0,1,0,0,5,0,8,0) and image (0,0,1,0,0,8,0,5,0) are the only non-clearable configurations of mass 14; neither is AS.
- K2c: every configuration of mass 15 is clearable (and, by C2, every mass >=15).
- K3c: every AS configuration of mass 14 is clearable.
- K4c: per-mass CLEAR losers for masses 2..14 are 36,137,384,932,1863,2887,3280,2510,1301,473,124,21,2 and AS losers 36,137,375,791,1185,1331,1116,734,391,177,60,10,0.
The same tool also re-derives the STACK facts K1-K4 (per-mass STACK losers 36,128,383,930,1862,2887,3280,2510,1301,473,124,21,2), as a by-product, not as the gate.

## M1.1 Definitions and lemmas

Re-derive from research/ASH_SPEC.md and S003 (Lemma 1, Lemma 2 = October Lemma 4.7, Prop. 3, Thm 4 with g=clear): terminal = total mass exactly 1; clear(G) is the least t>=2 with every size-t configuration clearable; bipartite graphs excluded; check C1-C7 and T1-T3 of research/S016_CLEAR.md line by line in sessions/S017/CLEAR_RECHECK.md.

## M1.2 NEW checker (written after this plan is hashed)

tools/s017_g9_dense.lean: a Lean 4 program (core library only, no Mathlib), run with `lean --run` (Lean 4.35.0 on this host). New language for this project, and a new algorithm/data structure: a DENSE FORWARD dynamic programme over the complete state space of all configurations of masses 0..16 on 9 vertices, each mass layer stored as a flat array indexed by the lexicographic combinatorial rank of the composition (stars-and-bars ranking from a binomial table; no hash set, no candidate generation, no backward closure, no DFS). For mass m, win_m[rank c] := goal(c) or OR over legal moves c->d of win_{m-1}[rank d], with goal = (mass = 1) for CLEAR and (exactly one occupied vertex) for STACK. Correctness: every legal move lowers mass by exactly one, so the recursion over mass is exact (C4 for CLEAR, its STACK analogue), with no completeness lemma needed because every configuration is enumerated. Self-checks: rank(enum[j])=j for every j of every layer; layer sizes equal C(m+8,8); graph decoded from the string HCQTaXi by an independent graph6 decoder in the same file and asserted equal to the edge list above; the stated image map (a permutation of the vertices taken from S016_CLEAR) is asserted to be an automorphism.
Outputs (stdout, archived under evidence/S017/m1/): per-mass totals, CLEAR losers and AS CLEAR losers, STACK losers and AS STACK losers for masses 0..16; the complete lists of CLEAR and STACK losers of masses 12..16; verdicts K1c-K4c and K1-K4. The output file is hashed with sha256sum.
Caps: <=8 GiB, <=2 h wall. If `lean --run` is too slow within the cap, the same file is compiled with a lake executable target (no source change); any change of source is a new hashed addendum. A cap is UNKNOWN; UNKNOWN or any discrepancy suspends the CLEAR status (outcome rule).

## M1.3 Replay of S016 CLEAR checkers

Re-hash every file listed in evidence/S016/HASHES.md. Rebuild/re-run, without source edits: tools/s016_g9_clear_reverse.rs (rustc -O) on G9, tools/s016_g9_clear_cert_check.py on the archived S016 certificate, tools/s016_clear_layers.rs and tools/s016_clear_check.mjs on G9 only; compare outputs with the archived S016 outputs byte-for-byte (or by content where line endings differ, recorded). A tool that cannot be re-run unchanged is recorded NOT_REPLAYED with the reason.

## M1.4 Outcome rule (binding)

All agree => CLEAR refutation COLD_RECHECK_PASS (Lean pending). Any discrepancy => suspend, diagnose, record without rewriting S016 bytes; Lean waits.

## Later milestones (each with its own hashed amendment before substantive work)

M2 Lean environment aligned with the current public Palomar registry requirements (read and recorded with URLs/timestamps). M3 formalisation plan (PLAN_AMENDMENT_1, hashed before substantive Lean). M4 formalisation with frozen green modules. Closeout per AGENTS.md with an S018 handoff.
