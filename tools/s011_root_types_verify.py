"""Independent complete forward recurrence and vertex-set critical classification."""
import hashlib,itertools,json,lzma,sys,time
from pathlib import Path

def main():
    start=time.monotonic();tables=json.loads(lzma.decompress(Path('evidence/S011/tree_tables.json.xz').read_bytes()))
    summary=json.loads(Path('evidence/S011/tree_summary.json').read_text(encoding='utf-8'))
    result=json.loads(Path('evidence/S011/root_types.json').read_text(encoding='utf-8'));records=[];clearcases=[];total=0;bipchecks=0
    for table,g in zip(tables,summary['graphs']):
        n=g['n'];edges=[tuple(e) for e in g['edges']];adj={u:{v for a,b in edges for v in ([b] if a==u else ([a] if b==u else []))} for u in range(n)}
        layers=[]
        for t in range(g['max_mass']+1):
            current={}
            for marks in itertools.combinations(range(t+n-1),n-1):
                cut=(-1,)+marks+(t+n-1,);c=tuple(cut[i+1]-cut[i]-1 for i in range(n));sets=[set() for _ in range(4)]
                occupied={v for v,a in enumerate(c) if a}
                if len(occupied)==1:
                    q=next(iter(occupied));sets[1].add(q)
                    for i,k in [(0,1),(2,2),(3,3)]:
                        if t==k:sets[i].add(q)
                for u in range(n):
                    if c[u]>=2:
                        for v in adj[u]:
                            d=list(c);d[u]-=2;d[v]+=1;prior=layers[t-1][tuple(d)]
                            for i in range(4):sets[i]|=prior[i]
                current[c]=sets
            actual=[[list(c),[sum(1<<v for v in s) for s in ss]] for c,ss in sorted(current.items())]
            assert actual==table['layers'][t] and len(current)<=300000;layers.append(current)
            if t>=2:
                for c,ss in current.items():
                    neighborhood=set().union(*(adj[u] for u in ss[2])) if ss[2] else set()
                    assert ss[0]==neighborhood and ss[1]==ss[0]|ss[2]|ss[3];total+=1
        gs=g['stack_threshold'];gc=g['clear_threshold']
        for c,ss in sorted(layers[gs-1].items()):
            if ss[1]:continue
            for w in range(n):
                d=list(c);d[w]+=1;C,S,D,T=layers[gs][tuple(d)]
                assert D and w not in D and not T and C==set.union(*(adj[u] for u in D)) and S==C|D
                assert (w in S)==(w in C)
                if g['graph'] in ('K2','P4'):
                    coloring={0:0};todo=[0]
                    for u in todo:
                        for v in adj[u]:
                            if v not in coloring:coloring[v]=1-coloring[u];todo.append(v)
                    assert all(coloring[q]!=coloring[w] for q in D) and all(coloring[q]==coloring[w] for q in C);bipchecks+=1
                records.append({'graph':g['graph'],'c':list(c),'w':w,'D_two':sum(1<<v for v in D),'C_clear':sum(1<<v for v in C),'S_stack':sum(1<<v for v in S)})
        if gc is not None:
            for c,ss in sorted(layers[gc-1].items()):
                if not ss[0]:clearcases.append({'graph':g['graph'],'c':list(c),'gap':gc-gs,'already_stackable':bool(ss[1])})
        assert time.monotonic()-start<600
    assert records==result['critical_insertions'] and clearcases==result['critical_clear_cases'] and total==result['checked_inputs']
    assigned=result['abstract_C5_model'];neighbors={i:{(i-1)%5,(i+1)%5} for i in range(5)}
    intersection=set(range(5))
    for r in assigned:
        D,C,S=map(set,(r['D'],r['C'],r['S']));w=r['w']
        assert D and w not in D and C==set.union(*(neighbors[v] for v in D)) and S==C|D and w in C
        intersection&=S
    assert not intersection and result['model_is_graph_configuration'] is False
    out={'campaign':'CAM-S011-03','all_verified':True,'checked_inputs':total,'critical_insertions':len(records),
        'critical_clear_cases':len(clearcases),'bipartite_insertion_checks':bipchecks,
        'already_stackable_critical_clear':sum(r['already_stackable'] for r in clearcases),
        'result_sha256':hashlib.sha256(Path('evidence/S011/root_types.json').read_bytes()).hexdigest()}
    p=Path('evidence/S011/root_types_verification.json')
    if '--check-only' in sys.argv:assert json.loads(p.read_text(encoding='utf-8'))==out
    else:p.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(out),flush=True)

if __name__=='__main__':main()
