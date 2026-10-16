from pathlib import Path
t=Path('tools/s014_cube_general_produce.py').read_text(encoding='utf-8').replace('evidence/S014/cube_general','evidence/S014/cube_orbits')
a='def win(x):\n    if x in memo:'
b="""def canonical(x):
    c=x.to_bytes(16,'little');m=max(c);shifts=[s for s in range(16) if c[s]==m]
    if len(shifts)==1 and shifts[0]==0:return x
    best=max(bytes(c[v^s] for v in range(16)) for s in shifts)
    return int.from_bytes(best,'little')
def win(x):
    x=canonical(x)
    if x in memo:"""
assert t.count(a)==1;t=t.replace(a,b);Path('tools/s014_cube_orbits_produce.py').write_text(t,encoding='utf-8',newline='\n')
t=Path('tools/s014_cube_general_verify.py').read_text(encoding='utf-8').replace('evidence/S014/cube_general','evidence/S014/cube_orbits')
a='assert len(ss)<=2000000;truth={};'
b="""def canonical(x):
    biggest=max(x);return max(tuple(x[v^s] for v in range(16)) for s in range(16) if x[s]==biggest)
for s in range(16):assert {frozenset([u^s,v^s]) for u,v in cfg['edges']}==E
assert len(ss)<=2000000;truth={};"""
assert t.count(a)==1;t=t.replace(a,b).replace('    assert sum(x)>0','    assert sum(x)>0 and canonical(x)==x')
t=t.replace('tuple(y) in truth and not truth[tuple(y)]','canonical(tuple(y)) in truth and not truth[canonical(tuple(y))]').replace('truth[tuple(y)]','truth[canonical(tuple(y))]').replace("truth[tuple(case['c'])]","truth[canonical(tuple(case['c']))]")
Path('tools/s014_cube_orbits_verify.py').write_text(t,encoding='utf-8',newline='\n')
t=Path('tools/s014_cube_general_run.py').read_text(encoding='utf-8').replace('evidence/S014/cube_general','evidence/S014/cube_orbits').replace('s014_cube_general_','s014_cube_orbits_');Path('tools/s014_cube_orbits_run.py').write_text(t,encoding='utf-8',newline='\n');print('CAM62 exact-orbit producer and separate canonical tuple checker generated')
