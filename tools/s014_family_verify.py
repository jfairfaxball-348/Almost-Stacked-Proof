"""Independent Hall/min-cut, complete fixed-count chronology and closure checker."""
import functools,hashlib,itertools,json,lzma,struct,sys
from pathlib import Path
B=Path('evidence/S014')
def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(lzma.decompress(b) if p.suffix=='.xz' else b)
def main():
    for p,h in read(B/'family_inputs.json').items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    cases=read(B/'family_counts.json.xz');tr=read(B/'triangular_transfer.json.xz');summary=read(B/'family_summary.json')
    graphs=read('evidence/S013/precision_inputs.json');tables=read('evidence/S013/precision_tables.json.xz');metadata=read('evidence/S013/precision.json')
    required=set();actual=set();reconstructed=literal=negative_states=proper_deficiencies=0;visits_max=0
    for graph,table,meta,row in zip(graphs,tables,metadata,tr['rows']):
        name,n=graph['graph'],graph['n'];E={tuple(e) for e in graph['edges']};arcs=sorted(E|{(v,u) for u,v in E});idx={p:i for i,p in enumerate(arcs)}
        edge=lambda a,b:(a,b) in idx
        degree=[sum(edge(v,u) for u in range(n)) for v in range(n)]
        ta={(a,b) for a,b in arcs if any(edge(a,z) and edge(b,z) for z in range(n))}
        layers=[{tuple(c):m for c,m in layer} for layer in table['layers']]
        def masks(c):return layers[sum(c)][tuple(c)]
        for layer in layers:
            eligible=sorted(c for c in layer if len([a for a in c if a>1])>=3)
            for goal,j in [('stack',1),('clear',0)]:
                first=next((c for c in eligible if layer[c][j]),None)
                for c in eligible:
                    if layer[c][j] and c!=first:continue
                    for t in range(n):
                        if c[t]<2:continue
                        d=[a%2 if v!=t and a>1 else a for v,a in enumerate(c)];d[t]+=sum(c[v]-d[v] for v in range(n) if v!=t)
                        if masks(d)[j]:required.add((name,goal,c,t))
        for case in (r for r in cases if r['graph']==name):
            c=tuple(case['c']);t=case['t'];key=(name,case['goal'],c,t);assert key not in actual;actual.add(key)
            donors=[v for v in range(n) if v!=t and c[v]>1];assert donors==case['donors']
            d=list(c)
            for s in donors:d[s]-=2*(c[s]//2);d[t]+=2*(c[s]//2)
            assert d==case['d'];j=0 if case['goal']=='clear' else 1
            assert case['original_wins']==bool(masks(c)[j])
            possibilities=[(k,q) for k,index in ([(1,0)] if j==0 else [(1,0),(2,2),(3,3)]) for q in range(n) if masks(d)[index]&(1<<q)]
            assert (case['k'],case['q'])==possibilities[0];k,q=possibilities[0]
            state=d.copy();count=[0]*len(arcs)
            for u,v in case['moves']:
                assert edge(u,v) and state[u]>=2;state[u]-=2;state[v]+=1;count[idx[u,v]]+=1;literal+=1
            terminal=[k if v==q else 0 for v in range(n)]
            assert state==terminal and count==case['counts']
            reserves=[None] if q==t else []
            if q!=t:
                for v in range(n):
                    if not edge(t,v) or not count[idx[t,v]]:continue
                    seen={v};todo=[v]
                    for u in todo:
                        for w in range(n):
                            if w!=t and edge(u,w) and count[idx[u,w]] and w not in seen:seen.add(w);todo.append(w)
                    if q in seen:reserves.append(v)
            assert reserves==[z['reserve'] for z in case['choices']] and reserves
            for z in case['choices']:
                b=[count[idx[t,v]]-(z['reserve']==v) if edge(t,v) else 0 for v in range(n)];assert z['capacity']==b and min(b)>=0
                A=sum(c[s]//2 for s in donors);maxdef=0;deficits=[]
                for size in range(1,len(donors)+1):
                    for U in itertools.combinations(donors,size):
                        neighbors=[v for v in range(n) if any(edge(s,v) for s in U)]
                        deficit=sum(c[s]//2 for s in U)-sum(b[v] for v in neighbors)
                        maxdef=max(maxdef,deficit)
                        if deficit>0:deficits.append([list(U),neighbors,deficit])
                assert sorted(deficits)==sorted(z['deficits']) and z['value']==A-maxdef
                used=[0]*n;filled={s:0 for s in donors}
                for s,v,a in z['assignment']:
                    assert s in donors and edge(s,v) and isinstance(a,int) and a>0;used[v]+=a;filled[s]+=a
                assert all(used[v]<=b[v] for v in range(n)) and all(filled[s]<=c[s]//2 for s in donors)
                assert sum(used)==sum(filled.values())==z['value']
                union=[v for v in range(n) if any(edge(s,v) for s in donors)]
                if maxdef and sum(b[v] for v in union)>=A:proper_deficiencies+=1
                if maxdef:
                    assert z['modified'] is None;continue
                assert case['original_wins']
                modified=count.copy()
                for s,v,a in z['assignment']:modified[idx[t,v]]-=a;modified[idx[s,v]]+=a
                assert modified==z['modified'] and min(modified)>=0
                balance=terminal.copy()
                for (u,v),a in zip(arcs,modified):balance[u]+=2*a;balance[v]-=a
                assert balance==list(c)
                nodes={q}|{v for v,a in enumerate(c) if a}|{v for e,a in zip(arcs,modified) if a for v in e};reach={q}
                while True:
                    added={u for (u,v),a in zip(arcs,modified) if a and v in reach}-reach
                    if not added:break
                    reach.update(added)
                assert nodes<=reach
                visits=0
                @functools.lru_cache(None)
                def order(rem):
                    nonlocal visits
                    visits+=1
                    if visits>300000:raise RuntimeError('REMAINING_COUNT_STATE_CAP_UNKNOWN')
                    x=list(c)
                    for (u,v),full,left in zip(arcs,modified,rem):x[u]-=2*(full-left);x[v]+=full-left
                    if not any(rem):return () if x==terminal else None
                    for a,(u,v) in enumerate(arcs):
                        if rem[a] and x[u]>=2:
                            rr=list(rem);rr[a]-=1;tail=order(tuple(rr))
                            if tail is not None:return (a,)+tail
                    return None
                sequence=order(tuple(modified));assert sequence is not None;visits_max=max(visits_max,visits)
                x=list(c)
                for a in sequence:
                    u,v=arcs[a];assert x[u]>=2;x[u]-=2;x[v]+=1;literal+=1
                assert x==terminal;reconstructed+=1
        failures=[];tested=0
        for mass,layer in enumerate(layers):
            Q=max((sum(v*v for v in c) for c,m in layer.items() if not m[0]),default=-1)
            for c in sorted(layer):
                if mass<4 or layer[c][0] or not layer[c][1]:continue
                transfers=[]
                for u,v in arcs:
                    if (u,v) not in ta or c[u]<2:continue
                    for a in [1,2]:
                        d=list(c);d[u]-=a;d[v]+=a;transfers.append([u,v,a,d,bool(masks(d)[1])])
                if not transfers:continue
                tested+=1
                if not any(not z[-1] for z in transfers):failures.append(dict(c=list(c),mass=mass,Qmax=sum(v*v for v in c)==Q,critical=mass==meta['thresholds']['clear']-1 if meta['thresholds']['clear'] else None,transfers=transfers))
        assert row==dict(graph=name,tested=tested,failures=failures,thresholds=meta['thresholds'])
        certificates=[r for r in tr['certificates'] if r['graph']==name];assert len(certificates)==bool(failures)
        if certificates:
            cert=certificates[0];assert cert['c']==failures[0]['c'];states={tuple(c) for c in cert['states']};assert len(states)==len(cert['states'])<=300000
            reachable={tuple(cert['c'])}
            for c in sorted(states,key=lambda c:-sum(c)):
                assert c in reachable and sum(c)!=1
                for u,v in arcs:
                    if c[u]<2:continue
                    d=list(c);d[u]-=2;d[v]+=1;assert tuple(d) in states;reachable.add(tuple(d))
            assert reachable==states;negative_states+=len(states)
            assert [(r['u'],r['v'],r['a']) for r in cert['transfer_traces']]==[(r[0],r[1],r[2]) for r in failures[0]['transfers']]
            for r in cert['transfer_traces']:
                x=list(cert['c']);x[r['u']]-=r['a'];x[r['v']]+=r['a'];assert x==r['d']
                for u,v in r['moves']:assert edge(u,v) and x[u]>=2;x[u]-=2;x[v]+=1;literal+=1
                assert x==[r['k'] if v==r['q'] else 0 for v in range(n)] and r['k'] in [1,2,3]
    assert actual==required and len(actual)==len(cases)
    archive=[]
    for inp in read(B/'gap_inputs.json'):
        for p,h in inp['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
        clear=read(inp['clear']);stack=read(inp['stack']) if inp['stack'] else {}
        if stack.get('scope')!='EXACT_THRESHOLD' or clear['threshold']<=stack['threshold']:continue
        with lzma.open(inp['certificate'],'rb') as f:
            while hdr:=f.read(12):
                mass,count=struct.unpack('<IQ',hdr)
                if mass!=clear['threshold']-1:
                    left=16*count
                    while left:part=f.read(min(left,65536));assert part;left-=len(part)
                    continue
                if count>300000:archive.append(dict(graph=clear['graph'],status='STATE_CAP_UNKNOWN'));break
                cs=[]
                for _ in range(count):
                    raw=f.read(16);assert len(raw)==16 and not any(raw[clear['n']:]);cs.append(tuple(raw[:clear['n']]))
                es={frozenset(e) for e in clear['edges']};triangle=set()
                for a,b,c in itertools.combinations(range(clear['n']),3):
                    if all(frozenset(e) in es for e in [(a,b),(b,c),(a,c)]):triangle.update([a,b,c])
                failures=[list(c) for c in sorted(cs) if any(c[v]>1 for v in triangle)]
                archive.append(dict(graph=clear['graph'],status='COMPLETE',gap=clear['threshold']-stack['threshold'],critical_count=len(cs),triangle_heavy_failures=failures));break
    assert archive==tr['archive']
    calculated=dict(matching_cases=len(cases),reservations=sum(len(c['choices']) for c in cases),reconstructions=reconstructed,losing_originals=sum(not c['original_wins'] for c in cases),transfer_tests=sum(r['tested'] for r in tr['rows']),transfer_failures=sum(len(r['failures']) for r in tr['rows']),negative_closures=len(tr['certificates']),archive_positive_cases=len(archive),archive_triangle_heavy=sum(len(r.get('triangle_heavy_failures',[])) for r in archive))
    assert calculated==summary
    calculated.update(literal_moves=literal,negative_closure_states=negative_states,max_fixed_count_search_states=visits_max,proper_subset_obstructions=proper_deficiencies,all_generated_keys_and_certificates_equal=True)
    p=B/'family_verification.json';raw=(json.dumps(calculated,indent=2)+'\n').encode()
    if '--check-only' in sys.argv:assert p.read_bytes()==raw
    else:p.write_bytes(raw)
    print(json.dumps(calculated),flush=True)
if __name__=='__main__':main()
