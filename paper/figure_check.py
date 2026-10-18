#!/usr/bin/env python3
"""Check the graph actually drawn by TikZ, not merely a free-standing edge list."""
import re
from pathlib import Path
edges = {(0,3),(0,5),(0,6),(1,4),(1,7),(1,8),(2,6),(2,8),(3,5),(3,6),(4,7),(4,8),(5,7),(6,8)}
s = Path(__file__).with_name("main.tex").read_text()
m = re.search(r"\\foreach \\a/\\b in \{([^}]+)\}", s)
assert m, "TikZ edge-source macro missing"
drawn = {tuple(map(int, edge.split("/"))) for edge in m.group(1).split(",")}
assert drawn == edges and len(drawn)==14 and all(0<=u<v<9 for u,v in drawn)
code = "HCQTaXi"
values = [ord(ch)-63 for ch in code]
assert values[0] == 9
bits = [(v>>j)&1 for v in values[1:] for j in range(5,-1,-1)]
decoded = {(i,j) for (i,j),bit in zip(((i,j) for j in range(1,9) for i in range(j)),bits) if bit}
assert decoded == drawn, (decoded,drawn)
c=(0,0,1,0,0,5,0,8,0)
image=(0,0,1,0,0,8,0,5,0)
assert len(c)==9 and sum(c)==14 and len([x for x in c if x>=2])==2
perm={0:1,1:0,2:2,3:4,4:3,5:7,6:8,7:5,8:6}
assert {tuple(sorted((perm[u],perm[v]))) for u,v in edges} == edges
assert tuple(c[perm[i]] for i in range(9))==image
for phrase in ("5 pebbles","8 pebbles","1 pebble","mass \\(s","13: AS","14: all"):
    assert phrase in s, phrase
print("FIGURE_INTEGRITY_PASS: n=9 m=14 graph6=HCQTaXi c*=14 image=14 automorphism")
