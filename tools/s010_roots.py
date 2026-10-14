"""CAM-S010-02 complete forward rooted masks for fixed compatibility obligations."""
import hashlib
import json
import lzma
import sys
import time
from pathlib import Path

GRAPHS=[('K2',2,[(0,1)],{'stack':3}),('K3',3,[(0,1),(0,2),(1,2)],{'stack':4,'clear':4}),
 ('P4',4,[(0,1),(1,2),(2,3)],{'stack':15}),
 ('C5',5,[(0,1),(1,2),(2,3),(3,4),(0,4)],{'stack':8,'clear':10}),
 ('triangle_tail2',5,[(0,1),(0,2),(1,2),(0,3),(3,4)],{'stack':16,'clear':22}),
 ('F2',5,[(0,1),(0,2),(1,2),(0,3),(0,4)],{'stack':11,'clear':13}),
 ('bowtie',5,[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)],{'stack':8,'clear':8}),
 ('diamond',4,[(0,1),(0,2),(0,3),(1,2),(2,3)],{'stack':7,'clear':7})]

def configurations(n,t):
    if n==1:yield (t,);return
    for a in range(t+1):
        for tail in configurations(n-1,t-a):yield (a,)+tail

def main():
    start=time.monotonic();tables=[];summary=[]
    for name,n,edges,goals in GRAPHS:
        arcs=[a for e in edges for a in (e,e[::-1])]
        for goal,g in goals.items():
            old={};layers=[];layer_meta=[];critical=None
            for t in range(1,g+1):
                current={}
                for c in configurations(n,t):
                    occupied=[v for v,x in enumerate(c) if x]
                    mask=(1<<occupied[0]) if len(occupied)==1 and (goal=='stack' or t==1) else 0
                    for u,v in arcs:
                        if c[u]>=2:
                            d=list(c);d[u]-=2;d[v]+=1;mask|=old[tuple(d)]
                    current[c]=mask
                assert len(current)<=300000
                rows=sorted(current.items());raw=json.dumps(rows,separators=(',',':')).encode()
                layers.append(rows);layer_meta.append({'mass':t,'configurations':len(rows),'losers':sum(mask==0 for _,mask in rows),
                                                     'root_mask_sha256':hashlib.sha256(raw).hexdigest()})
                if t==g-1:critical=sorted(c for c,m in current.items() if m==0)
                old=current
            assert critical and all(old.values()) and g>n
            common=(1<<n)-1;missing={}
            for c,mask in sorted(old.items()):
                common&=mask
                for q in range(n):
                    if not mask&(1<<q) and q not in missing:missing[q]=c
            crit_rows=[]
            for c in critical:
                masks=[]
                for w in range(n):
                    d=list(c);d[w]+=1;masks.append(old[tuple(d)])
                intersection=(1<<n)-1
                for m in masks:intersection&=m
                crit_rows.append({'c':c,'AS':sum(x>1 for x in c)<=1,'Q':sum(x*x for x in c),
                                  'insertion_masks':masks,'common_roots':intersection,
                                  'occupied_self_failures':[w for w in range(n) if c[w]>0 and not masks[w]&(1<<w)],
                                  'heavy_self_failures':[w for w in range(n) if c[w]>1 and not masks[w]&(1<<w)]})
            top=max(r['Q'] for r in crit_rows)
            row={'graph':name,'goal':goal,'n':n,'edges':edges,'threshold':g,'layers':layer_meta,'critical':crit_rows,
                 'whole_threshold_common_roots':common,'whole_threshold_missing_root_witnesses':missing,
                 'critical_losers':len(critical),'non_AS_critical':sum(not r['AS'] for r in crit_rows),
                 'critical_empty_insertion_intersection':sum(not r['common_roots'] for r in crit_rows),
                 'non_AS_empty_insertion_intersection':sum(not r['AS'] and not r['common_roots'] for r in crit_rows),
                 'occupied_self_failure_configs':sum(bool(r['occupied_self_failures']) for r in crit_rows),
                 'heavy_self_failure_configs':sum(bool(r['heavy_self_failures']) for r in crit_rows),
                 'Q_max':top,'Q_max_all_AS':all(r['AS'] for r in crit_rows if r['Q']==top)}
            summary.append(row);tables.append({'graph':name,'goal':goal,'layers':layers})
            assert time.monotonic()-start<600
    raw=json.dumps(tables,separators=(',',':')).encode()
    out={'campaign':'CAM-S010-02','cases':summary,'case_count':len(summary),
         'complete_layers':sum(len(r['layers']) for r in summary),
         'complete_configurations':sum(x['configurations'] for r in summary for x in r['layers']),
         'table_raw_sha256':hashlib.sha256(raw).hexdigest(),'seconds':time.monotonic()-start,
         'scope':'EXPLICIT_EIGHT_GRAPHS_FOURTEEN_GOAL_CASES_ONLY'}
    dest=Path('evidence/S010/root_tables.json.xz');mp=Path('evidence/S010/root_summary.json')
    if '--check-only' in sys.argv:
        assert lzma.decompress(dest.read_bytes())==raw
        old=json.loads(mp.read_text(encoding='utf-8'));actual=json.loads(json.dumps(out))
        assert {k:v for k,v in old.items() if k!='seconds'}=={k:v for k,v in actual.items() if k!='seconds'}
    else:
        dest.write_bytes(lzma.compress(raw));mp.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'}),flush=True)
    for r in summary:print(json.dumps({k:r[k] for k in ('graph','goal','threshold','whole_threshold_common_roots','critical_losers','non_AS_critical','critical_empty_insertion_intersection','non_AS_empty_insertion_intersection','heavy_self_failure_configs')}),flush=True)

if __name__=='__main__':main()
