"""CAM-S007-01 forward exact layers and constructive triangle-tail proof."""
import hashlib
import itertools
import json
import lzma
import time
from pathlib import Path

def edges(length):
    return [(0, 1), (0, 2), (1, 2)] + [(0 if i == 3 else i-1, i) for i in range(3, length+3)]

def configs(n, t):
    if n == 1:
        yield (t,)
    else:
        for x in range(t+1):
            for rest in configs(n-1, t-x):
                yield (x,) + rest

def digest(states):
    return hashlib.sha256(json.dumps(sorted(states), separators=(',', ':')).encode()).hexdigest()

def construct(original, length, goal='clear'):
    c = list(original)
    moves = []
    def move(u, v):
        assert c[u] >= 2 and tuple(sorted((u, v))) in {tuple(sorted(e)) for e in edges(length)}
        c[u] -= 2
        c[v] += 1
        moves.append([u, v])
    def clear(l):
        n, g = l+3, (6*2**l-2 if goal == 'clear' else 4*2**l)
        assert sum(c[:n]) >= g and not any(c[n:])
        # Source monotonicity above n: any move reaches the preceding full layer.
        while sum(c[:n]) > g:
            u = next(v for v in range(n) if c[v] >= 2)
            v = next(b if a == u else a for a, b in edges(l) if u in (a, b))
            move(u, v)
        if l == 0:
            # Completely explicit K3 size-four construction via finite recursion.
            def path(state):
                if sum(state) == 1:
                    return []
                for u, v in itertools.permutations(range(3), 2):
                    if state[u] >= 2:
                        d = list(state); d[u] -= 2; d[v] += 1
                        p = path(tuple(d))
                        if p is not None:
                            return [[u, v]] + p
                return None
            p = path(tuple(c[:3])); assert p is not None
            for u, v in p:
                move(u, v)
            return
        leaf, u = l+2, (0 if l == 1 else l+1)
        m = c[leaf]
        if m % 2 == 0:
            for _ in range(m//2):
                move(leaf, u)
        elif goal == 'stack' and m % 2 and sum(c[:leaf]) == 1:
            w = next(v for v in range(leaf) if c[v])
            # Unique tree path from new leaf to the singleton, choosing one
            # triangle arm. Replay the designated pullback operation.
            path = [leaf]
            while path[-1] >= 3:
                path.append(0 if path[-1] == 3 else path[-1]-1)
            if w in (1,2):
                path.append(w)
            else:
                path = path[:path.index(w)+1]
            d = len(path)-1
            for i in range(1,d+1):
                # Supply one pebble at each internal vertex and one at w.
                for j in range(i):
                    for _ in range(2**(i-j-1)):
                        move(path[j],path[j+1])
            for i in range(d,0,-1):
                move(path[i],path[i-1])
            assert sum(x>0 for x in c[:n]) == 1
            return
        elif m >= 5:
            for _ in range(m//2):
                move(leaf, u)
            move(u, leaf); move(leaf, u)
        else:
            assert m in (1, 3)
            if m == 3:
                move(leaf, u)
            # Root the old spanning broom at its tip. Only inward moves;
            # exact labelled ancestry leaves per output <=2^(old length+1).
            old = l-1
            parent = {1: 0, 2: 0}
            if old:
                parent[0] = 3
                for i in range(3, old+2):
                    parent[i] = i+1
            # Simulate with disjoint ancestry tokens, then replay ONLY the two
            # selected root trees. Other simulated merges must not be charged.
            tokens = [[(v, None) for _ in range(c[v])] for v in range(l+2)]
            while len(tokens[u]) < 2:
                v = next((v for v in range(l+2) if v != u and len(tokens[v]) >= 2), None)
                assert v is not None, ('two-pebble production failed', original, c)
                a, b = tokens[v].pop(), tokens[v].pop()
                tokens[parent[v]].append((parent[v], (a, b)))
            def evaluate(tree):
                vertex, children = tree
                if children is None:
                    return 1
                a, b = children
                cost = evaluate(a) + evaluate(b)
                assert a[0] == b[0]
                move(a[0], vertex)
                return cost
            before = sum(c[:l+2])
            cost = evaluate(tokens[u][0]) + evaluate(tokens[u][1])
            assert cost <= 4*2**old and sum(c[:l+2]) == before-cost+2
            if goal == 'stack' and m == 3:
                assert cost <= 1+2**(old+1)
            move(u, leaf); move(leaf, u)
        old_g = 6*2**(l-1)-2 if goal == 'clear' else 4*2**(l-1)
        assert c[leaf] == 0 and sum(c[:l+2]) >= old_g
        clear(l-1)
    clear(length)
    assert sum(c) == 1 if goal == 'clear' else sum(x>0 for x in c) == 1
    return moves

def main(goal='clear'):
    start = time.monotonic(); results, traces = [], []
    for l in range(3):
        n, g = l+3, (6*2**l-2 if goal == 'clear' else 4*2**l)
        arcs = [(u,v) for a,b in edges(l) for u,v in ((a,b),(b,a))]
        previous = set(); layers = []
        for t in range(1,g+1):
            assert time.monotonic()-start < 300
            states = list(configs(n,t)); assert len(states) <= 300000
            winning = set()
            for c in states:
                if t == 1 or goal == 'stack' and sum(x>0 for x in c) == 1:
                    winning.add(c); continue
                for u,v in arcs:
                    if c[u] >= 2:
                        d = list(c); d[u] -= 2; d[v] += 1
                        if tuple(d) in previous:
                            winning.add(c); break
            losers = set(states)-winning
            layers.append({'mass':t, 'configurations':len(states), 'winning':len(winning),
                           'losing':len(losers), 'winning_sha256':digest(winning),
                           'losing_sha256':digest(losers)})
            if t == g-1 and goal == 'clear':
                witness = (0,)*(n-1)+(t,)
                if l == 0:
                    witness = (t,0,0)
                assert witness in losers
            if t == g:
                assert not losers
                for c in states:
                    traces.append({'length':l,'configuration':c,'moves':construct(c,l,goal)})
            previous = winning
        results.append({'length':l,'n':n,'edges':edges(l),'threshold':g,
                        'scope':'COMPLETE_LABELLED_LAYERS','layers':layers})
    payload = json.dumps(traces,separators=(',',':')).encode()
    out={'campaign':('CAM-S007-01' if goal == 'clear' else 'CAM-S007-02'),'goal':goal,'graphs':results,'construction_traces':len(traces),
         'construction_moves':sum(len(r['moves']) for r in traces),'trace_raw_sha256':hashlib.sha256(payload).hexdigest(),
         'seconds':time.monotonic()-start}
    stem = 'tail' if goal == 'clear' else 'stack_tail'
    Path(f'evidence/S007/{stem}_traces.json.xz').write_bytes(lzma.compress(payload))
    Path(f'evidence/S007/{stem}_layers.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in out.items() if k != 'graphs'}))

if __name__ == '__main__':
    import sys
    main('stack' if '--stack' in sys.argv else 'clear')
