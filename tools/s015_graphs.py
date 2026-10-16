#!/usr/bin/env python3
"""CAM-S015-82 graph lists: decode graph6 lines (from nauty-geng -c N) into
'name n a-b,...' lines; name is the graph6 string itself.  Also provides an
independent count/canonical cross-check against the repository's own
S003 generator (tools/cam_s003_graphs.py) for orders <= 8.

usage: s015_graphs.py decode < g6  |  s015_graphs.py crosscheck N g6file
"""
import sys


def g6_decode(s):
    data = [ord(ch) - 63 for ch in s.strip()]
    n = data[0]
    bits = []
    for x in data[1:]:
        for k in range(5, -1, -1):
            bits.append((x >> k) & 1)
    edges = []
    i = 0
    for j in range(1, n):
        for a in range(j):
            if bits[i]:
                edges.append((a, j))
            i += 1
    return n, edges


def decode():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n, edges = g6_decode(line)
        es = ','.join(f'{a}-{b}' for a, b in edges) or '-'
        print(line, n, es)


def crosscheck(N, path):
    sys.path.insert(0, 'tools')
    import cam_s003_graphs as G
    mine = set()
    for line in open(path):
        n, edges = g6_decode(line)
        mine.add(G._canon(n, edges)[0])
    ref = set(G._canon(N, e)[0] for e in G.connected_atlas(N))
    print('geng_count', len(mine), 'distinct_canon', len(mine))
    print('repo_count', len(ref), 'equal', ref == mine)


if __name__ == '__main__':
    if sys.argv[1] == 'decode':
        decode()
    else:
        crosscheck(int(sys.argv[2]), sys.argv[3])


def g6_encode(n, edges):
    """graph6 string for an n<=62 vertex graph (inverse of g6_decode)."""
    es = {tuple(sorted(e)) for e in edges}
    bits = [1 if (a, j) in es else 0 for j in range(1, n) for a in range(j)]
    while len(bits) % 6:
        bits.append(0)
    return chr(n + 63) + ''.join(chr(63 + int(''.join(map(str, bits[i:i + 6])), 2)) for i in range(0, len(bits), 6))
