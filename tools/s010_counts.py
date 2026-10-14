"""CAM-S010-01 complete count-box connected ancestry certificates; no reachability."""
import hashlib
import json
import lzma
import sys
import time
from pathlib import Path

GRAPHS=[('K2',2,[(0,1)]),('P3',3,[(0,1),(0,2)]),('K3',3,[(0,1),(0,2),(1,2)]),
        ('triangle_leaf',4,[(0,1),(0,2),(1,2),(0,3)]),
        ('bowtie',5,[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)]),
        ('diamond',4,[(0,1),(0,2),(0,3),(1,2),(2,3)])]

def vectors(d,total):
    if d==1: yield (total,);return
    for x in range(total+1):
        for rest in vectors(d-1,total-x):yield (x,)+rest

def condition(n,arcs,m,c,q):
    used={q}|{v for v,x in enumerate(c) if x}
    reverse={v:set() for v in range(n)};weak={v:set() for v in range(n)}
    for (u,v),x in zip(arcs,m):
        if x:used|={u,v};reverse[v].add(u);weak[u].add(v);weak[v].add(u)
    def reach(adj):
        rank={q:0};todo=[q]
        for v in todo:
            for u in sorted(adj[v]):
                if u not in rank:rank[u]=rank[v]+1;todo.append(u)
        return rank
    ranks=reach(reverse);wr=reach(weak)
    return used<=ranks.keys(),used<=wr.keys(),[ranks.get(v,-1) for v in range(n)]

def main():
    start=time.monotonic();results=[];meta=[];transfers=[]
    for name,n,edges in GRAPHS:
        arcs=[a for u,v in edges for a in ((u,v),(v,u))];local=[];swap_stats={}
        for total in range(6):
            for m in vectors(len(arcs),total):
                balance=[0]*n
                for (u,v),x in zip(arcs,m):balance[u]+=2*x;balance[v]-=x
                for q in range(n):
                    for k in range(1,5):
                        c=balance.copy();c[q]+=k
                        if min(c)<0:continue
                        conn,weak,ranks=condition(n,arcs,m,c,q)
                        row={'m':m,'q':q,'k':k,'c':c,'connected':conn,'weak':weak,'ranks':ranks}
                        local.append(row)
                        if conn:
                            for i,(u,v) in enumerate(arcs):
                                if not m[i]:continue
                                mm=list(m);mm[i]-=1;mm[i^1]+=1
                                cc=c.copy();cc[u]-=3;cc[v]+=3
                                if min(cc)<0: tag='NEGATIVE_INPUT'
                                else:
                                    ok,_,_=condition(n,arcs,mm,cc,q)
                                    tag='CONNECTED_REVERSAL' if ok else 'ROOT_CONNECTION_LOST'
                                swap_stats[tag]=swap_stats.get(tag,0)+1
                                if tag not in {r['tag'] for r in transfers if r['graph']==name}:
                                    transfers.append({'graph':name,'tag':tag,'before':row,'arc':[u,v],'after_m':mm,'after_c':cc})
        assert len(local)<=300000 and time.monotonic()-start<600
        results.append({'graph':name,'certificates':local})
        meta.append({'graph':name,'n':n,'edges':edges,'arcs':arcs,'certificates':len(local),
                     'connected':sum(r['connected'] for r in local),'weak_only':sum(r['weak'] and not r['connected'] for r in local),
                     'reversals':swap_stats})
    raw=json.dumps(results,separators=(',',':')).encode()
    summary={'campaign':'CAM-S010-01','graphs':meta,'certificates':sum(r['certificates'] for r in meta),
             'connected':sum(r['connected'] for r in meta),'weak_only':sum(r['weak_only'] for r in meta),
             'certificate_raw_sha256':hashlib.sha256(raw).hexdigest(),'reversal_examples':transfers,
             'scope':'ALL_COUNTS_SUM_LE_5_ROOTS_AND_FINAL_PILES_1_TO_4_NONNEGATIVE_INPUTS_ONLY',
             'threshold_claims':0,'seconds':time.monotonic()-start}
    dest=Path('evidence/S010/count_certificates.json.xz');mp=Path('evidence/S010/count_summary.json')
    if '--check-only' in sys.argv:
        assert lzma.decompress(dest.read_bytes())==raw
        old=json.loads(mp.read_text(encoding='utf-8'));actual=json.loads(json.dumps(summary))
        assert {k:v for k,v in old.items() if k!='seconds'}=={k:v for k,v in actual.items() if k!='seconds'}
    else:
        dest.write_bytes(lzma.compress(raw));mp.write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in summary.items() if k not in ('graphs','reversal_examples')}),flush=True)

if __name__=='__main__':main()
