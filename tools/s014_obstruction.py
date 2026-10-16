"""Full closures and all six parity-class AS histories at genuine critical size."""
import collections,itertools,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/obstruction')
def layers(path,n):
    result={}
    with lzma.open(path,'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);result[mass]={tuple(f.read(16)[:n]) for _ in range(count)}
    return result
def explore(start,edges,stop):
    start=tuple(start);parent={start:None};queue=collections.deque([start]);arcs=[(u,v) for edge in edges for u,v in [edge,edge[::-1]]]
    while queue:
        c=queue.popleft()
        if stop and sum(x>0 for x in c)==1:
            moves=[];end=c
            while parent[c] is not None:c,move=parent[c];moves.append(move)
            return dict(moves=moves[::-1],final=end)
        for u,v in arcs:
            if c[u]>=2:
                d=list(c);d[u]-=2;d[v]+=1;d=tuple(d)
                if d not in parent:parent[d]=(c,[u,v]);queue.append(d)
        if len(parent)>300000:raise RuntimeError('CLOSURE_CAP_UNKNOWN')
    assert not stop
    return sorted(parent)
def main():
    results=[]
    for case in json.loads((B/'threshold_inputs.json').read_bytes())['cases']:
        g=case['graph'];name=g['graph'];n=g['n'];new=layers(B/(name+'_stack_threshold.bin.xz'),n);old=layers(case['old_certificate'],n);assert new==old
        c=[3,3,1,1,0,0];crit=new[8];assert tuple(c) in crit;other=min(d for d in crit if sum(x>1 for x in d)<=1 and [x%2 for x in d]!=[x%2 for x in c]);rows=[]
        for source in range(n):
            d=[x%2 for x in c];d[source]+=8-sum(d);assert tuple(d) not in crit;rows.append(dict(source=source,d=d,**explore(d,g['edges'],True)))
        units=[]
        for s in range(n):
            if c[s]:
                for t in range(n):
                    if s==t:continue
                    d=c.copy();d[s]-=1;d[t]+=1;units.append(dict(s=s,t=t,d=d,losing=tuple(d) in crit))
        alpha=max(len(U) for k in range(n+1) for U in itertools.combinations(range(n),k) if not any(u in U and v in U for u,v in g['edges']))
        results.append(dict(graph=g,c=c,negative=explore(c,g['edges'],False),AS_critical=other,AS_negative=explore(other,g['edges'],False),same_parity_AS_winners=rows,unit_redistributions=units,alpha=alpha))
    (B/'certificates.json.xz').write_bytes(lzma.compress((json.dumps(results,separators=(',',':'))+'\n').encode()));print(json.dumps(dict(graphs=len(results),all_six_parity_winners=sum(len(r['same_parity_AS_winners']) for r in results),negative_closure_states=sum(len(r['negative'])+len(r['AS_negative']) for r in results),literal_moves=sum(len(t['moves']) for r in results for t in r['same_parity_AS_winners']))),flush=True)
if __name__=='__main__':main()
