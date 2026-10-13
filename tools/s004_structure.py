"""Preregistered structural falsification on complete n<=5 critical layers."""
import json,itertools,time,sys
from pathlib import Path
from s004_cold import atlas,bipartite,full_layers,almost,closure,goal,successors,digest,conf

def main():
    start=time.monotonic();out={'atlas':[],'certificate_replay':[]}
    for path in sorted(Path('evidence/S003').glob('cert_*.json')):
        x=json.loads(path.read_text());e=x['edges'];n=x['n'];mode=x['goal'];t=x['t']
        seen=set()
        for row in x['as_winning_sequences']:
            c=tuple(row['config']);assert len(c)==n and sum(c)==t and almost(c);assert c not in seen;seen.add(c)
            for u,v in row['moves']:
                assert (u,v) in [p for a,b in e for p in [(a,b),(b,a)]] and c[u]>=2
                d=list(c);d[u]-=2;d[v]+=1;c=tuple(d)
            assert goal(c,mode)
        assert seen=={c for c in conf(n,t) if almost(c)}
        lw=x['losing_witness'];R=closure(tuple(lw['config']),e)
        assert R=={tuple(c) for c in lw['reachable_set']}
        assert not any(goal(c,mode) for c in R)
        out['certificate_replay'].append({'file':str(path),'as_count':len(seen),'reachable_count':len(R),'reachable_sha256':digest(R)})
    for n in range(2,6):
        for edges in atlas(n):
            for mode in ['stack','clear']:
                if mode=='clear' and bipartite(n,edges):continue
                rows,B=full_layers(n,edges,mode,32)
                assert not B[-1]
                critical=B[-2];asbad={c for c in critical if almost(c)}
                square=lambda c:sum(v*v for v in c)
                support=lambda c:sum(v>0 for v in c)
                top=max(map(square,critical));low=min(map(support,critical))
                sqmax={c for c in critical if square(c)==top};supmin={c for c in critical if support(c)==low}
                out['atlas'].append({'n':n,'edges':edges,'mode':mode,'threshold':rows[-1]['t'],
                    'critical_count':len(critical),'as_count':len(asbad),
                    'max_square':top,'max_square_has_AS':bool(sqmax&asbad),
                    'max_square_all_AS':sqmax<=asbad,'min_support':low,
                    'min_support_has_AS':bool(supmin&asbad),'min_support_all_AS':supmin<=asbad,
                    'non_AS_min_support':min(supmin-asbad) if supmin-asbad else None,
                    'non_AS_max_square':min(sqmax-asbad) if sqmax-asbad else None})
    # Elementary algebraic relaxation: on triangle all ones is terminal, yet
    # one firing each of 0->1 and 1->0 balances it to e2.
    c=(1,1,1);e=[(0,1),(1,2),(2,0)];balanced=list(c)
    for u,v in [(0,1),(1,0)]:balanced[u]-=2;balanced[v]+=1
    assert balanced==[0,0,1] and not list(successors(c,e))
    out['unschedulable_balance']={'graph':'K3','edges':e,'config':c,'formal_move_counts':[[0,1,1],[1,0,1]],'formal_final':balanced,'reachable':sorted(closure(c,e))}
    out['seconds']=time.monotonic()-start
    if '--check-only' not in sys.argv:
        Path('evidence/S004/structure.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'graphs_and_goals':len(out['atlas']),'failures':{k:sum(not r[k] for r in out['atlas']) for k in ['max_square_has_AS','max_square_all_AS','min_support_has_AS','min_support_all_AS']},'seconds':out['seconds']}))

if __name__=='__main__':main()
