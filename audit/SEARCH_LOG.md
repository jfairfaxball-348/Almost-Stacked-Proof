# First and final novelty review: audit log

**S001 is NOT a comprehensive novelty audit.** Bootstrap recorded:
- Primary initial ASH paper: Csernák–Soukup 2026, arXiv:2610.09650 (abstract inspected).
- Earlier foundational paper: Csernák–Soukup 2026, arXiv:2604.22341 (abstract inspected).
- Earlier, independently published tree estimator proof: Fairfax-Ball, arXiv:2609.31811; TreeStack README/Lean theorem declaration inspected.
- Davenport governance comparison: methodological only, not mathematical prior art.

**Early audit (Stage 2):** once exact new theorem/counterexample exists, search current arXiv, journals, theses, graph pebbling/covers, equivalent invariants, independent solver repositories, and relevant citations. Log queries, exact dates, statements, proof access level, true closest prior result and any uncertainties.

**Final audit (Stage 4):** redo search after Lean and actual final theorem are frozen, including alternate graph models and reductions. No 'world first' statement solely from negative web searching.

## S002 bounded source/frontier checks, 2026-10-12 (NOT Stage 2 novelty)
- Exact original April arXiv:2604.22341v1 PDF pp3,20,21–26; October 2610.09650 abstract and PDF/HTML retrieval failures; TreeStack arXiv:2609.31811 abstract and exact Lean source; publisher Sjöstrand 2005 EJC DOI 10.37236/1989.
- Queries: "2610.09650 cited by graph stacking", "Almost Stacked Hypothesis counterexample 2026", "The stacking number of a tree Fairfax-Ball", 2610.09650 alternate PDF/TeX/HTML, Sjöstrand cover pebbling theorem. No verified global ASH solution surfaced; negative search has no completeness claim.

## S003 bounded source/frontier checks, 2026-10-12 (NOT Stage 2 novelty)
- Fetched full arXiv PDFs: 2610.09650v1 (sha256 `cbc9877b…`; abstract page lists v1 only, 7 Oct 2026 08:23:38 UTC) and 2604.22341v1 (sha256 `ab34962a…`). Not mirrored.
- Atlas provenance: read-only shallow clone of public `github.com/lajossoukup/pebbling` @ `701cdd93dd19869a9b90947edd6361efd81cfc1f` (2026-04-01): `pebbling.py`, `atlas_ash_report.py`, `atlas_ash_report.tex`. Its check is the critical form. Not mirrored; no contact.
- Web queries (standard search): `"Almost Stacked Hypothesis" pebbling counterexample` and `Csernák Soukup stacking number clearing number almost stacked 2610.09650`. No source reporting a counterexample to, or proof of, ASH in either form was found; only a third-party summary page of the April paper surfaced. A negative search has no completeness claim.
- Phase 2 novelty audit for the printed-form counterexample is deferred until Phase 1 passes its independent audit (S004).

## 2026-10-13 provenance update, NOT a novelty search
Recipient-provided private reply from Tamás Csernák (cc Lajos Soukup) confirms that critical-form ASH* is the intended conjecture, that the printed stronger form is false, and that the authors' upward bad-set algorithm found ASH* throughout the <=7-vertex atlas. Registered as SRC-0010, summarized (not verbatim reproduced) in `outreach/2026-10-csernak-soukup/2026-10-13_AUTHOR_REPLY.md`. This **does not** update the current arXiv version list or discharge an independent novelty search, cold audit, or publication priority claim.

## S004 current source check, not Phase2 novelty

2026-10-13 direct current arXiv abs/PDF fetches for2610.09650 and2604.22341; bothv1 only and exact previous PDF digests. October Hyp3.2 / April Hyp9.1 re-read, unchanged. Web verification query `arxiv 2610.09650 Almost Stacked Hypothesis Csernak Soukup` with recent filter surfaced the primary current source. No comprehensive erratum/priority search was performed. Author summary remains SRC0010, not a posted erratum. The new AS witness/family result has no novelty claim.

## S005 source reconciliation — not Phase2 novelty
2026-10-13 current abs/PDF fetches bothv1, same hashes. 2026-10-14 fresh PDF retrieval and proof inspection of April Theorem6.1's rooted odd-walk claim and October equation4.10. The proposed exact pure-pile theorem's lower half is this prior claim, and residue1/2 clearing is the October observation; credited explicitly. Matching equal-level construction and alternative ancestry proof recorded without novelty assertion. No comprehensive prior-art search or published erratum inference.
