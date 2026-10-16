"""Producer-only guarded prefix construction; separate truth-table verifier."""
import itertools
def build(n,patterns):
    pairs=list(itertools.combinations(range(n),2));vid={e:i+1 for i,e in enumerate(pairs)};m=len(pairs);selectors=list(range(m+1,m+len(patterns)+1));nv=selectors[-1];fixed=[selectors.copy()]+[[-a,-b] for a,b in itertools.combinations(selectors,2)];selector_count=len(fixed);comparisons=[];blocks=[]
    def clean(C):
        S=set(C)
        if any(-v in S for v in S):return None
        return sorted(S)
    for index,c in enumerate(patterns):
        sel=selectors[index]
        for value in sorted(set(c)):
            group=[v for v,z in enumerate(c) if z==value]
            if len(group)<2:continue
            u,v=group[:2];perm=list(range(n));perm[u],perm[v]=v,u;nv+=1;prev=nv;fixed.append([prev]);comparisons.append(dict(pattern=index,swap=[u,v],prefix0=prev,first_block=len(blocks)))
            for i,(s,t) in enumerate(pairs):
                a=i+1;b=vid[tuple(sorted((perm[s],perm[t])))];nv+=1;cur=nv;raw=[[-sel,-prev,-a,b],[-cur,prev],[-cur,-a,b],[-cur,a,-b],[-prev,-a,-b,cur],[-prev,a,b,cur]];made=[D for C in raw if (D:=clean(C)) is not None];blocks.append(dict(pattern=index,selector=sel,previous=prev,current=cur,a=a,b=b,count=len(made)));fixed.extend(made);prev=cur
    return nv,selectors,fixed,dict(selector_clause_count=selector_count,comparisons=comparisons,blocks=blocks)
