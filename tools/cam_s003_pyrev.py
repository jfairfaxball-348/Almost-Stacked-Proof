#!/usr/bin/env python3
"""Pure-Python set-based reverse fixpoint (third, independent cold check; layers <= cap).

W_1 = all size-1 configurations. For t >= 2 a configuration p is winning iff it is
a goal (stack: singleton support) or p = d + 2e_u - e_v for a winning d of size t-1
and an edge uv with d(v) >= 1.  Generalises tools/reverse_cold_check.py (S002) to
arbitrary n and edge lists, and emits the same per-layer counts and fingerprints as
the C tools.  usage: cam_s003_pyrev.py NAME N "a-b,..." TMAX [CAP]
"""
import itertools
import json
import sys

P61 = (1 << 61) - 1


def comps(t, n):
    for div in itertools.combinations(range(t + n - 1), n - 1):
        prev, out = -1, []
        for pos in div:
            out.append(pos - prev - 1)
            prev = pos
        out.append(t + n - 2 - prev)
        yield tuple(out)


def h(c):
    v = 0
    for x in reversed(c):
        v = (v * 1000003 + x) % P61
    return v


def main():
    name, n, es, tmax = sys.argv[1], int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
    cap = int(sys.argv[5]) if len(sys.argv) > 5 else 5_000_000
    edges = sorted({tuple(sorted(map(int, e.split('-')))) for e in es.split(',') if e})
    arcs = [(a, b) for a, b in edges] + [(b, a) for a, b in edges]
    print(json.dumps({"graph": name, "n": n, "edges": len(edges), "tool": "pyrev"}))
    ws = wc = None
    for t in range(1, tmax + 1):
        layer = list(comps(t, n))
        if len(layer) > cap:
            print(json.dumps({"stopped_at": t, "reason": "cap"}))
            break
        if t == 1:
            ws, wc = set(layer), set(layer)
        else:
            ns = {tuple(t if i == j else 0 for i in range(n)) for j in range(n)}
            nc = set()
            for src, dst in ((ws, ns), (wc, nc)):
                for d in src:
                    for u, v in arcs:
                        if d[v] > 0:
                            p = list(d); p[u] += 2; p[v] -= 1
                            dst.add(tuple(p))
            ws, wc = ns, nc
        row = dict(t=t, total=len(layer), as_total=0, nonstack=0, as_nonstack=0, nonclear=0, as_nonclear=0)
        fs, fc = [0, 0], [0, 0]
        for c in layer:
            a = sum(x > 1 for x in c) <= 1
            row['as_total'] += a
            hv = h(c)
            if c not in ws:
                row['nonstack'] += 1; row['as_nonstack'] += a
                fs[0] = (fs[0] + hv) % P61; fs[1] = (fs[1] + hv * hv) % P61
            if c not in wc:
                row['nonclear'] += 1; row['as_nonclear'] += a
                fc[0] = (fc[0] + hv) % P61; fc[1] = (fc[1] + hv * hv) % P61
        row['fp_stack'], row['fp_clear'] = fs, fc
        print(json.dumps(row), flush=True)


if __name__ == '__main__':
    main()
