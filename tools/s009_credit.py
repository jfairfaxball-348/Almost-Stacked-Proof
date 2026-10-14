"""CAM-S009-02 constructive path credit with a protected triangular ancestry."""
import hashlib
import itertools
import json
import lzma
import sys
import time
from pathlib import Path

GRAPHS=[('diamond',4,[(0,1),(0,2),(0,3),(1,2),(2,3)],[[1,2,3]],9),
 ('book_leaf',5,[(0,1),(0,2),(0,3),(0,4),(1,2),(1,3)],[[2,1,3],[4]],12),
 ('bowtie',5,[(0,1),(0,2),(0,3),(0,4),(1,2),(3,4)],[[1,2],[3,4]],12)]

def configs(n,t):
    if n==1:yield (t,);return
    for v in range(t+1):
        for rest in configs(n-1,t-v):yield (v,)+rest

def construct(c,edges,paths):
    n=len(c);adj=[set() for _ in c]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    assert adj[0]==set(range(1,n))
    nonisolated={v for v in range(1,n) if adj[v]-{0}}
    nodes=[];tokens=[];moves=[];protected=None
    for v,count in enumerate(c):
        pile=[]
        for j in range(count):pile.append(len(nodes));nodes.append({'v':v,'leaf':[v,j],'children':None})
        tokens.append(pile)
    def move(u,v,mark_allowed=False):
        nonlocal protected
        assert v in adj[u]
        eligible=[i for i,x in enumerate(tokens[u]) if u!=0 or x!=protected]
        assert len(eligible)>=2
        ia,ib=eligible[:2];a,b=tokens[u][ia],tokens[u][ib]
        for i in (ib,ia):tokens[u].pop(i)
        node=len(nodes);nodes.append({'v':v,'leaf':None,'children':[a,b]});tokens[v].append(node);moves.append([u,v])
        if mark_allowed and v==0 and u in nonisolated and protected is None:protected=node
    odd={v for v in range(1,n) if c[v]%2}
    cover=[]
    for path in paths:
        part=[]
        for v in path:
            if v in odd:part.append(v)
            elif part:cover.append(part);part=[]
        if part:cover.append(part)
    E={tuple(p):sum(c[v]//2 for v in p) for p in cover}
    B=c[0]+sum(x//2 for x in c[1:])-len(cover);assert B>=2
    for v in range(1,n):
        if v not in odd:
            while tokens[v]:move(v,0,True)
    positive=[p for p in cover if E[tuple(p)]>=2]
    pending=[p for p in cover if E[tuple(p)]<=1]
    # If no positive triangular output exists, its nonpositive task goes last.
    candidates=[p for p in pending if p[-1] in nonisolated]
    if candidates:
        chosen=candidates[-1];pending.remove(chosen);pending.append(chosen)
    for path in positive+pending:
        for v in path:
            while len(tokens[v])>=2:move(v,0)
        move(0,path[0])
        for u,v in zip(path,path[1:]):move(u,v)
        move(path[-1],0,True)
    assert len(tokens[0])==B and all(not pile for pile in tokens[1:])
    evidence={'B':B,'odd_path_cover':cover,'protected_root_output':protected,'selected_triangle_edge':None}
    if B==3:
        assert protected in tokens[0]
        node=nodes[protected];a,b=node['children'];v=nodes[a]['v']
        assert nodes[b]['v']==v and v in nonisolated
        z=min(adj[v]&adj[0]);assert z not in (0,v)
        replay=[]
        def evaluate(j):
            node=nodes[j]
            if node['children'] is None:return
            x,y=node['children'];evaluate(x);evaluate(y);replay.append([nodes[x]['v'],node['v']])
        for j in tokens[0]:
            if j!=protected:evaluate(j)
        evaluate(a);evaluate(b);replay.extend([[v,z],[0,z],[z,0]])
        moves=replay;evidence['selected_triangle_edge']=[v,0]
        evidence['protected_tree_nodes']=nodes;evidence['final_root_forest']=tokens[0]
    elif B==2:
        moves.append([0,min(adj[0])])
    else:
        tri=[0]+sorted(next((u,v) for u,v in edges if u and v));state=[B,0,0]
        def append(u,v):
            assert state[u]>=2;state[u]-=2;state[v]+=1;moves.append([tri[u],tri[v]])
        while sum(state)>4:
            u=next(i for i in range(3) if state[i]>=2);append(u,(u+1)%3)
        def clear(x):
            if sum(x)==1:return []
            for u,v in itertools.permutations(range(3),2):
                if x[u]<2:continue
                y=list(x);y[u]-=2;y[v]+=1;path=clear(tuple(y))
                if path is not None:return [(u,v)]+path
            return None
        path=clear(tuple(state));assert path is not None
        for u,v in path:append(u,v)
    return {'configuration':c,'moves':moves,**evidence}

def main():
    start=time.monotonic();rows=[];info=[]
    for name,n,edges,paths,mass in GRAPHS:
        local=[]
        for c in configs(n,mass):local.append({'graph':name,**construct(c,edges,paths)})
        rows.extend(local);info.append({'graph':name,'n':n,'edges':edges,'base_paths':paths,'upper_mass':mass,
            'all_distribution_traces':len(local),'B3_traces':sum(r['B']==3 for r in local)})
        assert time.monotonic()-start<600
    raw=json.dumps(rows,separators=(',',':')).encode();dest=Path('evidence/S009/credit_traces.json.xz')
    meta={'campaign':'CAM-S009-02','graphs':info,'traces':len(rows),'moves':sum(len(r['moves']) for r in rows),
        'trace_raw_sha256':hashlib.sha256(raw).hexdigest(),'seconds':time.monotonic()-start}
    md=Path('evidence/S009/credit_upper.json')
    if '--check-only' in sys.argv:
        assert lzma.decompress(dest.read_bytes())==raw
        saved=json.loads(md.read_text(encoding='utf-8'))
        actual=json.loads(json.dumps(meta))
        assert {k:v for k,v in saved.items() if k!='seconds'}=={k:v for k,v in actual.items() if k!='seconds'}
    else:
        dest.write_bytes(lzma.compress(raw));md.write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(meta),flush=True)

if __name__=='__main__':main()
