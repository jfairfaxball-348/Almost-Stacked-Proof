"""Independent reverse masks, complete classifications and literal witness replay."""
import hashlib,itertools,json,lzma,sys,time
from pathlib import Path

REGISTERED={'K2':(2,[(0,1)],3,3,None),'K3':(3,[(0,1),(0,2),(1,2)],4,4,4),
 'P4':(4,[(0,1),(1,2),(2,3)],15,15,None),'C5':(5,[(0,1),(1,2),(2,3),(3,4),(0,4)],10,8,10),
 'triangle_tail2':(5,[(0,1),(0,2),(1,2),(0,3),(3,4)],22,16,22),
 'F2':(5,[(0,1),(0,2),(1,2),(0,3),(0,4)],13,11,13),
 'bowtie':(5,[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)],8,8,8),
 'diamond':(4,[(0,1),(0,2),(0,3),(1,2),(2,3)],7,7,7)}

def vectors(n,total):
    for cuts in itertools.combinations(range(total+n-1),n-1):
        marks=(-1,)+cuts+(total+n-1,)
        yield tuple(marks[i+1]-marks[i]-1 for i in range(n))

def main():
    start=time.monotonic();raw=lzma.decompress(Path('evidence/S011/tree_tables.json.xz').read_bytes())
    saved=json.loads(raw);summary=json.loads(Path('evidence/S011/tree_summary.json').read_text(encoding='utf-8'))
    assert hashlib.sha256(raw).hexdigest()==summary['table_raw_sha256']
    traces=[];negative=[];rows=[]
    for table,meta in zip(saved,summary['graphs']):
        name=table['graph'];n,edges,M,gs,gc=REGISTERED[name]
        assert meta['graph']==name and meta['n']==n and meta['edges']==[list(e) for e in edges]
        arcs=[a for u,v in edges for a in [(u,v),(v,u)]];layers=[]
        for t in range(M+1):
            layer={c:[0,0,0,0] for c in vectors(n,t)}
            for q in range(n):
                if t:
                    c=tuple(t if v==q else 0 for v in range(n));layer[c]=[int(t==1)<<q,1<<q,int(t==2)<<q,int(t==3)<<q]
            if t:
                for d,masks in layers[-1].items():
                    for u,v in arcs:
                        if d[v]:
                            c=list(d);c[v]-=1;c[u]+=2;c=tuple(c)
                            for i in range(4):layer[c][i]|=masks[i]
            assert len(layer)<=300000
            actual=[[list(c),m] for c,m in sorted(layer.items())];assert actual==table['layers'][t]
            assert hashlib.sha256(json.dumps(actual,separators=(',',':')).encode()).hexdigest()==meta['layer_hashes'][t]
            layers.append(layer)
        def literal(c,q,kind):
            original=list(c);c=tuple(c);moves=[]
            def terminal(x):return x[q]>0 and all(x[v]==0 for v in range(n) if v!=q) and (kind==1 or x[q]==[1,0,2,3][kind])
            while not terminal(c):
                for u,v in arcs:
                    if c[u]<2:continue
                    d=list(c);d[u]-=2;d[v]+=1;d=tuple(d)
                    if layers[sum(d)][d][kind]>>q&1:break
                else:raise AssertionError((name,c,q,kind))
                moves.append([u,v]);c=d
            state=original.copy()
            for u,v in moves:
                assert (u,v) in arcs and state[u]>=2;state[u]-=2;state[v]+=1
            assert tuple(state)==c and terminal(c)
            traces.append({'graph':name,'c':original,'root':q,'kind':kind,'moves':moves,'final':state})
        failures={k:[] for k in meta['failures']};critical=[];ternary=[];ic=dc=0
        for t in range(2,M+1):
            for c,masks in sorted(layers[t].items()):
                if masks[1] and not masks[0]:
                    R={v for v in range(n) if masks[3]>>v&1};assert R and all(v in R for v,a in enumerate(c) if a)
                    adjacency={u:{v for a,b in arcs if a==u and (v:=b) in R} for u in R}
                    coloring={min(R):0};queue=[min(R)];bip=True
                    for u in queue:
                        for v in adjacency[u]:
                            if v not in coloring:coloring[v]=1-coloring[u];queue.append(v)
                            elif coloring[v]==coloring[u]:bip=False
                    assert set(coloring)==R
                    row={'c':list(c),'R3':masks[3],'bipartite':bip,'critical_clear':bool(gc and t==gc-1)};ternary.append(row)
                    if not bip:failures['nonbipartite_ternary_clear_loser'].append(row)
                    for w,a in enumerate(c):
                        if a:
                            d=list(c);d[w]-=1;assert layers[t-1][tuple(d)][2]>>w&1;dc+=1;literal(d,w,2)
                if masks[1]==0 and t<M:
                    ins=[];allwin=True
                    for w in range(n):
                        d=list(c);d[w]+=1;mask=layers[t+1][tuple(d)];ins.append(mask[0]);allwin &= bool(mask[1])
                        if mask[1]:
                            ic+=1;assert mask[0]
                            if c[w] and not mask[1]>>w&1:failures['occupied_self_stack'].append({'c':list(c),'w':w})
                            if c[w] and not mask[0]>>w&1:
                                item={'c':list(c),'w':w};failures['occupied_self_clear'].append(item)
                                if t==gs-1:failures['critical_occupied_self_clear'].append(item)
                        if t==gs-1:
                            for q in range(n):
                                if mask[0]>>q&1:literal(d,q,0)
                    common=set.intersection(*[{q for q in range(n) if mask>>q&1} for mask in ins])
                    if t==gs-1:
                        assert allwin
                        row={'c':list(c),'AS':sum(a>=2 for a in c)<=1,'Q':sum(a**2 for a in c),'clear_insertion_masks':ins,'common_clear_roots':sum(1<<q for q in common)}
                        critical.append(row)
                        if not common:failures['critical_common_clear'].append(row)
        assert failures==meta['failures'] and critical==meta['critical_stack'] and ternary==meta['ternary_clear_losers']
        assert (ic,dc)==(meta['winning_insertions_checked'],meta['occupied_deletions_checked'])
        for g,i in [(gs,1),(gc,0)]:
            if g:
                assert all(m[i] for m in layers[g].values())
                assert all(any(not m[i] for m in layers[t].values()) for t in range(2,g))
        for predicate,items in failures.items():
            if not items:continue
            item=items[0];c=item['c'].copy()
            if 'w' in item:c[item['w']]+=1
            seen={tuple(c)};todo=[tuple(c)];rootmasks=[0]*4
            for x in todo:
                occ=[v for v,a in enumerate(x) if a]
                if len(occ)==1:
                    q=occ[0];rootmasks[1]|=1<<q
                    for index,pile in [(0,1),(2,2),(3,3)]:
                        if x[q]==pile:rootmasks[index]|=1<<q
                for u,v in arcs:
                    if x[u]>=2:
                        y=list(x);y[u]-=2;y[v]+=1;y=tuple(y)
                        if y not in seen:seen.add(y);todo.append(y)
                assert len(seen)<=300000
            assert rootmasks==layers[sum(c)][tuple(c)]
            negative.append({'graph':name,'predicate':predicate,'c':c,'masks':rootmasks,'closure':sorted(seen)})
        rows.append({'graph':name,'layers':M+1,'configurations':sum(len(x) for x in layers),'literal_deletion_count':dc})
        assert time.monotonic()-start<600
    trace_raw=json.dumps(traces,separators=(',',':')).encode();negative_raw=json.dumps(negative,separators=(',',':')).encode()
    out={'campaign':'CAM-S011-01','all_verified':True,'graphs':rows,'layers':sum(r['layers'] for r in rows),
        'configurations':sum(r['configurations'] for r in rows),'literal_traces':len(traces),'literal_moves':sum(len(r['moves']) for r in traces),
        'trace_raw_sha256':hashlib.sha256(trace_raw).hexdigest(),'negative_closures':len(negative),'negative_raw_sha256':hashlib.sha256(negative_raw).hexdigest()}
    dest=Path('evidence/S011/tree_verification.json');tp=Path('evidence/S011/tree_traces.json.xz');np=Path('evidence/S011/tree_negative_closures.json.xz')
    if '--check-only' in sys.argv:
        assert json.loads(dest.read_text(encoding='utf-8'))==out and lzma.decompress(tp.read_bytes())==trace_raw and lzma.decompress(np.read_bytes())==negative_raw
    else:
        dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');tp.write_bytes(lzma.compress(trace_raw));np.write_bytes(lzma.compress(negative_raw))
    print(json.dumps({k:v for k,v in out.items() if k!='graphs'}),flush=True)

if __name__=='__main__':main()
