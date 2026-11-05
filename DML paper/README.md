# DML paper — combined counterexample manuscript

**Status: proposed journal manuscript; not submitted.**
This directory is separate from the pre-existing paper/ and pending arXiv
preprint. The existing source and formalisation are unchanged.

Files:
- main.tex: full proposed article on pointwise and critical ASH.
- references.bib: bibliography from the existing manuscript.
- verify_pointwise.py: independent complete finite checks for P4 and bull.
- SUBMISSION_CHECKLIST.md: publication-readiness gates.

Principal theorem: one nine-vertex graph, graph6 HCQTaXi, disproves
the intended critical ASH for both STACK and CLEAR, with certified
losing layers and Palomar registry entry PALOMAR-2026-10-27-000023 v1.
The simpler printed-form counterexamples are introductory, not the
principal contribution. No uniqueness or infinite-family claim is made.

A mathematical presentation defect in the older manuscript recurrence
is corrected: STACK losing layers must exclude already stacked goals.
The Lean proof itself is unchanged.

From repository root, reproduce the small cases with:
    python3 "DML paper/verify_pointwise.py"

To compile a provisional article-class PDF, from this directory:
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

DML REQUIRES ITS OWN TEMPLATE. This is not yet formatted in that template.
The eight-page limit must be checked only after integrating it.
Official requirements: https://www.dmlett.com/manuscript-preparation-and-its-submission/

The next gates are: obtain official template, compile and visually inspect,
independent mathematical review, current novelty check, author sign-off
of affiliation/contact/funding/competing interests and accurate AI
assistance disclosure, and confirm DML's rules about the existing or pending
arXiv preprint and any substantially overlapping journal submission.
No journal contact or manuscript submission has occurred.
