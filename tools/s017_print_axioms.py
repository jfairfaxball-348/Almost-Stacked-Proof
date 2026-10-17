#!/usr/bin/env python3
"""S017: write a Lean file printing the axioms of every compared theorem (comparator.json)
and of the checker/layer theorems.  usage: s017_print_axioms.py formal OUT.lean"""
import json, sys, pathlib
root = pathlib.Path(sys.argv[1])
names = json.loads((root / 'comparator.json').read_text())['theorem_names']
extra = ['AlmostStacked.layer_step', 'AlmostStacked.layer_one'] + \
    [f'AlmostStacked.G9Data.{g}_check_{t}' for g in ['stack', 'clear'] for t in range(2, 16)] + \
    [f'AlmostStacked.G9Data.{g}_layer_{t}' for g in ['stack', 'clear'] for t in (14, 15)]
lines = ['import Solution', ''] + [f'#print axioms {n}' for n in names + extra]
pathlib.Path(sys.argv[2]).write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(len(names) + len(extra))
