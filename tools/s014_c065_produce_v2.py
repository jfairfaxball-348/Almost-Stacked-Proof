import heapq,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/fano_AS');cfg=json.loads((B/'inputs.json').read_bytes());n=cfg['n'];limit=1<<(n-1);start=time.monotonic();adj=[[v for u,v in cfg['arcs'] if u==q] for q in range(n)];dist={0:0};todo=[0]
for u in todo:
    for v in adj[u]:
        if v not in dist:dist[v]=dist[u]+1;todo.append(v)
assert len(dist)==n;P=[1<<dist[v] for v in range(n)];INF=10**8;plus=[P.copy()];anytree=[P.copy()];two=[[2*x for x in P]];three=[[3*x for x in P]];porig=[[(0,0,0)]*n];torig=[[(7,0,0)]*n];forig=[[(8,0,0)]*n];status='COMPLETE_POSITIVE_TABLE';first_missing=None
try:
    for mask in range(1,limit):
        if time.monotonic()-start>540:raise RuntimeError('TIME_BOUND_UNKNOWN')
        pair=[INF]*n;pa=[0]*n;a=(mask-1)&mask
        while a:
            b=mask^a
            if a<b:
                aa=anytree[a];bb=anytree[b]
                for q in range(n):
                    z=aa[q]+bb[q]
                    if z<pair[q]:pair[q]=z;pa[q]=a
            a=(a-1)&mask
        pc=[INF]*n;pr=[None]*n
        for u in range(n):
            if pair[u]==INF:continue
            for q in adj[u]:
                if pair[u]<pc[q]:pc[q]=pair[u];pr[q]=(2,u,pa[u])
        if mask&(mask-1)==0:
            u=mask.bit_length()
            for q in adj[u]:
                if P[u]<pc[q]:pc[q]=P[u];pr[q]=(3,u,0)
        heap=[(pc[q],q) for q in range(n) if pc[q]!=INF];heapq.heapify(heap)
        while heap:
            cost,u=heapq.heappop(heap)
            if cost!=pc[u]:continue
            z=cost+P[u]
            for q in adj[u]:
                if z<pc[q]:pc[q]=z;pr[q]=(1,u,0);heapq.heappush(heap,(z,q))
        assert all(0<z<=1024 for z in pc) and all(pr)
        ac=pc.copy()
        if mask&(mask-1)==0:ac[mask.bit_length()]=0
        tc=[];tr=[]
        for q in range(n):
            if pair[q]<ac[q]+P[q]:tc.append(pair[q]);tr.append((5,0,pa[q]))
            else:tc.append(ac[q]+P[q]);tr.append((4,0,0))
        fc=[P[q]+tc[q] for q in range(n)];fr=[(6,0,0)]*n
        for q in range(n):
            if ac[q]+2*P[q]<fc[q]:fc[q]=ac[q]+2*P[q];fr[q]=(6,0,mask)
        a=(mask-1)&mask
        while a:
            b=mask^a
            if a<b:
                aa=anytree[a];bb=anytree[b];ta=two[a];tb=two[b]
                for q in range(n):
                    z=aa[q]+tb[q]
                    if z<fc[q]:fc[q]=z;fr[q]=(6,0,a)
                    z=bb[q]+ta[q]
                    if z<fc[q]:fc[q]=z;fr[q]=(6,0,b)
            a=(a-1)&mask
        assert all(0<z<=1024 for z in tc+fc)
        plus.append(pc);anytree.append(ac);two.append(tc);three.append(fc);porig.append(pr);torig.append(tr);forig.append(fr)
        if mask%256==0:(B/'progress.json').write_text(json.dumps(dict(completed_masks=len(plus),seconds=time.monotonic()-start))+'\n',encoding='utf-8',newline='\n')
except RuntimeError as e:status=str(e)
count=len(plus);choices=[]
for mask in range(count):
    row=[]
    for residue in range(3):
        candidates=[(table[mask][q],q,k) for k,table in [(1,plus),(2,two),(3,three)] for q in range(n) if table[mask][q]%3==residue];assert candidates;row.append(min(candidates))
    choices.append(row)
with lzma.open(B/'nodes.bin.xz','wb') as f:
    for mask in range(count):
        for table,origins in [(plus,porig),(two,torig),(three,forig)]:
            for q in range(n):kind,u,a=origins[mask][q];f.write(struct.pack('<IBBH',table[mask][q],kind,u,a))
(B/'choices.json').write_text(json.dumps(choices,separators=(',',':'))+'\n',encoding='utf-8',newline='\n')
if count==limit:status='COMPLETE_POSITIVE_TABLE'
out=dict(status=status,completed_masks=count,nodes=count*3*n,first_missing=first_missing,seconds=time.monotonic()-start,scope='Positive witnesses only; missing witness does not prove loss');(B/'result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
