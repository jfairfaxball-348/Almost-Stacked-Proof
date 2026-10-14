"""Independent literal forest/count reconstruction and complete deleted-input closures."""
import hashlib
import json
import lzma
import sys
import time
from collections import deque
from pathlib import Path

GRAPHS={'K2':[(0,1)],'P3':[(0,1),(0,2)],'K3':[(0,1),(0,2),(1,2)],
        'triangle_leaf':[(0,1),(0,2),(1,2),(0,3)],
        'bowtie':[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)],
        'diamond':[(0,1),(0,2),(0,3),(1,2),(2,3)]}

def main():
    start=time.monotonic();sources=json.loads(lzma.decompress(Path('evidence/S010/count_traces.json.xz').read_bytes()))
    raw=lzma.decompress(Path('evidence/S010/reflection_traces.json.xz').read_bytes());produced=json.loads(raw)
    meta=json.loads(Path('evidence/S010/reflection_summary.json').read_text(encoding='utf-8'))
    assert hashlib.sha256(raw).hexdigest()==meta['output_raw_sha256']
    expected={(i,w) for i,r in enumerate(sources) if r['k']==3 for w,a in enumerate(r['c']) if a}
    actual={(r['source_index'],r['marked_leaf'][0]) for r in produced};assert actual==expected and len(actual)==len(produced)
    cached={};closed=[];moves=0
    for r in produced:
        original=sources[r['source_index']];w,j=r['marked_leaf'];assert j==0
        name=r['graph'];assert name==original['graph'];edges=GRAPHS[name];arcs=[a for e in edges for a in (e,e[::-1])]
        c=original['c'];n=len(c);deleted=c.copy();deleted[w]-=1;assert r['original_c']==c and r['deleted_c']==deleted
        state=c.copy()
        for i in original['arc_indices']:
            u,v=arcs[i];assert state[u]>=2;state[u]-=2;state[v]+=1
        assert state==[3 if v==original['q'] else 0 for v in range(n)]
        decoded=[]
        for i,node in enumerate(r['nodes']):
            if node['children'] is None:
                v,k=node['leaf'];assert v==node['v'] and 0<=k<c[v];part={(v,k)}
            else:
                a,b=node['children'];assert a<i and b<i and r['nodes'][a]['v']==r['nodes'][b]['v']
                assert (r['nodes'][a]['v'],node['v']) in arcs and not decoded[a]&decoded[b];part=decoded[a]|decoded[b]
            decoded.append(part)
        full={(v,k) for v,a in enumerate(c) for k in range(a)}
        roots=r['roots'];assert len(roots)==3 and all(r['nodes'][root]['v']==original['q'] for root in roots)
        assert set.union(*(decoded[root] for root in roots))==full and sum(len(decoded[root]) for root in roots)==len(full)
        mark=(w,0);marked=r['marked_tree_root'];assert marked in roots and mark in decoded[marked]
        remaining=[];walk=[];at=marked
        while r['nodes'][at]['children'] is not None:
            aa,bb=r['nodes'][at]['children']
            child=aa if mark in decoded[aa] else bb;sib=bb if child==aa else aa
            remaining.append(sib);walk.append([r['nodes'][at]['v'],r['nodes'][child]['v']]);at=child
        assert r['nodes'][at]['leaf']==[w,0] and walk==r['reversed_marked_walk'] and remaining==r['sibling_roots']
        parts=r['unmarked_roots']+remaining;assert len(r['unmarked_roots'])==2 and set(r['unmarked_roots'])==set(roots)-{marked}
        assert set.union(*(decoded[x] for x in parts))==full-{mark} and sum(len(decoded[x]) for x in parts)==len(full)-1
        state=deleted.copy();refcounts=[0]*len(arcs)
        for u,v in r['moves']:
            assert (u,v) in arcs and state[u]>=2;state[u]-=2;state[v]+=1;refcounts[arcs.index((u,v))]+=1;moves+=1
        assert state==r['final']==[2 if v==w else 0 for v in range(n)]
        expected_counts=original['m'].copy()
        for u,v in walk:expected_counts[arcs.index((v,u))]-=1;expected_counts[arcs.index((u,v))]+=1
        assert expected_counts==refcounts and min(expected_counts)>=0
        computed=[2 if v==w else 0 for v in range(n)]
        for (u,v),x in zip(arcs,expected_counts):computed[u]+=2*x;computed[v]-=x
        assert computed==deleted
        reverse={v:set() for v in range(n)};used={w}|{v for v,a in enumerate(deleted) if a}
        for (u,v),x in zip(arcs,expected_counts):
            if x:reverse[v].add(u);used|={u,v}
        reached={w};todo=[w]
        for v in todo:
            for u in reverse[v]:
                if u not in reached:reached.add(u);todo.append(u)
        assert used<=reached
        key=(name,tuple(deleted))
        if key not in cached:
            seen={tuple(deleted)};queue=deque(seen);stackmask=0
            while queue:
                x=queue.popleft();occupied=[v for v,a in enumerate(x) if a]
                if len(occupied)==1:stackmask|=1<<occupied[0]
                for u,v in arcs:
                    if x[u]>=2:
                        y=list(x);y[u]-=2;y[v]+=1;y=tuple(y)
                        if y not in seen:seen.add(y);queue.append(y)
                assert len(seen)<=300000
            cached[key]=(stackmask,len(seen))
            closed.append({'graph':name,'c':deleted,'stack_mask':stackmask,'states':len(seen),
                           'sha256':hashlib.sha256(json.dumps(sorted(seen),separators=(',',':')).encode()).hexdigest()})
        assert cached[key][0]&(1<<w) and time.monotonic()-start<600
    out={'campaign':'CAM-S010-03','all_verified':True,'marked_cases':len(produced),'reflected_literal_moves':moves,
         'distinct_deleted_inputs':len(cached),'complete_closure_states':sum(v[1] for v in cached.values()),
         'maximum_closure_states':max(v[1] for v in cached.values()),'closures':closed,'seconds':time.monotonic()-start}
    dest=Path('evidence/S010/reflection_verification.json')
    if '--check-only' in sys.argv:
        old=json.loads(dest.read_text(encoding='utf-8'))
        assert {k:v for k,v in old.items() if k!='seconds'}=={k:v for k,v in out.items() if k!='seconds'}
    else:dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in out.items() if k!='closures'}),flush=True)

if __name__=='__main__':main()
