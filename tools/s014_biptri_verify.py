"""Independent reverse full core masks and all ambient upper histories."""
import itertools,json,lzma,math,sys
from pathlib import Path
B=Path('evidence/S014')
def compositions(n,m):
    for cuts in itertools.combinations(range(m+n-1),n-1):
        points=(-1,)+cuts+(m+n-1,);yield tuple(points[i+1]-points[i]-1 for i in range(n))
def main():
    ident=sys.argv[1];data=json.loads(lzma.decompress((B/(ident+'_biptri.json.xz')).read_bytes()));g=data['graph'];assert g==next(g for g in json.loads((B/'biptri_inputs.json').read_bytes()) if g['id']==ident)
    n=g['core_n'];a=g['a'];edges={tuple(e) for e in g['core_edges']};arcs=sorted(edges|{(v,u) for u,v in edges});actual_edges={frozenset(e) for e in g['ambient_edges']};prev={};eligible=set();total=0
    for mass,saved in enumerate(data['layers']):
        layer={c:[0,0,0] for c in compositions(n,mass)};assert len(layer)==math.comb(mass+n-1,n-1)<=300000
        if mass in [1,2,3]:
            for v in range(n):c=tuple(mass if v==u else 0 for u in range(n));layer[c][mass-1]=1<<v
        for d,mask in prev.items():
            for u,v in arcs:
                if d[v]:
                    c=list(d);c[v]-=1;c[u]+=2;c=tuple(c)
                    for j in range(3):layer[c][j]|=mask[j]
        assert layer=={tuple(c):m for c,m in saved}
        for c in layer:
            h=max(len([v for v in range(a) if c[v]]),len([v for v in range(a,n) if c[v]]))
            if mass>=3*h+4:eligible.add(c)
        total+=len(layer);prev=layer
    assert len(data['layers'])==g['max_mass']+1
    seen=set();branches={};moves=0
    for r in data['traces']:
        c=tuple(r['c']);assert c in eligible and c not in seen;seen.add(c);root=r['root'];prefix=r['prefix'];x=list(c)
        for u,v in prefix:assert (u,v) in arcs and x[u]>=2;x[u]-=2;x[v]+=1
        assert x[root]>=4 and c[root]>=2
        reduced=x.copy();reduced[root]-=3;assert reduced==r['reduced'] and reduced[root]>=1
        h=max(sum(v>0 for v in reduced[:a]),sum(v>0 for v in reduced[a:]));edge=any(reduced[u] and reduced[v] for u,v in arcs)
        assert sum(reduced)>=3*h+1 or (sum(reduced)==3*h and edge)
        if r['branch']=='existing4':assert not prefix and c[root]>=4
        elif r['branch']=='adjacent3and2':assert len(prefix)==1 and c[root]==3 and c[prefix[0][0]]>=2
        elif r['branch']=='three_vs_ones':assert len(prefix)==4 and max(c)==3 and c[root]==3
        elif r['branch']=='all_at_most2':assert len(prefix)==4 and max(c)==2 and c[root]==2
        else:raise AssertionError(r['branch'])
        branches[r['branch']]=branches.get(r['branch'],0)+1;state=list(c)+[0]*(2*n)
        for u,v in r['moves']:assert frozenset([u,v]) in actual_edges and state[u]>=2;state[u]-=2;state[v]+=1;moves+=1
        assert state==r['final'] and sum(state)==1 and len(r['moves'])==sum(c)-1
    assert seen==eligible and branches==data['branches']
    result=dict(case=ident,configurations=total,upper_traces=len(seen),branches=branches,literal_moves=moves,all_complete_masks_and_histories_equal=True)
    p=B/(ident+'_biptri_verification.json');raw=(json.dumps(result,indent=2)+'\n').encode()
    if '--check-only' in sys.argv:assert p.read_bytes()==raw
    else:p.write_bytes(raw)
    print(json.dumps(result),flush=True)
if __name__=='__main__':main()
