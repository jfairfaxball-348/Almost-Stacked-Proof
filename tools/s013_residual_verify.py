"""Independent upper-extension adjacency and exact private-exit chronology."""
import functools,hashlib,json,lzma,struct,sys
from pathlib import Path
B=Path('evidence/S013')
def load(n):
    p=B/n;raw=p.read_bytes();return json.loads(lzma.decompress(raw) if p.suffix=='.xz' else raw)
def main():
    archive=load('archive_adjacency.json');inputs=load('archive_inputs.json');acs=load('archive_adjacency_closures.json.xz');statecount=pairs=0
    for reg,saved in zip(inputs,archive):
        for p,h in reg['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
        meta=json.loads(Path(reg['summary']).read_bytes());g=meta['threshold'];n=meta['n'];critical=None;skip=False
        with lzma.open(reg['certificate'],'rb') as stream:
            while block:=stream.read(12):
                t,count=struct.unpack('<IQ',block)
                if t==g-1:
                    if count>300000:skip=True;break
                    critical=set()
                    for _ in range(count):
                        rec=stream.read(16);assert len(rec)==16 and all(x==0 for x in rec[n:]);critical.add(tuple(rec[:n]))
                    assert len(critical)==count;break
                stream.seek(16*count,1)
        if skip:assert saved==dict(graph=meta['graph'],threshold=g,status='CRITICAL_STATE_CAP_UNKNOWN');continue
        assert critical is not None
        arcs=sorted({tuple(e) for e in meta['edges']}|{tuple(reversed(e)) for e in meta['edges']});upper={}
        for c in critical:
            for v in range(n):
                x=list(c);x[v]+=1;upper.setdefault(tuple(x),set()).add(v)
        found=set()
        for x,sites in upper.items():
            for u,v in arcs:
                if u in sites and v in sites:
                    c=list(x);c[v]-=1;d=list(x);d[u]-=1;found.add((tuple(c),u,v,tuple(d)))
        expected=[list(z) for z in sorted(found)];actual=[(tuple(c),u,v,tuple(d)) for c,u,v,d in saved['pairs']]
        assert actual==sorted(found) and saved['critical_losers']==len(critical);statecount+=len(critical);pairs+=len(found)
        these=[a for a in acs if a['graph']==meta['graph']];assert len(these)==bool(found)
        for obj in these:
            assert obj['pair']==saved['pairs'][0]
            for neg in obj['negative']:
                states={tuple(x) for x in neg['states']};todo=[tuple(neg['c'])];seen=set(todo)
                for x in todo:
                    assert sum(a>0 for a in x)!=1 and len(seen)<=300000
                    for u,v in arcs:
                        if x[u]>=2:
                            y=list(x);y[u]-=2;y[v]+=1;y=tuple(y);assert y in states
                            if y not in seen:seen.add(y);todo.append(y)
                assert seen==states
    configs=load('precision_inputs.json');tables=load('precision_tables.json.xz');rows=load('residual.json');certs=load('private_exit_counts.json.xz');moves=private=small=0
    for g,tab,row in zip(configs,tables,rows):
        name,n=g['graph'],g['n'];arcs=sorted({tuple(e) for e in g['edges']}|{tuple(reversed(e)) for e in g['edges']});N={v:{w for u,w in arcs if u==v} for v in range(n)};layers=[{tuple(c):m for c,m in lay} for lay in tab['layers']]
        def get(c):return layers[sum(c)][tuple(c)]
        actual={(tuple(r['c']),r['s'],r['t'],r['goal'],r['k'],r['q']):r for r in certs if r['graph']==name};expected=set();local=0
        for layer in layers:
            for c,m in layer.items():
                for goal,j in [('stack',1),('clear',0)]:
                    if m[j]:continue
                    for u,v in arcs:
                        for a in range(1,min(2,c[u])+1):
                            d=list(c);d[u]-=a;d[v]+=a;assert get(d)[3]==0;local+=1
                    for s in range(n):
                        for t in range(n):
                            if s==t or c[s]<2 or c[t]<2:continue
                            d=list(c);d[s]-=2*(c[s]//2);d[t]+=2*(c[s]//2)
                            if not get(d)[j]:continue
                            for k,z in ([(1,0)] if j==0 else [(1,0),(2,2),(3,3)]):
                                for q in range(n):
                                    if get(d)[z]&(1<<q):expected.add((c,s,t,goal,k,q))
        assert expected==actual.keys() and local==row['adjacent_small_transfer_tests'] and len(expected)==row['private_certificates'];small+=local;private+=len(expected)
        for key,r in actual.items():
            c,s,t,goal,k,q=key;a=c[s]//2;d=list(c);d[s]-=2*a;d[t]+=2*a;assert d==r['d'];m=r['m'];common=sum(z for z,(u,v) in zip(m,arcs) if u==t and v in N[s]);out=sum(z for z,(u,v) in zip(m,arcs) if u==t);priv=out-common
            assert (common,priv)==(r['common'],r['private']) and common<=a-(q==t)
            if q==t:assert priv>=1+(c[t]-k+1)//2
            else:
                assert priv>=(c[t]+1)//2
                if common==a:
                    for z,(u,v) in zip(m,arcs):
                        if not z or u!=t or v in N[s]:continue
                        seen={v};todo=[v]
                        for p in todo:
                            for z1,(w,y) in zip(m,arcs):
                                if z1 and w==p and y!=t and y not in seen:seen.add(y);todo.append(y)
                        assert q not in seen
            target=[k if v==q else 0 for v in range(n)];balance=target.copy()
            for (u,v),z in zip(arcs,m):balance[u]+=2*z;balance[v]-=z
            assert balance==d;visits=0
            @functools.lru_cache(None)
            def search(rem):
                nonlocal visits
                visits+=1;assert visits<=300000
                x=d.copy()
                for (u,v),full,left in zip(arcs,m,rem):x[u]-=2*(full-left);x[v]+=full-left
                if not any(rem):return () if x==target else None
                for z,(u,v) in enumerate(arcs):
                    if rem[z] and x[u]>=2:
                        rr=list(rem);rr[z]-=1;tail=search(tuple(rr))
                        if tail is not None:return (z,)+tail
                return None
            trace=search(tuple(m));assert trace is not None;moves+=len(trace)
    result=dict(archive_graphs=len(archive),archive_critical_losers=statecount,archive_adjacent_pairs=pairs,archive_unknown=sum(r['status'].endswith('UNKNOWN') for r in archive),private_certificates=private,private_literal_moves=moves,adjacent_small_transfer_tests=small,all_equal=True)
    p=B/'residual_verification.json';raw=(json.dumps(result,indent=2)+'\n').encode()
    if '--check-only' in sys.argv:assert p.read_bytes()==raw
    else:p.write_bytes(raw)
    print(json.dumps(result),flush=True)
if __name__=='__main__':main()
