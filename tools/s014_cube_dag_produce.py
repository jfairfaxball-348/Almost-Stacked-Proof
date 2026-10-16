"""Positive witness producer only; independent checker never trusts minima."""
import heapq,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/cube_dag');cfg=json.loads((B/'inputs.json').read_bytes());start=time.monotonic();P=[1<<v.bit_count() for v in range(16)];adj=[[u^(1<<i) for i in range(4)] for u in range(16)];INF=10**8;plus=[P.copy()];anytree=[P.copy()];two=[[2*x for x in P]];three=[[3*x for x in P]];porig=[[(0,0,0)]*16];torig=[[(7,0,0)]*16];forig=[[(8,0,0)]*16];status='COMPLETE_POSITIVE_TABLE';first_missing=None
try:
    for mask in range(1,32768):
        if time.monotonic()-start>540:raise RuntimeError('TIME_BOUND_UNKNOWN')
        pair=[INF]*16;pa=[0]*16;a=(mask-1)&mask
        while a:
            b=mask^a
            if a<b:
                aa=anytree[a];bb=anytree[b]
                for q in range(16):
                    z=aa[q]+bb[q]
                    if z<pair[q]:pair[q]=z;pa[q]=a
            a=(a-1)&mask
        pc=[INF]*16;pr=[None]*16
        for u in range(16):
            if pair[u]==INF:continue
            for q in adj[u]:
                if pair[u]<pc[q]:pc[q]=pair[u];pr[q]=(2,u,pa[u])
        if mask&(mask-1)==0:
            u=mask.bit_length()
            for q in adj[u]:
                if P[u]<pc[q]:pc[q]=P[u];pr[q]=(3,u,0)
        heap=[(pc[q],q) for q in range(16) if pc[q]!=INF];heapq.heapify(heap)
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
        for q in range(16):
            if pair[q]<ac[q]+P[q]:tc.append(pair[q]);tr.append((5,0,pa[q]))
            else:tc.append(ac[q]+P[q]);tr.append((4,0,0))
        fc=[P[q]+tc[q] for q in range(16)];fr=[(6,0,0)]*16
        for q in range(16):
            if ac[q]+2*P[q]<fc[q]:fc[q]=ac[q]+2*P[q];fr[q]=(6,0,mask)
        a=(mask-1)&mask
        while a:
            b=mask^a
            if a<b:
                aa=anytree[a];bb=anytree[b];ta=two[a];tb=two[b]
                for q in range(16):
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
        candidates=[(table[mask][q],q,k) for k,table in [(1,plus),(2,two),(3,three)] for q in range(16) if table[mask][q]%3==residue];assert candidates;row.append(min(candidates))
    choices.append(row)
    for mass in [31,32,33]:
        N=mass-mask.bit_count();cost,q,k=row[N%3]
        if cost>N and first_missing is None:first_missing=dict(mask=mask,mass=mass,N=N,certified_cost=cost,q=q,k=k)
with lzma.open(B/'nodes.bin.xz','wb') as f:
    for mask in range(count):
        for table,origins in [(plus,porig),(two,torig),(three,forig)]:
            for q in range(16):kind,u,a=origins[mask][q];f.write(struct.pack('<IBBH',table[mask][q],kind,u,a))
(B/'choices.json').write_text(json.dumps(choices,separators=(',',':'))+'\n',encoding='utf-8',newline='\n')
if count==32768:status='UPPER_WITNESS_MISSING_UNKNOWN' if first_missing else 'COMPLETE_AS_TAIL_UPPER31'
out=dict(status=status,completed_masks=count,nodes=count*48,first_missing=first_missing,seconds=time.monotonic()-start,scope='Positive witnesses only; missing witness does not prove loss');(B/'result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
