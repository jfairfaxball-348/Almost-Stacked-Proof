# Counterexample manuscript — S020

Paper source: main.tex, references.bib; reproducible vector figures are editable TikZ within main.tex. Diagram identity audit: python3 paper/figure_check.py (run from repository root) or python3 figure_check.py (from paper/).

Build (in paper/):

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main                  # or bibtex8 main if bibtex alias is absent
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

Alternatively: latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex, provided BibTeX is available. Inputs: TeX Live or equivalent, tikz/pgf, booktabs, hyperref, amsthm, BibTeX. Do not use AI-generated graph renderings. Figure 1 and 2 derive from identical canonical TikZ edge list. Text uses twenty-five formally checked theorem declarations in formal/Challenge.lean and formal/AlmostStacked/Main.lean; certificate data in formal/AlmostStacked/Data/ is untrusted but independently verified by proved layer checker.

Author and status: John Fairfax-Ball; manuscript draft, not submitted to arXiv or a journal. Palomar registration VERIFIED on 27 October 2026: PALOMAR-2026-10-27-000023, version 1 (https://palomar-registry.org/entry.html?id=PALOMAR-2026-10-27-000023&version=1). Archived registry source commit 358729c65c198db3a6a6973c666d3d9de4009bb7. Frozen, distinct Palomar submission snapshot: palomar/submission@34363e5222136c54b08e0c5550e2d49b9f23f5fd. Historical novelty audits 2/4 waived; no priority claim.

S020 text source here is the version under repository review; a separately shared local PDF preview may reflect additional copy-editing and is not asserted to be a byte-identical build from this commit. A clean-build and PDF-to-source equivalence check on the committed source are explicit S021 release prerequisites.

## S021 audit

Run python3 paper/figure_check.py and python3 paper/independent_layer_audit.py. The second independently reconstructs STACK and CLEAR losing layers 2–15 without consuming the generated Lean certificates. .github/workflows/paper-audit.yml performs these checks and a full exact-commit latexmk/BibTeX build, renders all PDF pages and uploads PDF, PNGs, log and commit/hash manifest. No PASS should be claimed without an actually completed run and human visual review; paper/AUTHOR_SIGNOFF.md lists unresolved release gates.

## 27 October 2026 editorial revision

Inserted the verified Palomar v1 citation and exact archive source commit; removed the non-mathematical boxed verification-workflow figure and retained its essential formal assurance in a short paragraph. Three mathematical vector figures remain (G9, critical loser, threshold gap). Exact-source PDF compilation and visual signoff must be rechecked on the final edited commit; registration does not substitute for manuscript release approval.
