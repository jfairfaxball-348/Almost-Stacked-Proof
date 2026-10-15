"""CAM-S012-01 producer: exact reciprocal roots and losing-prefix barriers."""
import hashlib,itertools,json,lzma,sys,time
from pathlib import Path

EXTRA=[('triangular_prism',6,[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)],14),
       ('bridged_triangles',6,[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(2,3)],14)]

def vectors(n,t):
    if n==1:yield (t,);return
    for a in range(t+1):
        for b in vectors(n-1,t-a):yield (a,)+b

def forward(n,edges,M):
    layers=[];arcs=[a for e in edges for a in (e,e[::-1])]
    for t in range(M+1):
        layer={}
        for c in vectors(n,t):
            occ=[v for v,a in enumerate(c) if a];p=1<<occ[0] if len(occ)==1 else 0
            masks=[p if t==1 else 0,p,p if t==2 else 0,p if t==3 else 0]
            for u,v in arcs:
                if c[u]>=2:
                    d=list(c);d[u]-=2;d[v]+=1
                    masks=[a|b for a,b in zip(masks,layers[-1][tuple(d)])]
            layer[c]=masks
        assert len(layer)<=300000;layers.append(layer)
    return layers

def analyze(name,n,edges,layers):
    M=len(layers)-1;arcs=[a for e in edges for a in (e,e[::-1])]
    adj=[{v for u,v in arcs if u==s} for s in range(n)]
    def change(c,v,a):d=list(c);d[v]+=a;return tuple(d)
    def mask(c,i):return layers[sum(c)][c][i]
    def N(m):return sum(1<<v for v in range(n) if any(m>>u&1 for u in adj[v]))
    counts=dict(two_symmetry=0,clear_reflection=0,protected_two_normal_form=0,unit_clear=0,unit_two=0,donor_two_clear=0,donor_two_two=0)
    dig=hashlib.sha256()
    for t,layer in enumerate(layers):
        for c in sorted(layer):
            if t<=M-2:
                for w in range(n):
                    dw=change(c,w,1)
                    for q in range(n):
                        dq=change(c,q,1);dqq=change(c,q,2)
                        a=bool(mask(dw,2)>>q&1);b=bool(mask(dq,2)>>w&1);assert a==b
                        a1=bool(mask(dw,0)>>q&1);b1=bool(mask(dqq,2)>>w&1);assert a1==b1
                        dig.update(bytes([a,a1]));counts['two_symmetry']+=1;counts['clear_reflection']+=1
                    union=(1<<w) if t==0 else 0
                    for z in adj[w]:union|=mask(change(c,z,1),2)
                    assert mask(change(c,w,2),2)==union
                    counts['protected_two_normal_form']+=1
            for s in range(n):
                if not c[s]:continue
                for r in range(n):
                    if r==s:continue
                    d=change(change(c,s,-1),r,1)
                    if t<M:
                        a=bool(mask(d,0)>>s&1);b=bool(mask(change(c,s,1),2)>>r&1);assert a==b
                        counts['unit_clear']+=1;dig.update(bytes([a]))
                    assert bool(mask(d,2)>>s&1)==bool(mask(c,2)>>r&1);counts['unit_two']+=1
                    if c[s]>=2:
                        dd=change(change(c,s,-2),r,2)
                        assert bool(mask(dd,0)>>s&1)==bool(mask(c,0)>>r&1);counts['donor_two_clear']+=1
                        assert bool(mask(dd,2)>>s&1)==bool(mask(change(c,s,-1),0)>>r&1);counts['donor_two_two']+=1
    gs=next((t for t in range(n+1,M+1) if all(m[1] for m in layers[t].values())),None)
    gc=next((t for t in range(n+1,M+1) if all(m[0] for m in layers[t].values())),None)
    thresholds={'stack':gs,'clear':gc}
    for i,g in [(1,gs),(0,gc)]:
        if g:assert all(any(not m[i] for m in layers[t].values()) for t in range(2,g))
    critical=[];traces=[];closures=[];dynamics=[];barriers=0
    def trace(c,q,kind):
        original=c;moves=[]
        while not (c[q]>0 and sum(c)==c[q] and (kind==1 or c[q]==[1,0,2,3][kind])):
            for u,v in arcs:
                if c[u]>=2:
                    d=change(change(c,u,-2),v,1)
                    if mask(d,kind)>>q&1:break
            else:raise AssertionError((name,c,q,kind))
            moves.append([u,v]);c=d
        traces.append({'graph':name,'c':original,'q':q,'kind':kind,'moves':moves,'final':c})
    for goal,g,index in [('stack',gs,1),('clear',gc,0)]:
        if g is None:continue
        for c,m in sorted(layers[g-1].items()):
            if m[index]:continue
            D=[mask(change(c,w,1),2) for w in range(n)]
            assert all(bool(D[w]>>q&1)==bool(D[q]>>w&1) for w in range(n) for q in range(n))
            S=[d|N(d) for d in D]
            common=(1<<n)-1
            for sm in S:common&=sm
            critical.append({'goal':goal,'c':c,'D':D,'common_D_neighborhood':common,'AS':sum(x>1 for x in c)<=1,'Q':sum(x*x for x in c),'already_stackable':bool(m[1])})
            for w in range(n):
                d=change(c,w,1)
                for q in range(n):
                    if mask(d,2)>>q&1:trace(d,q,2)
            # Full closure is a logically sufficient independent negative certificate.
            seen={c};todo=[c]
            for x in todo:
                assert len(seen)<=300000
                for u,v in arcs:
                    if x[u]>=2:
                        d=change(change(x,u,-2),v,1)
                        if d not in seen:seen.add(d);todo.append(d)
            assert all(not mask(x,index) for x in seen)
            closures.append({'graph':name,'goal':goal,'c':c,'states':sorted(seen)})
    for t,layer in enumerate(layers):
        for c,m in sorted(layer.items()):
            if not m[1] or m[0]:continue
            for u,v in arcs:
                if c[u]<2:continue
                d=change(change(c,u,-2),v,1);tri=bool(adj[u]&adj[v])
                if tri:assert not mask(d,1);barriers+=1
                if gc and t==gc-1:
                    if gc-gs>=2:assert not tri
                    if tri and gc-gs==1:assert sum(d)==gs-1 and not mask(d,1)
                    dynamics.append({'c':c,'move':[u,v],'triangular':tri,'successor':d,'stackable':bool(mask(d,1)),'gap':gc-gs})
    prefix_rows=[]
    if gs:
        for t in range(gs,M+1):
            for c,m in sorted(layers[t].items()):
                if m[0]:continue
                seen={c};todo=[c];arccount=0
                for x in todo:
                    assert mask(x,1) and not mask(x,0)
                    if sum(x)==gs:continue
                    for u,v in arcs:
                        if x[u]<2:continue
                        d=change(change(x,u,-2),v,1);assert not (adj[u]&adj[v]);arccount+=1
                        if d not in seen:seen.add(d);todo.append(d)
                prefix_rows.append({'c':c,'states':len(seen),'arcs':arccount})
    row={'graph':name,'n':n,'edges':edges,'max_mass':M,'configurations':sum(map(len,layers)),
         'thresholds':thresholds,'relation_counts':counts,'relation_digest':dig.hexdigest(),
         'critical':critical,'triangular_barriers':barriers,'critical_dynamics':dynamics,'prefixes':prefix_rows}
    return row,traces,closures

def main():
    start=time.monotonic();old=json.loads(lzma.decompress(Path('evidence/S011/tree_tables.json.xz').read_bytes()))
    meta=json.loads(Path('evidence/S011/tree_summary.json').read_text(encoding='utf-8'))
    cases=[(t['graph'],g['n'],[tuple(e) for e in g['edges']],[{tuple(c):m for c,m in layer} for layer in t['layers']]) for t,g in zip(old,meta['graphs'])]
    extra=[]
    for name,n,edges,M in EXTRA:
        layers=forward(n,edges,M);extra.append({'graph':name,'layers':[sorted(x.items()) for x in layers]});cases.append((name,n,edges,layers))
    rows=[];traces=[];closures=[]
    for name,n,edges,layers in cases:
        row,tt,cc=analyze(name,n,edges,layers);rows.append(row);traces+=tt;closures+=cc
        assert time.monotonic()-start<600
        print(json.dumps({'graph':name,'counts':row['relation_counts'],'thresholds':row['thresholds'],'critical':len(row['critical'])}),flush=True)
    model=[]
    for w in range(6):
        d=w+1 if w%2==0 else w-1;C=sorted([(d-1)%6,(d+1)%6]);S=sorted(set([d]+C));assert w in C
        model.append({'w':w,'D':[d],'C':C,'S':S})
    assert not set.intersection(*[set(r['S']) for r in model])
    traces=list({(r['graph'],tuple(r['c']),r['q'],r['kind']):r for r in traces}.values())
    outputs={'analysis.json':{'campaign':'CAM-S012-01','rows':rows,'abstract_C6_model':model,'model_is_realized':False},
             'extra_tables.json.xz':extra,'traces.json.xz':traces,'closures.json.xz':closures}
    for name,obj in outputs.items():
        p=Path('evidence/S012')/name;raw=(json.dumps(obj,separators=(',',':'))+'\n').encode()
        if '--check-only' in sys.argv:assert (lzma.decompress(p.read_bytes()) if p.suffix=='.xz' else p.read_bytes())==raw
        else:p.write_bytes(lzma.compress(raw) if p.suffix=='.xz' else raw)
    print(json.dumps({'graphs':len(rows),'configurations':sum(r['configurations'] for r in rows),'traces':len(traces),'moves':sum(len(r['moves']) for r in traces),'closures':len(closures)}),flush=True)

if __name__=='__main__':main()
