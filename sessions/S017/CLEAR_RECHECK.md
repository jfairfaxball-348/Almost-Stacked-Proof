# S017 Milestone 1 - independent cold re-check of the G9 CLEAR counterexample

Outcome: **COLD_RECHECK_PASS** (all checks agree; LEAN_PENDING at the time of this record). Plan: sessions/S017/PLAN.md (sha256 in PLAN.sha256), addenda 0-i, 0-ii.

## 1. Definitions re-derived (research/ASH_SPEC.md; S003 Lemma 1, Lemma 2 = October Lemma 4.7, Prop. 3, Thm 4 with g=clear)

G finite simple connected non-bipartite (so n>=3). A move u=>v along an edge needs c(u)>=2 and does c(u)-=2, c(v)+=1, so it lowers the total by exactly one. c is clearable iff some legal sequence (possibly empty) reaches total mass exactly 1. clear(G) = least t>=2 with every configuration of size exactly t clearable. AS: some v0 with c(u)<=1 for all u != v0 (equivalently at most one entry >=2). Critical ASH*-CLEAR(G): clear(G) equals the least t0>=2 such that every AS configuration of every size >=t0 is clearable. Bipartite graphs are excluded by the source; STACK and CLEAR are separate clauses.

## 2. Line-by-line check of research/S016_CLEAR.md

- C1. A 0/1 vector with t ones (2<=t<=n) has no legal move and mass t != 1, so it is not clearable, and it is AS (every entry <=1). Correct. Consequence L_AS>=n, clear>=n+1: correct.
- C2. If t>n and every size-t configuration clears, a configuration of size t+1>n has (pigeonhole) a vertex with >=2 pebbles; G connected with n>=2 gives it a neighbour, and one move reaches size t, which clears. Induction gives every larger size. Correct (needs only: no isolated vertex).
- C3. For 2<=t<clear(G), Lose(t) is nonempty by the definition of clear as a LEAST element; for t>=clear(G)>n (C1) emptiness propagates by C2. So L_all = clear-1. AS losers are losers, hence L_AS<=L_all, and the AS threshold of the critical form is L_AS+1 (L_AS>=n>=3, so this is >=2). Hence ASH*-CLEAR iff L_AS=L_all iff Lose(L_all) contains an AS configuration. Correct.
- C4. Mass 1 is cleared by the empty sequence. For t>=2 the empty sequence does not clear, so c clears iff some legal successor clears. Correct.
- C5. If c in Lose(t) has a legal move u=>v to s, then s in Lose(t-1) (C4) and c = s+2e_u-e_v with s_v = c_v+1 >= 1. Otherwise c has no legal move, so it is a 0/1 vector. Correct.
- C6. First empty layer t0>n by C1; C2 gives all later layers empty. Correct.
- C7. Correct as a remark; not used.
- T1. Mass exactly 1 means one vertex with one pebble, a stacked configuration; so clearable implies stackable and Lose_STACK(t) is contained in Lose_CLEAR(t). Correct.
- T2. k e_r with k>=4: r=>s twice gives (k-4)e_r+2e_s, then s=>r gives (k-3)e_r; k=2: one move gives e_s; k=1 is cleared. Correct.
- T3. With L=L_all^STACK: Lose_CLEAR(L) contains the nonempty Lose_STACK(L); Lose_CLEAR(L+1) empty and L+1>n give (C2) all larger layers empty, so L_all^CLEAR=L; no AS loser of mass L and none above gives L_AS^CLEAR<L. Correct.

No gap found. K1c's non-clearability rests on T1 plus the STACK K1 proof (cold-checked in S016 Gate 1) and is independently re-derived computationally below.

## 3. New checker (tools/s017_g9_dense.lean, sha256 37f8f195...930b)

Lean 4.35.0 program, core library only, run with `lean --run` (5 min 30 s wall). Dense forward dynamic programme over every configuration of masses 0..16 (2,042,975 configurations), each layer a flat array indexed by the lexicographic stars-and-bars rank, with the self-check rank(enum[j]) = j on every entry and layer sizes C(m+8,8). Graph decoded from `HCQTaXi` by its own graph6 decoder, equal as an edge set to the stated list; the map 0<->1, 3<->4, 5<->7, 6<->8 checked to be an automorphism. Output evidence/S017/m1/dense_output.txt (sha256 211574b6...b056).

Result: per-mass CLEAR losers (masses 2..16) 36,137,384,932,1863,2887,3280,2510,1301,473,124,21,2,0,0 and AS CLEAR losers 36,137,375,791,1185,1331,1116,734,391,177,60,10,0,0,0; mass-14 CLEAR losers exactly (0,0,1,0,0,5,0,8,0) and (0,0,1,0,0,8,0,5,0), both non-AS; 2304 AS configurations of mass 14. K1c, K2c, K3c, K4c all TRUE; clear(G9)=15, L_all=14, L_AS=13. The STACK by-product reproduces K1-K4 (stack losers 36,128,383,930,1862,2887,3280,2510,1301,473,124,21,2). The complete mass-13 and mass-14 CLEAR loser lists equal those of S016's reverse tool.

## 4. Replays of the S016 CLEAR tools (no source edits)

| tool | run | comparison |
|---|---|---|
| s016_g9_clear_reverse.rs (rustc 1.97.1 -O) | default (masses 1..16) | byte-identical to evidence/S016/gate2/cam04/clear_reverse_rust.txt |
| s016_g9_clear_cert_check.py (Python 3.12.10, -I) | archived certificate G9_clear_certificate.txt.xz | identical after CR removal (addendum 0-ii; the committed copy is stored LF-normalized and is then byte-identical): 492618 required/certified, 0 missing/extra/bad, both closures 1974 states, no mass-1 state |
| s016_clear_layers.rs clear / stack | G9 line of cam02 input, caps as CAM-S016-01/02 | byte-identical to cam02/rust.txt G9 line and cam01/g9_stack_rust.txt |
| s016_clear_check.mjs clear / stack (Node 24.18.0) | same | byte-identical to cam02/node.txt G9 line and cam01/g9_stack_node.txt |
| evidence/S016/HASHES.md | re-hash | 91/91 entries match |

The authors' public clearing code was not run (not mirrored; no download authorised).

## 5. Verdict

All checks agree. Under the binding outcome rule the G9 CLEAR refutation is **COLD_RECHECK_PASS**; status COMPUTED_EXACT, COLD_RECHECK_PASS, LEAN_PENDING (Lean work in this session: formal/ and sessions/S017/LEAN_RECORD.md).
