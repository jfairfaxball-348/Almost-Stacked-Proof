#!/usr/bin/env python3
"""S017 local stand-in for a Comparator run (NOT Comparator itself).

1. The definition block of formal/Challenge.lean must equal, byte for byte, the block of
   formal/AlmostStacked/Defs.lean between `namespace AlmostStacked` and `end AlmostStacked`.
2. Writes OUT.lean, which imports the Solution and re-states every Challenge theorem (inside
   `namespace AlmostStacked.ChallengeCopy`, so the statements elaborate against the Solution's
   definitions) with the proof `by exact?`-free term: the Solution theorem applied to the
   statement's own binders.  If OUT.lean compiles, every Challenge statement is implied
   verbatim (up to definitional unfolding by the elaborator) by the Solution theorem.

usage: s017_challenge_bridge.py formal OUT.lean
"""
import re, sys, pathlib

root = pathlib.Path(sys.argv[1])
ch = (root / 'Challenge.lean').read_text(encoding='utf-8')
de = (root / 'AlmostStacked' / 'Defs.lean').read_text(encoding='utf-8')
blk = lambda s: s[s.index('namespace AlmostStacked'):s.index('end AlmostStacked')]
chdefs = ch[ch.index('namespace AlmostStacked'):]
assert chdefs.startswith(blk(de)), 'Challenge definitions differ from Defs.lean'
stmts = chdefs[len(blk(de)):]
out = ['module', '', 'import Solution', '', 'namespace AlmostStacked.ChallengeCopy', 'open AlmostStacked', '']
n = 0
for m in re.finditer(r'(/--.*?-/\s*)?theorem (\S+)(.*?):= *\n?\s*sorry', stmts, re.S):
    name, sig = m.group(2), m.group(3)
    # explicit binder names before the colon, in order
    head = sig.split(' :\n')[0] if ' :\n' in sig else sig
    depth, i, colon = 0, 0, None
    while i < len(sig):
        ch_ = sig[i]
        if ch_ in '([{⦃': depth += 1
        elif ch_ in ')]}⦄': depth -= 1
        elif ch_ == ':' and depth == 0:
            colon = i; break
        i += 1
    binders = sig[:colon]
    args = []
    for b in re.finditer(r'\(([^():]+):', binders):
        args += b.group(1).split()
    out.append(f'theorem {name}{sig}:=\n  AlmostStacked.{name} ' + ' '.join(args))
    out.append('')
    n += 1
out.append('end AlmostStacked.ChallengeCopy')
pathlib.Path(sys.argv[2]).write_text('\n'.join(out) + '\n', encoding='utf-8')
print('definitions identical; statements', n)
