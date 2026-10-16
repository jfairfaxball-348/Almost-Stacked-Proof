"""General-buffer actual paths; no pebbling search, streamed complete histories."""
import functools,itertools,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014/joinpaths')

def covers(g):
    f=g['F'];s=f['n'];E={frozenset(e) for e in f['edges']};paths={};ends={}
    for v in range(s):ends[(1<<v,v)]=[v]
    for mask in range(1,1<<s):
        for v in range(s):
            if (mask,v) not in ends:continue
            path=ends[mask,v];paths.setdefault(mask,path)
            for w in range(s):
                if not mask>>w&1 and frozenset([v,w]) in E:ends.setdefault((mask|1<<w,w),path+[w])
    result=[[]]+[None]*((1<<s)-1)
    for mask in range(1,1<<s):
        for sub,path in paths.items():
            if sub&mask==sub:
                candidate=[path]+result[mask^sub]
                if result[mask] is None or len(candidate)<len(result[mask]):result[mask]=candidate
    assert max(mask.bit_count()+2*len(cover) for mask,cover in enumerate(result))==f['W']
    return result

def construct(g,c,cache):
    a,b=g['a'],g['b'];A=list(range(a));Bs=list(range(a,a+b));aux=list(range(a+b,g['n']));s=c.copy();moves=[]
    def choose(part):return next((v for v in part if s[v]>=2),next((v for v in part if s[v]),part[0]))
    r,t=choose(A),choose(Bs);u,v=s[r],s[t];p=sum(s[z] for z in A if z!=r);q=sum(s[z] for z in Bs if z!=t);e=sum(s[z] for z in aux);rho=u%2;sigma=v%2;D=p+rho+e-q
    def move(x,y):assert s[x]>=2;s[x]-=2;s[y]+=1;moves.append([x,y])
    def absorb(root,path):
        move(root,path[0])
        for x,y in zip(path,path[1:]):move(x,y)
        move(path[-1],root)
    def cover(left,right,blocks):
        used=set(z for block in blocks for z in block);blocks=[list(block) for block in blocks]+[[z] for z in left if z not in used];assert len(blocks)>=len(right)+1
        path=blocks[0].copy()
        for i,z in enumerate(right):path += [z]+blocks[i+1]
        return [path]+blocks[len(right)+1:]
    if D>=1:
        for _ in range(u//2):move(r,t)
        left=[z for z in A+aux if s[z]==1];right=[z for z in Bs if z!=t and s[z]==1];mask=sum(1<<i for i,z in enumerate(aux) if s[z]);paths=cache[mask];needed=min(e-len(paths),D-1);blocks=[]
        for path in paths:
            keep=min(needed,len(path)-1)
            if keep:blocks.append([a+b+z for z in path[:keep+1]]);needed-=keep
        assert not needed
        for path in cover(left,right,blocks):absorb(t,path)
        branch='B_root_internal_paths' if blocks else 'B_root'
    elif q+sigma-p-e>=1:
        for _ in range(v//2):move(t,r)
        left=[z for z in Bs if s[z]==1];right=[z for z in A+aux if z!=r and s[z]==1]
        for path in cover(left,right,[]):absorb(r,path)
        branch='A_root'
    else:
        assert rho==sigma==0 and q==p+e
        if not q:
            while s[r] and s[t]:move(r,t) if s[r]>=2 else move(t,r)
            branch='two_roots'
        elif u>=2:
            for _ in range(u//2-1):move(r,t)
            left=[z for z in Bs if z!=t and s[z]==1];right=[z for z in A+aux if z!=r and s[z]==1];path=[z for pair in zip(left,right) for z in pair];assert len(path)==2*q
            move(r,path[0])
            for x,y in zip(path,path[1:]):move(x,y)
            move(path[-1],t);branch='balanced_retain_A'
        else:
            for _ in range(v//2-1):move(t,r)
            left=[z for z in A+aux if z!=r and s[z]==1];right=[z for z in Bs if z!=t and s[z]==1];path=[z for pair in zip(left,right) for z in pair];assert len(path)==2*q
            move(t,path[0])
            for x,y in zip(path,path[1:]):move(x,y)
            move(path[-1],r);branch='balanced_retain_B'
    assert sum(x>0 for x in s)==1 and sum(s)>0
    return dict(c=c,moves=moves,final=s,branch=branch)

def main():
    inp=json.loads((B/'inputs.json').read_bytes());results=[]
    for g in inp['graphs']:
        a,b,n=g['a'],g['b'],g['n'];cache=covers(g);off=[z for z in range(n) if z not in [0,a]];count=moves=0;branches={}
        with lzma.open(B/(g['graph']+'.jsonl.xz'),'wt',encoding='utf-8',newline='\n') as dest:
            for bits in itertools.product(range(2),repeat=len(off)):
                for M in g['totals']:
                    for u in range(M-sum(bits)+1):
                        c=[0]*n
                        for z,x in zip(off,bits):c[z]=x
                        c[0]=u;c[a]=M-sum(bits)-u;row=construct(g,c,cache);dest.write(json.dumps(row,separators=(',',':'))+'\n');count+=1;moves+=len(row['moves']);branches[row['branch']]=branches.get(row['branch'],0)+1
                        if count>1000000:raise RuntimeError('TRACE_CAP_UNKNOWN')
        result=dict(graph=g['graph'],traces=count,moves=moves,branches=branches);results.append(result);print(json.dumps(result),flush=True)
    (B/'summary.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':main()
