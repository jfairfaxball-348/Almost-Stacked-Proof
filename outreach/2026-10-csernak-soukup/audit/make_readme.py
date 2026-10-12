#!/usr/bin/env python3
"""Generate certificates_readme.txt: hand-written header + appendix built from the P4 certificate."""
import json, sys, textwrap

base = sys.argv[1] if len(sys.argv) > 1 else "."
P4 = json.load(open(f"{base}/cert_P4_stack_t12.json"))
BULL = json.load(open(f"{base}/cert_bull_clear_t12.json"))
assert P4["edges"] == [[0, 1], [1, 2], [2, 3]] and BULL["edges"] == [[0, 4], [1, 3], [2, 3], [2, 4], [3, 4]]
v = lambda i: f"v{i + 1}"

HEADER = f"""\
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
    ({P4['as_count']} on P4, {BULL['as_count']} on the bull), each with an explicit move
    list [[u, v], ...] that reaches the goal;
  losing_witness: a configuration of size 12 and its complete reachable set
    ({len(P4['losing_witness']['reachable_set'])} configurations on P4,
    {len(BULL['losing_witness']['reachable_set'])} on the bull), which contains the
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

Appendix A. The {P4['as_count']} move sequences on P4 (size 12; labels v1..v4; "a>b" means a=>b)
-------------------------------------------------------------------------------
"""

lines = [HEADER]
for k, e in enumerate(P4["as_winning_sequences"], 1):
    c = e["config"]
    mv = " ".join(f"{v(a)}>{v(b)}" for a, b in e["moves"])
    final = list(c)
    for a, b in e["moves"]:
        final[a] -= 2; final[b] += 1
    lines.append(f"{k:2d}. ({','.join(map(str, c))}): {mv}  -> ({','.join(map(str, final))})")
R = sorted(P4["losing_witness"]["reachable_set"], key=lambda c: (-sum(c), c))
lines.append("")
lines.append(f"Appendix B. The closed reachable set of (v1,v2,v3,v4) = (1,0,2,9) on P4 ({len(R)} configurations,")
lines.append("grouped by size; none has one-vertex support; every legal move from each stays in the set)")
lines.append("-" * 79)
for s in sorted({sum(c) for c in R}, reverse=True):
    group = [c for c in R if sum(c) == s]
    body = " ".join("(" + ",".join(map(str, c)) + ")" for c in group)
    lines.extend(textwrap.wrap(body, 79, initial_indent=f"size {s:2d}: ", subsequent_indent=" " * 9))
open(f"{base}/certificates_readme.txt", "w").write("\n".join(lines) + "\n")
print("written")
