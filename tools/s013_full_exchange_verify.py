"""Independent full exchange coverage, exact chronology and global refinements."""
import functools,json,lzma,sys
from pathlib import Path
B=Path('evidence/S013')
def load(n):
    p=B/n;b=p.read_bytes();return json.loads(lzma.decompress(b) if p.suffix=='.xz' else b)
def main():
    inputs=load('precision_inputs.json');tabs=load('precision_tables.json.xz');reports=load('full_exchange.json');cc=load('full_exchange_counts.json.xz');ff=load('full_exchange_exceptions.json');ext=load('minimal_extrema.json')
    tests=exceptions=checked=move_count=extremizers=0;branches={}
    for g,tab,row in zip(inputs,tabs,reports):
        name,n=g['graph'],g['n'];arcs=sorted({(u,v) for u,v in g['edges']}|{(v,u) for u,v in g['edges']});N={v:{w for u,w in arcs if u==v} for v in range(n)};layers=[{tuple(c):m for c,m in lay} for lay in tab['layers']]
        def masks(c):return layers[sum(c)][tuple(c)]
        actual={(tuple(r['c']),r['s'],r['t'],r['a'],r['goal']):r for r in cc if r['graph']==name};expected=set();bad=[];count=0;localbranches={}
        for layer in layers:
            for c in sorted(layer):
                for s in range(n):
                    for t in range(n):
                        if s==t or c[s]<2 or c[t]>=2 or not N[t].issubset(N[s]):continue
                        for h in range(2,c[s]+1,2):
                            d=list(c);d[s]-=h;d[t]+=h
                            for goal,j in [('stack',1),('clear',0)]:
                                count+=1
                                if masks(d)[j] and not masks(c)[j]:
                                    assert goal=='stack' and sum(c)==3 and c[s]==2 and c[t]==1 and h==2
                                    # Every legal first move leaves two distinct singleton sites.
                                    for u,v in arcs:
                                        if c[u]>=2:
                                            z=list(c);z[u]-=2;z[v]+=1;assert sum(z)==2 and max(z)==1
                                    bad.append(dict(graph=name,c=list(c),d=d,s=s,t=t,a=h//2,goal=goal))
                                elif sum(c)<=8 and masks(d)[j]:expected.add((c,s,t,h//2,goal))
        assert expected==actual.keys() and count==row['tests'] and len(bad)==row['exceptions']
        assert bad==[r for r in ff if r['graph']==name];tests+=count;exceptions+=len(bad)
        for key,r in actual.items():
            c,s,t,a,goal=key;m=r['modified'];q=r['root'];k=r['k'];assert len(m)==len(arcs) and min(m)>=0 and k in ([1] if goal=='clear' else [1,2,3])
            f=[k if v==q else 0 for v in range(n)];balance=f.copy()
            for (u,v),z in zip(arcs,m):balance[u]+=2*z;balance[v]-=z
            assert balance==list(c)
            seen={q};used={v for v,z in enumerate(c) if z}|{q}|{v for e,z in zip(arcs,m) if z for v in e}
            while True:
                more=seen|{u for (u,v),z in zip(arcs,m) if z and v in seen}
                if more==seen:break
                seen=more
            assert used<=seen
            # Independently reconstruct exact-count legality, without redirection or grammar imports.
            visits=0
            @functools.lru_cache(None)
            def search(rem):
                nonlocal visits
                visits+=1;assert visits<=300000
                state=list(c)
                for (u,v),full,left in zip(arcs,m,rem):state[u]-=2*(full-left);state[v]+=full-left
                if not any(rem):return () if state==f else None
                for z,(u,v) in enumerate(arcs):
                    if rem[z] and state[u]>=2:
                        tail=list(rem);tail[z]-=1;ans=search(tuple(tail))
                        if ans is not None:return (z,)+ans
                return None
            order=search(tuple(m));assert order is not None;state=list(c);counts=[0]*len(arcs)
            for z in order:
                u,v=arcs[z];assert state[u]>=2;state[u]-=2;state[v]+=1;counts[z]+=1
            assert state==f and counts==m;move_count+=len(order);checked+=1
            localbranches[r['branch']]=localbranches.get(r['branch'],0)+1;branches[r['branch']]=branches.get(r['branch'],0)+1
        assert localbranches==row['branches']
        for er in [e for e in ext if e['graph']==name]:
            j=1 if er['goal']=='stack' else 0;t=next(t for t in range(n+1,len(layers)) if all(m[j] for m in layers[t].values()))
            losers=[c for c,m in layers[t-1].items() if not m[j]];Q=max(sum(a*a for a in c) for c in losers);qm=[c for c in losers if sum(a*a for a in c)==Q];P=min(sum(len(N[v])*c[v] for v in range(n)) for c in qm);selected=sorted(c for c in qm if sum(len(N[v])*c[v] for v in range(n))==P)
            assert er==dict(graph=name,goal=er['goal'],Q=Q,P=P,selected=[list(c) for c in selected]);extremizers+=len(selected)
            if t-1>=4:
                for c in selected:
                    heavy={v for v in range(n) if c[v]>1}
                    assert all(not N[w]<N[v] for v in heavy for w in range(n))
                    assert all(not N[w]<=N[v] for v in heavy for w in heavy if w!=v)
    result=dict(implications=tests,small_STACK_exceptions=exceptions,CLEAR_exceptions=0,count_reconstructions=checked,literal_moves=move_count,branches=branches,global_selected_extremizers=extremizers,all_equal=True)
    raw=(json.dumps(result,indent=2)+'\n').encode();p=B/'full_exchange_verification.json'
    if '--check-only' in sys.argv:assert p.read_bytes()==raw
    else:p.write_bytes(raw)
    print(json.dumps(result))
if __name__=='__main__':main()
