from pathlib import Path
t=Path('tools/s014_cube_general_produce.py').read_text(encoding='utf-8');prefix=t[:t.index("for case in cfg['candidates']:")].replace('import array,json,lzma,struct,time','import array,json,lzma,struct,time,sys').replace("B=Path('evidence/S014/cube_general')","B=Path('evidence/S014/cube_pointwise')/('shard'+sys.argv[1])").replace("cfg=json.loads((B/'inputs.json').read_bytes())","cfg=json.loads((B.parent/'inputs.json').read_bytes())").replace("before=0;results=[]","before=0;totalstates=0;stored=0;results=[]")
prefix=prefix.replace("        if len(memo)>=2000000:raise RuntimeError('GLOBAL_STATE_CAP_UNKNOWN')","        if totalstates+len(memo)>=8000000:raise RuntimeError('AGGREGATE_STATE_CAP_UNKNOWN')")
prefix=prefix.replace("    if len(memo)>=2000000:raise RuntimeError('GLOBAL_STATE_CAP_UNKNOWN')","    if totalstates+len(memo)>=8000000:raise RuntimeError('AGGREGATE_STATE_CAP_UNKNOWN')")
tail=r'''
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
'''
Path('tools/s014_cube_pointwise_produce.py').write_text(prefix+tail,encoding='utf-8',newline='\n')
t=Path('tools/s014_cube_general_verify.py').read_text(encoding='utf-8').replace('import hashlib,itertools,json,lzma,struct,time','import hashlib,itertools,json,lzma,struct,time,sys').replace("B=Path('evidence/S014/cube_general')","B=Path(sys.argv[1])")
Path('tools/s014_cube_pointwise_potential_verify.py').write_text(t,encoding='utf-8',newline='\n');print('CAM61 separate pointwise producer and saved independent potential checker')
