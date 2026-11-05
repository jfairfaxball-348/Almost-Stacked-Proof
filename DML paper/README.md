# DML paper — combined counterexample manuscript

**Status: DML-template manuscript in technical preflight; not submitted.**

This directory is separate from the pre-existing `paper/` and the pending
arXiv preprint. Neither the original paper nor any frozen Lean proof changed.

The current `main.tex` applies the actual [DML official 2026-01-04 LaTeX
template](https://www.dmlett.com/archive/DML-Template.zip): 10pt A4 article,
1.1 cm margins, section headings, sectional theorem/caption numbering,
bibliography spacing and journal header. Publication volume/page/acceptance
metadata have **not** been invented. The contact footnote remains explicitly
marked for author sign-off. The author's substantial AI-assistance disclosure
is preserved.

Files:
- `main.tex` — full DML-formatted proposed manuscript.
- `references.bib` — source-linked bibliography.
- `verify_pointwise.py` — exact independent P4/bull checks.
- `verify_g9_layers.py` — exact independent G9 STACK/CLEAR layer check,
  based on the explicit pebbling move, not Lean certificate arrays.
- `VALIDATION_REPORT.md` — mathematics and publication-rule audit.
- `SUBMISSION_CHECKLIST.md` — remaining gates.

To run the mathematical verifiers:
    python3 "DML paper/verify_pointwise.py"
    python3 "DML paper/verify_g9_layers.py"

To generate the manuscript PDF with TeX Live:
    cd "DML paper"
    latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex

The `DML manuscript preparation audit` GitHub Actions workflow independently
retrieves the official ZIP, checks required template settings, runs both
verification scripts, builds PDF and bibliography from the exact committed
source, renders PDF pages, and fails if the DML-template paper exceeds 8 pages.
Do not claim a final build or PDF pass until its specific commit run completes.

Official DML guidelines:
https://www.dmlett.com/manuscript-preparation-and-its-submission/

Remaining tasks include visually inspecting the rendered PDF, independent
editorial scrutiny, final bibliography and novelty check, corresponding
author contact details, declarations and arXiv overlap policy review.
No journal contact or submission has been undertaken.
