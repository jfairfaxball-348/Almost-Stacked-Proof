"""Complete finite boundary reachability; each retained history is literal."""
import collections,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014/firstfires')
def main():
    inp=json.loads((B/'inputs.json').read_bytes())
    for g in inp['graphs']:
        n=g['n'];arcs=[(u,v) for e in g['edges'] for u,v in [e,e[::-1]]];records=[];states=0;terminals=0
        for mask in range(1<<n):
            c=tuple(int(mask>>v&1) for v in range(n));start=(c,0,0);parents={start:None};todo=collections.deque([start])
            while todo:
                key=todo.popleft();c,I,O=key;nexts=[]
                if I<3:
                    for v in range(n):d=list(c);d[v]+=1;nexts.append(((tuple(d),I+1,O),['in',v]))
                for u in range(n):
                    if c[u]>=2:d=list(c);d[u]-=2;nexts.append(((tuple(d),I,O+1),['out',u]))
                for u,v in arcs:
                    if c[u]>=2:d=list(c);d[u]-=2;d[v]+=1;nexts.append(((tuple(d),I,O),['move',u,v]))
                for child,op in nexts:
                    if child not in parents:parents[child]=(key,op);todo.append(child)
                if len(parents)>300000:raise RuntimeError('CELL_CAP_UNKNOWN')
            ends=[]
            for key in sorted(parents):
                if sum(x>0 for x in key[0])>1:continue
                trace=[];k=key
                while parents[k] is not None:k,op=parents[k];trace.append(op)
                ends.append(dict(cell=key,ops=trace[::-1]))
            records.append(dict(mask=mask,cells=sorted(parents),terminal_histories=ends));states+=len(parents);terminals+=len(ends)
        data=dict(graph=g,subsets=records);(B/(g['name']+'.json.xz')).write_bytes(lzma.compress((json.dumps(data,separators=(',',':'))+'\n').encode()));print(json.dumps(dict(graph=g['name'],cells=states,terminal_histories=terminals)),flush=True)
if __name__=='__main__':main()
