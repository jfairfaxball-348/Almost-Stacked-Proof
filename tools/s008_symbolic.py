"""Universal linear production certificate, no optimization or sampled lengths.

For alpha*A+beta*t, A>=ratio*t>0, nonnegativity follows from
alpha>=0 and ratio*alpha+beta>=0. Residue parity cases are exhaustive.
"""
import itertools
import json
import sys
from pathlib import Path

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def sub(x,y):return (x[0]-y[0],x[1]-y[1])

def label(typ,scale,mask,r,forest,a_mod,t_mod):
    if r==3:
        return (0,0) if typ in ('one','two') and mask==(1 if typ=='one' else 2) else None
    if mask:
        unit_mod=a_mod if typ!='path' else scale*t_mod%3
        k=next(k for k in range(3) if (4*a_mod-k*unit_mod)%3==r)
        return (4-k,0) if typ!='path' else (4,-k*scale)
    if typ in ('one','two'):
        if forest:
            k=next(k for k in (1,2,3) if k*2*a_mod%3==r)
            return (2*k,0)
        if r==0:return (6,0)
        return (2,0) if r==2*a_mod%3 else (4,0)
    if typ=='core':
        if forest:
            k=next(k for k in (1,2,3) if k*a_mod%3==r)
            return (k,0)
        return (1,0) if r==a_mod else (6,0)
    if forest:
        k=next(k for k in (1,2,3) if k*scale*t_mod%3==r)
        return (0,k*scale)
    return (0,scale) if r==scale*t_mod%3 else (6,0)

def main():
    checks=[]
    def bound(parent,a,b,ratio,tag):
        if a is None or b is None:return
        assert parent is not None,tag
        delta=sub(add(a,b),parent)
        assert delta[0]>=0 and delta[0]*ratio+delta[1]>=0,(tag,delta,ratio)
        checks.append({'rule':tag,'difference_A_t':delta,'domain_A_ge_ratio_t':ratio})
    # Internal path edge has distances d,d+1 and A>=2t. Core edges use A alone.
    for am,tm in itertools.product((1,2),repeat=2):
        for u,v,ratio in [(('path',1),('path',2),2),(('path',2),('path',1),2),
                          (('core',1),('one',1),1),(('one',1),('core',1),1),
                          (('core',1),('two',1),1),(('two',1),('core',1),1),
                          (('one',1),('two',1),1),(('two',1),('one',1),1)]:
            for ma,mb,ra,rb in itertools.product(range(4),repeat=4):
                if ma&mb:continue
                rp=3 if ra==rb==3 else (ra%3+rb%3)%3
                a=label(*u,ma,ra,False,am,tm);b=label(*u,mb,rb,False,am,tm)
                p=label(*v,ma|mb,rp,False,am,tm)
                bound(p,a,b,ratio,'tree_merge')
        for typ,scale,ratio in [('path',1,1),('core',1,1),('one',1,1),('two',1,1)]:
            for m,r in itertools.product(range(4),repeat=2):
                c=label(typ,scale,m,r,False,am,tm);s=label(typ,scale,m,r,True,am,tm)
                bound(s,c,(0,0),ratio,'forest_seed')
            for ma,mb,ra,rb in itertools.product(range(4),repeat=4):
                if ma&mb:continue
                rp=3 if ra==rb==3 else (ra%3+rb%3)%3
                a=label(typ,scale,ma,ra,True,am,tm);b=label(typ,scale,mb,rb,True,am,tm)
                p=label(typ,scale,ma|mb,rp,True,am,tm)
                bound(p,a,b,ratio,'forest_concat')
    # Source leaf at tip t=1,r=1; l=0 source is core with A=1.
    assert label('path',1,0,1,False,1,1)==(0,1)
    assert label('path',1,0,1,False,2,1)==(0,1)
    assert label('core',1,0,1,False,1,1)==(1,0)
    assert label('one',1,1,3,False,1,1)==(0,0)
    assert label('two',1,2,3,False,1,1)==(0,0)
    out={'universal_domains':['A=2^l,t=2^d,0<=d<=l','internal path A>=2t','core edges A>0'],
         'all_production_inequalities':True,'checks':checks,'count':len(checks),
         'bases_checked':5,'candidate_all_root_forest_bound':'4A at residue4A and nonempty two-singleton mask'}
    if '--check-only' not in sys.argv:Path('evidence/S008/symbolic_certificate.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'universally_nonnegative_linear_differences':len(checks),'bases':5,'all_verified':True}))

if __name__=='__main__':main()
