# CAM49 literal-edge membership representation repair

Before replacement execution. The packed producer built directed arcs as
tuples, but tested a literal trace edge using a list, so even a legal edge
failed membership. It stopped with AssertionError before writing results.
Preserve that unsuccessful log, source and preflight; no mathematical result
was accepted. Separate even_extension_v2/source files change that one check
to tuple membership, with identical frozen graph/input/four manual histories,
caps and independent tuple BFS/trace verifier. Fresh producer and independent
verification are required; no original result file exists or is promoted.
