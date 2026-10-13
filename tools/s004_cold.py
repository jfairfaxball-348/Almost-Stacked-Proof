"""S004 cold checker, written before inspecting S003 solver/checker sources.

Full winning-layer predecessor DP and forward closure use independent traversals.
Only Python standard library; labelled configurations, no orbit quotient.
"""
import itertools, json, hashlib, time, sys
from pathlib import Path

def conf(n, t):
    if n == 1:
        yield (t,)
    else:
        for a in range(t+1):
            for rest in conf(n-1, t-a):
                yield (a,) + rest

def arcs(edges):
    return tuple((u,v) for a,b in edges for u,v in ((a,b),(b,a)))

def goal(c, mode):
    return sum(x>0 for x in c)==1 if mode=='stack' else sum(c)==1

def successors(c, edges):
    for u,v in arcs(edges):
        if c[u]>=2:
            d=list(c);d[u]-=2;d[v]+=1
            yield tuple(d)

def closure(c, edges):
    seen={tuple(c)}; queue=[tuple(c)]
    for x in queue:
        for d in successors(x, edges):
            if d not in seen: seen.add(d);queue.append(d)
    return seen

def almost(c):
    return sum(x>=2 for x in c)<=1

def full_layers(n, edges, mode, cap):
    win=set(); out=[]; losses=[]
    for t in range(1,cap+1):
        nextwin={c for c in conf(n,t) if goal(c,mode)}
        for c in win:
            for u,v in arcs(edges):
                if c[v]:
                    d=list(c);d[u]+=2;d[v]-=1;nextwin.add(tuple(d))
        allc=set(conf(n,t));bad=allc-nextwin
        out.append({'t':t,'total':len(allc),'losers':len(bad),
                    'as_losers':sum(almost(c) for c in bad)})
        losses.append(bad);win=nextwin
        if n>=2 and t>n and not bad:break
    return out,losses

def connected(n, edges):
    seen={0}
    while True:
        more=seen|{v for u,v in arcs(edges) if u in seen}
        if more==seen:return len(seen)==n
        seen=more

def bipartite(n, edges):
    colour={0:0}; todo=[0]
    for u in todo:
        for a,b in arcs(edges):
            if a!=u:continue
            if b in colour:
                if colour[b]==colour[u]:return False
            else:colour[b]=1-colour[u];todo.append(b)
    return True

def atlas(n):
    pairs=list(itertools.combinations(range(n),2)); seen=set()
    for mask in range(1<<len(pairs)):
        e=[p for i,p in enumerate(pairs) if mask>>i&1]
        if not connected(n,e):continue
        key=min(tuple(sorted(tuple(sorted((p[u],p[v]))) for u,v in e))
                for p in itertools.permutations(range(n)))
        if key not in seen:seen.add(key);yield list(key)

def digest(states):
    return hashlib.sha256(json.dumps(sorted(states),separators=(',',':')).encode()).hexdigest()

def audit():
    start=time.monotonic();out={'algorithm':'fresh full reverse winning DP + forward closure','core':[],'minimality':[]}
    for name,n,e,c in [('P4',4,[(0,1),(1,2),(2,3)],(1,0,2,9)),
                       ('bull',5,[(0,4),(1,3),(2,3),(2,4),(3,4)],(1,9,0,2,0))]:
        for mode in ['stack','clear']:
            if mode=='clear' and bipartite(n,e):continue
            rows,losses=full_layers(n,e,mode,16);R=closure(c,e)
            assert not any(goal(d,mode) for d in R)
            assert all(d in R for x in R for d in successors(x,e))
            as12={d for d in conf(n,12) if almost(d)}
            assert not(as12 & losses[11]);assert rows[-1]['t']==15 and not losses[-1]
            out['core'].append({'graph':name,'mode':mode,'edges':e,'bipartite':bipartite(n,e),
                'threshold':15,'as12_count':len(as12),'loser':c,'reachable_count':len(R),
                'reachable_sha256':digest(R),'layers':rows})
    for n in range(2,5):
        for e in atlas(n):
            for mode in ['stack','clear']:
                if mode=='clear' and bipartite(n,e):continue
                rows,_=full_layers(n,e,mode,32)
                assert rows[-1]['losers']==0
                gaps=[r['t'] for r in rows if r['t']>=2 and r['losers'] and not r['as_losers']]
                out['minimality'].append({'n':n,'edges':e,'mode':mode,'threshold':rows[-1]['t'],'gaps':gaps})
    out['boundaries']={'K1_stack':2,'K1_all_positive_stacked':True,'K2_stack':3,
                      'zero_goal_stack':False,'zero_goal_clear':False,'one_goal_both':True}
    out['seconds']=time.monotonic()-start
    if '--check-only' not in sys.argv:
        Path('evidence/S004/cold_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'core':[(r['graph'],r['mode'],r['threshold'],r['as12_count'],r['reachable_count']) for r in out['core']],
                      'minimality_failures':[r for r in out['minimality'] if r['gaps']],'seconds':out['seconds']}))

if __name__=='__main__':audit()
