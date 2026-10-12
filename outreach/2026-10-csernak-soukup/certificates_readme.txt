Certificates for two counterexamples to the printed Almost Stacked Hypothesis
(arXiv:2610.09650v1, Hypothesis 3.2 = arXiv:2604.22341v1, Hypothesis 9.1)
=============================================================================

Conventions. A move u=>v along an edge needs at least 2 pebbles on u; it removes 2 from u
and adds 1 to v. A configuration is stacked if exactly one vertex is occupied, and cleared
if it has exactly one pebble. It is almost stacked if at most one vertex carries 2 or more
pebbles.

Vertex labels. The files use 0-based labels, and a configuration is the list
[c(0), c(1), ...].
  * P4 (cert_P4_stack_t12.json): path 0-1-2-3, which is v1-v2-v3-v4 in the email
    (file vertex i = v(i+1)). The loser [1, 0, 2, 9] is (v1, v2, v3, v4) = (1, 0, 2, 9).
  * Bull (cert_bull_clear_t12.json): edges 0-4, 1-3, 2-3, 2-4, 3-4. The triangle is
    2, 3, 4; vertex 1 is a pendant on 3 and vertex 0 is a pendant on 4. In the email's
    names, the triangle is x, y, z with a pendant p on y and a pendant q on z:
        file vertex:  0  1  2  3  4
        email name:   q  p  x  y  z
    The file's loser [1, 9, 0, 2, 0] is therefore (p, q, x, y, z) = (9, 1, 0, 2, 0).

What each file contains (JSON).
  n, edges, goal ("stack" or "clear"), t = 12;
  as_count and as_winning_sequences: every almost stacked configuration of size 12
    (32 on P4, 80 on the bull), each with an explicit move
    list [[u, v], ...] that reaches the goal;
  losing_witness: a configuration of size 12 and its complete reachable set
    (50 configurations on P4,
    96 on the bull), which contains the
    configuration, is closed under every legal move, and contains no goal configuration.
    So the configuration is not stackable (P4) or not clearable (bull). A failed move
    sequence alone would not show this; closure of the full reachable set does.

How to check. With Python 3.8 or later (standard library only), in the folder holding the
three files, run:

    python3 verify_certificates.py cert_P4_stack_t12.json cert_bull_clear_t12.json

The script re-enumerates the almost stacked configurations of size 12 independently, checks
that they match the listed ones, and replays every move list. It then checks the reachable set:
it contains the loser, it is closed under moves, it contains no goal configuration, and it
equals a fresh breadth-first search from the loser. It prints one PASS line per file, and on
any failure prints FAIL and exits with status 1.

Consequence. Every almost stacked configuration of size 12 is stackable on P4 (clearable on
the bull), but some configuration of size 12 is not. Since 12 > |V|, Lemma 4.7 of
arXiv:2610.09650, together with the elementary bound stack(G), clear(G) >= |V|+1, gives
stack(P4) > 12 (clear(bull) > 12). So the least t >= 2 for which
every almost stacked configuration of size t is stackable (clearable) is at most 12, while
stack(P4) = 15 (Theorem 4.4 of arXiv:2610.09650) and clear(bull) = 15 (exhaustive
computation).

Appendix A. The 32 move sequences on P4 (size 12; labels v1..v4; "a>b" means a=>b)
-------------------------------------------------------------------------------

 1. (0,0,0,12): v4>v3 v4>v3 v3>v4 v4>v3 v4>v3 v3>v4 v4>v3 v4>v3 v3>v4  -> (0,0,0,3)
 2. (0,0,1,11): v4>v3 v3>v4 v4>v3 v4>v3 v3>v4 v4>v3 v4>v3 v3>v4 v4>v3 v4>v3 v3>v4  -> (0,0,0,1)
 3. (0,0,11,1): v3>v4 v3>v4 v3>v4 v3>v4 v3>v4 v4>v3 v3>v4 v4>v3 v4>v3 v3>v4  -> (0,0,0,2)
 4. (0,0,12,0): v3>v4 v3>v4 v3>v4 v3>v4 v3>v4 v3>v4 v4>v3 v4>v3 v3>v4  -> (0,0,0,3)
 5. (0,1,0,11): v4>v3 v4>v3 v3>v4 v4>v3 v4>v3 v3>v2 v2>v3 v4>v3 v3>v4  -> (0,0,0,3)
 6. (0,1,1,10): v4>v3 v3>v4 v4>v3 v4>v3 v3>v4 v4>v3 v4>v3 v3>v2 v2>v3 v4>v3 v3>v4  -> (0,0,0,1)
 7. (0,1,10,1): v3>v4 v3>v4 v3>v4 v3>v4 v3>v4 v4>v3 v4>v3 v3>v2 v2>v3 v4>v3 v3>v4  -> (0,0,0,1)
 8. (0,1,11,0): v3>v4 v3>v4 v3>v4 v3>v4 v3>v4 v4>v3 v3>v2 v2>v3 v4>v3 v3>v4  -> (0,0,0,2)
 9. (0,10,1,1): v2>v3 v2>v3 v2>v3 v2>v3 v2>v3 v3>v4 v3>v4 v3>v4 v4>v3 v4>v3 v3>v4  -> (0,0,0,1)
10. (0,11,0,1): v2>v3 v2>v3 v2>v3 v2>v3 v2>v3 v3>v4 v3>v2 v2>v3 v3>v4  -> (0,0,0,3)
11. (0,11,1,0): v2>v3 v2>v3 v2>v3 v2>v3 v2>v3 v3>v4 v3>v4 v3>v2 v2>v3 v4>v3 v3>v4  -> (0,0,0,1)
12. (0,12,0,0): v2>v3 v2>v3 v2>v3 v2>v3 v2>v3 v2>v3 v3>v4 v3>v4 v3>v4  -> (0,0,0,3)
13. (1,0,0,11): v4>v3 v4>v3 v3>v4 v4>v3 v4>v3 v3>v2 v4>v3 v4>v3 v3>v2 v2>v1 v1>v2  -> (0,1,0,0)
14. (1,0,1,10): v4>v3 v3>v2 v4>v3 v4>v3 v3>v2 v2>v1 v1>v2 v4>v3 v4>v3 v3>v2 v2>v3  -> (0,0,1,0)
15. (1,0,10,1): v3>v4 v3>v4 v3>v2 v3>v2 v2>v1 v1>v2 v3>v2 v2>v3 v4>v3 v3>v4  -> (0,0,0,2)
16. (1,0,11,0): v3>v4 v3>v4 v3>v2 v3>v2 v2>v1 v1>v2 v3>v2 v2>v3 v3>v4  -> (0,0,0,3)
17. (1,1,0,10): v4>v3 v4>v3 v3>v2 v2>v1 v1>v2 v4>v3 v4>v3 v3>v2 v2>v3 v4>v3 v3>v4  -> (0,0,0,1)
18. (1,1,1,9): v4>v3 v3>v2 v2>v1 v1>v2 v4>v3 v4>v3 v3>v2 v2>v3 v4>v3 v3>v4  -> (0,0,0,2)
19. (1,1,9,1): v3>v4 v3>v4 v3>v4 v3>v2 v2>v1 v1>v2 v4>v3 v3>v2 v2>v3 v4>v3 v3>v4  -> (0,0,0,1)
20. (1,1,10,0): v3>v4 v3>v4 v3>v4 v3>v2 v2>v1 v1>v2 v3>v2 v2>v3 v4>v3 v3>v4  -> (0,0,0,2)
21. (1,9,1,1): v2>v3 v2>v3 v2>v3 v2>v3 v3>v2 v2>v1 v1>v2 v3>v2 v2>v3 v3>v4  -> (0,0,0,2)
22. (1,10,0,1): v2>v3 v2>v3 v2>v3 v2>v3 v3>v4 v2>v1 v1>v2 v3>v2 v2>v3 v4>v3 v3>v4  -> (0,0,0,1)
23. (1,10,1,0): v2>v3 v2>v3 v2>v3 v2>v3 v3>v4 v2>v1 v1>v2 v3>v2 v2>v3 v3>v4  -> (0,0,0,2)
24. (1,11,0,0): v2>v3 v2>v3 v2>v3 v2>v3 v2>v3 v3>v2 v2>v1 v1>v2 v3>v2 v2>v3 v3>v4  -> (0,0,0,1)
25. (9,1,1,1): v1>v2 v1>v2 v1>v2 v1>v2 v2>v3 v3>v4 v2>v1 v1>v2 v2>v3 v4>v3 v3>v4  -> (0,0,0,1)
26. (10,0,1,1): v1>v2 v1>v2 v1>v2 v1>v2 v1>v2 v2>v3 v2>v3 v3>v2 v2>v3 v3>v4  -> (0,0,0,2)
27. (10,1,0,1): v1>v2 v1>v2 v1>v2 v1>v2 v1>v2 v2>v3 v2>v3 v2>v3 v3>v4 v4>v3 v3>v4  -> (0,0,0,1)
28. (10,1,1,0): v1>v2 v1>v2 v1>v2 v1>v2 v1>v2 v2>v3 v2>v3 v2>v3 v3>v4 v3>v4  -> (0,0,0,2)
29. (11,0,0,1): v1>v2 v1>v2 v1>v2 v1>v2 v1>v2 v2>v3 v2>v1 v1>v2 v2>v3 v3>v4  -> (0,0,0,2)
30. (11,0,1,0): v1>v2 v1>v2 v1>v2 v1>v2 v1>v2 v2>v3 v2>v1 v1>v2 v2>v3  -> (0,0,3,0)
31. (11,1,0,0): v1>v2 v1>v2 v1>v2 v1>v2 v1>v2 v2>v3 v2>v3 v2>v1 v1>v2 v3>v2 v2>v3  -> (0,0,1,0)
32. (12,0,0,0): v1>v2 v1>v2 v1>v2 v1>v2 v1>v2 v1>v2 v2>v3 v2>v3 v2>v3  -> (0,0,3,0)

Appendix B. The closed reachable set of (v1,v2,v3,v4) = (1,0,2,9) on P4 (50 configurations,
grouped by size; none has one-vertex support; every legal move from each stays in the set)
-------------------------------------------------------------------------------
size 12: (1,0,2,9)
size 11: (1,0,0,10) (1,0,3,7) (1,1,0,9)
size 10: (1,0,1,8) (1,0,4,5) (1,1,1,7)
size  9: (1,0,2,6) (1,0,5,3) (1,1,2,5)
size  8: (1,0,0,7) (1,0,3,4) (1,0,6,1) (1,1,0,6) (1,1,3,3) (1,2,0,5)
size  7: (1,0,1,5) (1,0,4,2) (1,1,1,4) (1,1,4,1) (1,2,1,3) (2,0,0,5)
size  6: (0,1,0,5) (1,0,2,3) (1,0,5,0) (1,1,2,2) (1,2,2,1) (2,0,1,3)
size  5: (0,1,1,3) (1,0,0,4) (1,0,3,1) (1,1,0,3) (1,1,3,0) (1,2,0,2) (1,3,0,1)
         (2,0,2,1)
size  4: (0,1,2,1) (1,0,1,2) (1,1,1,1) (1,2,1,0) (2,0,0,2) (2,1,0,1)
size  3: (0,1,0,2) (0,2,0,1) (1,0,2,0) (2,0,1,0)
size  2: (0,0,1,1) (0,1,1,0) (1,0,0,1) (1,1,0,0)
