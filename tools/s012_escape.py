"""CAM-S012-02 producer: exact first escape and partial fuel witnesses."""
import collections,json,lzma,sys,time
from pathlib import Path

def read(p):
    raw=Path(p).read_bytes();return json.loads(lzma.decompress(raw) if p.endswith('.xz') else raw)

def main():
    start=time.monotonic();analysis=read('evidence/S012/analysis.json')
    tables=read('evidence/S011/tree_tables.json.xz')+read('evidence/S012/extra_tables.json.xz')
    rows=[];fuel=[];closures=[];all_barriers=0
    for meta,table in zip(analysis['rows'],tables):
        name=meta['graph'];n=meta['n'];edges=meta['edges'];arcs=[(u,v) for a,b in edges for u,v in [(a,b),(b,a)]]
        adj=[sorted({v for u,v in arcs if u==s}) for s in range(n)]
        triangle={(u,v) for u,v in arcs if set(adj[u])&set(adj[v])}
        layers=[{tuple(c):m for c,m in layer} for layer in table['layers']]
        def masks(c):return layers[sum(c)][c]
        def successor(c,u,v):d=list(c);assert d[u]>=2;d[u]-=2;d[v]+=1;return tuple(d)
        def paths(s,t):
            distances={t:0};queue=[t]
            for u in queue:
                for v in adj[u]:
                    if v not in distances:distances[v]=distances[u]+1;queue.append(v)
            def rec(path):
                u=path[-1]
                if u==t:yield path;return
                for v in adj[u]:
                    if distances[v]==distances[u]-1:yield from rec(path+[v])
            yield from rec([s])
        for layer in layers:
            for c,m in layer.items():
                if m[0] or not m[1]:continue
                S=m[3]
                for u,v in arcs:
                    if c[u]>=2 and ((u,v) in triangle or not S>>v&1):
                        assert not masks(successor(c,u,v))[1];all_barriers+=1
        g=meta['thresholds']['clear'];s=meta['thresholds']['stack']
        if g is None:continue
        for c,m in sorted(layers[g-1].items()):
            if m[0] or not m[1]:continue
            S=m[3];distance={c:0};queue=collections.deque([c]);tau=None;forbidden=[]
            while queue:
                x=queue.popleft();assert len(distance)<=300000
                if masks(x)[1]:assert not masks(x)[0] and masks(x)[3]&~S==0
                for u,v in arcs:
                    if x[u]<2:continue
                    d=successor(x,u,v)
                    if (u,v) in triangle or not S>>v&1:
                        assert not masks(d)[1];length=distance[x]+1
                        tau=length if tau is None else min(tau,length)
                        forbidden.append([list(x),u,v,length])
                    if d not in distance:distance[d]=distance[x]+1;queue.append(d)
            if tau is not None:assert sum(c)-tau<s and g-s<=tau
            for x,l in distance.items():
                if l<g-s:assert masks(x)[1]
            rows.append({'graph':name,'c':c,'R3':S,'gap':g-s,'tau':tau,'states':len(distance),'forbidden_moves':len(forbidden)})
            closures.append({'graph':name,'c':c,'distances':sorted(distance.items()),'forbidden':sorted(forbidden)})
            for v in range(n):
                for u in range(n):
                    for path in paths(v,u):
                        d=len(path)-1
                        targets=[]
                        if any((u,w) in triangle for w in adj[u]) and c[v]>=2**(d+1):
                            for w in adj[u]:
                                if (u,w) in triangle:targets.append(('triangle',w,2**(d+1)))
                        if not S>>u&1 and d>=1 and c[v]>=2**d:targets.append(('outside',None,2**d))
                        for kind,w,amount in targets:
                            moves=[]
                            for i in range(d):moves += [[path[i],path[i+1]]]*(amount//(2**(i+1)))
                            if kind=='triangle':moves.append([u,w])
                            state=c
                            for a,b in moves:assert (a,b) in arcs;state=successor(state,a,b)
                            assert len(moves)==amount-1 and not masks(state)[1] and sum(state)<s and g-s<=len(moves)
                            fuel.append({'graph':name,'c':c,'kind':kind,'path':path,'last_neighbor':w,'fuel':amount,'moves':moves,'final':state})
        assert time.monotonic()-start<600
    out={'campaign':'CAM-S012-02','one_step_barriers':all_barriers,'critical':rows,'fuel_witnesses':len(fuel),'fuel_moves':sum(len(x['moves']) for x in fuel)}
    for name,obj in [('escape.json',out),('escape_closures.json.xz',closures),('escape_fuel.json.xz',fuel)]:
        raw=(json.dumps(obj,separators=(',',':'))+'\n').encode();p=Path('evidence/S012')/name
        if '--check-only' in sys.argv:assert (lzma.decompress(p.read_bytes()) if p.suffix=='.xz' else p.read_bytes())==raw
        else:p.write_bytes(lzma.compress(raw) if p.suffix=='.xz' else raw)
    print(json.dumps(out),flush=True)

if __name__=='__main__':main()
