"""Producer prefix-gate encoding; independently truth-table checked elsewhere."""
import itertools
def build(n,c):
    edges=list(itertools.combinations(range(n),2));vid={e:i+1 for i,e in enumerate(edges)};nv=len(edges);clauses=[];blocks=[];comparisons=[]
    def clean(C):
        S=set(C)
        if any(-v in S for v in S):return None
        return sorted(S)
    for value in sorted(set(c)):
        group=[i for i,z in enumerate(c) if z==value]
        for u,v in zip(group,group[1:]):
            permutation=list(range(n));permutation[u],permutation[v]=v,u;nv+=1;previous=nv;clauses.append([previous]);comparisons.append(dict(swap=[u,v],prefix0=previous,first_block=len(blocks)))
            for i,(s,t) in enumerate(edges):
                a=i+1;b=vid[tuple(sorted((permutation[s],permutation[t])))];nv+=1;current=nv;raw=[[-previous,-a,b],[-current,previous],[-current,-a,b],[-current,a,-b],[-previous,-a,-b,current],[-previous,a,b,current]];made=[D for C in raw if (D:=clean(C)) is not None];blocks.append(dict(previous=previous,current=current,a=a,b=b,count=len(made)));clauses.extend(made);previous=current
    return nv,clauses,dict(comparisons=comparisons,blocks=blocks)
