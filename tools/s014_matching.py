"""Explicit two-heavy path constructions; no reachability search."""
import hashlib,itertools,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014/matching')

def construct(g,c):
    a,b,m=g['a'],g['b'],g['m'];A=list(range(a));Bs=list(range(a,a+b));aux=list(range(a+b,g['n']));s=c.copy();moves=[]
    def choose(part):return next((v for v in part if s[v]>=2),next((v for v in part if s[v]),part[0]))
    r,t=choose(A),choose(Bs);u,v=s[r],s[t];p=sum(s[z] for z in A if z!=r);q=sum(s[z] for z in Bs if z!=t);e=sum(s[z] for z in aux);rho=u%2;sigma=v%2;D=p+rho+e-q
    def move(x,y):assert s[x]>=2;s[x]-=2;s[y]+=1;moves.append([x,y])
    def absorb(root,path):
        move(root,path[0])
        for x,y in zip(path,path[1:]):move(x,y)
        move(path[-1],root)
    def cover(left,right,pairs=[]):
        used=set(z for pair in pairs for z in pair);blocks=[list(pair) for pair in pairs]+[[z] for z in left if z not in used]
        assert len(blocks)>=len(right)+1
        path=blocks[0].copy()
        for i,z in enumerate(right):path += [z]+blocks[i+1]
        return [path]+blocks[len(right)+1:]
    if D>=1:
        for _ in range(u//2):move(r,t)
        left=[z for z in A+aux if s[z]==1];right=[z for z in Bs if z!=t and s[z]==1]
        pairs=[(z,z+1) for z in aux[::2] if s[z]==s[z+1]==1];pairs=pairs[:min(len(pairs),D-1)]
        for path in cover(left,right,pairs):absorb(t,path)
        branch='B_root_pairs' if pairs else 'B_root'
    else:
        E=q+sigma-p-e
        if E>=1:
            for _ in range(v//2):move(t,r)
            left=[z for z in Bs if s[z]==1];right=[z for z in A+aux if z!=r and s[z]==1]
            for path in cover(left,right):absorb(r,path)
            branch='A_root'
        else:
            assert rho==sigma==0 and q==p+e
            if not q:
                while s[r] and s[t]:move(r,t) if s[r]>=2 else move(t,r)
                branch='two_roots'
            elif u>=2:
                for _ in range(u//2-1):move(r,t)
                left=[z for z in Bs if z!=t and s[z]==1];right=[z for z in A+aux if z!=r and s[z]==1];assert len(left)==len(right)==q
                path=[z for pair in zip(left,right) for z in pair];move(r,path[0])
                for x,y in zip(path,path[1:]):move(x,y)
                move(path[-1],t);branch='balanced_retain_A'
            else:
                for _ in range(v//2-1):move(t,r)
                left=[z for z in A+aux if z!=r and s[z]==1];right=[z for z in Bs if z!=t and s[z]==1];assert len(left)==len(right)==q
                path=[z for pair in zip(left,right) for z in pair];move(t,path[0])
                for x,y in zip(path,path[1:]):move(x,y)
                move(path[-1],r);branch='balanced_retain_B'
    assert sum(z>0 for z in s)==1 and sum(s)>0
    return dict(c=c,moves=moves,final=s,branch=branch)

def main():
    inp=json.loads((B/'threshold_inputs.json').read_bytes());summaries=[]
    for g in inp['graphs']:
        a,b,n=g['a'],g['b'],g['n'];T=max(3*b+1,3*a+4*g['m']+1);seen=set();traces=[];branches={}
        for r in range(a):
            for t in range(a,a+b):
                off=[z for z in range(n) if z not in [r,t]]
                for bits in itertools.product(range(2),repeat=len(off)):
                    for mass in range(T,T+3):
                        for u in range(mass-sum(bits)+1):
                            c=[0]*n
                            for z,x in zip(off,bits):c[z]=x
                            c[r]=u;c[t]=mass-sum(bits)-u;k=tuple(c)
                            if k in seen:continue
                            seen.add(k)
                            if len(seen)>300000:raise RuntimeError('TRACE_CAP_UNKNOWN')
                            tr=construct(g,c);traces.append(tr);branches[tr['branch']]=branches.get(tr['branch'],0)+1
        raw=(json.dumps(dict(graph=g,traces=traces,branches=branches),separators=(',',':'))+'\n').encode();p=B/(g['graph']+'_paths.json.xz')
        if '--check-only' in sys.argv:assert lzma.decompress(p.read_bytes())==raw
        else:p.write_bytes(lzma.compress(raw))
        row=dict(graph=g['graph'],traces=len(traces),moves=sum(len(r['moves']) for r in traces),branches=branches);summaries.append(row);print(json.dumps(row),flush=True)
    (B/'paths_summary.json').write_text(json.dumps(summaries,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':main()
