#!/usr/bin/env python3
"""CAM-S015-92 wrapper: run the source authors' public Pebbling class
(lajossoukup/pebbling@701cdd93, pebbling.py, NOT mirrored here) on graphs given
as 'name n a-b,...' lines.  Usage: s015_author_check.py /path/to/pebbling.py < list
Prints: name stacking_number critical_AS_flag witness_count witness_list."""
import sys, io, contextlib, importlib.util
import networkx as nx
spec = importlib.util.spec_from_file_location('author_pebbling', sys.argv[1])
mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
for line in sys.stdin:
    name, n, es = line.split(); n = int(n)
    G = nx.Graph(); G.add_nodes_from(range(n))
    G.add_edges_from(tuple(map(int, t.split('-'))) for t in es.split(','))
    P = mod.Pebbling(G)
    assert P.vertices == list(range(n))
    with contextlib.redirect_stdout(io.StringIO()):
        i, W = P.stacking_number()
        flag = P.is_critical_stacked_almost_stacked()
    print(name, 'stacking_number', i, 'critical_AS', flag, 'witnesses', len(W), sorted(W), flush=True)
