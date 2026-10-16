"""Independent coordinates, all DAG dependencies, all queries and literal moves."""
import hashlib,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014/onebit');shard=int(sys.argv[1]);D=B/f'shard{shard}'
for pre in [B/'preflight.json',D/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes());graphs=cfg['graphs'];assert len(graphs)==27 and len(cfg['pairs'])==654
for g in graphs:
    n=g['n'];assert 2<=n<=6;E={frozenset(e) for e in g['edges']};assert len(E)==len(g['edges']);color={0:0};todo=[0]
    for u in todo:
        for e in E:
            if u not in e:continue
            v=next(iter(e-{u}));assert 0<=v<n
            if v not in color:color[v]=1-color[u];todo.append(v)
            assert color[v]!=color[u]
    assert len(color)==n
expected=[c for c in cfg['pairs'] if c['id']%2==shard];results=json.loads((D/'results.json').read_bytes());assert len(results)==len(expected);queries=states=moves=negative=0
assert len({(c['graph'],c['source'],c['singleton']) for c in cfg['pairs']})==sum(g['n']*(g['n']-1) for g in graphs)
for c,row in zip(expected,results):
    assert row['pair']==c['id'];g=graphs[c['graph']];n=g['n'];s=c['source'];t=c['singleton'];E={frozenset(e) for e in g['edges']};adj=[[v for v in range(n) if frozenset([u,v]) in E] for u in range(n)];dist={s:0};todo=[s]
    for u in todo:
        for v in adj[u]:
            if v not in dist:dist[v]=dist[u]+1;todo.append(v)
    d=dist[t];assert d==c['distance']>=1 and c['path'][0]==s and c['path'][-1]==t and len(c['path'])==d+1
    assert all(v in adj[u] for u,v in zip(c['path'],c['path'][1:]));A=2**d;Bmin=3*2**(d-1);C=2**(d+1);assert c['constructive_counts']==[A,Bmin,C]
    ss={};raw=lzma.decompress((D/row['certificate']).read_bytes());assert len(raw)%17==0
    for pos in range(0,len(raw),17):
        record=raw[pos:pos+17];assert not any(record[n:16]);x=tuple(record[:n]);assert x not in ss;ss[x]=record[16]
    assert len(ss)==row['states']<=300000;truth={}
    for x,kind in sorted(ss.items(),key=lambda kv:sum(kv[0])):
        if kind==255:assert sum(z>0 for z in x)==1;truth[x]=True;continue
        if kind==254:
            assert sum(z>0 for z in x)>1;negative+=1
            for u in range(n):
                if x[u]<2:continue
                for v in adj[u]:
                    y=list(x);y[u]-=2;y[v]+=1;assert tuple(y) in truth and not truth[tuple(y)]
            truth[x]=False
        else:
            u,v=divmod(kind,n);assert 0<=u<n and v in adj[u] and x[u]>=2;y=list(x);y[u]-=2;y[v]+=1;assert truth[tuple(y)];truth[x]=True
    wanted=list(range(C+1)) if d<=3 else [];assert c['queries']==wanted and [r[0] for r in row['answers']]==wanted
    for N,ok in row['answers']:
        x=tuple(N*int(v==s)+int(v==t) for v in range(n));res=N%3;cut= Bmin if res==0 else A if res==pow(2,d,3) else C;predicted=(N==0 or N>=cut);assert truth[x]==ok==predicted;queries+=1
    assert len(row['constructions'])==3
    for i,r in enumerate(row['constructions']):
        N=c['constructive_counts'][i];assert r['N']==N<=128 and len(r['moves'])<=256;x=[N*int(v==s)+int(v==t) for v in range(n)]
        for u,v in r['moves']:assert v in adj[u] and x[u]>=2;x[u]-=2;x[v]+=1;moves+=1
        q=t if i!=1 else c['path'][-2];k=2 if i<2 else 3;assert x==[k*int(v==q) for v in range(n)]
    states+=len(ss)
out=dict(shard=shard,graphs=27,ordered_pairs=len(results),queries=queries,states=states,negative_states=negative,literal_constructions=3*len(results),literal_moves=moves,all_queries_match_exact_residue_cutoffs=True,scope='Only registered27 graphs and d<=3 negative/positive query ranges; universal theorem100 is symbolic, ASH* OPEN')
(D/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
