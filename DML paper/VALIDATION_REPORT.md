# DML manuscript validation record — 5 November 2026

## Mathematical audit (independent recurrences)

Using an independent exact-integer computation from the graph edges and the
literal legal pebbling rule, every mass layer through the critical threshold
was recomputed. This independently corroborates the formally certified theorem;
it is not a substitute for Lean certification or external peer review.

G9 (graph6 `HCQTaXi`) edges:
`03 05 06 14 17 18 26 28 35 36 47 48 57 68`.

| Mass | STACK losers | CLEAR losers | STACK AS losers | CLEAR AS losers |
|---:|---:|---:|---:|---:|
| 2 | 36 | 36 | 36 | 36 |
| 3 | 128 | 137 | 128 | 137 |
| 4 | 383 | 384 | 375 | 375 |
| 5 | 930 | 932 | 789 | 791 |
| 6 | 1862 | 1863 | 1185 | 1185 |
| 7 | 2887 | 2887 | 1331 | 1331 |
| 8 | 3280 | 3280 | 1116 | 1116 |
| 9 | 2510 | 2510 | 734 | 734 |
| 10 | 1301 | 1301 | 391 | 391 |
| 11 | 473 | 473 | 177 | 177 |
| 12 | 124 | 124 | 60 | 60 |
| 13 | 21 | 21 | 10 | 10 |
| 14 | 2 | 2 | 0 | 0 |
| 15 | 0 | 0 | 0 | 0 |

The exactly two mass-14 losers are
`(0,0,1,0,0,5,0,8,0)` and
`(0,0,1,0,0,8,0,5,0)`, neither almost stacked.

P4 STACK has 32/32 almost-stacked mass-12 winners; bull CLEAR has
80/80. At masses 12, 13, 14, 15 both graphs have unrestricted
loser counts 4, 2, 2, 0, respectively. Both pointwise witnesses
`(1,0,2,9)` and `(1,9,0,2,0)` are losing.

## Mathematical presentation correction

Unlike an earlier version in `paper/main.tex`, the DML manuscript's
recurrence for losing layers includes
`not Goal_P(c)`, essential for STACK. Without this, a single
pile at mass greater than one can be incorrectly classified as losing.

## Official journal requirements

DML demands the downloadable journal template, at most eight
template-formatted pages for original articles, at least three
keywords, 2020 MSC and a PDF submission by email. The downloaded
ZIP contains a single `DML-Template/DML-Template.tex` (4,616 bytes,
dated 2026-01-04 inside the archive). The manuscript follows its
preamble and article header, omitting spurious accepted/published
bibliographic details.

https://www.dmlett.com/manuscript-preparation-and-its-submission/

## Research and editorial boundary

- Registered Lean proof: Palomar 2026-10-27-000023 v1.
- No independent human referee review has yet taken place.
- Printed pointwise and intended critical forms are distinguished.
- The public Csernak/Soukup papers are cited; a final version/novelty
  search is required before submission.
- Check that no substantially overlapping manuscript is concurrently
  before another journal; posting to arXiv is not itself peer review.
- The corresponding author's email and all declarations require signoff.
- Manuscript remains NOT SUBMITTED.

## Final DML-format PDF validation — 5 November 2026

[GitHub Actions run 42060980350](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/actions/runs/42060980350) passed on source commit `d07ce11109d63b0f86c0bfdc4730a2ca5857b772`. It built the paper using the official DML formatting, verified the pointwise and nine-vertex graph exact layer recurrences, compiled references, generated four A4 pages, and found no overfull boxes or unresolved final citations. All four pages of the identical LaTeX source's [successful CI run 42060911551](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/actions/runs/42060911551) were rendered and visually inspected. The PDF SHA-256 was `6dc8542d765ff860b4787a077652d01cc73a1cee1e58f38f9f06d517279e1167`.

This is a manuscript build audit, not independent human mathematical refereeing or an acceptance decision. Final author contact details, AI and other declarations, current novelty verification, arXiv/journal overlap policy and actual submission remain open.


## Fresh 5 November 2026 referee-style audit

Pinned starting \`main\`: \`17eeb93898bdeab9fef323788c1ea6d9ff4bba8c\`.
A new *full-configuration* integer dynamic programme, independent of the
repository's reverse-candidate recurrence and Lean layer data, was executed.
It enumerated all weak compositions at each mass, finding G9 STACK/CLEAR
counts exactly as in the table above, two and only two mass-14 losers,
none at mass 15, and ten AS mass-13 losers in each mode.
For P4 STACK and bull CLEAR, it found 32/32 and 80/80 AS mass-12 winners,
respectively, unrestricted losing counts 4,2,2,0 at masses 12–15.
The pointwise losing-state forward closures were separately checked to have
50 and 96 states and no goal state. No numerical defect was found.

Source checked: Csernák--Soukup arXiv:2604.22341 and arXiv:2610.09650
(including the printed pointwise Hypothesis 3.2); the latter explicitly
describes a separate ASH hypothesis for connected/non-bipartite graphs.
No verified later correction was located in the public source inspection.
Search did not reveal another independent published G9 counterexample;
absence of a web search result is *not* a novelty guarantee.

Editorial fixes: removed an unsupported reference to the original authors'
"public computational criterion", fixed the DML-specific figure-check path,
added separate all-configurations and figure validators to CI, and explicitly
stated that the original counterexample preprint substantially overlaps the
DML paper. The DML official submission page confirms mandatory template,
eight-page limit, PDF-by-email to m.secretary@dmlett.com, ≥3 keywords and MSC.
DML ethics policy explicitly prohibits substantially similar simultaneous
journal submission, requires funding and conflict-of-interest declarations,
and contains no located arXiv-specific or AI-specific procedure.

**Unresolved prior to submission:** author email and personal signoff; verify
whether the original paper has been submitted to any journal (arXiv alone is
not a journal submission), and confirm accurate funding/conflict declarations.
DML's public wording does not clearly resolve prior arXiv posting. No journal
editor was contacted. This is internal mathematical checking, NOT human
external refereeing. Current-PR final PDF build/CI/visual inspection evidence
must be added after observed completion; prior-passing runs do not suffice.
