import hashlib,json
from pathlib import Path
B=Path('evidence/S014/fano_AS');B.mkdir(exist_ok=True)
def dot(a,b):return (a&b).bit_count()%2
edges=[[p-1,7+l-1] for p in range(1,8) for l in range(1,8) if dot(p,l)==0];maps=[]
for a in range(1,8):
    for b in range(1,8):
        if b==a:continue
        for c in range(1,8):
            if c in [a,b,a^b]:continue
            f=[0]*14
            for x in range(1,8):f[x-1]=((a if x&1 else 0)^(b if x&2 else 0)^(c if x&4 else 0))-1
            for l in range(1,8):
                rs=[r for r in range(1,8) if dot(a,r)==(l&1) and dot(b,r)==((l>>1)&1) and dot(c,r)==((l>>2)&1)];assert len(rs)==1;f[7+l-1]=7+rs[0]-1
            maps.append(f);maps.append([v+7 if v<7 else v-7 for v in f])
assert len({tuple(f) for f in maps})==336 and len(edges)==21;source_maps=[next(f for f in maps if f[0]==v) for v in range(14)];cfg=dict(n=14,graph='FanoInc14',edges=edges,arcs=sorted((u,v) for e in edges for u,v in [e,e[::-1]]),source=0,masks=list(range(8192)),maps=maps,source_maps=source_maps,node_cap=344064,cost_cap=1024);(B/'inputs.json').write_text(json.dumps(cfg,separators=(',',':'))+'\n',encoding='utf-8',newline='\n');plan=Path('sessions/S014/PLAN_AMENDMENT_65.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files=[B/'inputs.json',plan,plan.with_suffix('.sha256'),Path('research/S014_BINARY_BUFFER_UPPER_CERTIFICATES.md'),Path('research/S014_BINARY_BUFFER_LOWER_ANNOTATIONS.md'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_c065_*')];(B/'preflight.json').write_text(json.dumps(dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}),indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM65 exact14-vertex/336-map/all8192-buffer inputs frozen')
