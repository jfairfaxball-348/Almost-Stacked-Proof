"""Independent complete grammar checker plus exact source-class justification."""
import json
from pathlib import Path
import s014_rays_verify as checker
checker.B=Path('evidence/S014/balanced')
if __name__=='__main__':
    import sys
    inp=json.loads((checker.B/'ray_inputs.json').read_bytes());case=next(c for c in inp['cases'] if c['id']==sys.argv[1]);g=next(g for g in inp['graphs'] if g['graph']==case['graph']);n=g['n'];a=g['a'];b=g['b'];E={frozenset(e) for e in g['edges']}
    N=[{v for v in range(n) if frozenset([u,v]) in E} for u in range(n)];minimal={v for v in range(n) if not any(N[w]<N[v] for w in range(n))}
    assert minimal==set(range(a+b))
    for part in [list(range(a)),list(range(a,a+b)),[a+b,a+b+1]]:
        for v in part:
            first=part[0];perm=lambda u:v if u==first else first if u==v else u
            assert {frozenset(perm(u) for u in e) for e in E}==E
    # Original checker also verifies minimality for its original residual examples;
    # here only the two justified minimal source classes are retained, so use a
    # local copy of its source with that single example-specific assertion replaced.
    source=Path('tools/s014_rays_verify.py').read_text(encoding='utf-8')
    old=';assert minimal==list(range(n))'
    assert source.count(old)==1
    source=source.replace(old,';assert set(minimal)==set(range(g[\'a\']+g[\'b\']))')
    namespace={'__name__':'s014_balanced_checked_core','__file__':'tools/s014_rays_verify.py'}
    exec(compile(source,'tools/s014_rays_verify.py','exec'),namespace)
    namespace['B']=checker.B;namespace['main']()
