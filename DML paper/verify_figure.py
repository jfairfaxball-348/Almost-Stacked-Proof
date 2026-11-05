#!/usr/bin/env python3
"""Audit the actual DML TikZ graph and claims against its canonical data."""
from pathlib import Path
import re
s=Path(__file__).with_name("main.tex").read_text()
m=re.search(r"\\foreach \\a/\\b in \{([^}]+)\}",s)
assert m, "DML TikZ edge source absent"
drawn={tuple(map(int,x.split("/"))) for x in m.group(1).split(",")}
edges={(0,3),(0,5),(0,6),(1,4),(1,7),(1,8),(2,6),(2,8),
       (3,5),(3,6),(4,7),(4,8),(5,7),(6,8)}
assert drawn==edges and len(drawn)==14 and all(0<=u<v<9 for u,v in drawn)
code="HCQTaXi"
bits=[(ord(ch)-63>>k)&1 for ch in code[1:] for k in range(5,-1,-1)]
assert ord(code[0])-63==9
decoded={(i,j) for (i,j),b in zip(((i,j) for j in range(1,9) for i in range(j)),bits) if b}
assert decoded==drawn
perm={0:1,1:0,2:2,3:4,4:3,5:7,6:8,7:5,8:6}
assert {tuple(sorted((perm[u],perm[v]))) for u,v in edges} == edges
c=(0,0,1,0,0,5,0,8,0)
cimage=tuple(c[perm[i]] for i in range(9))
assert cimage==(0,0,1,0,0,8,0,5,0)
assert all(("\\node" in s, "\\Gedges" in s, "\\Gvertices" in s))
assert all(x in s for x in ("5 pebbles","8 pebbles","1 pebble"))
print("DML TikZ/graph6/automorphism consistency PASS")
