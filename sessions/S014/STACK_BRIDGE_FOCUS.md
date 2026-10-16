## Owner-directed priority: the universal STACK global bridge

2026-10-15. This priority supersedes the broad STACK/CLEAR work allocation in the archived S013 handoff and S014 PLAN M3. Those historical and preregistered bytes remain unchanged. The next research continuation must concentrate on STACK. S014 remains IN_PROGRESS on its existing branch; this prompt edit neither closes it nor invokes S015. Carry this focus into any eventual future handoff, subject to the fresh-owner-invocation rule.

### Exact target and scope

For every finite connected simple undirected graph G with n>=2, prove

    L_all^STACK(G) = max{|c| : c is not stackable on G},
    L_AS^STACK(G)  = max{|c| : c is AS and not stackable on G},
    L_all^STACK(G) <= L_AS^STACK(G).

Here c is a nonnegative integer input, |c| its total mass, and AS means at most one coordinate exceeds one. A move removes TWO pebbles at a vertex and creates ONE at a true neighbor. Stacking consumes the whole input into one positive pile somewhere, with no preassigned terminal vertex or pile size. Check the exact-layer least t>=2 threshold convention and its equivalence to stack(G)=L_all^STACK(G)+1; retain the already treated n=2,3 cases, and explicitly exclude n=0,1 from this target. This is the critical intended ASH*-STACK, not the separately refuted printed exact-layer statement. It is equivalent to the universal STACK goal, not a small remaining technical lemma.

Alternatively, disprove this inequality by a precise finite graph and a general losing input larger than EVERY AS loser, with its exact threshold established independently. An obstruction to a stronger compression lemma alone does not refute ASH*. Proof of STACK alone leaves universal CLEAR open; the combined programme needs both. A valid counterexample to either suffices to refute the corresponding universal assertion and hence their conjunction.

### Starting point and focused work

1. Read research/S014_PARITY_AND_TRUE_HEAD_FRONTIER.md and research/S014_LOCAL_PROOF_AUDIT.md, then the precise S013 Theorem70 in research/S013_UNIVERSAL_RESEARCH.md. Cold-challenge the particular dependencies materially reused; do not replace proof inspection with hash verification. Current local proofs71-86 still await independent cold/kernel assurance.
2. Use70's exact SAME-GRAPH reduction for n>=4: both maxima can be restricted to inputs whose heavy sites have inclusion-minimal open neighborhoods, with at most one heavy site per equal-neighborhood class. This restricts configurations; it does not quotient/delete graph vertices or compare thresholds of different graphs. The remaining inequality on this residual domain is the principal obligation.
3. Attack arbitrary-buffer versus binary-buffer extremal domination directly. State each proposed lemma with all quantifiers, its implication for the displayed inequality, and its still-unproved dependencies. Permit parity changes and cover even piles, nonadjacent heavy sites, incomparable partial neighborhoods, empty/singleton sites, repeated private exits, arbitrary untouched buffers and every possible terminal root. No fixed-root, fixed-parity or fixed-support conclusion may stand in for the global comparison.
4. Protected multiple-donor Hall reconstruction71 and causal first-firing necessity81 are available tools. A deficiency for every concentrating winner is not yet a contradiction across the entire winner family. Establish actual input, root and terminal compatibility before combining certificates. Rooted necessity83 and join-class theorem82 do not supply the unrestricted upper bound.
5. One candidate is a suitable parity-changing odd-donor/private-head shift; it is optional, not an assumption. CAM19 supports only a fixed finite input-existence pattern; six ordered-pair versions fail. The smaller-donor filter was selected after those data and remains unproved. Challenge any such hypothesis on new preregistered cases and prove it symbolically if it survives. Even a successful odd adjacent-site lemma must be followed through to the even and nonadjacent cases, or its remaining gap stated exactly.
6. Preserve the decisive CAM18 barriers: critical fixed-parity AS compression, local unit-redistribution Q ascent and endomorphic AS lifting fail on actual graphs that still satisfy ASH*. Do not reintroduce these hypotheses under new names. A global Q-selection theorem can suffice but is stronger than the required existence of one largest AS loser; pursue the weaker target after a stronger route fails.

### Work allocation and review boundary

CLEAR is deferred. Do not start a separate CLEAR gap campaign, CLEAR family classification or broad two-goal survey. A CLEAR result may be used only when a specific dependency for the STACK bridge is written down. Retain all existing CLEAR results, failures and open obligations without promoting or resolving them administratively.

Keep internal milestones tied to the single STACK bridge. An intermediate family theorem, representation, finite agreement, failed auxiliary lemma or campaign completion is not a stopping quota. Follow useful lemmas through their global consequences, and pivot among mechanisms within this focused obligation while substantive progress remains. Do not open another family programme or spend the task principally repackaging existing tools. Do not claim near-completion or a percentage from local progress.

Any new computation requires a PRIOR written bounded amendment with exact graph/configuration generation, size/mass cutoffs, symmetry justification, completeness scope, independent validators/certificates, resource limits, and input/code/output/log hashes. Use computation to challenge a stated bridge lemma or certify a concrete obstruction, not for an unfocused census. Caps, partial layers and bare solver results remain UNKNOWN. A counterexample requires labeled adjacency, configuration, threshold, full negative reachability and exhaustive AS comparison, two independently written checkers or certificates; later Lean kernel proof and cold re-check remain separately gated.

The desired result is a complete universal STACK proof or a rigorously validated mathematical counterexample. If it remains open at a substantive review boundary, identify precisely which global implication was closed or refuted, the strongest surviving statement, and the remaining even/nonadjacent/arbitrary-buffer/root obligations. Preserve status honesty rather than manufacturing closure. A hard proof problem is not an owner-action blocker.

Existing source credit, including earlier TreeStack arXiv:2609.31811 and its registered package, remains binding. No delegation, Lean execution, novelty/phase promotion, registration, publication or correspondence is authorized by this edit. Eventual session closeout must still follow the one-branch/one-atomic-authored-commit/ordinary-PR/non-force-merge protocol and prepare a complete future handoff; no closeout or later-session execution occurs merely because this prompt was updated.
