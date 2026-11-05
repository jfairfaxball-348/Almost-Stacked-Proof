# DML paper — combined counterexample manuscript

**Status: internal final referee audit; not submitted; author signoff required.**

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
Verified after the official-format build: [CI run 42060980350](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/actions/runs/42060980350) PASS, 4 pages, no final undefined citations or overfull boxes. All four pages were independently rendered and visually inspected. The author still needs to approve contact details and submission.

Official DML guidelines:
https://www.dmlett.com/manuscript-preparation-and-its-submission/

Remaining tasks include visually inspecting the rendered PDF, independent
editorial scrutiny, final bibliography and novelty check, corresponding
author contact details, declarations and arXiv overlap policy review.
No journal contact or submission has been undertaken.


## Final audit additions (5 November 2026)

The DML manuscript also has \`verify_all_configurations.py\`, a **separate
full-state dynamic programme** that enumerates every weak composition at every
mass (rather than consuming the reverse-predecessor candidate generator).
It checks both pointwise examples and all G9 layers to mass 15.
Run \`python3 "DML paper/verify_figure.py"\` to check the exact TikZ
edge source, graph6 encoding, automorphism and occupied labels.
The DML CI executes both original scripts plus both new checks.

The exact finite calculations have been independently recomputed from the
pebbling moves. See \`REFEREE_REPORT.md\` and \`VALIDATION_REPORT.md\`.
The prior source/Palomar record is preserved; the live Lean build is not
rerun by the DML-only workflow. A final-source Actions PDF and visual inspection
must be checked against **the final PR head**, not inferred from earlier runs.

DML policy: <https://www.dmlett.com/publication-ethics/> prohibits
concurrent journal submissions of substantially similar results and requires
disclosure of funding and competing interests. The public DML rules do not
expressly mention arXiv preprints or an AI-specific disclosure format. The
substantially overlapping original counterexample preprint is already in the
arXiv process; the author must disclose this when submitting, confirm no
other journal is considering essentially the same manuscript, and approve
contact/affiliation/funding/conflict wording. Do not invent any personal facts.
