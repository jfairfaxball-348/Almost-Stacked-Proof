import array,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/cube_general');S=Path('evidence/S014/cube_dag');cfg=json.loads((B/'inputs.json').read_bytes());choices=json.loads((S/'choices.json').read_bytes());raw=lzma.decompress((S/'nodes.bin.xz').read_bytes());nodes=list(struct.iter_unpack('<IBBH',raw));units=[1<<(8*v) for v in range(16)];P=[1<<v.bit_count() for v in range(16)];memo={};anchors={};start=time.monotonic();before=0;results=[];status='COMPLETE_REGISTERED_CASES';potential=None
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
        if len(memo)>=2000000:raise RuntimeError('GLOBAL_STATE_CAP_UNKNOWN')
        if len(memo)-before>=300000:raise RuntimeError('QUERY_STATE_CAP_UNKNOWN')
    if len(memo)%1000==0 and time.monotonic()-start>540:raise RuntimeError('TIME_BOUND_UNKNOWN')
    memo[x]=k
def win(x):
    if x in memo:return memo[x] not in [65534,65532]
    if len(memo)>=2000000:raise RuntimeError('GLOBAL_STATE_CAP_UNKNOWN')
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
for case in cfg['candidates']:
    if time.monotonic()-start>540:status='TIME_BOUND_UNKNOWN';break
    before=len(memo);x=sum(a*units[v] for v,a in enumerate(case['c']))
    try:ok=win(x);result=dict(id=case['id'],winning=ok)
    except RuntimeError as e:
        result=dict(id=case['id'],winning=None,status=str(e));results.append(result)
        if str(e)!='QUERY_STATE_CAP_UNKNOWN':status=str(e);break
        continue
    results.append(result)
    if not ok:potential=case;status='POTENTIAL_ACTUAL_COUNTEREXAMPLE';break
    if len(results)%100==0:(B/'progress.json').write_text(json.dumps(dict(cases=len(results),states=len(memo),seconds=time.monotonic()-start))+'\n',encoding='utf-8',newline='\n')
with lzma.open(B/'states.bin.xz','wb') as f:
    for x,k in sorted(memo.items()):f.write(x.to_bytes(16,'little')+struct.pack('<H',k))
with lzma.open(B/'anchors.bin.xz','wb') as f:
    for x,moves in sorted(anchors.items()):f.write(x.to_bytes(16,'little')+bytes([len(moves)])+moves)
(B/'results.json').write_text(json.dumps(results,separators=(',',':'))+'\n',encoding='utf-8',newline='\n');out=dict(status=status,candidates=len(cfg['candidates']),completed=len(results),winners=sum(r['winning'] is True for r in results),unknown=sum(r['winning'] is None for r in results),states=len(memo),literal_AS_anchors=len(anchors),potential=potential,seconds=time.monotonic()-start,scope='Only frozen candidates; no general threshold from winning samples');(B/'result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
