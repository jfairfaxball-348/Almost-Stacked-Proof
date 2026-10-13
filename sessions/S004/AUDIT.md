# S004 cold mathematical and source audit — 2026-10-13

**Printed-form Phase 1: PASS. Universal ASH*: OPEN, Phase 1 IN_PROGRESS.** Lean remains unstarted. No mathematical defect was found in the P4/bull certificates or S003 elementary reformulation. This is a fresh-session implementation audit, not an independent human review or Lean kernel check.

## Independent construction and results

`tools/s004_cold.py` was constructed before inspecting any S003 solver/checker source. It uses full reverse winning-set propagation over tuple states and separately enumerates forward reachability closures. S003 solver/checker sources were not needed; only certificate JSON was subsequently inspected/replayed by `s004_structure.py`. Graph enumeration for minimality is independent: all labelled edge subsets, connectivity, and minimum over every vertex permutation. This is an exact isomorphism quotient of graphs only, never of configurations.

| Graph/goal | AS states at 12 | All AS win | General loser | Closed goal-free reachable states | True threshold |
|---|---:|---|---|---:|---:|
| P4, stack | 32 | yes | (1,0,2,9) | 50 | 15 |
| Bull, stack | 80 | yes | (1,9,0,2,0) | 96 | 15 |
| Bull, clear | 80 | yes | (1,9,0,2,0) | 96 | 15 |

P4 labels are 0-1-2-3. Bull edges are 0-4,1-3,2-3,2-4,3-4; 2-3-4 is an explicit odd cycle. The cold closure exactly equals each original supplied reachable set, every legal successor stays inside, and none is a goal. Every original winning move sequence is replayed, checked legal, ends at the correct goal, and covers the complete independently enumerated AS set without duplicates. Original certificate bytes remain unchanged; the S003 manifest is rechecked by the governance validator.

Every connected graph with 2<=n<=4 has a complete exact threshold, using cap 32; none reached the cap. Only P4 has a stacking printed-form gap (t=12), no order <=3 stacking gap occurs, and no non-bipartite graph of order <=4 has a clearing gap. These scopes establish the claimed smallest graph order for P4 and lower bound five for a clear failure. The original source's three distinct order-five clear failures were not a required cold-minimality claim, but S004's structural atlas computes all order-five thresholds as well.

## Elementary proof audit

1. For n>=2 and 2<=t<=n, a state consisting of t singleton pebbles has no legal move, is AS, and is neither goal. Thus both eligible thresholds are at least n+1.
2. At any mass >n, a vertex has two pebbles; connectivity and n>=2 give a neighbour. Arbitrary legal moves reduce mass one at a time to any prescribed t>n. If all mass-t states win, all larger masses win. This statement concerns **all configurations**, not AS configurations.
3. A missing losing layer below the first universal threshold would contradict its definition; all layers at/above it are empty by the preceding monotonicity. Thus B_t is nonempty exactly at 2<=t<g.
4. AS_t is a subset of Conf_t, so its largest losing size M is <=g-1 and exists for n>=2 by singleton losers. The least all-larger-masses AS threshold is M+1. Hence intended ASH* iff M=g-1. Printed ASH requires an AS loser at **every** smaller candidate size. The two statements are not equivalent.
5. At t>n, all AS winners plus one general loser imply the printed form fails, even without an exact true threshold. This is the precise logical content of the P4/bull refutations.

K1: every positive configuration is already stacked, and the threshold convention t>=2 gives stack=2; clearing excluded. The g-1 AS-loser equivalence is deliberately not asserted there. Zero has empty support and is neither goal; one pebble is both goals. K2 has stack=3, critical state (1,1) is terminal; clearing excluded. Exact mass drops by one per move. These cover S003 Lemmas 1,2, Proposition 3, Theorem 4, Corollary 5 and the relevant boundaries.

## Fresh primary sources

Both current abstract/version lists and actual PDFs were fetched directly on 2026-10-13. Both lists show v1 only. The current PDFs have exactly the S003 digests:

- October 2610.09650v1, 390157 bytes, SHA256 cbc9877b3ce37e720f2305333a21d0078ac2e31f57991c03baedcb4683c27313.
- April 2604.22341v1, 652580 bytes, SHA256 ab34962a77a7caa4126d07430e48ba47b04c57f5ef71c21f85803cf959cbabed.

Fresh PDF text inspection confirms October Hypothesis 3.2 and April Hypothesis 9.1 retain the stronger least-exact-t statement. Source definitions, October Lemma 4.7 and the Lemma 6.4 proof were inspected. April Theorems 8.2/8.3 exact threshold statements and the ending of the 8.3 proof were inspected for the family consequence. The complete Proposition 8.5 proof is not independently audited. No public erratum was present in these fetched versions; this is a bounded current-source check, not an assertion that no correction exists anywhere. SRC-0010 remains attributed owner-supplied author testimony, not a posted revision. PDFs are in scratch and not redistributed.

## Repository entry audit

Entry main e7d0c793df056935c83c76f526da46fb3beb427d, tree 48d3535d18139bf6bfc917e347bde0fcf3278cdc, parents 080fdf7bbd5e4ab5ec3bfd37c3194f42950bc0de and de1c4c3bc6affbcf3126ec623b494bd9b594cf02. PR3 is one authored S003 commit 6ac5553774bb80ca1f1e7f3ad365482c0956e6c3, merged at a4724513ece45ceb28d7ba13907e185e41982b4a. PR4 prepared correspondence, merged 080fdf7b; PR5 records author confirmation, merged e7d0c793. No open PR or competing S004 branch appeared at entry.

Actual Actions runs for the S003 head and merge and current entry main were success; jobs and individual governance/certificate steps were inspected, not inferred. Current main check validate 115407765257 / run 38429534347 succeeded. Traditional status contexts are empty/pending, which does not negate the successful check run. Ruleset list empty; branch protection access returns 403 and is **UNKNOWN**, not absent. Raw compact metadata in `evidence/S004/entry_remote.json`. Historical bootstrap-only and unexecuted-S004 statements are historical, superseded by the explicit current invocation, and the current mirrors are updated at exit.

## Audit boundary

The printed-form result has a complete independently recomputed finite proof and passes its mathematics exit. This authorises only a scope-limited first novelty review for that result, which S004 did not undertake. Universal ASH* was not proved/refuted; its Phase 1 remains IN_PROGRESS. No Phase 2 promotion, formal certification, submission or external contact is inferred.
