"""Independent complete key regeneration, source symmetries and literal moves."""
import itertools,json,lzma
from pathlib import Path
B=Path('evidence/S014/joinpaths')
def main():
    results=[]
    for g in json.loads((B/'inputs.json').read_bytes())['graphs']:
        a,b,n=g['a'],g['b'],g['n'];E={frozenset(e) for e in g['edges']};N=[{v for v in range(n) if frozenset([u,v]) in E} for u in range(n)];assert {v for v in range(n) if not any(N[w]<N[v] for w in range(n))}==set(range(a+b))
        for part in [range(a),range(a,a+b)]:
            for v in part:
                first=part.start;perm=lambda u:v if u==first else first if u==v else u;assert {frozenset(perm(u) for u in edge) for edge in E}==E
        off=[v for v in range(n) if v not in [0,a]];wanted=set();seen=set();branches={};moves=0
        for k in range(len(off)+1):
            for sites in itertools.combinations(off,k):
                for M in g['totals']:
                    for y in range(M-k+1):wanted.add(tuple(M-k-y if v==0 else y if v==a else int(v in sites) for v in range(n)))
        with lzma.open(B/(g['graph']+'.jsonl.xz'),'rt',encoding='utf-8') as source:
            for line in source:
                row=json.loads(line);c=tuple(row['c']);assert c in wanted and c not in seen;seen.add(c);s=list(c)
                for u,v in row['moves']:assert frozenset([u,v]) in E and s[u]>=2;s[u]-=2;s[v]+=1;moves+=1
                assert s==row['final'] and sum(x>0 for x in s)==1 and sum(s)>0;branch=row['branch'];branches[branch]=branches.get(branch,0)+1
        assert seen==wanted and len(seen)<=1000000
        if g['F']['n']==10:
            f=g['F'];assert len({frozenset(e) for e in f['edges']})==45 and f['W']==12
            assert g['totals']==[17] and max(n+1,3*b+1,3*a+f['W']+1)==17 and 17>max(3*b+1,3*a+f['W']+1)
            assert sum((1,)*n)==16 and not any(x>=2 for x in (1,)*n)
        result=dict(graph=g['graph'],traces=len(seen),literal_moves=moves,branches=branches,all_keys_moves_and_true_source_symmetries_verified=True);results.append(result);print(json.dumps(result),flush=True)
    (B/'verification.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':main()
