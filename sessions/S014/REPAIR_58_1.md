# CAM58 independent-checker evaluation-order repair

2026-10-16. During local code inspection, the original checker was found to
evaluate1<<(q-1) BEFORE checking q>0 in its zero-singleton helper. Valid
root0 calls therefore raise a negative-shift error. This is an implementation
error, not failed mathematics or evidence for a cube/ASH* claim.

Preserve the original frozen producer, checker, preflight, emitted nodes,
choices, result and actual failed-check log unchanged. The separate v2
checker changes ONLY this Boolean evaluation order (test q>0 first), adds
its own repair preflight to hash checking, and writes a distinct
verification_v2.json. Reuse the SAME frozen positive certificate data; do
not repeat or enlarge the mathematical search, node/cost/time/memory caps.
Freeze v2 code, this repair note and original derived files before replay.
The original failed attempt remains unsuccessful; only a complete independent
v2 replay can establish the AS-tail upper. S014 stays ACTIVE.
