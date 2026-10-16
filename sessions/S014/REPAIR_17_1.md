# CAM17 metadata-reader repair, prior to retry

Initial attempt exited1 with KeyError 'n' when reaching new CAM15 summaries,
after reading historical cases: those store graph metadata in case.graph, while
S005 summary records store n/edges/name at top level. No mathematical output
was produced, no resource cap hit and no conclusion follows from that failure.
Original code/preflight/checks.json stay unchanged. New _v2 producer/checker
ONLY normalize this existing schema before using n/edges/name; threshold,
critical mass, full receiver formulas and all343 prescribed cases unchanged.
Separate repair preflight/code hashes and repair_checks.json preserve both
attempts. No cutoff/search scope expansion or old evidence edits.
