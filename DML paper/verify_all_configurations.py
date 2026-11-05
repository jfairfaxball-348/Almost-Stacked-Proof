#!/usr/bin/env python3
"""Full-space independent pebbling DP: no Lean arrays, no reverse-layer candidate generator."""
from itertools import combinations

G9 = ((0,3),(0,5),(0,6),(1,4),(1,7),(1,8),(2,6),(2,8),
      (3,5),(3,6),(4,7),(4,8),(5,7),(6,8))
P4 = ((0,1),(1,2),(2,3))
BULL = ((0,4),(1,3),(2,3),(2,4),(3,4))
COUNTS_STACK = (36,128,383,930,1862,2887,3280,2510,1301,473,124,21,2,0)
COUNTS_CLEAR = (36,137,384,932,1863,2887,3280,2510,1301,473,124,21,2,0)
CRITICAL = {(0,0,1,0,0,5,0,8,0),(0,0,1,0,0,8,0,5,0)}
W13 = (0,0,1,0,1,11,0,0,0)

def compositions(n, mass):
    """Every nonnegative n-vector of the requested mass, exactly once."""
    for dividers in combinations(range(mass+n-1), n-1):
        previous = -1
        vector = []
        for pos in dividers:
            vector.append(pos-previous-1)
            previous = pos
        vector.append(mass+n-2-previous)
        yield tuple(vector)

def calculate(n, edges, limit):
    neighbors = [[] for _ in range(n)]
    for u,v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    older_stack, older_clear = set(), set()
    output = {}
    for mass in range(1,limit+1):
        loses_stack, loses_clear = set(), set()
        as_stack = as_clear = as_total = 0
        num = 0
        for c in compositions(n,mass):
            num += 1
            stack = sum(x>0 for x in c) == 1
            clear = mass == 1
            if not (stack and clear):
                for u in range(n):
                    if c[u] < 2:
                        continue
                    for v in neighbors[u]:
                        d = list(c)
                        d[u] -= 2
                        d[v] += 1
                        d = tuple(d)
                        if not stack and d not in older_stack:
                            stack = True
                        if not clear and d not in older_clear:
                            clear = True
                        if stack and clear:
                            break
                    if stack and clear:
                        break
            if not stack:
                loses_stack.add(c)
            if not clear:
                loses_clear.add(c)
            if sum(x>1 for x in c) <= 1:
                as_total += 1
                if not stack:
                    as_stack += 1
                if not clear:
                    as_clear += 1
        output[mass] = (num,loses_stack,loses_clear,as_total,as_stack,as_clear)
        older_stack,older_clear = loses_stack,loses_clear
    return output

def main():
    for title,n,edges,goal,witness,as_count in (
        ("P4",4,P4,1,(1,0,2,9),32),
        ("BULL",5,BULL,2,(1,9,0,2,0),80)):
        d = calculate(n,edges,15)
        t12 = d[12]
        assert t12[3] == as_count
        assert t12[4 if goal==1 else 5] == 0
        assert witness in t12[goal]
        assert tuple(len(d[t][goal]) for t in range(12,16)) == (4,2,2,0)
        print(title,"pointwise and exact threshold PASS")
    d = calculate(9,G9,15)
    assert tuple(len(d[t][1]) for t in range(2,16)) == COUNTS_STACK
    assert tuple(len(d[t][2]) for t in range(2,16)) == COUNTS_CLEAR
    for idx in (1,2):
        assert d[13][idx] and W13 in d[13][idx]
        assert d[14][idx] == CRITICAL
        assert not d[15][idx]
    assert d[13][4] == d[13][5] == 10
    assert d[14][4] == d[14][5] == 0
    print("G9 full-composition STACK/CLEAR layers through mass 15 PASS")
    print("mass14 unrestricted losers:",sorted(d[14][1]))
if __name__=="__main__":
    main()
