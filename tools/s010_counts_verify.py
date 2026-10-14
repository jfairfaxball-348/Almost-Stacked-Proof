"""Independent complete fixed-count chronology and unrestricted closures, no producer import."""
import hashlib
import itertools
import json
import lzma
import sys
import time
from collections import deque
from functools import lru_cache
from pathlib import Path

GRAPHS={'K2':(2,[(0,1)]),'P3':(3,[(0,1),(0,2)]),'K3':(3,[(0,1),(0,2),(1,2)]),
        'triangle_leaf':(4,[(0,1),(0,2),(1,2),(0,3)]),
        'bowtie':(5,[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)]),
        'diamond':(4,[(0,1),(0,2),(0,3),(1,2),(2,3)])}

def counts(d,t):
    for cuts in itertools.combinations(range(t+d-1),d-1):
        marks=(-1,)+cuts+(t+d-1,)
        yield tuple(marks[i+1]-marks[i]-1 for i in range(d))

def order(c,arcs,m,q,k):
    @lru_cache(None)
    def solve(rem):
        state=list(c)
        for (u,v),total,left in zip(arcs,m,rem):
            used=total-left;state[u]-=2*used;state[v]+=used
        assert min(state)>=0
        if not sum(rem):
            assert state==[k if v==q else 0 for v in range(len(c))]
            return ()
        for i,(u,v) in enumerate(arcs):
            if rem[i] and state[u]>=2:
                rr=list(rem);rr[i]-=1
                rest=solve(tuple(rr))
                if rest is not None:return (i,)+rest
        return None
    result=solve(tuple(m));assert solve.cache_info().currsize<=300000
    return result,solve.cache_info().currsize

def closure(c,arcs):
    seen={tuple(c)};todo=deque(seen);cm=sm=0
    while todo:
        state=todo.popleft();occupied=[v for v,x in enumerate(state) if x]
        if len(occupied)==1:
            sm|=1<<occupied[0]
            if sum(state)==1:cm|=1<<occupied[0]
        for u,v in arcs:
            if state[u]<2:continue
            nxt=list(state);nxt[u]-=2;nxt[v]+=1;nxt=tuple(nxt)
            if nxt not in seen:seen.add(nxt);todo.append(nxt)
        assert len(seen)<=300000
    return {'states':len(seen),'clear_mask':cm,'stack_mask':sm,
            'sha256':hashlib.sha256(json.dumps(sorted(seen),separators=(',',':')).encode()).hexdigest()}

def main():
    start=time.monotonic();raw=lzma.decompress(Path('evidence/S010/count_certificates.json.xz').read_bytes())
    produced=json.loads(raw);meta=json.loads(Path('evidence/S010/count_summary.json').read_text(encoding='utf-8'))
    assert hashlib.sha256(raw).hexdigest()==meta['certificate_raw_sha256']
    traces=[];all_closures=[];rows=[];weak_loss_examples=[]
    for data in produced:
        name=data['graph'];n,edges=GRAPHS[name];arcs=[a for e in edges for a in (e,e[::-1])]
        actual={(tuple(r['m']),r['q'],r['k']):r for r in data['certificates']}
        assert len(actual)==len(data['certificates'])<=300000
        expected=set()
        for total in range(6):
            for m in counts(len(arcs),total):
                for q in range(n):
                    for k in range(1,5):
                        c=[k if v==q else 0 for v in range(n)]
                        for (u,v),x in zip(arcs,m):c[u]+=2*x;c[v]-=x
                        if min(c)>=0:
                            key=(m,q,k);expected.add(key);assert actual[key]['c']==c
        assert expected==actual.keys()
        local_closures={};sched=weak_fail=0;memo_total=0;max_memo=0
        for key,row in actual.items():
            m,q,k=key;c=row['c'];trace,states=order(c,arcs,m,q,k)
            memo_total+=states;max_memo=max(max_memo,states)
            assert (trace is not None)==row['connected'],(name,row,trace)
            cc=tuple(c)
            if cc not in local_closures:local_closures[cc]=closure(c,arcs)
            if trace is not None:
                state=c.copy();usage=[0]*len(m)
                for i in trace:
                    u,v=arcs[i];assert state[u]>=2;state[u]-=2;state[v]+=1;usage[i]+=1
                assert usage==list(m) and state==[k if v==q else 0 for v in range(n)]
                assert local_closures[cc]['stack_mask']&(1<<q)
                if k==1:assert local_closures[cc]['clear_mask']&(1<<q)
                traces.append({'graph':name,'m':m,'q':q,'k':k,'c':c,'arc_indices':trace});sched+=1
            elif row['weak']:
                weak_fail+=1
                if k==1 and not local_closures[cc]['clear_mask']&(1<<q):
                    if len([r for r in weak_loss_examples if r['graph']==name])<3:
                        weak_loss_examples.append({'graph':name,'certificate':row,'closure':local_closures[cc]})
            assert time.monotonic()-start<600
        all_closures.append({'graph':name,'configurations':[{'c':c,**v} for c,v in sorted(local_closures.items())]})
        rows.append({'graph':name,'certificates':len(expected),'legal_exact_count_traces':sched,'weak_failures':weak_fail,
                     'distinct_configurations':len(local_closures),'total_closure_states':sum(v['states'] for v in local_closures.values()),
                     'maximum_closure_states':max(v['states'] for v in local_closures.values()),
                     'fixed_count_memo_states':memo_total,'maximum_fixed_count_memo_states':max_memo})
    for ex in meta['reversal_examples']:
        name=ex['graph'];n,edges=GRAPHS[name];arcs=[a for e in edges for a in (e,e[::-1])]
        if ex['tag']=='CONNECTED_REVERSAL':
            trace,_=order(ex['after_c'],arcs,ex['after_m'],ex['before']['q'],ex['before']['k']);assert trace is not None
        elif ex['tag']=='ROOT_CONNECTION_LOST':
            trace,_=order(ex['after_c'],arcs,ex['after_m'],ex['before']['q'],ex['before']['k']);assert trace is None
    # The precise written weak-connectivity counterexample and all unrestricted roots.
    arcs=[(0,1),(1,0),(0,2),(2,0),(1,2),(2,1)]
    c=[0,1,3];m=[1,1,0,1,0,0];path,_=order(c,arcs,m,2,1);assert path is None
    explicit=closure(c,arcs);assert not explicit['clear_mask']&(1<<2) and explicit['clear_mask']>0
    trace_raw=json.dumps(traces,separators=(',',':')).encode();closure_raw=json.dumps(all_closures,separators=(',',':')).encode()
    out={'campaign':'CAM-S010-01','all_verified':True,'graphs':rows,'certificates':sum(r['certificates'] for r in rows),
         'legal_exact_count_traces':len(traces),'weak_failures':sum(r['weak_failures'] for r in rows),
         'trace_raw_sha256':hashlib.sha256(trace_raw).hexdigest(),'closure_raw_sha256':hashlib.sha256(closure_raw).hexdigest(),
         'weak_root_loss_examples':weak_loss_examples,'explicit_K3_weak_counterexample':{'c':c,'q':2,'k':1,'m':m,'closure':explicit},
         'threshold_claims':0,'seconds':time.monotonic()-start}
    dest=Path('evidence/S010/count_verification.json')
    if '--check-only' in sys.argv:
        old=json.loads(dest.read_text(encoding='utf-8'));actual=json.loads(json.dumps(out))
        assert {k:v for k,v in old.items() if k!='seconds'}=={k:v for k,v in actual.items() if k!='seconds'}
        assert lzma.decompress(Path('evidence/S010/count_traces.json.xz').read_bytes())==trace_raw
        assert lzma.decompress(Path('evidence/S010/count_closures.json.xz').read_bytes())==closure_raw
    else:
        dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
        Path('evidence/S010/count_traces.json.xz').write_bytes(lzma.compress(trace_raw))
        Path('evidence/S010/count_closures.json.xz').write_bytes(lzma.compress(closure_raw))
    print(json.dumps({k:v for k,v in out.items() if k not in ('graphs','weak_root_loss_examples')}),flush=True)

if __name__=='__main__':main()
