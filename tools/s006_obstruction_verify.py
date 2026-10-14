"""Independent closure/trace verification of the S006 auxiliary obstructions."""
import json
import sys
from pathlib import Path


def verify(row, mode='clear', excluded_target=None):
    start = tuple(row['configuration'])
    states = {tuple(c) for c in row['reachable']}
    assert start in states
    n = len(start)
    adjacent = [[False] * n for _ in range(n)]
    for u, v in row['edges']:
        assert u != v
        adjacent[u][v] = adjacent[v][u] = True
    reached = {start}
    queue = [start]
    for c in queue:
        assert len(c) == n and min(c) >= 0 and 1 <= sum(c) <= sum(start)
        for u in range(n):
            if c[u] < 2:
                continue
            for v in range(n):
                if adjacent[u][v]:
                    d = tuple(c[i] - 2 * (i == u) + (i == v) for i in range(n))
                    assert d in states
                    if d not in reached:
                        reached.add(d)
                        queue.append(d)
    assert reached == states
    goal = lambda c: sum(c) == 1 if mode == 'clear' else sum(x > 0 for x in c) == 1
    if excluded_target is None:
        assert any(goal(c) for c in states) == row['clearable']
    else:
        assert tuple(int(v == excluded_target) for v in range(n)) not in states
    if row['clearable'] and row['trace']:
        c = start
        for step in row['trace']:
            assert tuple(step['from']) == c
            u, v = step['move']
            assert adjacent[u][v] and c[u] >= 2
            c = tuple(c[i] - 2 * (i == u) + (i == v) for i in range(n))
            assert tuple(step['to']) == c
        assert goal(c)
    return len(states)


def main():
    challenges = json.loads(Path('evidence/S006/rooted_challenges.json').read_text())
    extra = json.loads(Path('evidence/S006/attachment_obstructions.json').read_text())
    rows = [challenges['first_scalar_false_positive'], challenges['first_scalar_false_negative']] + extra
    total = sum(verify(r) for r in rows)
    total += verify(challenges['K3_fixed_target_obstruction'], excluded_target=0)
    extrema = json.loads(Path('evidence/S006/extremal_challenge.json').read_text())['first_failure']
    assert extrema['configuration'] == [3, 3, 0] and extrema['edges'] == [[0, 2], [1, 2]]
    assert extrema['class_states'] == [[3, 3, 0]] and not extrema['class_has_AS']
    assert extrema['class_Qmax'] == 18 < extrema['global_Qmax'] == 26
    # Independent complete closure of the minimal inherited critical class loser.
    queue = [tuple(extrema['configuration'])]
    seen = set(queue)
    for c in queue:
        assert sum(x > 0 for x in c) != 1
        for u, v in ((0, 2), (2, 0), (1, 2), (2, 1)):
            if c[u] >= 2:
                d = list(c)
                d[u] -= 2
                d[v] += 1
                d = tuple(d)
                if d not in seen:
                    seen.add(d)
                    queue.append(d)
    output = {'auxiliary_closures_verified': len(rows) + 1,
              'closed_states': total, 'P3_critical_loser_closure': len(seen),
              'all_verified': True}
    if '--check-only' not in sys.argv:
        Path('evidence/S006/obstruction_verification.json').write_text(json.dumps(output, indent=2) + '\n', newline='\n')
    print(json.dumps(output))


if __name__ == '__main__':
    main()
