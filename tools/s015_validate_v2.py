#!/usr/bin/env python3
"""CAM-S015-83 independent validator v2.  Reuses the separately written v1
recursion (tools/s015_validate.py, unchanged) and compares its OWN critical
layer, as a set of tuples, with the producer's critical-layer file.
usage: s015_validate_v2.py graphs.txt producer_crit.txt [lo hi]
Prints one line per graph: name Lall LAS crit critAS SET_EQUAL|SET_DIFF FWD_OK|FWD_FAIL ASH_OK|ASH_FAIL
Graphs absent from the critical file (producer capped) are reported NOT_IN_PRODUCER."""
import sys
sys.path.insert(0, 'tools')
import s015_validate as V

def main():
    gfile, cfile = sys.argv[1], sys.argv[2]
    lo = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    hi = int(sys.argv[4]) if len(sys.argv) > 4 else 10**12
    pc = {}
    for line in open(cfile):
        f = line.split()
        pc[f[0]] = (int(f[1]), {tuple(map(int, x.split('.'))) for x in f[2:]})
    for i, line in enumerate(open(gfile)):
        if i < lo or i >= hi:
            continue
        name, n, nb = V.parse(line.strip())
        if name not in pc:
            print(name, 'NOT_IN_PRODUCER', flush=True); continue
        last, las, crit = V.run(n, nb)
        crit = set(crit)
        heavy = lambda p: sum(1 for k in p if k > 1)
        ascount = sum(1 for p in crit if heavy(p) <= 1)
        same = (pc[name][0] == last and pc[name][1] == crit)
        fw = all(V.forward_loses(p, nb) for p in crit if heavy(p) > 1)
        aw = min((p for p in crit if heavy(p) <= 1), default=None)
        if aw is not None:
            fw = fw and V.forward_loses(aw, nb)
        print(name, last, las, len(crit), ascount, 'SET_EQUAL' if same else 'SET_DIFF',
              'FWD_OK' if fw else 'FWD_FAIL', 'ASH_OK' if las == last else 'ASH_FAIL', flush=True)

if __name__ == '__main__':
    main()
