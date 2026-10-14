"""Independent complete reverse rooted layers and literal positive insertion traces."""
import hashlib
import itertools
import json
import lzma
import sys
import time
from pathlib import Path

REGISTERED={'K2':(2,[(0,1)],{'stack':3}),'K3':(3,[(0,1),(0,2),(1,2)],{'stack':4,'clear':4}),
 'P4':(4,[(0,1),(1,2),(2,3)],{'stack':15}),
 'C5':(5,[(0,1),(1,2),(2,3),(3,4),(0,4)],{'stack':8,'clear':10}),
 'triangle_tail2':(5,[(0,1),(0,2),(1,2),(0,3),(3,4)],{'stack':16,'clear':22}),
 'F2':(5,[(0,1),(0,2),(1,2),(0,3),(0,4)],{'stack':11,'clear':13}),
 'bowtie':(5,[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)],{'stack':8,'clear':8}),
 'diamond':(4,[(0,1),(0,2),(0,3),(1,2),(2,3)],{'stack':7,'clear':7})}

def states(n,t):
    for cuts in itertools.combinations(range(t+n-1),n-1):
        marks=(-1,)+cuts+(t+n-1,)
        yield tuple(marks[i+1]-marks[i]-1 for i in range(n))

def main():
    start=time.monotonic();raw=lzma.decompress(Path('evidence/S010/root_tables.json.xz').read_bytes())
    saved=json.loads(raw);meta=json.loads(Path('evidence/S010/root_summary.json').read_text(encoding='utf-8'))
    assert hashlib.sha256(raw).hexdigest()==meta['table_raw_sha256'] and len(saved)==len(meta['cases'])==14
    traces=[];rows=[]
    for table,r in zip(saved,meta['cases']):
        name=table['graph'];goal=table['goal'];n,edges,goals=REGISTERED[name];g=goals[goal]
        assert (name,goal)==(r['graph'],r['goal']) and r['n']==n and r['edges']==[list(e) for e in edges] and r['threshold']==g
        arcs=[a for e in edges for a in (e,e[::-1])];layers=[{}]
        for t in range(1,g+1):
            current={c:0 for c in states(n,t)}
            if goal=='stack' or t==1:
                for q in range(n):current[tuple(t if v==q else 0 for v in range(n))]=1<<q
            for prior,mask in layers[-1].items():
                if not mask:continue
                for u,v in arcs:
                    if prior[v]:
                        c=list(prior);c[u]+=2;c[v]-=1;current[tuple(c)]|=mask
            assert len(current)<=300000 and sorted(current.items())==[(tuple(c),m) for c,m in table['layers'][t-1]]
            digest=hashlib.sha256(json.dumps(sorted(current.items()),separators=(',',':')).encode()).hexdigest()
            assert digest==r['layers'][t-1]['root_mask_sha256']
            layers.append(current)
        critical={c for c,m in layers[g-1].items() if m==0}
        assert critical=={tuple(x['c']) for x in r['critical']} and all(layers[g].values()) and g>n
        assert all(any(m==0 for m in layers[t].values()) for t in range(2,g))
        whole=(1<<n)-1
        for m in layers[g].values():whole&=m
        assert whole==r['whole_threshold_common_roots']
        for q,c in r['whole_threshold_missing_root_witnesses'].items():assert not layers[g][tuple(c)]&(1<<int(q))
        def literal(c,q):
            state=tuple(c);moves=[]
            while not (sum(x>0 for x in state)==1 and state[q]>0 and (goal=='stack' or sum(state)==1)):
                assert sum(state)>1
                for u,v in arcs:
                    if state[u]<2:continue
                    d=list(state);d[u]-=2;d[v]+=1;d=tuple(d)
                    if layers[sum(d)][d]&(1<<q):break
                else:raise AssertionError((state,q))
                moves.append([u,v]);state=d
            replay=list(c)
            for u,v in moves:assert (u,v) in arcs and replay[u]>=2;replay[u]-=2;replay[v]+=1
            assert tuple(replay)==state and state[q]>0 and all(not x for v,x in enumerate(state) if v!=q)
            if goal=='clear':assert sum(state)==1
            return moves,list(state)
        for cr in r['critical']:
            c=cr['c'];masks=[]
            for w in range(n):
                d=c.copy();d[w]+=1;mask=layers[g][tuple(d)];assert mask>0;masks.append(mask)
                for q in range(n):
                    if mask&(1<<q):
                        moves,final=literal(d,q);traces.append({'graph':name,'goal':goal,'critical':c,'inserted':w,'root':q,'moves':moves,'final':final})
            assert masks==cr['insertion_masks']
            common=(1<<n)-1
            for m in masks:common&=m
            assert common==cr['common_roots'] and cr['AS']==(sum(x>1 for x in c)<=1) and cr['Q']==sum(x*x for x in c)
            assert cr['occupied_self_failures']==[w for w in range(n) if c[w] and not masks[w]&(1<<w)]
            assert cr['heavy_self_failures']==[w for w in range(n) if c[w]>1 and not masks[w]&(1<<w)]
        rows.append({'graph':name,'goal':goal,'threshold':g,'layers':g,'configurations':sum(len(x) for x in layers),
                     'critical_losers':len(critical),'whole_threshold_common_roots':whole})
        assert time.monotonic()-start<600
    trace_raw=json.dumps(traces,separators=(',',':')).encode()
    out={'campaign':'CAM-S010-02','all_verified':True,'cases':rows,'complete_layers':sum(r['layers'] for r in rows),
         'complete_configurations':sum(r['configurations'] for r in rows),'literal_insertion_root_traces':len(traces),
         'literal_moves':sum(len(r['moves']) for r in traces),'trace_raw_sha256':hashlib.sha256(trace_raw).hexdigest(),
         'seconds':time.monotonic()-start}
    dest=Path('evidence/S010/root_verification.json');tp=Path('evidence/S010/root_traces.json.xz')
    if '--check-only' in sys.argv:
        old=json.loads(dest.read_text(encoding='utf-8'))
        assert {k:v for k,v in old.items() if k!='seconds'}=={k:v for k,v in out.items() if k!='seconds'}
        assert lzma.decompress(tp.read_bytes())==trace_raw
    else:
        dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');tp.write_bytes(lzma.compress(trace_raw))
    print(json.dumps({k:v for k,v in out.items() if k!='cases'}),flush=True)

if __name__=='__main__':main()
