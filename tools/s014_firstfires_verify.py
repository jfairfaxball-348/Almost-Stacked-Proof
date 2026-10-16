"""Whole coordinate box predecessor DP, independent linear forests and moves."""
import itertools,json,lzma
from pathlib import Path
B=Path('evidence/S014/firstfires')
def comps(m,n):
    if n==1:yield (m,);return
    for x in range(m+1):
        for tail in comps(m-x,n-1):yield (x,)+tail
def theta(g,mask):
    U={v for v in range(g['n']) if mask>>v&1};es=[e for e in g['edges'] if set(e)<=U];best=len(U)
    for flags in itertools.product([0,1],repeat=len(es)):
        parent=list(range(g['n']));deg=[0]*g['n'];count=0
        def root(v):
            while parent[v]!=v:v=parent[v]
            return v
        for (u,v),flag in zip(es,flags):
            if not flag:continue
            deg[u]+=1;deg[v]+=1;x,y=root(u),root(v)
            if deg[u]>2 or deg[v]>2 or x==y:break
            parent[x]=y;count+=1
        else:best=min(best,len(U)-count)
    return best
def main():
    inp=json.loads((B/'inputs.json').read_bytes());results=[]
    for g in inp['graphs']:
        n=g['n'];E={frozenset(e) for e in g['edges']};arcs=[(u,v) for u in range(n) for v in range(n) if frozenset([u,v]) in E];data=json.loads(lzma.decompress((B/(g['name']+'.json.xz')).read_bytes()));assert data['graph']==g;allcells=0;allends=0;strict=0;empties=0;extracted=0
        assert [r['mask'] for r in data['subsets']]==list(range(1<<n))
        for row in data['subsets']:
            mask=row['mask'];U={v for v in range(n) if mask>>v&1};e=len(U);start=tuple(int(v in U) for v in range(n));seen=set();wanted={(tuple(c),I,O) for c,I,O in row['cells']};assert len(wanted)==len(row['cells'])<=300000
            for I in range(4):
                for mass in range(e+I,-1,-1):
                    for O in range((e+I-mass)//2+1):
                        for c in comps(mass,n):
                            yes=(c,I,O)==(start,0,0)
                            if I:
                                for v in range(n):
                                    if c[v]:d=list(c);d[v]-=1;yes |= (tuple(d),I-1,O) in seen
                            if O:
                                for v in range(n):d=list(c);d[v]+=2;yes |= (tuple(d),I,O-1) in seen
                            for u,v in arcs:
                                if c[v]:d=list(c);d[u]+=2;d[v]-=1;yes |= (tuple(d),I,O) in seen
                            if yes:seen.add((c,I,O))
            assert seen==wanted,(g['name'],mask,len(seen),len(wanted));h=theta(g,mask);seenends=set()
            for end in row['terminal_histories']:
                c,I,O=end['cell'];key=(tuple(c),I,O);assert key in seen and key not in seenends;seenends.add(key);s=list(start);k=[0]*n;parents={};i=o=0
                for op in end['ops']:
                    if op[0]=='in':v=op[1];s[v]+=1;i+=1;parents.setdefault(v,None)
                    elif op[0]=='out':u=op[1];assert s[u]>=2;s[u]-=2;o+=1;k[u]+=1
                    else:u,v=op[1:];assert frozenset([u,v]) in E and s[u]>=2;s[u]-=2;s[v]+=1;k[u]+=1;parents.setdefault(v,u)
                assert s==c and (i,o)==(I,O) and sum(x>0 for x in s)<=1
                occupied=[v for v in range(n) if s[v]];K=sum(s)
                if not occupied:bound=2*I-O;empties+=1
                elif occupied[0] not in U or occupied[0] in parents:bound=2*I-O-1;strict+=1
                else:continue
                assert h<=bound
                # Construct the proof's actual path forest on the initial U.
                chosen=[];used_sources=set()
                for v in sorted(U):
                    assert v in parents
                    u=parents[v]
                    if u in U and u not in used_sources:chosen.append((u,v));used_sources.add(u)
                degree={v:0 for v in U};rep={v:v for v in U}
                def root(v):
                    while rep[v]!=v:v=rep[v]
                    return v
                for u,v in chosen:
                    assert frozenset([u,v]) in E;degree[u]+=1;degree[v]+=1;x,y=root(u),root(v);assert x!=y and degree[u]<=2 and degree[v]<=2;rep[x]=y
                assert len(U)-len(chosen)<=bound;extracted+=1
            assert seenends=={cell for cell in seen if sum(x>0 for x in cell[0])<=1}
            allcells+=len(seen);allends+=len(seenends)
        result=dict(graph=g['name'],all_cells=allcells,all_terminal_histories=allends,empty_end_cases=empties,strict_single_end_cases=strict,true_extracted_path_covers=extracted,complete_independent_sets_equal=True);results.append(result);print(json.dumps(result),flush=True)
    (B/'verification.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':main()
