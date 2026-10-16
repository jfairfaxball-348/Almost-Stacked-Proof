# CAM21 output-pipe repair, BEFORE rerun

Original CAM21 was interrupted explicitly after209.672seconds with exit
4294967295 and no complete results file. Its 471 partial graph certificates,
frozen input/code/preflight and checks.json remain at evidence/S014/oddlarge.
Partial scope is UNVERIFIED, not a passed challenge. The child accumulated
progress output while the existing supervisor waited for process exit without
draining its pipe; after graph460's progress report it stalled. Low CPU and
unchanged certificate count corroborated this implementation deadlock.

Separate v2 producer changes only its output folder and progress frequency
from every10 to every500 graphs. Separate v2 checker changes its input folder
and additionally reconstructs ALL4096 edge completions/connectedness to check
the exact frozen input list independently. The graph/input/move algorithms,
assertion, bounds and scope remain identical. Original files are not edited.
The v2 runner uses the same600second/2GiB process caps. New preflight and
outputs go to evidence/S014/oddlarge_v2. A passing v2 result does not turn the
original attempt into a success or erase its partial certificates.
