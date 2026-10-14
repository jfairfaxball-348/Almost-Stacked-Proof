"""Independent all-label reverse winning layers and literal trace/ancestry check."""
import hashlib
import itertools
import json
import lzma
import sys
import time
from pathlib import Path

def states(n,t):
    for cuts in itertools.combinations(range(t+n-1),n-1):
        marks=(-1,)+cuts+(t+n-1,)
        yield tuple(marks[i+1]-marks[i]-1 for i in range(n))

def main():
    start=time.monotonic();raw=lzma.decompress(Path('evidence/S009/credit_traces.json.xz').read_bytes())
    meta=json.loads(Path('evidence/S009/credit_upper.json').read_text(encoding='utf-8'));traces=json.loads(raw)
    assert hashlib.sha256(raw).hexdigest()==meta['trace_raw_sha256']
    graphs={'diamond':(4,{(0,1),(0,2),(0,3),(1,2),(2,3)},9),
        'book_leaf':(5,{(0,1),(0,2),(0,3),(0,4),(1,2),(1,3)},12),
        'bowtie':(5,{(0,1),(0,2),(0,3),(0,4),(1,2),(3,4)},12)}
    layers=[];total=0;coverage={name:set() for name in graphs};moves=B3=0
    for name,(n,edges,upper) in graphs.items():
        old={};rows=[]
        for t in range(1,upper+1):
            current={c:0 for c in states(n,t)};assert len(current)<=300000
            if t==1:
                for q in range(n):current[tuple(int(v==q) for v in range(n))]=1<<q
            else:
                for c,mask in old.items():
                    if not mask:continue
                    for u,v in edges:
                        for a,b in ((u,v),(v,u)):
                            if c[b]:
                                d=list(c);d[a]+=2;d[b]-=1;current[tuple(d)]|=mask
            packed=json.dumps(sorted(current.items()),separators=(',',':')).encode()
            rows.append({'mass':t,'configurations':len(current),'winning':sum(bool(v) for v in current.values()),
                'root_mask_sha256':hashlib.sha256(packed).hexdigest()})
            total+=len(current);old=current
        assert all(old.values());layers.append({'graph':name,'upper_mass':upper,'layers':rows})
    for row in traces:
        name=row['graph'];n,edges,upper=graphs[name];c=tuple(row['configuration'])
        assert len(c)==n and sum(c)==upper and min(c)>=0 and c not in coverage[name];coverage[name].add(c)
        state=list(c)
        for u,v in row['moves']:
            assert tuple(sorted((u,v))) in edges and state[u]>=2
            state[u]-=2;state[v]+=1;moves+=1
        assert sum(state)==1 and len(row['moves'])==upper-1
        odd={q for q in range(1,n) if c[q]%2};cover=row['odd_path_cover']
        vertices=[v for path in cover for v in path];assert set(vertices)==odd and len(vertices)==len(odd)
        assert all(tuple(sorted((u,v))) in edges for p in cover for u,v in zip(p,p[1:]))
        assert row['B']==c[0]+sum(x//2 for x in c[1:])-len(cover)>=2
        if row['B']==3:
            B3+=1;nodes=row['protected_tree_nodes'];decoded=[]
            for i,node in enumerate(nodes):
                if node['children'] is None:
                    v,j=node['leaf'];assert v==node['v'] and 0<=j<c[v];leaves={(v,j)}
                else:
                    a,b=node['children'];assert a<i and b<i and nodes[a]['v']==nodes[b]['v']
                    assert tuple(sorted((node['v'],nodes[a]['v']))) in edges and not decoded[a]&decoded[b]
                    leaves=decoded[a]|decoded[b]
                decoded.append(leaves)
            forest=row['final_root_forest'];assert len(forest)==3 and row['protected_root_output'] in forest
            all_leaves=set()
            for i in forest:assert nodes[i]['v']==0 and not all_leaves&decoded[i];all_leaves|=decoded[i]
            assert all_leaves=={(v,j) for v in range(n) for j in range(c[v])}
            selected=nodes[row['protected_root_output']];a,b=selected['children'];v=nodes[a]['v']
            assert row['selected_triangle_edge']==[v,0]
            assert any(tuple(sorted((v,z))) in edges and (0,z) in edges for z in range(1,n) if z!=v)
    for name,(n,_,upper) in graphs.items():assert coverage[name]==set(states(n,upper))
    assert len(traces)==meta['traces']==3860 and moves==meta['moves']==41800
    assert B3==795
    out={'campaign':'CAM-S009-02','all_verified':True,'layers':layers,'complete_layers':33,'complete_configurations':total,
        'upper_traces':len(traces),'literal_moves':moves,'protected_B3_trees':B3,'threshold_claims':0,'seconds':time.monotonic()-start}
    dest=Path('evidence/S009/credit_verification.json')
    if '--check-only' in sys.argv:
        old=json.loads(dest.read_text(encoding='utf-8'))
        assert {k:v for k,v in old.items() if k!='seconds'}=={k:v for k,v in out.items() if k!='seconds'}
    else:dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in out.items() if k!='layers'}),flush=True)

if __name__=='__main__':main()
