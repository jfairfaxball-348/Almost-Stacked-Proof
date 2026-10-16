"""Complete independent production inequalities plus attaining-DAG proof checker."""
import hashlib,itertools,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014/coupled_rays')
def main():
    ident=sys.argv[1];r=json.loads(lzma.decompress((B/(ident+'_rays.json.xz')).read_bytes()));g=r['graph'];case=r['case'];inputs=json.loads((B/'ray_inputs.json').read_bytes())
    assert g==next(g for g in inputs['graphs'] if g['graph']==case['graph']) and case==next(c for c in inputs['cases'] if c['id']==ident)
    n=g['n'];source=case['source'];off=[v for v in range(n) if v!=source];vectors=[tuple(d) for d in r['vectors']];index={d:i for i,d in enumerate(vectors)}
    assert vectors==list(itertools.product(*(range(b+1) for b in case['box']))) and len(vectors)*4*n<=300000
    edges={frozenset(e) for e in g['edges']};neighbors=[{v for v in range(n) if frozenset([u,v]) in edges} for u in range(n)]
    assert all(len(e)==2 for e in edges) and len(edges)==len(g['edges'])
    seen={0};todo=[0];colors={0:0};odd=False
    for u in todo:
        for v in neighbors[u]:
            if v not in seen:seen.add(v);todo.append(v);colors[v]=1-colors[u]
            elif colors[v]==colors[u]:odd=True
    assert len(seen)==n and odd
    minimal=[v for v in range(n) if not any(neighbors[u]<neighbors[v] for u in range(n))]
    orbit_record=next(o for o in inputs['automorphisms'] if o['graph']==g['graph'])
    for p in orbit_record['permutations']:
        assert sorted(p)==list(range(n)) and {frozenset([p[u],p[v]]) for u,v in g['edges']}==edges
    computed=[]
    for rep in [0,2,4]:
        reach={rep}
        for _ in range(n):reach|={p[u] for u in reach for p in orbit_record['permutations']}
        computed.append(sorted(reach))
    assert computed==orbit_record['orbits'] and set().union(*map(set,computed))==set(range(n))
    def addkind(a,b):
        if a==3 and b==3:return 3
        return ((0 if a==3 else a)+(0 if b==3 else b))%3
    nodes=r['nodes'];assert len(nodes)<=2000000;output=[]
    for i,node in enumerate(nodes):
        typ,v,di,k,cost,a,b=node;assert typ in [0,1,2] and 0<=v<n and 0<=di<len(vectors) and k in range(4) and isinstance(cost,int) and cost>=0
        assert (cost==0 if k==3 else cost>0 and cost%3==k)
        if typ==0:
            assert a==v and b==-1
            d=tuple(int(w==v) for w in off);wanted_cost=int(v==source)
            assert vectors[di]==d and cost==wanted_cost and k==(1 if v==source else 3);output.append(1)
        else:
            assert 0<=a<i and 0<=b<i
            A=nodes[a];C=nodes[b]
            assert tuple(x+y for x,y in zip(vectors[A[2]],vectors[C[2]]))==vectors[di] and A[4]+C[4]==cost and addkind(A[3],C[3])==k
            if typ==1:assert A[1]==C[1] and A[1] in neighbors[v] and output[a]==output[b]==1;output.append(1)
            else:assert A[1]==C[1]==v;output.append(output[a]+output[b])
    for name,witness in [('C','CW'),('S','SW')]:
        V=r[name];W=r[witness];assert len(V)==len(W)==len(vectors)
        for di,(values,ws) in enumerate(zip(V,W)):
            assert len(values)==len(ws)==4*n
            for j,value in enumerate(values):
                if value is None:assert ws[j] is None;continue
                assert isinstance(value,int) and value>=0 and ws[j] in range(len(nodes));node=nodes[ws[j]];v,k=divmod(j,4)
                assert node[1:5]==[v,di,k,value]
                if name=='C':assert output[ws[j]]==1
    def at(V,d,v,k):return r[V][index[d]][4*v+k]
    zero=(0,)*(n-1)
    assert at('C',zero,source,1)<=1
    for v in off:
        d=tuple(int(w==v) for w in off);assert at('C',d,v,3)==0
    inequalities=0
    def bound(parent,cost):
        nonlocal inequalities
        inequalities+=1;assert parent is not None and parent<=cost
    for di,d in enumerate(vectors):
        for j,x in enumerate(r['C'][di]):
            if x is not None:bound(r['S'][di][j],x)
        # Includes BOTH zero/nonzero splits and all proper splits, unlike optimizer ordering.
        for a in itertools.product(*(range(x+1) for x in d)):
            b=tuple(x-y for x,y in zip(d,a));ai=index[a];bi=index[b]
            for u in range(n):
                for ka in range(4):
                    for kb in range(4):
                        k=addkind(ka,kb)
                        x=r['C'][ai][4*u+ka];y=r['C'][bi][4*u+kb]
                        if x is not None and y is not None:
                            for v in neighbors[u]:bound(r['C'][di][4*v+k],x+y)
                        x=r['S'][ai][4*u+ka];y=r['S'][bi][4*u+kb]
                        if x is not None and y is not None:bound(r['S'][di][4*u+k],x+y)
    analyses={};traces=[];literal_moves=0
    for goal,V in [('stack',r['S'])]:
        all_losers=[]
        for di,d in enumerate(vectors):
            if all(V[di][4*q+3] is None for q in range(n)):
                c=[0]*n
                for v,a in zip(off,d):c[v]=a
                all_losers.append((sum(c),c,0,di,None))
            for residue in range(3):
                possible=[V[di][4*q+residue] for q in range(n) if V[di][4*q+residue] is not None];assert possible
                last=min(possible)-3
                if last>0:
                    assert last%3==residue;c=[0]*n;c[source]=last
                    for v,a in zip(off,d):c[v]=a
                    all_losers.append((sum(c),c,last,di,residue))
        maxmass=max(t[0] for t in all_losers);selected=sorted([t for t in all_losers if t[0]==maxmass],key=lambda t:(t[1],t[3],t[2]))
        maximizers=[dict(c=c,source_count=N,off_index=di,residue=residue) for mass,c,N,di,residue in selected]
        nonAS=max((mass for mass,c,*_ in all_losers if len([v for v in c if v>=2])>1),default=-1)
        assert r['analysis'][goal]['max_losing_mass']==maxmass and r['analysis'][goal]['maximizers']==maximizers and r['analysis'][goal]['max_nonAS_losing_mass']==nonAS
        frontier=r['analysis'][goal]['frontier']
        if frontier is not None:
            witness=frontier['witness'];node=nodes[witness];assert node[1:5]==[frontier['root'],frontier['vector_index'],frontier['kind'],frontier['source_count']]
            d=vectors[frontier['vector_index']];start=[0]*n;start[source]=frontier['source_count']
            for v,a in zip(off,d):start[v]=a
            state=start.copy();stack=[(witness,False)];moves=[]
            while stack:
                i,ready=stack.pop();typ,v,di,k,cost,a,b=nodes[i]
                if typ==0:continue
                if not ready:stack.extend([(i,True),(b,False),(a,False)]);continue
                if typ==1:
                    u=nodes[a][1];assert u in neighbors[v] and state[u]>=2;state[u]-=2;state[v]+=1;moves.append([u,v])
                    if len(moves)>300000:raise RuntimeError('LITERAL_TRACE_CAP_UNKNOWN')
            wanted=[output[witness] if v==frontier['root'] else 0 for v in range(n)]
            assert state==wanted and sum(state)>=1
            if goal=='clear':assert sum(state)==1
            assert len(moves)==sum(start)-sum(state)
            traces.append(dict(goal=goal,start=start,moves=moves,final=state));literal_moves+=len(moves)
        analyses[goal]=dict(max_losing_mass=maxmass,max_nonAS_losing_mass=nonAS,maximizers=maximizers)
    result=dict(case=ident,cells=len(vectors)*4*n,nodes=len(nodes),production_inequalities=inequalities,literal_moves=literal_moves,graph_minimal_neighborhoods=minimal,analysis=analyses,frontier_traces=traces,all_minima_and_infinities_certified=True)
    raw=(json.dumps(result,separators=(',',':'))+'\n').encode();p=B/(ident+'_verification.json.xz')
    if '--check-only' in sys.argv:assert lzma.decompress(p.read_bytes())==raw
    else:p.write_bytes(lzma.compress(raw))
    print(json.dumps({k:v for k,v in result.items() if k not in ['analysis','frontier_traces']}),flush=True)
if __name__=='__main__':main()
