"""Independent exhaustive implication/coverage, fixed-count DFS and closure validation."""
import functools,json,lzma,sys
from pathlib import Path

ROOT=Path('evidence/S013')
def read(name):
    p=ROOT/name;b=p.read_bytes();return json.loads(lzma.decompress(b) if p.suffix=='.xz' else b)
def main():
    inputs=read('precision_inputs.json');tabs=read('precision_tables.json.xz');rows=read('concentration.json');certs=read('concentration_counts.json.xz');fails=read('concentration_failures.json.xz');gaps=read('gap1_certificates.json.xz')
    total_tests=closedtests=closedbad=countchecks=literal_moves=closure_states=gap_successors=0
    for g,tab,row in zip(inputs,tabs,rows):
        name,n=g['graph'],g['n'];arcs=sorted({(u,v) for u,v in g['edges']}|{(v,u) for u,v in g['edges']});neighbors={v:{w for a,w in arcs if a==v} for v in range(n)}
        layers=[{tuple(c):m for c,m in lay} for lay in tab['layers']]
        def mask(c,j):return layers[sum(c)][tuple(c)][j]
        actual={(tuple(r['c']),r['s'],r['t'],r['a'],r['goal']):r for r in certs if r['graph']==name};assert len(actual)==row['count_certificates']
        expected=set();first={};op=cl=bad=0
        for layer in layers:
            for x in sorted(layer):
                heavy=[v for v in range(n) if x[v]>1]
                for s in heavy:
                    for t in heavy:
                        if s==t:continue
                        openok=all((s,v) in arcs for v in neighbors[t]);closeok=(s,t) in arcs and all(v==s or (s,v) in arcs for v in neighbors[t])
                        if not openok and not closeok:continue
                        for h in range(2,x[s]+1,2):
                            y=list(x);y[s]-=h;y[t]+=h
                            for goal,j in [('stack',1),('clear',0)]:
                                win=bool(mask(y,j));original=bool(mask(x,j))
                                if openok:
                                    op+=1;assert not win or original
                                    if sum(x)<=8 and win:expected.add((x,s,t,h//2,goal))
                                if closeok:
                                    cl+=1
                                    if win and not original:
                                        bad+=1
                                        if goal not in first:first[goal]=dict(graph=name,c=list(x),d=y,s=s,t=t,a=h//2,goal=goal)
        assert expected==actual.keys();assert (op,cl,bad)==(row['open_tests'],row['closed_tests'],row['closed_failures']) and list(first.values())==row['first']
        total_tests+=op;closedtests+=cl;closedbad+=bad
        for key,r in actual.items():
            x,s,t,a,goal=key;d=list(x);d[s]-=2*a;d[t]+=2*a;assert d==r['d'];q,k=r['q'],r['k'];assert k in ([1] if goal=='clear' else [1,2,3])
            m=r['m'];mm=r['modified'];assert min(m)>=0 and min(mm)>=0
            f=[k if v==q else 0 for v in range(n)]
            def equation(vv,counts):
                v=f.copy()
                for (u,w),z in zip(arcs,counts):v[u]+=2*z;v[w]-=z
                assert list(vv)==v
                used={q}|{v for v,z in enumerate(vv) if z}|{v for e,z in zip(arcs,counts) if z for v in e};reach={q}
                while True:
                    more=reach|{u for (u,w),z in zip(arcs,counts) if z and w in reach}
                    if more==reach:break
                    reach=more
                assert used<=reach
            equation(d,m);equation(x,mm)
            pos=t;seen={t}
            for z in r['path']:
                u,v=arcs[z];assert u==pos and m[z]>0 and v not in seen;pos=v;seen.add(v)
            assert pos==q and (r['path'] or q==t)
            needed=m.copy();removed=0
            for z,amount in r['redirect']:
                u,v=arcs[z];assert u==t and amount>0 and (s,v) in arcs
                needed[z]-=amount;needed[arcs.index((s,v))]+=amount;removed+=amount
            assert removed==a and needed==mm
            if q!=t:assert mm[r['path'][0]]>=1
            # Complete independently written fixed-count chronology. No producer scheduling import.
            explored=0
            @functools.lru_cache(None)
            def solve(rem):
                nonlocal explored
                explored+=1;assert explored<=300000
                state=list(x)
                for (u,v),full,left in zip(arcs,mm,rem):state[u]-=2*(full-left);state[v]+=full-left
                if not any(rem):return () if state==f else None
                for z,(u,v) in enumerate(arcs):
                    if rem[z] and state[u]>=2:
                        rr=list(rem);rr[z]-=1;tail=solve(tuple(rr))
                        if tail is not None:return (z,)+tail
                return None
            trace=solve(tuple(mm));assert trace is not None;state=list(x);usage=[0]*len(arcs)
            for z in trace:
                u,v=arcs[z];assert state[u]>=2;state[u]-=2;state[v]+=1;usage[z]+=1
            assert state==f and usage==mm;literal_moves+=len(trace);countchecks+=1
        def check_trace(tr):
            nonlocal literal_moves
            cur=tr['c'].copy()
            for u,v in tr['moves']:
                assert (u,v) in arcs and cur[u]>=2;cur[u]-=2;cur[v]+=1;literal_moves+=1
            assert cur==tr['final'] and sum(a>0 for a in cur)==1 and sum(cur)>0
            if tr['kind']==0:assert sum(cur)==1
        def check_negative(c,states,goal):
            nonlocal closure_states
            ss={tuple(x) for x in states};assert len(ss)==len(states)<=300000 and tuple(c) in ss;reachable={tuple(c)};todo=[tuple(c)]
            for cur in todo:
                if goal=='stack':assert sum(a>0 for a in cur)!=1
                else:assert sum(cur)!=1
                for u,v in arcs:
                    if cur[u]>=2:
                        d=list(cur);d[u]-=2;d[v]+=1;d=tuple(d);assert d in ss
                        if d not in reachable:reachable.add(d);todo.append(d)
            assert reachable==ss;closure_states+=len(ss)
        selected=[r for r in fails if r['diagnostic']['graph']==name];assert [r['diagnostic'] for r in selected]==list(first.values())
        for r in selected:check_trace(r['positive']);check_negative(r['diagnostic']['c'],r['negative'],r['diagnostic']['goal'])
        for r in [r for r in gaps if r['graph']==name]:
            check_negative(r['c'],r['negative'],'clear');expected={(u,v) for u,v in arcs if r['c'][u]>=2};assert expected=={tuple(t['move']) for t in r['successors']}
            for tr in r['successors']:
                u,v=tr['move'];d=r['c'].copy();d[u]-=2;d[v]+=1;assert tr['trace']['c']==d;check_trace(tr['trace']);gap_successors+=1
    result=dict(open_implications=total_tests,adjacent_closed_tests=closedtests,adjacent_closed_failures=closedbad,reconstructed_counts=countchecks,literal_moves=literal_moves,negative_closure_states=closure_states,gap1_inputs=len(gaps),gap1_first_successors=gap_successors,all_equal=True)
    raw=(json.dumps(result,indent=2)+'\n').encode();p=ROOT/'concentration_verification.json'
    if '--check-only' in sys.argv:assert p.read_bytes()==raw
    else:p.write_bytes(raw)
    print(json.dumps(result))
if __name__=='__main__':main()
