"""Independent complete reverse layers and literal upper-trace arithmetic."""
import hashlib
import itertools
import json
import lzma
import sys
import time
from pathlib import Path

def fingerprint(states):return hashlib.sha256(json.dumps(sorted(states),separators=(',',':')).encode()).hexdigest()

def main():
    start=time.monotonic();cert=json.loads(Path('evidence/S008/branch_layers.json').read_text());states=layers=0
    assert [(r['k'],r['goal']) for r in cert['graphs']]==[(k,g) for k in range(1,4) for g in ('stack','clear')]
    for row in cert['graphs']:
        k=row['k'];n=k+3;g=3*k+(5 if row['goal']=='stack' else 7);edges={(0,1),(0,2),(1,2)}|{(0,v) for v in range(3,n)}
        assert row['n']==n and row['threshold']==g and {tuple(e) for e in row['edges']}==edges
        assert len(row['layers'])==g
        previous=set()
        for t,layer in enumerate(row['layers'],1):
            all_states=set()
            for cuts in itertools.combinations(range(t+n-1),n-1):
                marks=(-1,)+cuts+(t+n-1,)
                all_states.add(tuple(marks[i+1]-marks[i]-1 for i in range(n)))
            winners=set()
            if t==1:winners=all_states.copy()
            else:
                for c in previous:
                    for a,b in edges:
                        for u,v in ((a,b),(b,a)):
                            if c[v]:
                                d=list(c);d[u]+=2;d[v]-=1;winners.add(tuple(d))
                if row['goal']=='stack':winners|={tuple(t if v==q else 0 for v in range(n)) for q in range(n)}
            assert winners<=all_states and len(all_states)<=300000
            losers=all_states-winners
            assert layer=={'mass':t,'configurations':len(all_states),'winning':len(winners),'losing':len(losers),'winning_sha256':fingerprint(winners),'losing_sha256':fingerprint(losers)}
            if 2<=t<g:assert losers
            if t==g-1:
                candidate=tuple((2*k+(3 if row['goal']=='stack' else 7)) if v==3 else int(v>=4 or (row['goal']=='stack' and v in (1,2))) for v in range(n))
                assert tuple(row['critical_AS_candidate'])==candidate and candidate in losers
                assert sum(x>1 for x in candidate)<=1
            if t==g:assert not losers
            states+=len(all_states);layers+=1;previous=winners
            assert time.monotonic()-start<600
    raw=lzma.decompress(Path('evidence/S008/branch_traces.json.xz').read_bytes())
    assert hashlib.sha256(raw).hexdigest()==cert['trace_raw_sha256']
    traces=json.loads(raw);moves=0;seen=set()
    for row in traces:
        k=row['k'];c=list(row['configuration']);n=k+3;goal=row['goal'];g=3*k+(5 if goal=='stack' else 7)
        assert k in (1,2,3) and goal in ('stack','clear')
        key=(k,goal,tuple(c));assert key not in seen;seen.add(key)
        assert len(c)==n and min(c)>=0 and sum(c)==g
        edges={frozenset((0,v)) for v in range(1,n)}|{frozenset((1,2))}
        for u,v in row['moves']:
            assert u!=v and frozenset((u,v)) in edges and c[u]>=2
            c[u]-=2;c[v]+=1;moves+=1
        assert (sum(c)==1 if goal=='clear' else sum(x>0 for x in c)==1)
        assert len(row['moves'])==g-sum(c)
    assert len(traces)==cert['construction_traces']==sum(r['layers'][-1]['configurations'] for r in cert['graphs'])
    assert moves==cert['construction_moves']
    out={'campaign':'CAM-S008-02','complete_layers':layers,'complete_configurations':states,'independent_traces':len(traces),'legal_moves':moves,'all_verified':True,'seconds':time.monotonic()-start}
    if '--check-only' not in sys.argv:Path('evidence/S008/branch_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(out))

if __name__=='__main__':main()
