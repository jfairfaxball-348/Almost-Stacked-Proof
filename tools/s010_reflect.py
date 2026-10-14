"""CAM-S010-03 full marked-tree reflection of every registered three-pile trace."""
import hashlib
import json
import lzma
import sys
import time
from pathlib import Path

EDGES={'K2':[(0,1)],'P3':[(0,1),(0,2)],'K3':[(0,1),(0,2),(1,2)],
       'triangle_leaf':[(0,1),(0,2),(1,2),(0,3)],
       'bowtie':[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)],
       'diamond':[(0,1),(0,2),(0,3),(1,2),(2,3)]}

def main():
    start=time.monotonic();source_raw=lzma.decompress(Path('evidence/S010/count_traces.json.xz').read_bytes())
    sources=json.loads(source_raw);rows=[]
    for source_index,source in enumerate(sources):
        if source['k']!=3:continue
        c=source['c'];n=len(c);arcs=[a for e in EDGES[source['graph']] for a in (e,e[::-1])]
        nodes=[];piles=[]
        for v,count in enumerate(c):
            pile=[]
            for j in range(count):pile.append(len(nodes));nodes.append({'v':v,'leaf':[v,j],'children':None})
            piles.append(pile)
        for i in source['arc_indices']:
            u,v=arcs[i];assert len(piles[u])>=2;a=piles[u].pop(0);b=piles[u].pop(0)
            piles[v].append(len(nodes));nodes.append({'v':v,'leaf':None,'children':[a,b]})
        roots=piles[source['q']];assert len(roots)==3 and sum(map(len,piles))==3 and len(nodes)<=300000
        leaves=[]
        for node in nodes:
            leaves.append({tuple(node['leaf'])} if node['children'] is None else leaves[node['children'][0]]|leaves[node['children'][1]])
        for w,amount in enumerate(c):
            if not amount:continue
            marked=(w,0);root=next(r for r in roots if marked in leaves[r]);siblings=[];backwards=[]
            current=root
            while nodes[current]['children'] is not None:
                a,b=nodes[current]['children'];child,sibling=(a,b) if marked in leaves[a] else (b,a)
                siblings.append(sibling);backwards.append([nodes[current]['v'],nodes[child]['v']]);current=child
            assert nodes[current]['leaf']==[w,0]
            parts=[r for r in roots if r!=root]+siblings
            moves=[]
            def evaluate(j):
                nd=nodes[j]
                if nd['children'] is None:return
                a,b=nd['children'];evaluate(a);evaluate(b);moves.append([nodes[a]['v'],nd['v']])
            for j in parts:evaluate(j)
            moves.extend(backwards)
            deleted=c.copy();deleted[w]-=1;state=deleted.copy()
            for u,v in moves:assert state[u]>=2;state[u]-=2;state[v]+=1
            assert state==[2 if v==w else 0 for v in range(n)]
            rows.append({'source_index':source_index,'graph':source['graph'],'original_c':c,'deleted_c':deleted,
                         'marked_leaf':[w,0],'final_original_root':source['q'],'nodes':nodes,'roots':roots,
                         'marked_tree_root':root,'sibling_roots':siblings,'unmarked_roots':[r for r in roots if r!=root],
                         'reversed_marked_walk':backwards,'moves':moves,'final':state})
        assert time.monotonic()-start<600
    raw=json.dumps(rows,separators=(',',':')).encode()
    out={'campaign':'CAM-S010-03','input_trace_raw_sha256':hashlib.sha256(source_raw).hexdigest(),
         'marked_cases':len(rows),'original_three_pile_traces':sum(r['k']==3 for r in sources),
         'reflected_moves':sum(len(r['moves']) for r in rows),'empty_marked_paths':sum(not r['reversed_marked_walk'] for r in rows),
         'output_raw_sha256':hashlib.sha256(raw).hexdigest(),'seconds':time.monotonic()-start}
    dest=Path('evidence/S010/reflection_traces.json.xz');mp=Path('evidence/S010/reflection_summary.json')
    if '--check-only' in sys.argv:
        assert lzma.decompress(dest.read_bytes())==raw
        old=json.loads(mp.read_text(encoding='utf-8'))
        assert {k:v for k,v in out.items() if k!='seconds'}=={k:v for k,v in old.items() if k!='seconds'}
    else:
        dest.write_bytes(lzma.compress(raw));mp.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(out),flush=True)

if __name__=='__main__':main()
