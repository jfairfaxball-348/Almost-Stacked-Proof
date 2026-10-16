"""Literal parity-sensitive AS upper constructions, no move search."""
import itertools,json,lzma,sys,hashlib
from pathlib import Path
B=Path('evidence/S014')
def paths(L,R,pair=None):
    blocks=([[pair[0],pair[1]]]+[[v] for v in L if v not in pair]) if pair else [[v] for v in L]
    assert len(blocks)>=len(R)+1
    path=blocks[0].copy()
    for i,v in enumerate(R):path += [v]+blocks[i+1]
    return [path]+blocks[len(R)+1:]
def construct(g,c,goal):
    a=g['a'];b=g['b'];n=g['n'];x=a+b;y=x+1;r=0;A=list(range(a));Bs=list(range(a,a+b));state=c.copy();moves=[]
    def move(u,v):assert state[u]>=2;state[u]-=2;state[v]+=1;moves.append([u,v])
    def walk(root,path,return_last=True):
        move(root,path[0])
        for u,v in zip(path,path[1:]):move(u,v)
        if return_last:move(path[-1],root)
    def reduce_nonzero(root):
        while state[root]>=4:neighbor=Bs[0] if root in A else r;move(root,neighbor);move(root,neighbor);move(neighbor,root)
        if state[root]==2:move(root,Bs[0] if root in A else r)
        assert sum(state)==1
    def clear_tri(root):
        while state[root]>=7:move(root,x);move(root,x);move(x,root)
        if state[root] in [4,5]:move(root,x);move(root,x);move(x,root)
        if state[root]==2:move(root,x)
        elif state[root]==6:
            for u,v in [(root,x),(root,y),(root,x),(x,y),(y,root)]:move(u,v)
        assert sum(state)==1
    def clear_two(left,right):
        assert sum(state)==state[left]+state[right] and sum(state)>=10
        if (state[left]-state[right])%3:
            while state[left] and state[right]:
                u=left if state[left]>=2 else right;v=right if u==left else left;move(u,v)
            reduce_nonzero(left if state[left] else right)
        else:
            for _ in range(state[left]//2):move(left,right)
            if state[left]:move(right,left);move(left,right)
            assert state[right]>=6;clear_tri(right)
    N=c[r];rho=N%2;p=sum(c[v] for v in A if v!=r);q=sum(c[v] for v in Bs);e=c[x]+c[y];delta=int(q>0);L=p+rho+e;D=L-q+delta
    if D>=1:
        root=next((v for v in Bs if c[v]),Bs[0])
        for _ in range(N//2):move(r,root)
        left=[v for v in A+[x,y] if state[v]==1];right=[v for v in Bs if v!=root and state[v]==1];pair=(x,y) if goal=='stack' and e==2 and D>=2 else None
        for path in paths(left,right,pair):walk(root,path)
        branch='B_root_with_xy' if pair else 'B_root'
        assert sum(state)==state[root] and state[root]>=1
        if goal=='clear':assert state[root]>=4;clear_tri(root)
    else:
        left=[v for v in Bs if c[v]];right=[v for v in A+[x,y] if v!=r and c[v]]
        if not left and not right:
            branch='pure_A'
            if goal=='clear':clear_two(r,Bs[0])
        else:
            cover=paths(left,right);K=sum(c)-2*q
            if goal=='stack' or K%3:
                for path in cover:walk(r,path)
                branch='A_root'
                assert state[r]==K and sum(state)==K and K>=1
                if goal=='clear':reduce_nonzero(r)
            elif K>=9:
                for path in cover[:-1]:walk(r,path)
                walk(r,cover[-1],False);end=cover[-1][-1];branch='A_root_last_pair';clear_two(r,end)
            else:
                assert g['a']==1 and g['b']==2 and c[r]==8 and q==2 and p==e==0 and K==6
                one,other=Bs;move(r,one);move(one,x)
                for _ in range(3):move(r,other)
                for u,v in [(other,y),(other,x),(x,y),(y,other)]:move(u,v)
                branch='exception_K6'
    assert (sum(state)==1 if goal=='clear' else sum(a>0 for a in state)==1 and sum(state)>0)
    return dict(graph=g['graph'],goal=goal,c=c,moves=moves,final=state,branch=branch)
def main():
    for p,h in json.loads((B/'aspaths_inputs.json').read_bytes()).items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    graphs=json.loads((B/'balanced/ray_inputs.json').read_bytes())['graphs'];traces=[];branches={}
    for g in graphs:
        a=g['a'];n=g['n'];x=n-2;y=n-1
        for goal,base in [('stack',3*a+5),('clear',3*a+7)]:
            off=[v for v in range(1,n) if goal=='stack' or v not in [x,y]]
            for bits in itertools.product(range(2),repeat=len(off)):
                for M in range(base,base+3):
                    c=[0]*n
                    for v,b in zip(off,bits):c[v]=b
                    c[0]=M-sum(bits);assert c[0]>=4
                    trace=construct(g,c,goal);traces.append(trace);key=goal+':'+trace['branch'];branches[key]=branches.get(key,0)+1
        if len(traces)>300000:raise RuntimeError('TRACE_LIST_CAP_UNKNOWN')
    result=dict(traces=traces,branches=branches);raw=(json.dumps(result,separators=(',',':'))+'\n').encode();p=B/'aspaths.json.xz'
    if '--check-only' in sys.argv:assert lzma.decompress(p.read_bytes())==raw
    else:p.write_bytes(lzma.compress(raw))
    print(json.dumps(dict(traces=len(traces),literal_moves=sum(len(t['moves']) for t in traces),branches=branches)),flush=True)
if __name__=='__main__':main()
