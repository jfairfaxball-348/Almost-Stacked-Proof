"""Constructive complete-bipartite triangular-heavy upper proof, finite challenge."""
import itertools,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014')
def compositions(n,m):
    if n==1:yield (m,);return
    for a in range(m+1):
        for tail in compositions(n-1,m-a):yield (a,)+tail
def main():
    ident=sys.argv[1];g=next(g for g in json.loads((B/'biptri_inputs.json').read_bytes()) if g['id']==ident);n=g['core_n'];a=g['a'];arcs=sorted((u,v) for e in g['core_edges'] for u,v in [e,e[::-1]]);N=[sorted(v for u,v in arcs if u==s) for s in range(n)];layers=[]
    for mass in range(g['max_mass']+1):
        layer={}
        for c in compositions(n,mass):
            occupied=[v for v in range(n) if c[v]];bit=1<<occupied[0] if len(occupied)==1 else 0;m=[bit if mass==k else 0 for k in [1,2,3]]
            for u,v in arcs:
                if c[u]>=2:
                    d=list(c);d[u]-=2;d[v]+=1;dm=layers[-1][tuple(d)];m=[x|y for x,y in zip(m,dm)]
            layer[c]=m
        if len(layer)>300000:raise RuntimeError('ROOT_LAYER_STATE_CAP_UNKNOWN')
        layers.append(layer)
    traces=[];branches={}
    for layer in layers:
        for c in sorted(layer):
            occupied=[v for v in range(n) if c[v]];h=max(sum(v<a for v in occupied),sum(v>=a for v in occupied))
            if sum(c)<3*h+4:continue
            if any(x>=4 for x in c):r=next(v for v in range(n) if c[v]>=4);prefix=[];branch='existing4'
            elif any(c[r]==3 and c[u]>=2 for r in range(n) for u in N[r]):
                r,u=next((r,u) for r in range(n) for u in N[r] if c[r]==3 and c[u]>=2);prefix=[[u,r]];branch='adjacent3and2'
            elif 3 in c:
                part=range(a) if any(c[v]==3 for v in range(a)) else range(a,n);opposite=range(a,n) if part==range(a) else range(a)
                z,r=[v for v in part if c[v]==3][:2];y,y2=[v for v in opposite if c[v]==1][:2];prefix=[[z,y],[y,z],[z,y2],[y2,r]];branch='three_vs_ones'
            else:
                part=range(a) if sum(c[v]==2 for v in range(a))>=3 else range(a,n);opposite=range(a,n) if part==range(a) else range(a)
                z,w,r=[v for v in part if c[v]==2][:3];y=next(v for v in opposite if c[v]==2);prefix=[[z,y],[y,r],[w,y],[y,r]];branch='all_at_most2'
            x=list(c)
            for u,v in prefix:assert x[u]>=2;x[u]-=2;x[v]+=1
            assert x[r]>=4;b=x.copy();b[r]-=3;hb=max(sum(v<a and b[v]>0 for v in range(n)),sum(v>=a and b[v]>0 for v in range(n)));has_edge=any(b[u] and b[v] for u,v in arcs)
            assert sum(b)>=3*hb+1 or (sum(b)==3*hb and has_edge)
            masks=layers[sum(b)][tuple(b)];assert any(masks);moves=prefix.copy()
            if masks[0] or masks[1]:
                k=1 if masks[0] else 2;q=next(v for v in range(n) if masks[k-1]>>v&1);w=N[r][0];moves.extend([[r,w],[r,w],[w,r]])
            else:k=3;q=r;assert masks[2]>>r&1
            state=tuple(b)
            while not (sum(state)==k and state[q]==k):
                for u,v in arcs:
                    if state[u]<2:continue
                    d=list(state);d[u]-=2;d[v]+=1;d=tuple(d)
                    if layers[sum(d)][d][k-1]>>q&1:break
                else:raise AssertionError(state)
                moves.append([u,v]);state=d
            if k==2:moves.append([q,N[q][0]])
            elif k==3:
                t1=n+2*r;t2=t1+1;moves.extend([[r,t1],[r,t2],[r,t1],[t1,t2],[t2,r]])
            full=list(c)+[0]*(2*n)
            for u,v in moves:assert full[u]>=2;full[u]-=2;full[v]+=1
            assert sum(full)==1
            traces.append(dict(c=c,branch=branch,root=r,prefix=prefix,reduced=b,moves=moves,final=full));branches[branch]=branches.get(branch,0)+1
    result=dict(graph=g,layers=[[[c,m] for c,m in sorted(layer.items())] for layer in layers],traces=traces,branches=branches)
    raw=(json.dumps(result,separators=(',',':'))+'\n').encode();p=B/(ident+'_biptri.json.xz')
    if '--check-only' in sys.argv:assert lzma.decompress(p.read_bytes())==raw
    else:p.write_bytes(lzma.compress(raw))
    print(json.dumps(dict(case=ident,configurations=sum(map(len,layers)),upper_traces=len(traces),branches=branches)),flush=True)
if __name__=='__main__':main()
