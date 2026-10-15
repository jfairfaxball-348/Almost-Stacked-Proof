"""Independent CAM-S012-03 recursive full root predicates/negative closures."""
import functools,itertools,json,lzma,sys,time
from pathlib import Path

def load(p):
    b=Path(p).read_bytes();return json.loads(lzma.decompress(b) if p.endswith('.xz') else b)

def main():
    start=time.monotonic();saved=load('evidence/S012/exceptions.json');meta=load('evidence/S012/analysis.json');traces=load('evidence/S012/exception_traces.json.xz')
    expected_pairs=[];extrema=[];controls=[];negative=[];trace_keys=set();rooted=0
    for g in meta['rows']:
        name=g['graph'];n=g['n'];arcs={(u,v) for a,b in g['edges'] for u,v in [(a,b),(b,a)]}
        def kids(c):
            for u,v in sorted(arcs):
                if c[u]>=2:
                    d=list(c);d[u]-=2;d[v]+=1;yield tuple(d)
        @functools.cache
        def solve(c):
            nonzero=[v for v,a in enumerate(c) if a];size=sum(c);p=1<<nonzero[0] if len(nonzero)==1 else 0
            m=[p if size==1 else 0,p,p if size==2 else 0,p if size==3 else 0]
            for d in kids(c):
                for j,mask in enumerate(solve(d)):m[j]|=mask
            return tuple(m)
        for goal,j in [('stack',1),('clear',0)]:
            threshold=g['thresholds'][goal]
            if threshold is None:continue
            total=threshold-1;losers=[]
            for cuts in itertools.combinations(range(total+n-1),n-1):
                marks=(-1,)+cuts+(total+n-1,);c=tuple(marks[i+1]-marks[i]-1 for i in range(n))
                if solve(c)[j]==0:losers.append(c)
            maximum=max(sum(x*x for x in c) for c in losers);maxima=[c for c in losers if sum(x*x for x in c)==maximum];asmax=[c for c in maxima if len([x for x in c if x>=2])<=1]
            extrema.append({'graph':name,'goal':goal,'threshold':threshold,'losers':len(losers),'Qmax':maximum,'maximizers':[list(c) for c in maxima],'AS_maximizers':len(asmax),'nonAS_maximizers':len(maxima)-len(asmax)})
            if asmax:controls.append({'graph':name,'goal':goal,'c':list(asmax[0])})
            if goal!='stack':continue
            for c in losers:
                if len([x for x in c if x>1])<2:continue
                controls.append({'graph':name,'goal':goal,'c':list(c)})
                for s,t in itertools.product(range(n),repeat=2):
                    if s==t or not 2<=c[s]<=c[t]:continue
                    for a in range(1,min(3,c[s])+1):
                        d=list(c);d[s]-=a;d[t]+=a;dm=solve(tuple(d));rooted+=1
                        insertion=list(c);insertion[s]+=1;deletion=list(c);deletion[s]-=1
                        donor=[bool(dm[j]&(1<<s)) for j in (0,2,3)];D=bool(solve(tuple(insertion))[2]&(1<<t));deleted=bool(solve(tuple(deletion))[0]&(1<<t))
                        if a==1:assert donor[0]==D and donor[1]==False
                        if a==2:assert donor[0]==False and donor[1]==deleted
                        if (s,t) in arcs:
                            if a==1:assert donor[1:]==[False,False]
                            if a==2:assert not donor[0] and not donor[2]
                        expected_pairs.append({'graph':name,'c':list(c),'s':s,'t':t,'a':a,'d':d,'donor_1_2_3':donor,'stackable':bool(dm[1]),'AS':len([x for x in d if x>=2])<=1,'Q_increase':sum(x*x for x in d)-sum(x*x for x in c),'D_edge':D,'deletion_clear_at_t':deleted})
                        for j in (0,2):
                            if dm[j]&(1<<s):trace_keys.add((name,tuple(d),s,j))
        for r in [r for r in saved['controls'] if r['graph']==name]:
            initial=tuple(r['c']);seen={initial};todo=[initial]
            while todo:
                c=todo.pop();assert len(seen)<=300000
                for d in kids(c):
                    if d not in seen:seen.add(d);todo.append(d)
            assert all(sum(c)!=1 if r['goal']=='clear' else len([a for a in c if a])!=1 for c in seen)
            negative.append({'graph':name,'goal':r['goal'],'c':r['c'],'states':sorted(seen)})
        for r in [r for r in traces if r['graph']==name]:
            x=list(r['c'])
            for u,v in r['moves']:
                assert (u,v) in arcs and x[u]>=2;x[u]-=2;x[v]+=1
            assert x==r['final'] and sum(x)==x[r['q']]==(1 if r['kind']==0 else 2)
        solve.cache_clear();assert time.monotonic()-start<600
    controls=list({(r['graph'],r['goal'],tuple(r['c'])):r for r in controls}.values())
    assert expected_pairs==saved['pairs'] and extrema==saved['extrema'] and controls==saved['controls']
    assert {(r['graph'],tuple(r['c']),r['q'],r['kind']) for r in traces}==trace_keys and len(trace_keys)==len(traces)
    out={'pairs':len(expected_pairs),'increasing_losing_transfers':sum(not r['stackable'] for r in expected_pairs),'literal_traces':len(traces),'literal_moves':sum(len(r['moves']) for r in traces),'complete_negative_closures':len(negative),'negative_closure_states':sum(len(r['states']) for r in negative),'global_extrema':len(extrema),'nonAS_global_Qmax':sum(r['nonAS_maximizers'] for r in extrema),'all_equal':True}
    for name,obj in [('exceptions_verification.json',out),('exception_negative_closures.json.xz',negative)]:
        raw=(json.dumps(obj,separators=(',',':'))+'\n').encode();p=Path('evidence/S012')/name
        if '--check-only' in sys.argv:assert (lzma.decompress(p.read_bytes()) if p.suffix=='.xz' else p.read_bytes())==raw
        else:p.write_bytes(lzma.compress(raw) if p.suffix=='.xz' else raw)
    print(json.dumps(out),flush=True)

if __name__=='__main__':main()
