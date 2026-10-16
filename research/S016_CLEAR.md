# S016 Gate 2: critical ASH*-CLEAR - lemmas, computations and status

Status: universal critical ASH*-CLEAR remains as recorded at the end of this file (section 9). Gate 1 (G9 STACK cold re-check) passed first: sessions/S016/GATE1_AUDIT.md.

## 1. Definitions (research/ASH_SPEC.md)

G finite, simple, connected and NON-bipartite, n=|V|>=3 (a non-bipartite simple graph has a triangle or longer odd cycle, so n>=3). Moves as for STACK. c is *clearable* if some legal sequence reaches total mass exactly 1. clear(G) is the least t>=2 such that every configuration of size exactly t is clearable. Lose(t) = non-clearable configurations of size t; L_all = max{t : Lose(t) nonempty}; L_AS = max{t : Lose(t) contains an AS configuration}. Critical ASH*-CLEAR(G): L_AS = L_all, equivalently ASLose(clear(G)-1) nonempty (S003 Theorem 4(ii) with g=clear). Bipartite graphs are excluded by the source (clear undefined there); STACK and CLEAR are separate statements and are never conflated.

## 2. Lemmas (PROGRAMME_PROVED; S003 section 2 already proves C1-C3 for g in {stack, clear}; re-stated and re-checked for CLEAR)

C1 (terminal singletons; S003 Lemma 1). For 2<=t<=n every 0/1 configuration with t ones is AS, has no legal move and mass t>=2, so it is a non-clearable AS configuration. Hence L_AS>=n, clear(G)>=n+1.

C2 (monotonicity above n; S003 Lemma 2 = October Lemma 4.7). If t>n and Lose(t) is empty then Lose(t') is empty for all t'>=t. (A configuration of size t'>t>n has a vertex with >=2 pebbles, which has a neighbour; one move lowers the size by one.)

C3 (S003 Prop. 3, Thm 4(ii)). Lose(t) is nonempty for 2<=t<clear(G) and empty for t>=clear(G); L_all = clear(G)-1; ASH*-CLEAR(G) iff Lose(L_all) contains an AS configuration.

C4 (exact losing-layer recursion). Lose(1) is empty (mass 1 is cleared). For t>=2, c of size t is non-clearable iff every legal successor (size t-1) is non-clearable; a configuration with no legal move and t>=2 is non-clearable. Proof: clearable means a sequence reaching mass 1; t>=2 excludes the empty sequence, so the first move must go to a clearable successor, and conversely.

C5 (candidate completeness). Every c in Lose(t), t>=2, is either a 0/1 vector (no legal move) or c = s + 2e_u - e_v for some s in Lose(t-1) and an ordered edge (u,v) with s_v>=1 (namely the successor along any legal move u->v). Thus Lose(t) = { c in Cand(t) : c has no legal move, or every legal successor lies in Lose(t-1) }, where Cand(t) = {0/1 vectors of mass t} union {s+2e_u-e_v : s in Lose(t-1), uv in E, s_v>=1}.

C6 (termination). By C1 Lose(t) is nonempty for t<=n, so the first empty layer t0 satisfies t0>n, and by C2 every later layer is empty; clear(G)=t0 and L_all=t0-1. The recursion therefore halts at the first empty layer and decides ASH*-CLEAR(G) exactly.

C7 (difference from STACK). For STACK the base terminal winners are all single piles k*e_v; for CLEAR only mass 1. Non-bipartiteness is needed for clear(G) to exist; on bipartite G the signed-charge invariant prevents clearing of suitable inputs at every size (not used here; bipartite graphs are simply excluded).

## 3. STACK-to-CLEAR transfer (PROGRAMME_PROVED, elementary)

T1 (loser inclusion). Let G be connected and non-bipartite. Every configuration of total mass 1 is a single pile, so every clearable configuration is stackable. Hence Lose_STACK(t) is contained in Lose_CLEAR(t) for every t, L_all^STACK <= L_all^CLEAR and stack(G) <= clear(G).

T2 (pile upgrade). If c reaches a pile k*e_r with k not divisible by 3, then c is clearable: for k>=4, two moves r->s and one move s->r (s a neighbour of r) turn k*e_r into (k-3)*e_r; at k=2 one move r->s leaves e_s; k=1 is cleared. So a stackable non-clearable configuration reaches only piles of size divisible by 3, and none of those piles is clearable.

T3 (transfer criterion). Let G be connected and non-bipartite with L := L_all^STACK(G). Suppose Lose_CLEAR(L+1) is empty and no AS configuration of mass L lies in Lose_CLEAR(L). Then Lose_CLEAR(L) contains the nonempty Lose_STACK(L), so by C2/C3 L_all^CLEAR = L, clear(G)=stack(G)=L+1, and L_AS^CLEAR < L: ASH*-CLEAR(G) fails. In particular the non-clearability of any STACK critical loser needs no separate proof: it is inherited from T1.

T3 is how G9 fails CLEAR: its two STACK critical losers are non-clearable by T1 and K1, and the finite facts "every configuration of mass 15 is clearable" and "every AS configuration of mass 14 is clearable" are certified in section 5. T3 is a criterion, not a theorem that every STACK failure transfers: a STACK counterexample transfers iff, at its own L, the stackable-but-not-clearable configurations (T2: those that reach only piles of size divisible by 3, none clearable) contain no AS configuration and nothing of mass L+1.

## 4. Computations (sessions/S016/PLAN_AMENDMENT_1, _2 and addenda; tools hashed before use)

Producer tools/s016_clear_layers.rs (Rust, hash-set recursion C4-C6); independent checker tools/s016_clear_check.mjs (Node, separately written). Protocol deviation: a 5-graph smoke test including G9 ran before amendment 1 was hashed (archived, not used as evidence; see FAILURE ledger). Comparator defect: graph6 names containing '|' broke the first comparator; it aborted on its own assertion before any result was accepted and was fixed (addendum 1-iii).

| campaign | scope | result |
|---|---|---|
| CAM-S016-01 controls | STACK on G9; CLEAR on all frozen S003 T2 (orders 1-6) and T2b (853 order-7) graphs with their own labels | G9 STACK reproduces S015 exactly; CLEAR 115 + 806 graphs agree with frozen S003 thresholds/ASH flags, 27 + 44 bipartite skips agree, the 3 S003-UNKNOWN order-7 graphs match S004 (A7_0025 94, A7_0252 63, A7_0506 63); both tools agree on every critical layer |
| CAM-S016-02 cheapest test | G9, 559 CAM90 + 29 CAM91 graphs | 560 ASH_OK, 17 ASH_FAIL (G9, X1_05b, X1_069, X1_11b, X1_144, X1_14d, X1_156, X1_15b, X1_192, F_4_4_1, F_4_5_1, P_4_2, P_5_2, PB_4_4_0_1, PB_4_4_2_1, PB_4_5_2_1, PB_5_5_2_1), 1 bipartite, 11 UNKNOWN at caps, 0 disagreements (dual). STACK and CLEAR ASH* verdicts coincide on every graph where both are known; clear=stack on 556 of 562 graphs with both thresholds |
| CAM-S016-03 complete orders 2-8 | frozen S015 nauty lists, 995 + 11117 graphs | dual: orders 2-7 924 ASH_OK, 71 bipartite; order 8 10935 ASH_OK, 182 bipartite (= OEIS A005142), 0 UNKNOWN, 0 disagreements. **Every non-bipartite connected graph of order <=8 satisfies critical ASH*-CLEAR** |
| CAM-S016-04 G9 certification | section 5 | PASS |
| CAM-S016-05 order 9 | all 261080 graphs | producer complete: 260349 ASH_OK, 1 ASH_FAIL (HCQTaXi = G9), 730 bipartite (= OEIS), 0 UNKNOWN. Checker stopped at the owner's request after 207794 graphs: 207492 dual ASH_OK + G9 dual ASH_FAIL + 301 bipartite agreements, 0 disagreements; 53286 graphs PRODUCER_ONLY |
| CAM-S016-06 STACK, S015 order-9 UNKNOWN list | 71 graphs | producer 69 ASH_OK, 2 capped; checker stopped at owner request: 9 dual ASH_OK, 3 checker-capped; the list is NOT closed at dual level |

## 5. The CLEAR counterexample G9 (COMPUTED_EXACT, multi-checker; INDEPENDENT_COLD_RECHECK_PENDING; LEAN_PENDING)

G9 = graph6 `HCQTaXi`, edges 0-3,0-5,0-6,1-4,1-7,1-8,2-6,2-8,3-5,3-6,4-7,4-8,5-7,6-8; connected, non-bipartite (triangle 0-3-5).

(K1c) c* = (0,0,1,0,0,5,0,8,0) and its image (0,0,1,0,0,8,0,5,0) are not clearable; they are the only non-clearable configurations of mass 14; neither is AS.
(K2c) Every configuration of mass 15 is clearable; by C2 every configuration of every mass >=15 is clearable.
(K3c) Every AS configuration of mass 14 is clearable.
(K4c) Every layer 2..14 has a non-clearable configuration (per-mass losers 36,137,384,932,1863,2887,3280,2510,1301,473,124,21,2; AS losers 36,137,375,791,1185,1331,1116,734,391,177,60,10,0).

Hence clear(G9)=15, L_all^CLEAR=14 > L_AS^CLEAR=13: **critical ASH*-CLEAR fails on G9.** Together with the STACK failure, the intended critical hypothesis fails in both clauses on one nine-vertex graph.

Human proof of K1c: by T1 a clearable configuration is stackable; c* and its image are not stackable (S015 K1, hand proof audited in S016 Gate 1 with repairs R1-R3). K2c-K4c are finite statements verified by: (i) the bare-definition backward closure from the nine mass-1 configurations (tools/s016_g9_clear_reverse.rs; no recursion lemma, no single-pile winners) over all configurations of masses 1..16; (ii) explicit legal clearing sequences for all 2304 AS configurations of mass 14 and all 490314 configurations of mass 15 (tools/s016_g9_clear_cert.mjs), replayed with independently enumerated coverage by tools/s016_g9_clear_cert_check.py, which also recomputes both critical closures (1974 states each, no mass-1 state); (iii) the two layer tools (CAM02/CAM05). The source authors' public clearing code was NOT run in S016.

Minimality: by CAM-S016-03 no non-bipartite graph of order <=8 fails, so 9 is the minimum order of a CLEAR counterexample. On order 9 the producer finds G9 unique (dual for 207794 graphs only).

## 6. Mechanism

On G9 the CLEAR and STACK losing layers coincide from mass 7 upward (they differ only at masses 3..6, by the clearing-specific piles 3e_v and a few related small configurations). The STACK obstruction (parity markers m2, m5 forcing a subcubic boundary tree that cannot be built: S015 section 5) therefore governs both clauses near the threshold, and T3 applies. On the S015 families the two clauses fail together on every graph where both were computed; we have no example where one clause fails and the other holds. That coincidence is an observation on finite listed families, not a theorem.

## 7. Limits

- The CLEAR refutation has not had a fresh-session cold re-check (S017 Gate 1) and has no Lean proof (Phase 3, owner-gated). The authors' code was not run for CLEAR.
- 53286 order-9 graphs (CLEAR) and 62 of the 71 S015 STACK-UNKNOWN order-9 graphs are single-implementation only; 11 CAM02 family graphs are UNKNOWN at caps. The PB(4,4,2j,1) infinite family remains a conjecture for both clauses.
- No novelty or priority claim; Phase 2 not started. No author contact.

## 8. Dependency DAG

C1-C3 (S003 Lemma 1, Lemma 2 = October Lemma 4.7, Prop. 3, Thm 4) -> C4-C6 -> layer tools. T1 (mass-1 is a single pile) + S015 K1 (S014-111/112, elementary direction of 113; audited S016 Gate 1) -> K1c. Certificates (i)-(iii) -> K2c-K4c. K1c-K4c + C3 -> ASH*-CLEAR fails on G9.

## 9. Status

Universal critical ASH*-CLEAR: **REFUTED at COMPUTED_EXACT level by G9** (multi-checker, explicit replayable certificates, human proof of the non-clearable part); INDEPENDENT_COLD_RECHECK_PENDING (S017), LEAN_PENDING. Universal critical ASH*-STACK: refuted by the same graph, COLD_RECHECK_PASS (S016 Gate 1), LEAN_PENDING. Bipartite critical ASH*-STACK: no bipartite counterexample known, OPEN.
