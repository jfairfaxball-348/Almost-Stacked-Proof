"""Independent CAM-S012-02 DAG shortest escape and literal transport check."""
import functools,itertools,json,lzma,sys,time
from pathlib import Path

def load(p):
    raw=Path(p).read_bytes();return json.loads(lzma.decompress(raw) if p.endswith('.xz') else raw)

def main():
    start=time.monotonic();meta=load('evidence/S012/analysis.json');saved=load('evidence/S012/escape.json')
    tables=load('evidence/S011/tree_tables.json.xz')+load('evidence/S012/extra_tables.json.xz')
    certs=load('evidence/S012/escape_closures.json.xz');fuel=load('evidence/S012/escape_fuel.json.xz')
    expected_critical=set();expected_fuel=set();barriers=0;taus=[];statecount=0
    bykey={(x['graph'],tuple(x['c'])):x for x in certs};assert len(bykey)==len(certs)
    summary={(x['graph'],tuple(x['c'])):x for x in saved['critical']};assert len(summary)==len(saved['critical'])
    for g,table in zip(meta['rows'],tables):
        name=g['graph'];n=g['n'];arcs={(u,v) for a,b in g['edges'] for u,v in [(a,b),(b,a)]}
        neighbors={u:{v for a,v in arcs if a==u} for u in range(n)}
        triangular={(u,v) for u,v in arcs if neighbors[u].intersection(neighbors[v])}
        layers=[{tuple(c):m for c,m in layer} for layer in table['layers']]
        def mask(c):return layers[sum(c)][c]
        def children(c):
            for u,v in sorted(arcs):
                if c[u]>=2:
                    x=list(c);x[u]-=2;x[v]+=1;yield u,v,tuple(x)
        for layer in layers:
            for c,m in layer.items():
                if not m[1] or m[0]:continue
                for u,v,d in children(c):
                    if (u,v) in triangular or not m[3]&(1<<v):assert mask(d)[1]==0;barriers+=1
        cg=g['thresholds']['clear'];sg=g['thresholds']['stack']
        if not cg:continue
        for c,m in sorted(layers[cg-1].items()):
            if not m[1] or m[0]:continue
            key=(name,c);expected_critical.add(key);S=m[3];visited=set()
            @functools.cache
            def recurrence(x):
                visited.add(x);assert len(visited)<=300000
                options=[]
                if mask(x)[1]:assert mask(x)[3]&~S==0 and mask(x)[0]==0
                for u,v,d in children(x):
                    tail=recurrence(d)
                    if (u,v) in triangular or not S&(1<<v):assert mask(d)[1]==0;options.append(1)
                    elif tail is not None:options.append(1+tail)
                return min(options) if options else None
            tau=recurrence(c);taus.append(tau)
            if tau is not None:assert sum(c)-tau<sg and cg-sg<=tau
            cert=bykey[key];distances={tuple(x):d for x,d in cert['distances']}
            assert set(distances)==visited and distances[c]==0;statecount+=len(visited)
            # Independently check shortest distances via all incoming actual edges.
            incoming={x:[] for x in visited};forbidden=[]
            for x in visited:
                if distances[x]<cg-sg:assert mask(x)[1]
                for u,v,d in children(x):
                    assert d in visited;incoming[d].append(distances[x]+1)
                    if (u,v) in triangular or not S&(1<<v):forbidden.append([list(x),u,v,distances[x]+1])
            for x in visited:
                if x!=c:assert distances[x]==min(incoming[x])
            assert sorted(forbidden)==cert['forbidden']
            expected={'graph':name,'c':list(c),'R3':S,'gap':cg-sg,'tau':tau,'states':len(visited),'forbidden_moves':len(forbidden)}
            assert summary[key]==expected
            for source,target in itertools.product(range(n),repeat=2):
                # Enumerate all simple paths, then retain minimum length; n<=6.
                def walk(path):
                    if path[-1]==target:yield path;return
                    for nxt in sorted(neighbors[path[-1]]-set(path)):yield from walk(path+[nxt])
                allpaths=list(walk([source]));dist=min(map(len,allpaths))-1
                for path in allpaths:
                    if len(path)!=dist+1:continue
                    if c[source]>=2**(dist+1):
                        for w in neighbors[target]:
                            if (target,w) in triangular:expected_fuel.add((name,c,'triangle',tuple(path),w,2**(dist+1)))
                    if not S&(1<<target) and dist>=1 and c[source]>=2**dist:expected_fuel.add((name,c,'outside',tuple(path),None,2**dist))
            recurrence.cache_clear()
        assert time.monotonic()-start<600
    actual_fuel=set();moves=0
    graph_arcs={g['graph']:{(u,v) for a,b in g['edges'] for u,v in [(a,b),(b,a)]} for g in meta['rows']}
    graph_tables={t['graph']:[{tuple(c):m for c,m in layer} for layer in t['layers']] for t in tables}
    graph_info={g['graph']:g for g in meta['rows']}
    for r in fuel:
        key=(r['graph'],tuple(r['c']),r['kind'],tuple(r['path']),r['last_neighbor'],r['fuel']);assert key not in actual_fuel;actual_fuel.add(key)
        state=list(r['c']);path=r['path'];d=len(path)-1;amount=2**(d+1) if r['kind']=='triangle' else 2**d
        assert amount==r['fuel'] and state[path[0]]>=amount
        expected=[]
        for i in range(d):expected += [[path[i],path[i+1]]]*(amount//2**(i+1))
        if r['kind']=='triangle':expected.append([path[-1],r['last_neighbor']])
        assert expected==r['moves'] and len(expected)==amount-1
        for u,v in r['moves']:
            assert (u,v) in graph_arcs[r['graph']] and state[u]>=2;state[u]-=2;state[v]+=1;moves+=1
        assert state==r['final'] and graph_tables[r['graph']][sum(state)][tuple(state)][1]==0
        info=graph_info[r['graph']];assert sum(state)<info['thresholds']['stack'] and info['thresholds']['clear']-info['thresholds']['stack']<=len(expected)
    assert actual_fuel==expected_fuel and set(bykey)==set(summary)==expected_critical
    assert saved['one_step_barriers']==barriers and saved['fuel_witnesses']==len(fuel) and saved['fuel_moves']==moves
    out={'one_step_barriers':barriers,'critical_inputs':len(expected_critical),'complete_closure_states':statecount,'fuel_witnesses':len(fuel),'literal_moves':moves,'finite_tau':sum(t is not None for t in taus),'no_escape_after_complete_closure':sum(t is None for t in taus),'all_equal':True}
    p=Path('evidence/S012/escape_verification.json')
    if '--check-only' in sys.argv:assert load(str(p).replace('\\','/'))==out
    else:p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(out),flush=True)

if __name__=='__main__':main()
