"""CAM-S013-02 full forward masks and proposed extremal lemma challenges."""
import hashlib,itertools,json,lzma,sys
from pathlib import Path

OUT=Path('evidence/S013')
def vectors(n,t):
    if n==1:yield (t,);return
    for a in range(t+1):
        for b in vectors(n-1,t-a):yield (a,)+b
def save(name,x):
    p=OUT/name;raw=(json.dumps(x,separators=(',',':'))+'\n').encode()
    if '--check-only' in sys.argv:assert (lzma.decompress(p.read_bytes()) if p.suffix=='.xz' else p.read_bytes())==raw
    else:p.write_bytes(lzma.compress(raw) if p.suffix=='.xz' else raw)

def main():
    inputs=json.loads((OUT/'precision_inputs.json').read_bytes());tables=[];reports=[];certificates=[]
    for g in inputs:
        name,n,edges,M=g['graph'],g['n'],g['edges'],g['max_mass'];arcs=sorted((u,v) for a,b in edges for u,v in [(a,b),(b,a)])
        layers=[]
        for t in range(M+1):
            layer={}
            for c in vectors(n,t):
                occ=[i for i in range(n) if c[i]];root=(1<<occ[0]) if len(occ)==1 else 0
                masks=[root if t==1 else 0,root,root if t==2 else 0,root if t==3 else 0]
                for u,v in arcs:
                    if c[u]>=2:
                        d=list(c);d[u]-=2;d[v]+=1
                        masks=[a|b for a,b in zip(masks,layers[-1][tuple(d)])]
                layer[c]=masks
            assert len(layer)<=300000;layers.append(layer)
        def change(c,v,a):d=list(c);d[v]+=a;return tuple(d)
        def get(c):return layers[sum(c)][c]
        thresholds={}
        for goal,j in [('stack',1),('clear',0)]:
            thresholds[goal]=next((t for t in range(n+1,M+1) if all(m[j] for m in layers[t].values())),None)
            if thresholds[goal]:assert all(any(not m[j] for m in layers[t].values()) for t in range(2,thresholds[goal]))
        count=critical_count=0;first=critical_first=None;checks=0;triple_relation_checks=0
        for t,layer in enumerate(layers):
            for c,m in sorted(layer.items()):
                # R2(c) = {q : c+q reaches3}; root3 is all occupied labels or empty.
                if t<M:
                    assert m[2]==sum(1<<q for q in range(n) if get(change(c,q,1))[3]);triple_relation_checks+=n
                if m[3]:assert all(m[3]>>q&1 for q in range(n) if c[q])
                if not m[1]:continue
                B=[w for w in range(n) if c[w] and not get(change(c,w,-1))[1]]
                for u,v in edges:
                    checks+=1
                    if u in B and v in B:
                        count+=1
                        row={'graph':name,'x':c,'edge':[u,v],'deletions':[change(c,u,-1),change(c,v,-1)],'threshold_layer':t==thresholds['stack']}
                        if first is None:first=row
                        if t==thresholds['stack']:
                            critical_count+=1
                            if critical_first is None:critical_first=row
        extrema=[];shadows=[]
        for goal,j in [('stack',1),('clear',0)]:
            threshold=thresholds[goal]
            if not threshold:continue
            losers=[c for c,m in sorted(layers[threshold-1].items()) if not m[j]]
            Q=max(sum(a*a for a in c) for c in losers);qmax=[c for c in losers if sum(a*a for a in c)==Q]
            extrema.append({'goal':goal,'threshold':threshold,'losers':len(losers),'AS_losers':sum(sum(a>1 for a in c)<=1 for c in losers),'Qmax':Q,'maxima':qmax})
        if thresholds['clear'] and thresholds['clear']==thresholds['stack']+1:
            for c,m in sorted(layers[thresholds['stack']].items()):
                if m[0]:continue
                negative=[];as_negative=[]
                for u,v in arcs:
                    if c[u]>=2:
                        d=list(c);d[u]-=2;d[v]+=1;d=tuple(d)
                        if not get(d)[1]:negative.append([u,v,d]);as_negative+=([[u,v,d]] if sum(a>1 for a in d)<=1 else [])
                shadows.append({'c':c,'AS':sum(a>1 for a in c)<=1,'nonstacking_first_moves':negative,'AS_nonstacking_first_moves':as_negative})
        # Complete selected counterexample certificates, literal STACK and negative closures.
        for row in [r for r in [first,critical_first] if r is not None]:
            if row in [r['diagnostic'] for r in certificates]:continue
            x=tuple(row['x']);cur=x;moves=[]
            while sum(a>0 for a in cur)>1:
                for u,v in arcs:
                    if cur[u]>=2:
                        d=list(cur);d[u]-=2;d[v]+=1;d=tuple(d)
                        if get(d)[1]:break
                else:raise AssertionError(cur)
                moves.append([u,v]);cur=d
            negatives=[]
            for c in row['deletions']:
                c=tuple(c);seen={c};todo=[c]
                for a in todo:
                    assert len(seen)<=300000
                    for u,v in arcs:
                        if a[u]>=2:
                            b=list(a);b[u]-=2;b[v]+=1;b=tuple(b)
                            if b not in seen:seen.add(b);todo.append(b)
                assert all(not get(a)[1] for a in seen)
                negatives.append({'c':c,'states':sorted(seen)})
            certificates.append({'diagnostic':row,'moves':moves,'final':cur,'negative':negatives})
        report={'graph':name,'thresholds':thresholds,'configurations':sum(map(len,layers)),'adjacent_tests':checks,'adjacent_deletion_failures':count,'threshold_adjacent_failures':critical_count,'first':first,'threshold_first':critical_first,'extrema':extrema,'gap1_shadows':shadows,'three_relation_checks':triple_relation_checks}
        reports.append(report);tables.append({'graph':name,'layers':[[[c,m] for c,m in sorted(layer.items())] for layer in layers]})
        print(json.dumps({k:report[k] for k in ['graph','thresholds','configurations','adjacent_deletion_failures','threshold_adjacent_failures','first','threshold_first']}),flush=True)
    save('precision_tables.json.xz',tables);save('precision.json',reports);save('precision_certificates.json.xz',certificates)

if __name__=='__main__':main()
