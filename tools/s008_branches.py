"""CAM-S008-02 complete forward layers and constructive F_k upper traces."""
import hashlib
import itertools
import json
import lzma
import math
import time
from pathlib import Path

def configurations(n,t):
    if n==1:yield (t,);return
    for x in range(t+1):
        for c in configurations(n-1,t-x):yield (x,)+c

def fingerprint(states):return hashlib.sha256(json.dumps(sorted(states),separators=(',',':')).encode()).hexdigest()

def construct(c,k,goal):
    c=list(c);moves=[]
    def move(u,v):
        assert c[u]>=2 and (u==0 or v==0 or {u,v}=={1,2})
        c[u]-=2;c[v]+=1;moves.append([u,v])
    for u in (1,2):
        for _ in range(c[u]//2):move(u,0)
    pending=[]
    for v in range(3,k+3):
        m=c[v]
        if m%2==0:
            for _ in range(m//2):move(v,0)
        elif m>=5:
            for _ in range(m//2):move(v,0)
            move(0,v);move(v,0)
        else:pending.append(v)
    for v in pending:
        if c[v]==3:move(v,0)
        move(0,v);move(v,0)
    assert not any(c[3:])
    if goal=='stack' and sum(x>0 for x in c)==1:return moves
    if goal=='stack' and sum(c)==3:
        assert c[0]==2 and c[1]+c[2]==1
        move(0,1 if c[1] else 2);return moves
    assert sum(c)>=4
    while sum(c)>4:
        u=next(v for v in range(3) if c[v]>=2);move(u,(u+1)%3)
    def triangle(state):
        if sum(state)==1:return []
        for u,v in itertools.permutations(range(3),2):
            if state[u]<2:continue
            d=list(state);d[u]-=2;d[v]+=1;p=triangle(tuple(d))
            if p is not None:return [[u,v]]+p
        return None
    p=triangle(tuple(c[:3]));assert p is not None
    for u,v in p:move(u,v)
    assert sum(c)==1
    return moves

def main():
    start=time.monotonic();rows=[];traces=[]
    for k in range(1,4):
        n=k+3;edges=[(0,1),(0,2),(1,2)]+[(0,v) for v in range(3,n)]
        for goal in ('stack','clear'):
            g=3*k+(5 if goal=='stack' else 7);previous=set();layers=[]
            candidate=tuple((2*k+(3 if goal=='stack' else 7)) if v==3 else int(v>=4 or (goal=='stack' and v in (1,2))) for v in range(n))
            for t in range(1,g+1):
                assert math.comb(t+n-1,n-1)<=300000
                winners=set();losers=set()
                for c in configurations(n,t):
                    ok=sum(c)==1 if goal=='clear' else sum(x>0 for x in c)==1
                    if not ok:
                        for a,b in edges:
                            for u,v in ((a,b),(b,a)):
                                if c[u]<2:continue
                                d=list(c);d[u]-=2;d[v]+=1
                                if tuple(d) in previous:ok=True;break
                            if ok:break
                    (winners if ok else losers).add(c)
                    if t==g:traces.append({'k':k,'goal':goal,'configuration':c,'moves':construct(c,k,goal)})
                if 2<=t<g:assert losers
                if t==g-1:assert candidate in losers
                if t==g:assert not losers
                layers.append({'mass':t,'configurations':len(winners)+len(losers),'winning':len(winners),'losing':len(losers),'winning_sha256':fingerprint(winners),'losing_sha256':fingerprint(losers)})
                previous=winners;assert time.monotonic()-start<600
            rows.append({'k':k,'n':n,'goal':goal,'edges':edges,'threshold':g,'critical_AS_candidate':candidate,'layers':layers})
            print(k,goal,g,sum(x['configurations'] for x in layers),flush=True)
    raw=json.dumps(traces,separators=(',',':')).encode();Path('evidence/S008/branch_traces.json.xz').write_bytes(lzma.compress(raw))
    out={'campaign':'CAM-S008-02','graphs':rows,'trace_raw_sha256':hashlib.sha256(raw).hexdigest(),'construction_traces':len(traces),'construction_moves':sum(len(x['moves']) for x in traces),'seconds':time.monotonic()-start}
    Path('evidence/S008/branch_layers.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')

if __name__=='__main__':main()
