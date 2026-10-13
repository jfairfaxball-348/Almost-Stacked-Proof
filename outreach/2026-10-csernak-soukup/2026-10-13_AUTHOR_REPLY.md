# 2026-10-13 — author reply: intended conjecture confirmed (owner-supplied)

**Record type:** correspondence/provenance update, **NOT a numbered mathematics session**. This document is a factual, attributed *summary*, not an authorised publication of the complete private email. Source: the recipient provided a pasted incoming message in the project conversation on 2026-10-13, displayed as from **Tamás Csernák**, addressed to John and copied to Lajos Soukup, with Gmail displaying **2:59 PM** (interface timezone/underlying SMTP header not independently checked). No raw headers or attachments were inspected. The full private email is **not reproduced** in this public repository.

## Account of what Tamás wrote

- He thanked John for the suggestion and explained that the conjecture arose from an algorithm calculating `stack(G)` and `clear(G)`: track non-stackable/non-clearable ("bad") configurations by increasing total pebble count, checking successor moves and retaining a configuration as bad when it has no legal move to a good configuration.
- He explained that their actual idea concerns the **largest bad configurations**, within which they observed almost-stacked examples. He **explicitly confirmed** that this is the formulation called **ASH\*** in John's email.
- He acknowledged that **the stronger formulation as printed is not true**: having an almost-stacked configuration among the largest bad configurations does not imply the corresponding property at all smaller counts.
- He reported that **their algorithm successfully computed both thresholds for all graphs with at most seven vertices** (clearing restricted to the non-bipartite case), with the intended critical-form ASH\* holding throughout their tested universe.

## What this evidence does and does NOT establish

1. This is **direct author testimony about intended meaning**, not an arXiv revision, public erratum, new universal theorem, independent recomputation, or formal proof.
2. The author did **not** explicitly certify the individual P4 or bull certificate files; our own finite certificates and the separately required S004 cold audit retain their original status.
3. Our **independent** seven-vertex computation has threshold-complete data for 845/853 stacking cases and 806/809 non-bipartite clearing cases within the cutoff t<=55. The author's claim of complete n<=7 coverage is stronger and remains **AUTHOR_REPORTED**; the exact graph-count conventions in the atlas (995/924 for 2<=n<=7) should be reconciled on source inspection.
4. The paper version checked in S003/pre-send audit was October arXiv:2610.09650v1. The current version must be checked afresh in S004, since correspondence does not edit the published text.
5. The real headline research problem is **ASH\***: for connected graphs with at least two vertices, a bad almost-stacked configuration exists at the last bad size `g(G)-1` (stack for connected, clear for connected non-bipartite). Universal ASH\* is OPEN.
6. The earlier TreeStack result plus the author's tree theorem settles the tree case only; there is no general proof and no general ASH\* counterexample.
7. John described the earlier email as having been sent. The repository can record **OWNER_REPORTED_SENT**, but no original outgoing mail headers, sending timestamp or delivery receipt were independently checked.
8. The reply draft `reply_draft_2026-10-13.txt` is a **proposal for John**, not an email sent by an agent or proof that John sent it. Any future author contact must be specifically authorised by the owner.

## Research consequence / handoff

See [the proof-first recurrence brief](../../research/ASHSTAR_ATTACK_BRIEF.md) and [the updated FUTURE S004 prompt](../../authoritative/NEXT_SESSION_PROMPT.md). S004 must first cold-audit the printed-form certificates and determine the Phase 1 gate for that **separate printed statement**, then mount an aggressive ASH\* proof/counterexample attack using the exact bad-layer recurrence as a new leading route. No S004 work was performed by this correspondence update.

## Correspondence / integrity note

Do not claim the authors have accepted a correction for publication or invited collaboration. Do not quote this private email verbatim in a paper or public release without consent. Record any next reply only when the owner confirms actual sending.
