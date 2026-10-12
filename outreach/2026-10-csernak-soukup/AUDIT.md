# Pre-send audit of the email to Tamás Csernák and Lajos Soukup (2026-10-12)

**Status.** The owner authorised preparing this correspondence. The email was **prepared, not sent**: the agent sent nothing and contacted no one, and the owner sends it.
- This is **not** research session S004. No phase, headline or catalogue claim status was changed, and no claim needed downgrading.
- **The repository's S004 independent cold audit of the printed-form counterexamples has NOT been run.** Step 1 below is only a pre-send check of the specific claims made in this email. It does not replace S004's gate-critical audit, and it records no Phase 1 decision.

Files in this folder:
- `email.txt`: the final email.
- Attachments: `cert_P4_stack_t12.json`, `cert_bull_clear_t12.json`, `verify_certificates.py`, `certificates_readme.txt`.
- `SHA256SUMS`.
- `audit/`: the fresh verifier, pre-registration, results and readme generator. These are not attachments.

## 1. Sources and versions checked (2026-10-12, ~14:38 UTC)

| Source | Version checked | Evidence |
|---|---|---|
| [O] arXiv:2610.09650, Csernák & Soukup, "The Almost Stacked Hypothesis: A Conjectural Analogue of Sjöstrand's Cover Pebbling Theorem" | **v1 only** (submitted 2026-10-07 08:23:38 UTC; arXiv API `<updated>` unchanged) | PDF fetched to scratch (not committed), SHA-256 `cbc9877b3ce37e720f2305333a21d0078ac2e31f57991c03baedcb4683c27313`, identical to the S003 copy. **Printed hypothesis unchanged.** |
| [A] arXiv:2604.22341, Csernák & Soukup, "Stacking and clearing in graph pebbling" | **v1 only** (2026-04-24) | SHA-256 `ab34962a77a7caa4126d07430e48ba47b04c57f5ef71c21f85803cf959cbabed`, identical to S003 |
| arXiv:2609.31811, J. Fairfax-Ball, "The stacking number of a tree" | **v2** (v1 2026-09-25; v2 2026-10-09: "adds a corollary on computing stackability, cites arXiv:2610.09650 and expands the AI-use statement") | v2 PDF SHA-256 `79f1d8e4ea707206e72fce3e43fabcf8803376987f6b4da6d5fa9b5a16b4b720`; v1 `41650683dc2f416d3c9dc7384811b4261d6a7d53677e0a9833d072fa02d787c4` |
| Authors' code `github.com/lajossoukup/pebbling` | HEAD `701cdd93dd19869a9b90947edd6361efd81cfc1f` (2026-04-01, "Revised and renamed reports"), same as in S003 | Read-only shallow clone in scratch (not committed) |

Author data (from [O] p.23; [A] p.28 is identical):
- Tamás Csernák, University of Pannonia, Hungary, `tamas@csernak.com`.
- Lajos Soukup, HUN-REN Rényi Institute of Mathematics, Budapest, Hungary, `soukup@renyi.hu`.
- Diacritics as printed: Tamás Csernák.
- **No academic titles appear in either PDF.**

## 2. Fresh verification (Step 1)

`audit/verify_fresh.py` (SHA-256 `d7501059b063aaa5336591218dd860a4fec25e638e650c40112aba1d33e59f71`) is standard-library Python, written before any `tools/cam_s003_*` source was opened.
- **Algorithms:** full reachable-set BFS per configuration, and a layered win-DP (a configuration is g-able iff it is a goal or has a move into the g-able set one size lower, starting from size 1).
- **Move rule:** u⇒v along an edge needs c(u)≥2, then c(u)−=2 and c(v)+=1.
- **Goals:** stacked means one-vertex support; cleared means total size 1.
- **Results:** `audit/fresh_core.json`.

| Check | Result |
|---|---|
| (a) P4 (v1–v2–v3–v4 = file 0–1–2–3): number of AS configurations of size 12; all stackable? | **32; all stackable** |
| (b) (1,0,2,9): reachable set size / closed / contains stacked? | **50 / closed / none stacked**, so not stackable |
| (c) AS loser for every 2≤t≤11 | **yes**: e.g. t=2 (1,1,0,0), 3 (2,0,1,0), 4 (3,0,1,0), 5 (4,0,0,1), 6 (5,0,1,0), 7 (6,0,0,1), 8 (7,0,0,1), 9 (7,1,0,1), 10 (9,0,0,1), 11 (10,0,0,1). No AS loser at 12, so the least t in printed Hyp 3.2(1) is **exactly 12** |
| (d) stack(P4), exhaustive over all sizes ≤16 | losers per size 2..16: 6,10,16,20,24,22,21,14,11,8,4,2,2,0,0. With [O, Lemma 4.7], **stack(P4)=15**. AS loser at 14 = (13,0,0,1) |
| (e) bull (file edges 0-4,1-3,2-3,2-4,3-4) non-bipartite? | **yes**: triangle {2,3,4}, pendant 1 on 3, pendant 0 on 4 |
| (f) all AS configurations of size 12 clearable? | **80; all clearable** (and all stackable) |
| (g) file (1,9,0,2,0) not clearable; mapping | reachable set **96**, closed, no cleared and no stacked configuration. Mapping x=2, y=3, p=1 (pendant on y), z=4, q=0 (pendant on z) gives **(p,q,x,y,z)=(9,1,0,2,0)**, so the draft's mapping is correct |
| (h) clear(bull) | **15** (and stack(bull)=15); the least t in printed Hyp 3.2(2) is 12 |
| K_{a,b} witness (2α+1)e_w+Σ_{B′}e_x, for (a,b) ∈ {(1,2),(2,2),(1,3),(2,3),(3,3),(2,4),(1,5)} | AS, size 3α, **not stackable**; stack = 3α+1 in each case |

**Shipped certificates.**
- `python3 tools/cam_s003_cert.py check` passes on all three `evidence/S003/cert_*.json` (32/50, 80/96, 80/96).
- Their SHA-256 values match `evidence/S003/HASHES.md`: P4 `5520c5e4…`, bull clear `2e2853e5…`, bull stack `0dc46fcb…`.
- `validation/validate_governance.py` passes (20 hashed files match).
- The new attachment checker `verify_certificates.py` also passes on both attached certificates.

**Pre-registered T2b spot-check.**
- `audit/SPOTCHECK_PREREG.md` was hashed before running (first version `9796a3bb…`).
- Seed 20261012; 20 graphs fully verified.
- Two sampled graphs were skipped per the rule: A7_0001 is undecided in S003 (stack > 55), and A7_0076 is above the layer cap (stack 41, clear 55).
- **20/20 agree** with `evidence/S003/T2b_analysis.json` on threshold, literal AS threshold, literal gaps and ASH* verdict, for both goals. Every sampled graph has an AS loser at g−1.
- Sampled graphs include literal-form failures: A7_0575 (gap 12, stack 15), A7_0684 and A7_0573 (gap 17, threshold 20), A7_0235 (stack gap 12).
- A re-run under the final verifier version gave identical results.
- Output: `audit/spotcheck_T2b.json`.

**Full n≤6 re-check.**
- Pre-registered as an addendum; `audit/recheck_T2_n_le_6.json`.
- **142/143** graphs fully recomputed, with **zero disagreements** with `T2_analysis.json`.
- The only graph without an AS loser at g−1 is K1. This is the |V|≥2 boundary case; ASH* in the threshold form holds for K1 trivially.
- P6 (stack 63) is above the fresh cap. It is a tree, so it is covered by the tree theorem below and by S003's solvers.
- Literal failures recomputed: 20 stacking (21 in S003 including P6) and 19 clearing, matching S003.

**n=8 counts.** Read directly from `evidence/S003/A3_n8_analysis.json.xz`; not freshly recomputed.
- 11117 graphs (10935 non-bipartite), cap t≤26.
- Stacking: 10225 decided, all with an AS loser at g−1; 892 above the cap.
- Clearing: 10052 decided, all with an AS loser at g−1; 883 above the cap.
- The reverse solver agrees on all 10225 decided stacking cases.

**n=7 counts** (from `T2b_analysis.json`):
- Stacking: 845/853 decided, all ASH*; 8 have threshold > 55 (`NO_GAP_UP_TO_55`, threshold undetermined).
- Clearing: 806/809 non-bipartite decided, all ASH*; 3 above the cap.

## 3. Cold mathematical checks (Step 3)

- **ASH\* equivalence (S003 Thm 4(ii)), |V|=n≥2.**
  - Lemma 1: a 0/1 configuration of size t, 2≤t≤n, is AS, terminal and not stacked/cleared. So AS losers exist at every t≤n, and g(G)≥n+1.
  - [O, Lemma 4.7] (proof re-read; it needs a vertex with a neighbour, true for connected n≥2): no losers at size g implies no losers at any size ≥ g. Hence Lose(t)≠∅ exactly for 2≤t<g.
  - Let M = max{t≥2 : an AS loser of size t exists}. M exists because t=2 qualifies, and M≤g−1. The least t₀ with no AS losers at any size ≥t₀ is M+1.
  - So ASH\* ⇔ M+1=g ⇔ an AS loser exists at size g−1.
  - n=1: stack(K1)=2 and size g−1=1 is excluded by t≥2, so the equivalence needs |V|≥2. The email states it only for |V(G)|≥2. Threshold-form ASH\* holds on K1.
  - n=2: stack(K2)=3, with (1,1) an AS loser at size 2.
  - Clearing is stated only for non-bipartite G.
  - **VERIFIED.**
- **§4–5 under ASH\*.**
  - [O, Thms 4.10/4.11] (pp.6–7) are "‖c‖ ≥ bound ⇒ stackable/clearable" for AS c. So the least t₀ of ASH\* is at most the bound, and ASH\* yields Thms 4.12/4.13; the lower bounds Cor 4.5/4.6 are unconditional.
  - Trees: for AS c at r of size ≥ estim(T), we have ‖c‖ ≥ ρ_T(r)+leaf_T(r)+1 ≥ ρ_S(r)+leaf_S(r)+1 by (5.9) (p.13), and Thm 5.3 applies.
  - **CORRECTED:** the draft cited Thm 5.3 alone; (5.9) is needed.
- **§6.** [O, Cor 6.6] (p.15) assumes AS stackability at size |V|+1 only. The proof of [O, Thm 6.9] (pp.17–18) proves exactly "every almost stacked configuration in Conf_{n+1}(G) is stackable" and then invokes ASH. Thms 6.11 and 6.13 apply Thm 6.9 and use ASH nowhere else. Under ASH\*, sizes >n+1 are also needed. **VERIFIED** (wording: "would need an additional argument").
- **Trees.** [O, Thm 5.2] proof (pp.10–12) re-read line by line.
  - Witness c(r)=ρ_T(r), c=1 on leaves ≠ r: AS at r, size estim−1.
  - R=2^dist; losses 0 (downward) / 3R(u) (upward), so w_R(c)=Σ3R(u)≡0 mod 3.
  - Every subtree off the r–s path must send a pebble upward.
  - Then w_R(final) ≤ 3(2^m−1) < 3·2^m ≤ w_R(final). Sound.
  - Combined with arXiv:2609.31811v2 Thm 1.1 ("For every finite tree T with at least two vertices, stack(T)=estim(T)"; p.1, least t≥2, exact size), this gives ASH\* for trees with |V|≥2.
  - Estimator conventions: 2609.31811 uses σ_T(r)=1+Σ deg·2^dist and estim=max_r(σ+ℓ), which is [A]'s formula (p.26). [O, Def 5.1] (p.10) gives estim=max{2, 1+max_r(ρ+leaf)} with ρ=σ−1. These are **equal for |V|≥2**, and differ only at K1, where [A] gives 1 and [O] gives 2.
  - Hence 2609.31811 proves [A, Conj 10.3] (p.27) for |V|≥2, and [O, Conj 5.6] (p.14) in full (K1: stack=2=estim by [O]'s convention, as in [O, Thm 5.2]'s proof).
  - This is a theorem in another repository (Lean/Palomar per its abstract); it was not rebuilt here.
- **K_{a,b} (S003 Thm 10)** re-checked; **VERIFIED, relative to [A, Thm 8.2]**, which is SOURCE_STATED and whose proof was not inspected.
  - Setup: |B|=α=max(a,b)≥2, w∈B, B′=B∖{w}; R=1 on w, 2 on A, 4 on B′.
  - Losses: w⇒A 0, A⇒w 3, A⇒B′ 0, B′⇒A 6. Initial weight 6α−3≡0 (mod 3).
  - A final stack k·e_s needs 3|k and weight ≥3R(s).
  - Each x∈B′∖{s} must fire at least once (loss ≥6 each). Cases s∈A (3<6) and s∈B′ (9<12) are contradictions.
  - Case s=w forces total loss exactly 6(α−1). So no A⇒w move occurs, and each x∈B′ fires exactly once and receives exactly one pebble, before its firing (it starts with 1).
  - Let x\* be the last to fire, at time T: its pebble lands in A. Afterwards no move leaves A, since A⇒w is absent and every A⇒y precedes y's firing ≤ T. So A ≠ ∅ at the end, a contradiction.
  - The ordering argument is airtight. A fresh computation confirms the 7 small cases above.
  - Note: [A, Thm 5.1]'s witness (3 pebbles on each vertex of an independent set) is *not* AS, so the email does not attribute the AS witness to the authors.
- **Authors' code.**
  - `Pebbling.stacking_number` returns `(i, witness_set)`. Here `i` is the first level >n at which the recursion dies out, i.e. stack(G). `witness_set` is the set of fully matched (all children losing, non-stacked) configurations at level i−1, i.e. the non-stackable configurations of size stack(G)−1.
  - `Pebbling.is_critical_stacked_almost_stacked` returns `any(self.is_almost_stacked(c) for c in witness_set)`. `Pebbling.is_critical_clear_almost_stacked` does the same with `clearing_number()`.
  - `atlas_ash_report.tex`: 995 connected graphs tested, 995 successful stacked tests; 924 non-bipartite, 924 successful clear tests (0 failures).
  - This is exactly the critical form (equivalence above). **VERIFIED.**

## 4. Claim-by-claim table (draft → final)

| # | Draft claim | Verified how | Result | Evidence |
|---|---|---|---|---|
| 1 | To: tamas@csernak.com, soukup@renyi.hu | [O] p.23, [A] p.28 | VERIFIED | §1 |
| 2 | "Dear Dr. Csernák and Dr. Soukup" | Titles searched for in both PDFs; none printed | CORRECTED → "Dear Tamás Csernák and Lajos Soukup," (owner may restore titles if known) | §1 |
| 3 | "your two papers on stacking and clearing (2604.22341 and 2610.09650)" | arXiv metadata, PDF titles | CORRECTED: exact titles given, tagged [A] and [O] | §1 |
| 4 | Hyp 3.2 (October) = Hyp 9.1 (April) | Both PDFs: [O] p.3, [A] p.20; wording identical apart from "The stack(G)" | VERIFIED | §1 |
| 5 | "the statement your atlas code actually checks" differs from the printed one | Code read (§3) | VERIFIED | §3 |
| 6 | "Hypothesis 3.2(1) says stack(G) is the least t ≥ 2 such that every AS configuration of size t is stackable" | Quoted [O] p.3: "least integer t ≥ 2 such that every almost stacked configuration in Conf_t(G) is stackable" | VERIFIED (now uses the paper's own words) | — |
| 7 | All 32 AS configurations of size 12 on P4 are stackable | Fresh enumeration and BFS; certificate replay by two checkers | VERIFIED | §2 (a) |
| 8 | (1,0,2,9) not stackable; 50 reachable, closed, no stacked | Fresh BFS; certificate | VERIFIED | §2 (b) |
| 9 | "the least such t is 12" | AS losers found at each 2≤t≤11 | VERIFIED | §2 (c) |
| 10 | "stack(P4) = 15 by your Theorem 7.4" | [O] p.4: Thm 4.4 (stack(P_n)=2^n−1, quoting [A, Thm 7.4], [A] p.14); fresh exhaustive check | CORRECTED numbering → "[O, Theorem 4.4] (= [A, Theorem 7.4])" | §2 (d) |
| 11 | "Since 12 > \|V\| and a size-12 configuration loses, Lemma 4.7 already rules out stack(P4) ≤ 12" | [O] Lemma 4.7 (p.4) plus the lower bound (6.1) stack ≥ \|V\|+1 (p.15) | CORRECTED (made explicit: "with [O, Lemma 4.7] and (6.1) … stack(P4) > 12") | §3 |
| 12 | Bull = triangle x,y,z, pendant p on y, pendant q on z | Re-derived from certificate edges | VERIFIED | §2 (e) |
| 13 | Every AS configuration of size 12 on the bull is clearable | Fresh (80 configurations); certificate | VERIFIED (count 80 added) | §2 (f) |
| 14 | (p,q,x,y,z)=(9,1,0,2,0) not clearable | Fresh BFS (96, closed); mapping re-derived | VERIFIED (mapping correct; 96 and "non-bipartite" added) | §2 (g) |
| 15 | clear = 15 | Fresh layered DP to size 16 + Lemma 4.7; S003 three solvers | VERIFIED ("by exhaustive computation"); least t for Hyp 3.2(2) = 12 added and verified | §2 (h) |
| 16 | Lemma 4.7 makes all-configuration stackability monotone for t > \|V\| | [O] p.4 statement and proof | VERIFIED | §3 |
| 17 | "a move usually destroys the almost stacked property" | A move from the pile onto an empty vertex keeps AS; "usually" is unsupported | CORRECTED → "need not produce an almost stacked one" | — |
| 18 | "Your is_critical_stacked_almost_stacked() checks … at level stack(G) − 1" | Source read at HEAD 701cdd93 | VERIFIED; CORRECTED to the exact qualified names `Pebbling.is_critical_stacked_almost_stacked` / `Pebbling.is_critical_clear_almost_stacked`, with `stacking_number()` / `clearing_number()` | §3 |
| 19 | ASH* definition and the \|V\|≥2 equivalence | Cold proof incl. n=1, n=2, t≥2 | VERIFIED | §3 |
| 20 | "largest losing size is attained by an AS configuration" | Same proof | VERIFIED | §3 |
| 21 | "matches the intuition in your §3.1 and your computations" | [O] §3.1 p.3 ("extremal counterexamples should have at most one vertex carrying more than one pebble"); code | VERIFIED; "computations" made precise → "exactly what the atlas code tests" | §3 |
| 22 | §4–5 go through because Thms 4.10, 4.11, 5.3 hold at or above the bound | Statements and proofs read | CORRECTED: Thm 5.3 needs (5.9) to cover all sizes ≥ estim(T) | §3 |
| 23 | §6 (Cor 6.6, Thms 6.9/6.11/6.13) use AS stackability only at size \|V\|+1; need an additional argument under ASH* | Proofs read | VERIFIED | §3 |
| 24 | "I have no counterexample to ASH*" | No ASH* failure anywhere in the S003 evidence or the fresh runs | VERIFIED | §2 |
| 25 | "verified … on every connected graph with at most 7 vertices, agreeing with your atlas" | T2/T2b counts; fresh n≤6 census (142/143) and n=7 spot-check (20/20) | CORRECTED → "every connected graph with at most 6 vertices; every connected 7-vertex graph whose threshold is at most 55 (all but 8 of 853 for stacking, all but 3 of 809 non-bipartite for clearing; the rest not decided) … consistent with your atlas report" | §2 |
| 26 | "every connected 8-vertex graph whose threshold is at most 26" | A3 counts read from evidence (not freshly recomputed) | VERIFIED; counts added (10,225 / 10,052) and "larger thresholds not decided" | §2 |
| 27 | "stacking and clearing checked separately" | T1/T2/T2b/A3 record both goals separately | VERIFIED | §2 |
| 28 | "It also holds for all trees" | TreeStack Thm 1.1 + [O] Thm 5.2 (proof re-read) | CORRECTED to "every finite tree with at least two vertices" (K1 is trivial in threshold form; omitted for clarity) | §3 |
| 29 | "the witness in your Theorem 5.2 is almost stacked" | [O] pp.10–11, (5.1) | VERIFIED | §3 |
| 30 | "stack(T)=estim(T) is known for \|V\|≥2: I proved this in The stacking number of a tree (arXiv:2609.31811, September 2026, with a Lean formalisation)" | arXiv metadata (sole author John Fairfax-Ball, v1 2026-09-25); v2 PDF Thm 1.1; abstract states Lean 4 formalisation; estim convention checked | VERIFIED; "v2 cites [O]" added (factual, no priority framing) | §1, §3 |
| 31 | "so your Conjecture 5.6 is settled" | Conventions compared | CORRECTED: precise statement — [A, Conj 10.3] for \|V\|≥2; [O, Conj 5.6] in full with [O]'s K1 convention | §3 |
| 32 | ASH* for K_{a,b} via an AS witness of size 3α + "your Theorem 8.2" | S003 Thm 10 cold-checked; fresh computation on 7 cases; [A] p.17 | VERIFIED; CORRECTED attribution → "[A, Theorem 8.2]", hypothesis a+b≥3 and α=max(a,b) stated, argument described as "mod-3 weight argument with a short counting step" | §2, §3 |
| 33 | Attachments: certificates list move sequences for every AS configuration plus the full closed reachable set | Certificate structure; new checker | VERIFIED; checker and readme added to the attachment list | §5 |
| 34 | Subject line "… a suggested fix" | Style | CORRECTED → "… a suggested reformulation" (it proposes a statement and does not claim a proof) | — |

## 5. Attachments, SHA-256 and recipient dry-run

| File | SHA-256 |
|---|---|
| `cert_P4_stack_t12.json` (byte-identical to `evidence/S003/`) | `5520c5e434b5ed501b13306fb6487c0930b85a0136264f986829032fc5a5055e` |
| `cert_bull_clear_t12.json` (byte-identical to `evidence/S003/`) | `2e2853e52e074205730cbea3bf1ef47d4451bef8ca407ad7cd39b98326f7b95c` |
| `verify_certificates.py` (76 lines, stdlib, Python ≥3.8) | `067086a8050bea2a8503c60648abaf5e908878418116eabbc40a55de3287066a` |
| `certificates_readme.txt` (generated by `audit/make_readme.py` from the certificate) | `5c6ed9e4aa9a725870370b8c0a1dc9c6b6c37edfe0473a896301b2bb7f38f492` |

`SHA256SUMS` also covers `email.txt` and this file.

**Recipient dry-run.** Only the four attachments were copied into an empty scratch directory, and the readme's command was run verbatim: `python3 verify_certificates.py cert_P4_stack_t12.json cert_bull_clear_t12.json`. Both files printed PASS and the exit status was 0. Running with no arguments prints the usage and exits with status 1.

**Tamper tests.** Each of the following was rejected with FAIL and exit status 1:
- a reachable-set element dropped;
- a goal configuration added to the set;
- an extra configuration added to the set;
- one AS configuration removed;
- a move sequence with its first move deleted;
- a move along a non-edge.

One tamper did *not* fail, correctly: deleting the last move of P4 sequence 6 leaves (0,0,2,0), which is already stacked.

## 6. Diff summary against the draft
1. Salutation: titles removed (not verifiable from the papers).
2. Papers named by title and tagged [A]/[O]; every citation names its paper.
3. Fixed the citations: "Theorem 7.4" → [O, Thm 4.4] = [A, Thm 7.4]; Theorem 8.2 → [A, Thm 8.2]; Conjecture 5.6 → [O, Conj 5.6], with [A, Conj 10.3] for |V|≥2.
4. Hypothesis 3.2(1) quoted in the paper's own words; the least t = 12 is justified by an explicit statement of AS losers at every 2≤t≤11. The Lemma 4.7 remark now cites (6.1).
5. Bull: noted as non-bipartite; counts 80 and 96 added; least t = 12 for clearing stated. The mapping was already correct.
6. "a move usually destroys the AS property" → "need not produce an almost stacked one".
7. Code: exact qualified function names, plus the clearing analogue and the witness-set definition.
8. §4–5: inequality (5.9) added for trees.
9. Evidence: "≤7 vertices" weakened to the exact supported scope, with the undecided over-cap graphs disclosed. n=8 counts added. "agreeing with your atlas" → "consistent with your atlas report".
10. Trees: restricted to |V|≥2. Conjecture statement made precise. "v2 cites [O]" added.
11. K_{a,b}: hypothesis and witness spelled out; Theorem 8.2 attributed to [A].
12. Attachments sentence updated (checker and readme). Subject: "fix" → "reformulation".

## 7. Residual risks
- The S004 independent cold audit (fresh checker in a different language/algorithm, minimality checks, gate decision) has **not** been run. The counterexamples have no Lean proof yet. The finite certificates themselves are complete, and are checked by three separately written implementations (the S003 checker, this audit's verifier, the attachment checker).
- The n=8 claim relies on S003's computation (two solvers agree). Here it was re-read, not recomputed.
- [A, Thm 8.2] was used as stated; its proof was not inspected.
- The authors may already be aware of the gap or plan a revision. The email claims no novelty.
- The tree result is the sender's own paper. The email keeps that factual and does not frame it as priority.
