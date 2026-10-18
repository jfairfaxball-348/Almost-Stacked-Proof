# S021 AUDIT — hostile mathematical/editorial examination

Entry research main a61662304df3d8cbd797a3de85ff1e379b42df7c (S020 merged PR #27). Manuscript source is paper/main.tex with four vector TikZ figures and references.bib. Frozen Palomar snapshot not altered.

INDEPENDENT PASS: graph6 HCQTaXi decodes to precisely 9 vertices and 14 manuscript edges. Displayed (0 1)(3 4)(5 7)(6 8) automorphism preserves all edges; independent enumeration gives 8 automorphisms. Triangle 0-3-5 establishes non-bipartiteness and the graph is connected.

INDEPENDENT PASS: a newly written Python backward-losing-layer recurrence, using zero/one no-move states and reverse moves from prior losers, was run without importing original Lean/certificate data. Separate legal-successor goal predicates yield STACK counts mass 2..15: 36,128,383,930,1862,2887,3280,2510,1301,473,124,21,2,0. CLEAR: 36,137,384,932,1863,2887,3280,2510,1301,473,124,21,2,0. Both have exactly the two asserted 14-pebble losers and AS loser w13=(0,0,1,0,1,11,0,0,0). No mass 15 loser. Completeness follows because any movable loser has a losing successor (reverse a move); no-move losers are 0/1. Soundness follows by excluding goals and checking every successor. Induction above 15 uses mass>=9 to guarantee a move. Therefore both guaranteed exact thresholds are 15 and both critical AS thresholds 14: L_AS=13, L_all=14.

Reviewed: formal/Challenge.lean is deliberately sorry-bearing theorem SPECIFICATION, not implementation; Checker.lean has ordered-key, soundness, candidate completeness and terminal coverage; StackLayers.lean and ClearLayers.lean separately certify masses 2..15; Main.lean has both universal negations. Previously reported S019 kernel/Comparator result was not re-run in S021. No Palomar accepted-registration claim.

CONFIRMED DEFECT FIX: paper/figure_check.py searches for absent literal phrase mass-backslash-leftparen-s, causing a false failure. Replaced with matching phrase size-backslash-leftparen-s. Added clean-room independent enumerator and hosted exact-source PDF/BibTeX/figure build workflow that renders every page and carries a commit + SHA256 manifest. Its actual execution and visual page-by-page result are PENDING; no speculative PASS.

SOURCE LIMITS: Original April Hypothesis 9.1 is pointwise least exact-size, not the author-reported critical ASH*. The private October source-author clarification is testimony, NOT a published erratum or endorsement. Existing TreeStack (arXiv 2609.31811) is independently prior. Unresolved nine-vertex atlas UNKNOWNs forbid uniqueness and suggested infinite bridge-path family remains conjectural. Owner waived novelty audits 2/4, not passed; owner decisions 1/3 outstanding; Palomar gated. No worldwide priority claim.

**RELEASE NO-GO** until actual committed-source TeX run and rendered page audit, author signoff and explicit permission. No external submission or contact.
