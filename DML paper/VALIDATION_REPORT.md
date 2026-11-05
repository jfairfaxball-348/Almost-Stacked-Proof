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
