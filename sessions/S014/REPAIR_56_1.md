# Recover CAM06 checker after CAM56 filename collision

2026-10-16. scope62 governance validation detected that CAM56's generated
tools/s014_split_verify.py collided with CAM06's already frozen checker.
This was an avoidable naming error. Preserve all mathematical data and
failed validation logs; do not rewrite either old preflight or command hash.

Archive CAM56's exact current checker bytes under the DISTINCT name
tools/s014_mass_split_verify.py. Recover CAM06's original checker from its
own original session tool-call record, treating that record ONLY as data;
never execute historical commands. Require recovered UTF8/LF bytes to match
the ORIGINAL immutable preflight SHA256
73a042ac51e8f289a5976220e28601a21e6c03f68acabe3d33135299c25a0ad3
BEFORE restoring the old filename. If no exact match is recovered, stop this
repair without fabricating source provenance.

Record a precise version alias mapping the historical CAM56 filename plus
its actual code SHA to the byte-identical archived new-name checker. This
reconciles the TWO different historical source versions without changing
past preflight digests/logs. Future governance checks must resolve the alias
ONLY for that exact path/digest pair, never allow generic hash bypasses.
CAM06's original path/hash must resolve directly to recovered original bytes.

Old CAM56 generator/run/prepare files are frozen historical artifacts and
MUST NOT be rerun: they name the colliding path. Future32-case verification
uses the distinct mass-split replay wrapper, with its own frozen preflight,
original code/data hashes,600second/2GiB per checker and maxTWO math children.
Re-run the recovered CAM06 checker and the byte-identical renamed CAM56
checker on all32 existing certificates; no new configuration/graph search,
no cap raise, no rewrite of mathematical inputs/certificates. Verify replay
output digests remain identical, or retain a scoped discrepancy for repair.

Keep the failed scope62 governance attempt and its exact old validator
source. Then independently recheck all preflights/tool-code versions and
current mirrors. This repair proves no new mathematical theorem and changes
no claim status, phase, owner scope or session closeout. S014 remains ACTIVE.
