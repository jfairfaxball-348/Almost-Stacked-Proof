"""CAM-S009-01: exact consuming first-return fragment substitution.

No legal-reachability traversal or S006 optimizer import. Full inputs retained.
"""
import hashlib
import itertools
import json
import sys
import time
from functools import lru_cache
from pathlib import Path

GRAPHS=[('P3',3,[(0,1),(0,2)]),
 ('triangle_leaf',4,[(0,1),(0,2),(1,2),(0,3)]),
 ('triangle_tail2',5,[(0,1),(0,2),(1,2),(0,3),(3,4)]),
 ('F2',5,[(0,1),(0,2),(1,2),(0,3),(0,4)]),
 ('bowtie',5,[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)]),
 ('diamond',4,[(0,1),(0,2),(1,2),(1,3),(2,3)])]

def inputs():
    rows=[]
    for name,n,edges in GRAPHS:
        x,y=(0,1) if name=='P3' else (1,2)
        for N in range(13):
            for b in range(4):
                c=[0]*n;c[n-1]=N
                if b>=1:c[x]+=1 if b<3 else 3
                if b>=2:c[y]+=1 if b<3 else 3
                rows.append({'id':f'{name}_N{N}_b{b}','graph':name,'n':n,'edges':edges,'port':0,'configuration':c})
    extra=[('F2',(0,1,1,7,1)),('F2',(0,0,0,11,1)),('P3',(0,3,3)),('P3',(0,6,3))]
    for i,(name,c) in enumerate(extra):
        _,n,edges=next(g for g in GRAPHS if g[0]==name)
        rows.append({'id':f'explicit_{i}','graph':name,'n':n,'edges':edges,'port':0,'configuration':c})
    for N in (5,6):rows.append({'id':f'K3_pure{N}','graph':'K3','n':3,'edges':[(0,1),(0,2),(1,2)],'port':0,'configuration':[N,0,0]})
    assert len(rows)==318 and all(sum(r['configuration'])<=18 for r in rows)
    return rows

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def subtract(a,b):return tuple(x-y for x,y in zip(a,b))
def below(a,b):return all(x<=y for x,y in zip(a,b))

def solve(n,edges,c):
    c=tuple(c);T=sum(c);zero=(0,)*n;adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    unseen=set(range(1,n));pieces=[]
    while unseen:
        seed=min(unseen);todo=[seed];K={seed};unseen.remove(seed)
        while todo:
            for v in adj[todo.pop()]-{0}:
                if v in unseen:unseen.remove(v);K.add(v);todo.append(v)
        pieces.append(sorted(K))
    returns=[];root_profiles={q:[] for q in range(1,n)};profile_count=0
    for K in pieces:
        dims=len(K);pos={v:i for i,v in enumerate(K)};bounds=[c[v] for v in K]+[T]
        states={v:[set() for _ in range(T+1)] for v in K};fragments=set()
        for v in K:
            if c[v]:
                d=[0]*(dims+1);d[pos[v]]=1;states[v][1].add(tuple(d))
        # Two abstract port holes can merge across a port->interior edge.
        if T>=2:
            for v in adj[0]:
                d=[0]*(dims+1);d[-1]=2
                if v in pos:states[v][2].add(tuple(d))
        for m in range(2,T+1):
            for u in K:
                for i in range(1,m):
                    for a in states[u][i]:
                        for b in states[u][m-i]:
                            d=add(a,b)
                            if not below(d,bounds):continue
                            for v in adj[u]:
                                if v==0:fragments.add(d)
                                else:states[v][m].add(d)
            assert sum(len(s) for layers in states.values() for s in layers)+len(fragments)<=300000
        def encode(d):
            x=[0]*n
            for v in K:x[v]=d[pos[v]]
            assert d[-1]%2==0
            return tuple(x),d[-1]
        returns.extend(encode(d) for d in fragments)
        for q in K:
            root_profiles[q]=[encode(d) for layer in states[q] for d in layer]
        profile_count+=sum(len(s) for layers in states.values() for s in layers)+len(fragments)
    returns.sort(key=lambda d:(sum(d[0])+d[1],d[0],d[1]))
    for profiles in root_profiles.values():profiles.sort(key=lambda d:(sum(d[0])+d[1],d[0],d[1]))
    def subvectors(x):return itertools.product(*(range(v+1) for v in x))

    @lru_cache(None)
    def port_tree(x):
        m=sum(x)
        if m==1:return x[0]==1
        if m==0:return False
        for d,h in returns:
            if h>m or not below(d,x):continue
            rem=subtract(x,d)
            if port_forest(h,rem):return True
        return False

    @lru_cache(None)
    def port_forest(h,x):
        m=sum(x)
        if h==0:return m==0
        if m<h:return False
        if h==1:return port_tree(x)
        for a in subvectors(x):
            if not 1<=sum(a)<=m-h+1:continue
            if port_tree(a) and port_forest(h-1,subtract(x,a)):return True
        return False

    @lru_cache(None)
    def clear(q,x):
        if q==0:return port_tree(x)
        for d,h in root_profiles[q]:
            if below(d,x) and port_forest(h,subtract(x,d)):return True
        return False

    @lru_cache(None)
    def stack(q,x):
        m=sum(x)
        if not m:return False
        if clear(q,x):return True
        for a in subvectors(x):
            if not 1<=sum(a)<m:continue
            if clear(q,a) and stack(q,subtract(x,a)):return True
        return False

    cm=sum((1<<q) for q in range(n) if clear(q,c))
    sm=sum((1<<q) for q in range(n) if stack(q,c))
    caches=sum(f.cache_info().currsize for f in (port_tree,port_forest,clear,stack))
    assert caches<=300000
    return {'clear_mask':cm,'stack_mask':sm,'pieces':pieces,'fragment_states':profile_count,
        'return_profiles':len(returns),'cache_states':caches}

def main():
    start=time.monotonic();rows=inputs()
    input_raw=(json.dumps(rows,indent=2)+'\n').encode()
    dest=Path('evidence/S009/port_inputs.json')
    if '--check-only' in sys.argv:assert dest.read_bytes()==input_raw
    else:dest.write_bytes(input_raw)
    output=[]
    for i,row in enumerate(rows):
        result=solve(row['n'],row['edges'],row['configuration']);output.append({'id':row['id'],**result})
        if i%40==0:print(json.dumps({'completed':i+1,'seconds':time.monotonic()-start}),flush=True)
        assert time.monotonic()-start<600
    out={'campaign':'CAM-S009-01','input_sha256':hashlib.sha256(input_raw).hexdigest(),'cases':output,
         'complete_cases':len(output),'mass_cap':18,'seconds':time.monotonic()-start}
    dest=Path('evidence/S009/port_results.json')
    if '--check-only' in sys.argv:
        saved=json.loads(dest.read_text(encoding='utf-8'))
        assert {k:v for k,v in out.items() if k!='seconds'}=={k:v for k,v in saved.items() if k!='seconds'}
    else:dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in out.items() if k!='cases'}),flush=True)

if __name__=='__main__':main()
