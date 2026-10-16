"""CAM-S014-02: capacitated whole-family certificates and competing CLEAR bridge."""
import hashlib,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014')
def load(p):
    p=Path(p);raw=p.read_bytes();return json.loads(lzma.decompress(raw) if p.suffix=='.xz' else raw)
def save(p,obj):
    p=B/p;raw=(json.dumps(obj,separators=(',',':'))+'\n').encode()
    if '--check-only' in sys.argv:assert (lzma.decompress(p.read_bytes()) if p.suffix=='.xz' else p.read_bytes())==raw
    else:p.write_bytes(lzma.compress(raw) if p.suffix=='.xz' else raw)

def flow(donors,demand,N,capacity):
    n=len(N);source=2*n;sink=source+1;C=[[0]*(2*n+2) for _ in range(2*n+2)];original={}
    for s in donors:
        C[source][s]=demand[s]
        for v in N[s]:C[s][n+v]=sum(demand.values());original[s,v]=C[s][n+v]
    for v in range(n):C[n+v][sink]=capacity[v]
    total=0
    while True:
        parent={source:None};queue=[source]
        for u in queue:
            if sink in parent:break
            for v,a in enumerate(C[u]):
                if a and v not in parent:parent[v]=u;queue.append(v)
        if sink not in parent:break
        u=sink;amount=10**9
        while parent[u] is not None:amount=min(amount,C[parent[u]][u]);u=parent[u]
        u=sink
        while parent[u] is not None:v=parent[u];C[v][u]-=amount;C[u][v]+=amount;u=v
        total+=amount
    assignment=[[s,v,z-C[s][n+v]] for (s,v),z in sorted(original.items()) if z-C[s][n+v]]
    return total,assignment

def critical(inp):
    m=load(inp['clear']);sm=load(inp['stack']) if inp['stack'] else {}
    if sm.get('scope')!='EXACT_THRESHOLD' or m['threshold']<=sm['threshold']:return None
    with lzma.open(inp['certificate'],'rb') as f:
        while h:=f.read(12):
            mass=int.from_bytes(h[:4],'little');count=int.from_bytes(h[4:],'little');remaining=count*16
            if mass==m['threshold']-1:
                if count>300000:return dict(graph=m['graph'],status='STATE_CAP_UNKNOWN')
                raw=f.read(remaining);assert len(raw)==remaining
                cs=sorted(tuple((int.from_bytes(raw[i:i+16],'little')>>(8*v))&255 for v in range(m['n'])) for i in range(0,len(raw),16))
                N=[set() for _ in range(m['n'])]
                for u,v in m['edges']:N[u].add(v);N[v].add(u)
                tri={u for u in range(m['n']) if any(N[u]&N[v] for v in N[u])}
                return dict(graph=m['graph'],status='COMPLETE',gap=m['threshold']-sm['threshold'],critical_count=len(cs),triangle_heavy_failures=[c for c in cs if any(c[v]>=2 for v in tri)])
            while remaining:part=f.read(min(remaining,65536));assert part;remaining-=len(part)
    raise AssertionError(m['graph'])

def main():
    for p,h in load(B/'family_inputs.json').items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    graphs=load('evidence/S013/precision_inputs.json');tables=load('evidence/S013/precision_tables.json.xz');meta=load('evidence/S013/precision.json')
    allcases=[];trirows=[];certs=[]
    for g,table,metadata in zip(graphs,tables,meta):
        n=g['n'];arcs=sorted((u,v) for e in g['edges'] for u,v in [e,e[::-1]]);index={a:i for i,a in enumerate(arcs)};N=[set() for _ in range(n)]
        for u,v in arcs:N[u].add(v)
        layers=[{tuple(c):mask for c,mask in layer} for layer in table['layers']]
        def val(c):return layers[sum(c)][tuple(c)]
        def trace(start,k,q):
            kind={1:0,2:2,3:3}[k];x=tuple(start);m=[0]*len(arcs);moves=[]
            while not (x[q]==k and sum(x)==k):
                for z,(u,v) in enumerate(arcs):
                    if x[u]<2:continue
                    y=list(x);y[u]-=2;y[v]+=1;y=tuple(y)
                    if val(y)[kind]>>q&1:break
                else:raise AssertionError(x)
                moves.append([u,v]);m[z]+=1;x=y
            return m,moves
        cases=[];failures=[];tested=0
        for mass,layer in enumerate(layers):
            for goal,j in [('clear',0),('stack',1)]:
                control=next((c for c in sorted(layer) if layer[c][j] and sum(x>=2 for x in c)>=3),None)
                for c in sorted(layer):
                    if sum(x>=2 for x in c)<3 or (layer[c][j] and c!=control):continue
                    heavy=[v for v in range(n) if c[v]>=2]
                    for t in heavy:
                        donors=[s for s in heavy if s!=t];d=list(c);dem={s:c[s]//2 for s in donors}
                        for s,a in dem.items():d[s]-=2*a;d[t]+=2*a
                        if not val(d)[j]:continue
                        k,q=next((k,q) for k,kind in ([(1,0)] if j==0 else [(1,0),(2,2),(3,3)]) for q in range(n) if val(d)[kind]>>q&1)
                        counts,moves=trace(d,k,q)
                        reach={q};change=True
                        while change:
                            more=reach|{u for (u,v),z in zip(arcs,counts) if z and u!=t and v in reach};change=more!=reach;reach=more
                        protected=[None] if q==t else [v for v in sorted(N[t]) if counts[index[t,v]] and v in reach]
                        assert protected
                        choices=[]
                        for reserve in protected:
                            b=[counts[index[t,v]]-(reserve==v) if v in N[t] else 0 for v in range(n)]
                            value,assignment=flow(donors,dem,N,b);deficits=[]
                            for bits in range(1,1<<len(donors)):
                                U=[s for i,s in enumerate(donors) if bits>>i&1];heads=set().union(*(N[s] for s in U));deficit=sum(dem[s] for s in U)-sum(b[v] for v in heads)
                                if deficit>0:deficits.append([U,sorted(heads),deficit])
                            assert bool(deficits)==(value<sum(dem.values()))
                            modified=None
                            if not deficits:
                                assert layer[c][j]
                                modified=counts.copy()
                                for s,v,a in assignment:modified[index[t,v]]-=a;modified[index[s,v]]+=a
                                assert min(modified)>=0
                            choices.append(dict(reserve=reserve,capacity=b,value=value,assignment=assignment,deficits=deficits,modified=modified))
                        cases.append(dict(graph=g['graph'],goal=goal,c=c,original_wins=bool(layer[c][j]),t=t,donors=donors,d=d,k=k,q=q,counts=counts,moves=moves,choices=choices))
                        if len(cases)>300000:raise RuntimeError('MATCHING_CASE_CAP_UNKNOWN')
            clear_losers=[c for c,m in layer.items() if not m[0]];Q=max((sum(a*a for a in c) for c in clear_losers),default=-1)
            for c in sorted(clear_losers):
                if mass<4 or not val(c)[1]:continue
                transfer=[]
                for u,v in arcs:
                    if c[u]<2 or not N[u]&N[v]:continue
                    for a in [1,2]:
                        d=list(c);d[u]-=a;d[v]+=a;transfer.append([u,v,a,d,bool(val(d)[1])])
                if not transfer:continue
                tested+=1
                if all(z[-1] for z in transfer):
                    failures.append(dict(c=c,mass=mass,Qmax=sum(a*a for a in c)==Q,critical=mass==metadata['thresholds']['clear']-1 if metadata['thresholds']['clear'] else None,transfers=transfer))
        if failures:
            row=failures[0];start=tuple(row['c']);states={start};todo=[start]
            for c in todo:
                if len(states)>300000:raise RuntimeError('CLOSURE_STATE_CAP_UNKNOWN')
                assert sum(c)!=1
                for u,v in arcs:
                    if c[u]>=2:
                        d=list(c);d[u]-=2;d[v]+=1;d=tuple(d)
                        if d not in states:states.add(d);todo.append(d)
            traces=[]
            for u,v,a,d,_ in row['transfers']:
                k,q=next((k,q) for k,kind in [(1,0),(2,2),(3,3)] for q in range(n) if val(d)[kind]>>q&1)
                counts,moves=trace(d,k,q);traces.append(dict(u=u,v=v,a=a,d=d,k=k,q=q,moves=moves))
            certs.append(dict(graph=g['graph'],c=start,states=sorted(states),transfer_traces=traces))
        allcases.extend(cases);trirows.append(dict(graph=g['graph'],tested=tested,failures=failures,thresholds=metadata['thresholds']))
        print(json.dumps(dict(graph=g['graph'],matching_cases=len(cases),transfer_tests=tested,transfer_failures=len(failures))),flush=True)
    archive=[]
    for inp in load(B/'gap_inputs.json'):
        for p,h in inp['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
        row=critical(inp)
        if row:archive.append(row)
    save('family_counts.json.xz',allcases);save('triangular_transfer.json.xz',dict(rows=trirows,certificates=certs,archive=archive))
    summary=dict(matching_cases=len(allcases),reservations=sum(len(c['choices']) for c in allcases),reconstructions=sum(z['modified'] is not None for c in allcases for z in c['choices']),losing_originals=sum(not c['original_wins'] for c in allcases),transfer_tests=sum(r['tested'] for r in trirows),transfer_failures=sum(len(r['failures']) for r in trirows),negative_closures=len(certs),archive_positive_cases=len(archive),archive_triangle_heavy=sum(len(r.get('triangle_heavy_failures',[])) for r in archive))
    save('family_summary.json',summary);print(json.dumps(summary),flush=True)
if __name__=='__main__':main()
