"""Independent reverse predecessor propagation and complete diagnostic checking."""
import itertools,json,lzma,math,sys
from pathlib import Path

BASE=Path('evidence/S013')
def load(n):
    p=BASE/n;b=p.read_bytes();return json.loads(lzma.decompress(b) if p.suffix=='.xz' else b)
def compositions(n,t):
    for cuts in itertools.combinations(range(t+n-1),n-1):
        z=(-1,)+cuts+(t+n-1,);yield tuple(z[i+1]-z[i]-1 for i in range(n))

def main():
    inputs=load('precision_inputs.json');saved=load('precision.json');tables=load('precision_tables.json.xz');certs=load('precision_certificates.json.xz')
    configs=relations=edges_checked=bad=criticalbad=closures=moves=0;keys=set();gapshadows=0
    for g,row,tab in zip(inputs,saved,tables):
        name,n,M=g['graph'],g['n'],g['max_mass'];assert row['graph']==tab['graph']==name
        edges={tuple(sorted(e)) for e in g['edges']};arcs=sorted(edges|{(v,u) for u,v in edges});rev=[]
        for t in range(M+1):
            current={c:[0,0,0,0] for c in compositions(n,t)};assert len(current)==math.comb(t+n-1,n-1)<=300000
            if t:
                for q in range(n):
                    c=tuple(t if q==v else 0 for v in range(n));current[c][1]=1<<q
                    for index,mass in [(0,1),(2,2),(3,3)]:
                        if t==mass:current[c][index]=1<<q
            if t:
                for d,mask in rev[-1].items():
                    for u,v in arcs:
                        if d[v]:
                            c=list(d);c[v]-=1;c[u]+=2;c=tuple(c)
                            for j in range(4):current[c][j]|=mask[j]
            wanted={tuple(c):m for c,m in tab['layers'][t]};assert current==wanted,(name,t);configs+=len(current);rev.append(current)
        assert len(tab['layers'])==M+1
        def val(c):return rev[sum(c)][tuple(c)]
        def minus(c,w):d=list(c);d[w]-=1;return tuple(d)
        thresholds={}
        for goal,index in [('stack',1),('clear',0)]:
            ts=[t for t in range(n+1,M+1) if all(m[index] for m in rev[t].values())];thresholds[goal]=min(ts) if ts else None
            if ts:assert all(any(not m[index] for m in rev[t].values()) for t in range(2,min(ts)))
        assert row['thresholds']==thresholds
        first=cf=None;bad_here=cb_here=checks=rel=0
        for t in range(M+1):
            for x in sorted(rev[t]):
                m=val(x)
                if t<M:
                    for q in range(n):
                        y=list(x);y[q]+=1
                        assert bool(m[2]&(1<<q))==bool(val(y)[3]);rel+=1
                if m[3]:assert all(m[3]&(1<<w) for w in range(n) if x[w])
                if not m[1]:continue
                lost={w for w in range(n) if x[w]>0 and not val(minus(x,w))[1]}
                for u,v in g['edges']:
                    checks+=1
                    if {u,v}<=lost:
                        r=dict(graph=name,x=list(x),edge=[u,v],deletions=[list(minus(x,u)),list(minus(x,v))],threshold_layer=t==thresholds['stack'])
                        bad_here+=1
                        if first is None:first=r
                        if r['threshold_layer']:
                            cb_here+=1
                            if cf is None:cf=r
        assert row['first']==first and row['threshold_first']==cf and row['adjacent_deletion_failures']==bad_here and row['threshold_adjacent_failures']==cb_here and row['adjacent_tests']==checks and row['three_relation_checks']==rel
        assert row['configurations']==sum(map(len,rev));bad+=bad_here;criticalbad+=cb_here;edges_checked+=checks;relations+=rel
        extrema=[]
        for goal,j in [('stack',1),('clear',0)]:
            t=thresholds[goal]
            if not t:continue
            losing=sorted(x for x,m in rev[t-1].items() if not m[j]);q=max(sum(a*a for a in c) for c in losing)
            extrema.append(dict(goal=goal,threshold=t,losers=len(losing),AS_losers=sum(sum(a>1 for a in c)<=1 for c in losing),Qmax=q,maxima=[list(c) for c in losing if sum(a*a for a in c)==q]))
        assert row['extrema']==extrema
        expected=[]
        if thresholds['clear'] and thresholds['clear']==thresholds['stack']+1:
            for x in sorted(rev[thresholds['stack']]):
                if val(x)[0]:continue
                nonstack=[];asnonstack=[]
                for u,v in arcs:
                    if x[u]>=2:
                        y=list(x);y[u]-=2;y[v]+=1
                        if not val(y)[1]:
                            nonstack.append([u,v,y])
                            if sum(a>1 for a in y)<=1:asnonstack.append([u,v,y])
                expected.append(dict(c=list(x),AS=sum(a>1 for a in x)<=1,nonstacking_first_moves=nonstack,AS_nonstacking_first_moves=asnonstack))
        assert expected==row['gap1_shadows'];gapshadows+=len(expected)
        for cert in [c for c in certs if c['diagnostic']['graph']==name]:
            r=cert['diagnostic'];assert r==first or r==cf;keys.add((name,tuple(r['x']),tuple(r['edge'])))
            cur=list(r['x'])
            for u,v in cert['moves']:
                assert (u,v) in arcs and cur[u]>=2;cur[u]-=2;cur[v]+=1;moves+=1
            assert cur==cert['final'] and sum(a>0 for a in cur)==1 and sum(cur)>0
            for negative,initial in zip(cert['negative'],r['deletions']):
                assert negative['c']==initial;states={tuple(s) for s in negative['states']};assert len(states)==len(negative['states']) and tuple(initial) in states and len(states)<=300000
                reachable={tuple(initial)};todo=[tuple(initial)]
                for x in todo:
                    assert sum(a>0 for a in x)!=1
                    for u,v in arcs:
                        if x[u]>=2:
                            y=list(x);y[u]-=2;y[v]+=1;y=tuple(y);assert y in states
                            if y not in reachable:reachable.add(y);todo.append(y)
                assert reachable==states;closures+=len(states)
        expectedkeys={(name,tuple(r['x']),tuple(r['edge'])) for r in [first,cf] if r}
        assert {k for k in keys if k[0]==name}==expectedkeys
    assert len(inputs)==len(saved)==len(tables)==11
    result=dict(graphs=11,configurations=configs,three_relations=relations,adjacent_tests=edges_checked,adjacent_failures=bad,threshold_adjacent_failures=criticalbad,gap1_critical_losers=gapshadows,negative_closure_states=closures,literal_moves=moves,all_full_masks_and_diagnostics_equal=True)
    p=BASE/'precision_verification.json';b=(json.dumps(result,indent=2)+'\n').encode()
    if '--check-only' in sys.argv:assert p.read_bytes()==b
    else:p.write_bytes(b)
    print(json.dumps(result))

if __name__=='__main__':main()
