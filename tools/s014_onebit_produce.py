"""Packed forward DAG and designated source-group path constructions."""
import json,lzma,sys,time
from pathlib import Path
B=Path('evidence/S014/onebit');shard=int(sys.argv[1]);D=B/f'shard{shard}';D.mkdir(exist_ok=True);cfg=json.loads((B/'inputs.json').read_bytes());start=time.monotonic();results=[];queries=0
for case in cfg['pairs']:
    if case['id']%2!=shard:continue
    assert time.monotonic()-start<540
    g=cfg['graphs'][case['graph']];n=g['n'];s=case['source'];t=case['singleton'];d=case['distance'];units=[1<<(8*i) for i in range(n)];arcs=sorted((u,v) for e in g['edges'] for u,v in [e,e[::-1]]);memo={}
    def win(x):
        if x in memo:return memo[x]!=254
        assert len(memo)<300000 and time.monotonic()-start<540
        if sum(bool((x>>(8*i))&255) for i in range(n))==1:memo[x]=255;return True
        for u,v in arcs:
            if ((x>>(8*u))&255)>=2 and win(x-2*units[u]+units[v]):memo[x]=u*n+v;return True
        memo[x]=254;return False
    answers=[]
    for N in case['queries']:
        ok=win(N*units[s]+units[t]);queries+=1;assert queries<=12000;answers.append([N,ok])
    dest=D/f"pair{case['id']:04d}.bin.xz"
    with lzma.open(dest,'wb') as f:
        for x in sorted(memo):f.write(x.to_bytes(16,'little')+bytes([memo[x]]))
    constructions=[]
    for k,N in enumerate(case['constructive_counts']):
        moves=[]
        def group(path):
            length=len(path)-1
            for i,(u,v) in enumerate(zip(path,path[1:])):moves.extend([[u,v]]*(2**(length-i-1)))
        if k==0:group(case['path'])
        elif k==1:group(case['path']);group(case['path'][:-1]);moves.append([t,case['path'][-2]])
        else:group(case['path']);group(case['path'])
        assert len(moves)<=256 and N<=128;constructions.append(dict(N=N,moves=moves))
    results.append(dict(pair=case['id'],states=len(memo),answers=answers,certificate=dest.name,constructions=constructions))
(D/'results.json').write_text(json.dumps(results,separators=(',',':'))+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(shard=shard,pairs=len(results),queries=queries,states=sum(r['states'] for r in results),seconds=time.monotonic()-start)))
