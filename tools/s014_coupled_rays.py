"""Exact known buffer grammar via off-source ordering and nonnegative shortest paths.

Attaining node=[type,root,vector_index,source_kind,source_count,left,right].
Types:0 leaf(left=label,right=-1);1 two-child move;2 same-root forest join.
Source kind3 is EXACTLY zero, distinct from positive residue0.
"""
import heapq,itertools,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014/coupled_rays')
def kind(a,b):return 3 if a==b==3 else (a%3+b%3)%3
def main():
    ident=sys.argv[1];inputs=json.loads((B/'ray_inputs.json').read_bytes());case=next(c for c in inputs['cases'] if c['id']==ident);g=next(g for g in inputs['graphs'] if g['graph']==case['graph'])
    n=g['n'];s=case['source'];off=[v for v in range(n) if v!=s];vectors=list(itertools.product(*(range(x+1) for x in case['box'])));ix={d:i for i,d in enumerate(vectors)};K=4*n
    if len(vectors)*K>300000:raise RuntimeError('GRAMMAR_CELL_CAP_UNKNOWN')
    neighbors=[[] for _ in range(n)]
    for u,v in g['edges']:neighbors[u].append(v);neighbors[v].append(u)
    for row in neighbors:row.sort()
    C=[[None]*K for _ in vectors];CW=[[None]*K for _ in vectors];S=[[None]*K for _ in vectors];SW=[[None]*K for _ in vectors];nodes=[]
    def improve(V,W,di,v,k,cost,typ,left,right):
        j=v*4+k
        if V[di][j] is not None and V[di][j]<=cost:return False
        if len(nodes)>=2000000:raise RuntimeError('ATTAINING_DAG_NODE_CAP_UNKNOWN')
        W[di][j]=len(nodes);V[di][j]=cost;nodes.append([typ,v,di,k,cost,left,right]);return True
    improve(C,CW,0,s,1,1,0,s,-1)
    for _ in range(K+1):
        changed=False
        for u in range(n):
            for a in range(4):
                x=C[0][4*u+a]
                if x is None:continue
                for b in range(4):
                    y=C[0][4*u+b]
                    if y is None:continue
                    for v in neighbors[u]:changed|=improve(C,CW,0,v,kind(a,b),x+y,1,CW[0][4*u+a],CW[0][4*u+b])
        if not changed:break
    else:raise RuntimeError('PURE_RELAXATION_HEIGHT_UNKNOWN')
    S[0]=C[0].copy();SW[0]=CW[0].copy()
    for _ in range(K+1):
        changed=False
        for v in range(n):
            for a in range(4):
                x=S[0][4*v+a]
                if x is None:continue
                for b in range(4):
                    y=S[0][4*v+b]
                    if y is not None:changed|=improve(S,SW,0,v,kind(a,b),x+y,2,SW[0][4*v+a],SW[0][4*v+b])
        if not changed:break
    else:raise RuntimeError('PURE_FOREST_HEIGHT_UNKNOWN')
    def seeds(V,W,di,parts,forest):
        for ai,bi in parts:
            for u in range(n):
                for a in range(4):
                    x=V[ai][4*u+a]
                    if x is None:continue
                    for b in range(4):
                        y=V[bi][4*u+b]
                        if y is None:continue
                        for v in ([u] if forest else neighbors[u]):improve(V,W,di,v,kind(a,b),x+y,2 if forest else 1,W[ai][4*u+a],W[bi][4*u+b])
    def close(V,W,di,forest):
        heap=[(cost,j) for j,cost in enumerate(V[di]) if cost is not None];heapq.heapify(heap)
        while heap:
            cost,j=heapq.heappop(heap)
            if V[di][j]!=cost:continue
            u,a=divmod(j,4)
            for b in range(4):
                y=V[0][4*u+b]
                if y is None:continue
                for v in ([u] if forest else neighbors[u]):
                    k=kind(a,b)
                    if improve(V,W,di,v,k,cost+y,2 if forest else 1,W[di][j],W[0][4*u+b]):heapq.heappush(heap,(cost+y,4*v+k))
    for di in sorted(range(1,len(vectors)),key=lambda i:(sum(vectors[i]),vectors[i])):
        d=vectors[di]
        if sum(d)==1:
            leaf=off[d.index(1)];improve(C,CW,di,leaf,3,0,0,leaf,-1)
        parts=[]
        for a in itertools.product(*(range(x+1) for x in d)):
            b=tuple(x-y for x,y in zip(d,a))
            if any(a) and any(b) and a<=b:parts.append((ix[a],ix[b]))
        seeds(C,CW,di,parts,False);close(C,CW,di,False)
        S[di]=C[di].copy();SW[di]=CW[di].copy();seeds(S,SW,di,parts,True);close(S,SW,di,True)
    analyses={}
    for goal,V in [('stack',S)]:
        maximum=-1;maxima=[];nonAS=-1;frontier=None
        for di,d in enumerate(vectors):
            def record(N,residue):
                nonlocal maximum,maxima,nonAS,frontier
                c=[0]*n;c[s]=N
                for v,a in zip(off,d):c[v]=a
                mass=sum(c);row=dict(c=c,source_count=N,off_index=di,residue=residue)
                if sum(a>1 for a in c)>1:nonAS=max(nonAS,mass)
                if mass>maximum:maximum=mass;maxima=[row]
                elif mass==maximum:maxima.append(row)
            if not any(V[di][4*v+3] is not None for v in range(n)):record(0,None)
            for r in range(3):
                available=[(V[di][4*v+r],v) for v in range(n) if V[di][4*v+r] is not None]
                if not available:raise RuntimeError('UNBOUNDED_RAY_OR_PROOF_FAILURE')
                minimum,q=min(available);last=minimum-3
                if last>=({0:3,1:1,2:2}[r]):record(last,r)
        maxima.sort(key=lambda r:(r['c'],r['off_index'],r['source_count']))
        positive=next((r for r in maxima if r['source_count']>0),None)
        if positive:
            di=positive['off_index'];r=positive['residue'];cost,q=min((V[di][4*v+r],v) for v in range(n) if V[di][4*v+r] is not None)
            frontier=dict(vector_index=di,kind=r,root=q,source_count=cost,witness=(CW if goal=='clear' else SW)[di][4*q+r])
        analyses[goal]=dict(max_losing_mass=maximum,maximizers=maxima,max_nonAS_losing_mass=nonAS,frontier=frontier)
    result=dict(case=case,graph=g,vectors=vectors,C=C,CW=CW,S=S,SW=SW,nodes=nodes,analysis=analyses,assurance='Exact known grammar; no full general threshold or universal inference.')
    raw=(json.dumps(result,separators=(',',':'))+'\n').encode();dest=B/(ident+'_rays.json.xz')
    if '--check-only' in sys.argv:assert lzma.decompress(dest.read_bytes())==raw
    else:dest.write_bytes(lzma.compress(raw))
    print(json.dumps(dict(case=ident,cells=len(vectors)*K,nodes=len(nodes),analysis={goal:{k:v for k,v in r.items() if k not in ['maximizers','frontier']} for goal,r in analyses.items()})),flush=True)
if __name__=='__main__':main()
