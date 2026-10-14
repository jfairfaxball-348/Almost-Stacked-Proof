"""Independent full reverse sets and literal trace arithmetic; no producer import."""
import hashlib
import itertools
import json
import lzma
import sys
import time
from pathlib import Path

def fingerprint(states):
    return hashlib.sha256(json.dumps(sorted(states),separators=(',',':')).encode()).hexdigest()

def main():
    start=time.monotonic()
    goal='stack' if '--stack' in sys.argv else 'clear'
    stem='stack_tail' if goal=='stack' else 'tail'
    cert=json.loads(Path(f'evidence/S007/{stem}_layers.json').read_text())
    assert len(cert['graphs'])==3
    count=0
    for l,row in enumerate(cert['graphs']):
        n=l+3; g=(6*(1<<l)-2 if goal=='clear' else 4*(1<<l))
        edges={(0,1),(0,2),(1,2)} | {(0 if v==3 else v-1,v) for v in range(3,n)}
        assert row['length']==l and row['n']==n and row['threshold']==g
        assert {tuple(e) for e in row['edges']}==edges
        assert len(row['layers'])==g
        winning=set()
        for t,layer in enumerate(row['layers'],1):
            assert time.monotonic()-start<300
            # Generate compositions through cut positions, unlike primary recursion.
            all_states=set()
            for cuts in itertools.combinations(range(t+n-1),n-1):
                marks=(-1,)+cuts+(t+n-1,)
                all_states.add(tuple(marks[i+1]-marks[i]-1 for i in range(n)))
            reverse=set()
            if t==1:
                reverse=all_states.copy()
            else:
                for c in winning:
                    for a,b in edges:
                        for source,dest in ((a,b),(b,a)):
                            if c[dest]:
                                d=list(c);d[source]+=2;d[dest]-=1
                                reverse.add(tuple(d))
                if goal=='stack':
                    reverse|={tuple(t if v==q else 0 for v in range(n)) for q in range(n)}
            assert reverse<=all_states
            losers=all_states-reverse
            assert layer=={'mass':t,'configurations':len(all_states),'winning':len(reverse),
                           'losing':len(losers),'winning_sha256':fingerprint(reverse),
                           'losing_sha256':fingerprint(losers)}
            if 2<=t<=n:
                assert losers  # exact least threshold has no earlier empty layer
            if n<t<g:
                assert losers
            if t==g-1 and goal=='clear':
                pure=tuple(t if v==(0 if l==0 else n-1) else 0 for v in range(n))
                assert pure in losers
            if t==g:
                assert not losers
            count+=len(all_states);winning=reverse
    raw=lzma.decompress(Path(f'evidence/S007/{stem}_traces.json.xz').read_bytes())
    assert hashlib.sha256(raw).hexdigest()==cert['trace_raw_sha256']
    traces=json.loads(raw);seen=set();moves=0
    for row in traces:
        l=row['length'];n=l+3;g=(6*2**l-2 if goal=='clear' else 4*2**l);c=list(row['configuration'])
        key=(l,tuple(c));assert key not in seen;seen.add(key)
        assert len(c)==n and sum(c)==g and min(c)>=0
        allowed={frozenset((0,1)),frozenset((0,2)),frozenset((1,2))}
        allowed|={frozenset((0 if v==3 else v-1,v)) for v in range(3,n)}
        for u,v in row['moves']:
            assert u!=v and frozenset((u,v)) in allowed and c[u]>=2
            c[u]-=2;c[v]+=1;moves+=1
        assert min(c)>=0 and (sum(c)==1 if goal=='clear' else sum(x>0 for x in c)==1)
        assert len(row['moves'])==g-sum(c)
    assert len(traces)==cert['construction_traces']==sum(r['layers'][-1]['configurations'] for r in cert['graphs'])
    assert moves==cert['construction_moves']
    out={'campaign':cert['campaign'],'goal':goal,'full_reverse_layer_matches':sum(len(r['layers']) for r in cert['graphs']),
         'complete_configurations':count,'independent_legal_traces':len(traces),'legal_moves':moves,
         'exact_thresholds':[r['threshold'] for r in cert['graphs']], 'all_verified':True,
         'seconds':time.monotonic()-start}
    if '--check-only' not in sys.argv:
        Path(f'evidence/S007/{stem}_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(out))

if __name__=='__main__':
    main()
