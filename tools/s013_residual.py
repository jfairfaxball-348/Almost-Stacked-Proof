"""CAM-S013-05: archive critical adjacency and full actual private-exit family."""
import hashlib,json,lzma,sys
from pathlib import Path
B=Path('evidence/S013')
def read(n):
    p=B/n;b=p.read_bytes();return json.loads(lzma.decompress(b) if p.suffix=='.xz' else b)
def save(n,x):
    p=B/n;b=(json.dumps(x,separators=(',',':'))+'\n').encode()
    if '--check-only' in sys.argv:assert (lzma.decompress(p.read_bytes()) if p.suffix=='.xz' else p.read_bytes())==b
    else:p.write_bytes(lzma.compress(b) if p.suffix=='.xz' else b)
def main():
    archive=[];certs=[];rows=[];archive_closures=[]
    for inp in read('archive_inputs.json'):
        for p,h in inp['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
        m=json.loads(Path(inp['summary']).read_bytes());g=m['threshold'];critical=None;unknown=False
        with lzma.open(inp['certificate'],'rb') as f:
            while hdr:=f.read(12):
                t=int.from_bytes(hdr[:4],'little');count=int.from_bytes(hdr[4:],'little');size=count*16
                if t==g-1:
                    if count>300000:unknown=True;break
                    raw=f.read(size);assert len(raw)==size;critical={tuple((int.from_bytes(raw[k:k+16],'little')>>(8*i))&255 for i in range(m['n'])) for k in range(0,size,16)};assert len(critical)==count;break
                while size:
                    z=f.read(min(size,1048576));assert z;size-=len(z)
        if unknown:archive.append(dict(graph=m['graph'],threshold=g,status='CRITICAL_STATE_CAP_UNKNOWN'));continue
        assert critical is not None
        arcs=sorted((u,v) for a,b in m['edges'] for u,v in [(a,b),(b,a)]);pairs=[]
        for c in sorted(critical):
            for u,v in arcs:
                if c[u]:
                    d=list(c);d[u]-=1;d[v]+=1;d=tuple(d)
                    if d in critical:pairs.append([c,u,v,d])
        archive.append(dict(graph=m['graph'],n=m['n'],edges=m['edges'],threshold=g,status='COMPLETE_HISTORICAL_CRITICAL_LAYER',critical_losers=len(critical),pairs=pairs))
        if pairs:
            c,u,v,d=pairs[0];negative=[]
            for start in [c,d]:
                seen={tuple(start)};todo=[tuple(start)]
                for x in todo:
                    assert len(seen)<=300000
                    assert sum(a>0 for a in x)!=1
                    for s,t in arcs:
                        if x[s]>=2:
                            y=list(x);y[s]-=2;y[t]+=1;y=tuple(y)
                            if y not in seen:seen.add(y);todo.append(y)
                negative.append(dict(c=start,states=sorted(seen)))
            archive_closures.append(dict(graph=m['graph'],pair=pairs[0],negative=negative))
    for g,tab in zip(read('precision_inputs.json'),read('precision_tables.json.xz')):
        name,n=g['graph'],g['n'];arcs=sorted((u,v) for a,b in g['edges'] for u,v in [(a,b),(b,a)]);N=[{v for u,v in arcs if u==s} for s in range(n)];layers=[{tuple(c):m for c,m in lay} for lay in tab['layers']]
        def get(c):return layers[sum(c)][tuple(c)]
        small=private=0
        for lay in layers:
            for c,mask in sorted(lay.items()):
                for goal,j in [('stack',1),('clear',0)]:
                    if mask[j]:continue
                    for s,t in arcs:
                        for a in (1,2):
                            if c[s]>=a:
                                d=list(c);d[s]-=a;d[t]+=a;assert not get(d)[3];small+=1
                    heavy=[s for s in range(n) if c[s]>=2]
                    for s in heavy:
                        for t in heavy:
                            if s==t:continue
                            a=c[s]//2;d=list(c);d[s]-=2*a;d[t]+=2*a;dm=get(d)
                            if not dm[j]:continue
                            for kind in ([0] if j==0 else [0,2,3]):
                                k={0:1,2:2,3:3}[kind]
                                for q in range(n):
                                    if not dm[kind]>>q&1:continue
                                    x=tuple(d);m=[0]*len(arcs)
                                    while not (sum(x)==x[q] and x[q]==k):
                                        for z,(u,v) in enumerate(arcs):
                                            if x[u]>=2:
                                                y=list(x);y[u]-=2;y[v]+=1;y=tuple(y)
                                                if get(y)[kind]>>q&1:break
                                        else:raise AssertionError(x)
                                        m[z]+=1;x=y
                                    common=sum(z for (u,v),z in zip(arcs,m) if u==t and v in N[s]);priv=sum(z for (u,v),z in zip(arcs,m) if u==t and v not in N[s])
                                    assert common<=a-(q==t)
                                    if q==t:assert priv>=1+(c[t]-k+1)//2
                                    else:
                                        assert priv>=(c[t]+1)//2
                                        if common==a:
                                            reached={q};change=True
                                            while change:
                                                more=reached|{u for (u,v),z in zip(arcs,m) if z and u!=t and v in reached};change=more!=reached;reached=more
                                            assert not any(z and u==t and v not in N[s] and v in reached for (u,v),z in zip(arcs,m))
                                    certs.append(dict(graph=name,c=c,d=d,s=s,t=t,a=a,goal=goal,q=q,k=k,m=m,common=common,private=priv));private+=1;assert len(certs)<=300000
        rows.append(dict(graph=name,adjacent_small_transfer_tests=small,private_certificates=private))
    save('archive_adjacency.json',archive);save('archive_adjacency_closures.json.xz',archive_closures);save('residual.json',rows);save('private_exit_counts.json.xz',certs)
    print(json.dumps({'archive_graphs':len(archive),'archive_pairs':sum(len(r.get('pairs',[])) for r in archive),'private_certificates':len(certs),'small_transfer_tests':sum(r['adjacent_small_transfer_tests'] for r in rows)}),flush=True)
if __name__=='__main__':main()
