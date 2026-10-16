import array,json,lzma,struct,time,sys
from pathlib import Path
B=Path('evidence/S014/cube_pointwise')/('shard'+sys.argv[1]);S=Path('evidence/S014/cube_dag');cfg=json.loads((B.parent/'inputs.json').read_bytes());choices=json.loads((S/'choices.json').read_bytes());raw=lzma.decompress((S/'nodes.bin.xz').read_bytes());nodes=list(struct.iter_unpack('<IBBH',raw));units=[1<<(8*v) for v in range(16)];P=[1<<v.bit_count() for v in range(16)];memo={};anchors={};start=time.monotonic();before=0;totalstates=0;stored=0;results=[];status='COMPLETE_REGISTERED_CASES';potential=None
def node(mask,typ,q):return nodes[(mask*3+typ)*16+q]
def literal(mask,typ,q,moves):
    if mask==0:
        for _ in range(typ+1):pure(q,moves)
        return
    cost,kind,u,a=node(mask,typ,q)
    if typ==0:
        if kind==1:literal(mask,0,u,moves);pure(u,moves);moves.append(u*16+q)
        elif kind==2:anytree(a,u,moves);anytree(mask^a,u,moves);moves.append(u*16+q)
        else:assert kind==3;pure(u,moves);moves.append(u*16+q)
    elif typ==1:
        if kind==4:anytree(mask,q,moves);pure(q,moves)
        else:assert kind==5;anytree(a,q,moves);anytree(mask^a,q,moves)
    else:assert kind==6;anytree(a,q,moves);literal(mask^a,1,q,moves)
def anytree(mask,q,moves):
    if q>0 and mask==1<<(q-1):return
    literal(mask,0,q,moves)
def pure(q,moves):
    if q==0:return
    u=q&(q-1);pure(u,moves);pure(u,moves);moves.append(u*16+q)
def put(x,k):
    if x not in memo:
        if totalstates+len(memo)>=8000000:raise RuntimeError('AGGREGATE_STATE_CAP_UNKNOWN')
        if len(memo)-before>=300000:raise RuntimeError('QUERY_STATE_CAP_UNKNOWN')
    if len(memo)%1000==0 and time.monotonic()-start>540:raise RuntimeError('TIME_BOUND_UNKNOWN')
    memo[x]=k
def win(x):
    if x in memo:return memo[x] not in [65534,65532]
    if totalstates+len(memo)>=8000000:raise RuntimeError('AGGREGATE_STATE_CAP_UNKNOWN')
    if len(memo)-before>=300000:raise RuntimeError('QUERY_STATE_CAP_UNKNOWN')
    c=[(x>>(8*v))&255 for v in range(16)];occupied=[v for v in range(16) if c[v]]
    if len(occupied)==1:put(x,65535);return True
    heavy=[v for v in occupied if c[v]>=2]
    if len(heavy)==1:
        s=heavy[0];N=c[s];mask=sum(1<<((v^s)-1) for v in occupied if v!=s);cost,q,k=choices[mask][N%3]
        if N<cost:put(x,65532);return False
        moves=[]
        for _ in range((N-cost)//3):moves.extend([1,1,16])
        literal(mask,k-1,q,moves);translated=bytes(((code//16)^s)*16+((code%16)^s) for code in moves);assert len(translated)<=100;y=c.copy()
        for code in translated:u,v=divmod(code,16);assert y[u]>=2 and (u^v).bit_count()==1;y[u]-=2;y[v]+=1
        assert sum(z>0 for z in y)==1;put(x,65533);anchors[x]=translated;return True
    for u in sorted(heavy,key=lambda u:-c[u]):
        if c[u]>=4 and win(x-3*units[u]):put(x,256+u);return True
    moves=sorted(((u,u^(1<<j)) for u in heavy for j in range(4)),key=lambda uv:(0 if c[uv[1]]>=2 else 1 if c[uv[1]] else 2,-c[uv[1]],c[uv[0]],uv))
    for u,v in moves:
        if win(x-2*units[u]+units[v]):put(x,u*16+v);return True
    put(x,65534);return False

B.mkdir(exist_ok=True);shard=int(sys.argv[1]);selected=[c for c in cfg['candidates'] if c['id']%2==shard]
def preserve(case,ok,error=None):
    global stored
    D=B/('case'+str(case['id']));D.mkdir(exist_ok=True)
    with lzma.open(D/'states.bin.xz','wb') as f:
        for x,k in sorted(memo.items()):f.write(x.to_bytes(16,'little')+struct.pack('<H',k))
    with lzma.open(D/'anchors.bin.xz','wb') as f:
        for x,ms in sorted(anchors.items()):f.write(x.to_bytes(16,'little')+bytes([len(ms)])+ms)
    local=dict(case);local['original_id']=local['id'];local['id']=0;localcfg=dict(cfg);localcfg['candidates']=[local]
    (D/'inputs.json').write_text(json.dumps(localcfg,separators=(',',':'))+'\n',encoding='utf-8',newline='\n')
    (D/'results.json').write_text(json.dumps([dict(id=0,winning=ok,**(dict(status=error) if error else {}))])+'\n',encoding='utf-8',newline='\n')
    (D/'result.json').write_text(json.dumps(dict(status=error or 'POTENTIAL_ACTUAL_COUNTEREXAMPLE',completed=1,states=len(memo),potential=local if ok is False else None))+'\n',encoding='utf-8',newline='\n');stored+=len(memo);return D.as_posix()
for case in selected:
    if time.monotonic()-start>540:status='TIME_BOUND_UNKNOWN';break
    if totalstates>=8000000:status='AGGREGATE_STATE_CAP_UNKNOWN';break
    if stored>1700000:status='PARTIAL_STORAGE_CAP_UNKNOWN';break
    memo={};anchors={};before=0;x=sum(a*units[v] for v,a in enumerate(case['c']))
    try:ok=win(x)
    except RuntimeError as e:
        totalstates+=len(memo);location=preserve(case,None,str(e));results.append(dict(id=case['id'],winning=None,status=str(e),states=len(memo),partial=location))
        if str(e)!='QUERY_STATE_CAP_UNKNOWN':status=str(e);break
        continue
    totalstates+=len(memo)
    if not ok:
        potential=case;location=preserve(case,False);results.append(dict(id=case['id'],winning=False,states=len(memo),potential_certificate=location));status='POTENTIAL_ACTUAL_COUNTEREXAMPLE';break
    moves=[]
    while memo[x]!=65535:
        k=memo[x]
        if k==65533:
            for code in anchors[x]:u,v=divmod(code,16);moves.append(code);x=x-2*units[u]+units[v]
            break
        if 256<=k<272:
            u=k-256;w=u^1;moves.extend([u*16+w,u*16+w,w*16+u]);x-=3*units[u]
        else:u,v=divmod(k,16);moves.append(k);x=x-2*units[u]+units[v]
    assert len(moves)<=100 and sum(bool((x>>(8*v))&255) for v in range(16))==1;results.append(dict(id=case['id'],winning=True,moves=moves,states=len(memo)))
    if len(results)%100==0:(B/'progress.json').write_text(json.dumps(dict(cases=len(results),cumulative_states=totalstates,seconds=time.monotonic()-start))+'\n',encoding='utf-8',newline='\n')
(B/'results.json').write_text(json.dumps(results,separators=(',',':'))+'\n',encoding='utf-8',newline='\n');out=dict(shard=shard,status=status,selected_candidates=len(selected),completed=len(results),winning=sum(r['winning'] is True for r in results),unknown=sum(r['winning'] is None for r in results),cumulative_states=totalstates,retained_partial_states=stored,potential=potential,seconds=time.monotonic()-start,scope='Pointwise literal winners only; caps/suffix UNKNOWN, no full threshold');(B/'result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
