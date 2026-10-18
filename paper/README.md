# Counterexample manuscript — S020

Paper source: main.tex, references.bib; reproducible vector figures are editable TikZ within main.tex. Diagram identity audit: python3 paper/figure_check.py (run from repository root) or python3 figure_check.py (from paper/).

Build (in paper/):

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main                  # or bibtex8 main if bibtex alias is absent
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

Alternatively: latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex, provided BibTeX is available. Inputs: TeX Live or equivalent, tikz/pgf, booktabs, hyperref, amsthm, BibTeX. Do not use AI-generated graph renderings. Figure 1 and 2 derive from identical canonical TikZ edge list. Text uses twenty-five formally checked theorem declarations in formal/Challenge.lean and formal/AlmostStacked/Main.lean; certificate data in formal/AlmostStacked/Data/ is untrusted but independently verified by proved layer checker.

Author and status: John Fairfax-Ball; draft only, not submitted. Phases 2/4 novelty waived by owner and priority claims forbidden; Palomar registration status pending. Frozen distinct Palomar candidate: palomar/submission@34363e5222136c54b08e0c5550e2d49b9f23f5fd; NOT a registry record.

S020 text source here is the version under repository review; a separately shared local PDF preview may reflect additional copy-editing and is not asserted to be a byte-identical build from this commit. A clean-build and PDF-to-source equivalence check on the committed source are explicit S021 release prerequisites.
