import json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/cube_tail');cfg=json.loads((B/'inputs.json').read_bytes());n=16;units=[1<<(8*v) for v in range(n)];arcs=sorted((u,v) for e in cfg['edges'] for u,v in [e,e[::-1]]);memo={};start=time.monotonic();completed=[];status='COMPLETE_AS_TAIL';bad=None;queries=0
def win(x):
    if x in memo:return memo[x]!=65534
    if len(memo)>=cfg['state_cap']:raise RuntimeError('STATE_CAP_UNKNOWN')
    if len(memo)%1000==0 and time.monotonic()-start>540:raise RuntimeError('TIME_BOUND_UNKNOWN')
    if sum(bool((x>>(8*v))&255) for v in range(n))==1:memo[x]=65535;return True
    for u,v in arcs:
        if ((x>>(8*u))&255)>=2 and win(x-2*units[u]+units[v]):memo[x]=u*n+v;return True
    memo[x]=65534;return False
try:
    for mass in cfg['masses']:
        for mask in cfg['masks']:
            if time.monotonic()-start>540:raise RuntimeError('TIME_BOUND_UNKNOWN')
            x=(mass-mask.bit_count())*units[0]+sum(units[i+1] for i in range(15) if mask>>i&1);ok=win(x);completed.append([mass,mask,ok]);queries+=1
            if not ok:bad=dict(mass=mass,mask=mask,input=[(x>>(8*v))&255 for v in range(n)]);status='AS_LOSER_FOUND_REJECT_T31';break
        if bad:break
except RuntimeError as e:status=str(e)
with lzma.open(B/'states.bin.xz','wb') as f:
    for x,k in sorted(memo.items()):f.write(x.to_bytes(16,'little')+struct.pack('<H',k))
(B/'queries.json').write_text(json.dumps(completed,separators=(',',':'))+'\n',encoding='utf-8',newline='\n');out=dict(status=status,queries=queries,states=len(memo),bad=bad,seconds=time.monotonic()-start,scope='AS only, no general threshold or universal ASH* conclusion');(B/'result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
