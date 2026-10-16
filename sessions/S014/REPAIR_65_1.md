# CAM65 variable-width producer repair

2026-10-16. Original generalized positive producer fails its first buffer
assertion: the generator changed root loops to n14 but left several temporary
arrays at literal width16. Their two untouched entries stay infinity/None.
This is an implementation error, not a mathematical discrepancy or graph
counterexample. The failed original source, preflight/check log and all
inputs remain byte-for-byte unchanged; no result/node artifact was emitted.

Separate s014_c065_produce_v2.py replaces the remaining literal16 temporary
widths with the declared n. The node format remains8 bytes and the exact
14-vertex graph,336 maps,8192 buffers,cost1024,344064-node and time/memory
bounds remain unchanged. Freeze v2, this note, original preflight/input/source
and independent checker BEFORE rerun. Derived nodes frozen before the SAME
separately written complete positive/lower verifier. Only repaired complete
checks can promote an exact AS result; original failure remains unsuccessful.
No source overwrite, cap increase, phase/closeout or future session action.
