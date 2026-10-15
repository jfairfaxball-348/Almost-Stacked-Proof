"""Independent CAM-S012-01 full reverse masks and literal certificate checker."""
import hashlib,itertools,json,lzma,sys,time
from pathlib import Path

def read(p):
    raw=Path(p).read_bytes()
    return json.loads(lzma.decompress(raw) if p.endswith('.xz') else raw)

def check():
    start=time.monotonic();report=read('evidence/S012/analysis.json')
    tables=read('evidence/S011/tree_tables.json.xz')+read('evidence/S012/extra_tables.json.xz')
    assert [r['graph'] for r in report['rows']]==[r['graph'] for r in tables]
    # Fixed labelled registrations, independent of the producer module.
    expected=[('K2',2,[(0,1)],3),('K3',3,[(0,1),(0,2),(1,2)],4),('P4',4,[(0,1),(1,2),(2,3)],15),
      ('C5',5,[(0,1),(1,2),(2,3),(3,4),(0,4)],10),('triangle_tail2',5,[(0,1),(0,2),(1,2),(0,3),(3,4)],22),
      ('F2',5,[(0,1),(0,2),(1,2),(0,3),(0,4)],13),('bowtie',5,[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)],8),
      ('diamond',4,[(0,1),(0,2),(0,3),(1,2),(2,3)],7),
      ('triangular_prism',6,[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)],14),
      ('bridged_triangles',6,[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(2,3)],14)]
    literal=read('evidence/S012/traces.json.xz');negative=read('evidence/S012/closures.json.xz')
    traces_by={};closures_by={}
    for r in literal:
        key=(r['graph'],tuple(r['c']),r['q'],r['kind']);assert key not in traces_by;traces_by[key]=r
    # A trace can be requested by more than one critical base: allow duplicates if identical.
    trace_keys=set(traces_by);negative_keys=set();configs=relations=moves=0
    for row,table,reg in zip(report['rows'],tables,expected):
        name,n,edges,M=reg;assert row['graph']==name and row['n']==n and row['edges']==[list(e) for e in edges] and row['max_mass']==M
        arcs=[(u,v) for a,b in edges for u,v in [(a,b),(b,a)]]
        neighbors={v:{b for a,b in arcs if a==v} for v in range(n)}
        layers=[]
        for t in range(M+1):
            fresh={}
            for cuts in itertools.combinations(range(t+n-1),n-1):
                marks=(-1,)+cuts+(t+n-1,);c=tuple(marks[i+1]-marks[i]-1 for i in range(n));fresh[c]=[0,0,0,0]
            if t:
                for q in range(n):
                    c=tuple(t if q==v else 0 for v in range(n));fresh[c]=[int(t==1)<<q,1<<q,int(t==2)<<q,int(t==3)<<q]
                for state,masks in layers[-1].items():
                    for u,v in arcs:
                        if state[v]:
                            parent=list(state);parent[v]-=1;parent[u]+=2;value=fresh[tuple(parent)]
                            for j in range(4):value[j]|=masks[j]
            assert len(fresh)<=300000
            assert [[list(c),m] for c,m in sorted(fresh.items())]==table['layers'][t]
            layers.append(fresh);configs+=len(fresh)
        def get(c,j):return layers[sum(c)][tuple(c)][j]
        def plus(c,v,a=1):x=list(c);x[v]+=a;return tuple(x)
        def relation(c,j,q):return q in {v for v in range(n) if get(c,j)&(1<<v)}
        totals={k:0 for k in row['relation_counts']};digest=hashlib.sha256()
        for t in range(M+1):
            for c in sorted(layers[t]):
                if t+2<=M:
                    for w in range(n):
                        for q in range(n):
                            left=relation(plus(c,w),2,q);right=relation(plus(c,q),2,w);assert left==right
                            clear=relation(plus(c,w),0,q);trans=relation(plus(c,q,2),2,w);assert clear==trans
                            digest.update(bytes([left,clear]));totals['two_symmetry']+=1;totals['clear_reflection']+=1
                        target={q for q in range(n) if relation(plus(c,w,2),2,q)}
                        union={q for z in neighbors[w] for q in range(n) if relation(plus(c,z),2,q)}
                        assert target==union;totals['protected_two_normal_form']+=1
                for donor,receiver in itertools.permutations(range(n),2):
                    if c[donor]==0:continue
                    shifted=plus(plus(c,donor,-1),receiver)
                    if t<M:
                        left=relation(shifted,0,donor);assert left==relation(plus(c,donor),2,receiver)
                        totals['unit_clear']+=1;digest.update(bytes([left]))
                    assert relation(shifted,2,donor)==relation(c,2,receiver);totals['unit_two']+=1
                    if c[donor]>1:
                        shifted=plus(plus(c,donor,-2),receiver,2)
                        assert relation(shifted,0,donor)==relation(c,0,receiver);totals['donor_two_clear']+=1
                        assert relation(shifted,2,donor)==relation(plus(c,donor,-1),0,receiver);totals['donor_two_two']+=1
        assert totals==row['relation_counts'] and digest.hexdigest()==row['relation_digest'];relations+=sum(totals.values())
        thresholds={}
        for goal,j in [('stack',1),('clear',0)]:
            good=[t for t in range(n+1,M+1) if all(m[j] for m in layers[t].values())]
            g=min(good) if good else None;thresholds[goal]=g
            if g:assert all(any(m[j]==0 for m in layers[t].values()) for t in range(2,g))
        assert thresholds==row['thresholds'];critical=[]
        for goal,j in [('stack',1),('clear',0)]:
            g=thresholds[goal]
            if g is None:continue
            for c,m in sorted(layers[g-1].items()):
                if m[j]:continue
                D=[get(plus(c,w),2) for w in range(n)]
                assert all(bool(D[w]&(1<<q))==bool(D[q]&(1<<w)) for w,q in itertools.product(range(n),repeat=2))
                roots=set(range(n))
                for d in D:
                    ds={v for v in range(n) if d&(1<<v)};roots&=ds|{v for u in ds for v in neighbors[u]}
                critical.append({'goal':goal,'c':list(c),'D':D,'common_D_neighborhood':sum(1<<q for q in roots),'AS':len([a for a in c if a>=2])<=1,'Q':sum(a*a for a in c),'already_stackable':bool(m[1])})
                for w,q in itertools.product(range(n),repeat=2):
                    if relation(plus(c,w),2,q):assert (name,plus(c,w),q,2) in trace_keys
                negative_keys.add((name,goal,c))
        assert critical==row['critical']
        dynamics=[];barriers=0
        for t in range(M+1):
            for c,m in sorted(layers[t].items()):
                if not m[1] or m[0]:continue
                for u,v in arcs:
                    if c[u]<2:continue
                    d=plus(plus(c,u,-2),v);tri=bool(neighbors[u].intersection(neighbors[v]))
                    if tri:assert get(d,1)==0;barriers+=1
                    if thresholds['clear'] and t==thresholds['clear']-1:
                        gap=thresholds['clear']-thresholds['stack']
                        if gap>=2:assert not tri
                        if tri and gap==1:assert t-1==thresholds['stack']-1 and get(d,1)==0
                        dynamics.append({'c':list(c),'move':[u,v],'triangular':tri,'successor':list(d),'stackable':bool(get(d,1)),'gap':gap})
        assert barriers==row['triangular_barriers'] and dynamics==row['critical_dynamics']
        prefix=[];s=thresholds['stack']
        if s:
            for t in range(s,M+1):
                for c,m in sorted(layers[t].items()):
                    if m[0]:continue
                    found={c};queue=[c];arc_count=0
                    while queue:
                        x=queue.pop();assert get(x,1) and not get(x,0)
                        if sum(x)==s:continue
                        for u,v in arcs:
                            if x[u]<2:continue
                            assert not neighbors[u].intersection(neighbors[v]);arc_count+=1
                            d=plus(plus(x,u,-2),v)
                            if d not in found:found.add(d);queue.append(d)
                    prefix.append({'c':list(c),'states':len(found),'arcs':arc_count})
        assert prefix==row['prefixes']
        for r in (x for x in literal if x['graph']==name):
            state=list(r['c'])
            for u,v in r['moves']:
                assert (u,v) in arcs and state[u]>=2;state[u]-=2;state[v]+=1;moves+=1
            assert state==r['final'] and state[r['q']]==2 and sum(state)==2
        for r in (x for x in negative if x['graph']==name):
            key=(name,r['goal'],tuple(r['c']));assert key in negative_keys and key not in closures_by;closures_by[key]=True
            seen={tuple(r['c'])};todo=[tuple(r['c'])]
            while todo:
                x=todo.pop();assert len(seen)<=300000
                for u,v in arcs:
                    if x[u]>=2:
                        d=plus(plus(x,u,-2),v)
                        if d not in seen:seen.add(d);todo.append(d)
            assert sorted(seen)==[tuple(x) for x in r['states']]
            assert all((sum(x)!=1 if r['goal']=='clear' else len([a for a in x if a])!=1) for x in seen)
        assert time.monotonic()-start<600
    assert set(closures_by)==negative_keys
    model=report['abstract_C6_model'];assert not report['model_is_realized'] and len(model)==6
    for r in model:
        w=r['w'];partner=w+1 if w%2==0 else w-1;C={(partner-1)%6,(partner+1)%6}
        assert r['D']==[partner] and set(r['C'])==C and set(r['S'])==C|{partner} and w in C
        assert w in model[partner]['D'] and w%2!=partner%2
    assert not set.intersection(*(set(r['S']) for r in model))
    out={'graphs':len(tables),'configurations':configs,'relations':relations,'literal_traces':len(literal),'literal_moves':moves,'complete_negative_closures':len(negative),'all_full_masks_and_relations_equal':True}
    p=Path('evidence/S012/verification.json')
    if '--check-only' in sys.argv:assert read(str(p).replace('\\','/'))==out
    else:p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(out),flush=True)

if __name__=='__main__':check()
