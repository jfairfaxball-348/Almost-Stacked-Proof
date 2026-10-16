"""All parity-class AS candidates at actual critical masses; literal winners."""
import hashlib,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/parity');R=Path('evidence/S014/regular')
def readcritical(g,goal):
    stem=g['graph']+'_'+goal+'_threshold';T=json.loads((R/(stem+'.json')).read_bytes())['threshold'];result=[]
    with lzma.open(R/(stem+'.bin.xz'),'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw)
            for _ in range(count):
                c=tuple(f.read(16)[:g['n']])
                if mass==T-1:result.append(c)
    return T,result
def winning_trace(g,d,source,goal):
    gram=json.loads(lzma.decompress((R/(g['graph']+'_binary_s'+str(source)+'_rays.json.xz')).read_bytes()));off=tuple(d[v] for v in range(g['n']) if v!=source);di=next(i for i,v in enumerate(gram['vectors']) if tuple(v)==off);N=d[source];V=gram['S'] if goal=='stack' else gram['C'];W=gram['SW'] if goal=='stack' else gram['CW'];poss=[(V[di][4*q+N%3],q,W[di][4*q+N%3]) for q in range(g['n']) if V[di][4*q+N%3] is not None];cost,q,w=min(poss);assert cost<=N and cost>=1 and (N-cost)%3==0;s=list(d);moves=[]
    neighbor=next(v for e in g['edges'] for u,v in [e,e[::-1]] if u==source)
    def move(u,v):assert s[u]>=2;s[u]-=2;s[v]+=1;moves.append([u,v]);assert len(moves)<=300000
    while s[source]>cost:move(source,neighbor);move(source,neighbor);move(neighbor,source)
    nodes=gram['nodes'];todo=[(w,False)]
    while todo:
        z,ready=todo.pop();typ,v,ix,k,cost,a,b=nodes[z]
        if not typ:continue
        if not ready:todo.extend([(z,True),(b,False),(a,False)])
        elif typ==1:move(nodes[a][1],v)
    assert sum(x>0 for x in s)==1 and (goal=='stack' or sum(s)==1)
    return dict(moves=moves,final=s)
def main():
    for p,h in json.loads((B/'inputs.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    graphs=json.loads((R/'ray_inputs.json').read_bytes())['graphs'];rows=[];groups=[]
    for g in graphs:
        for goal in ['stack','clear']:
            T,critical=readcritical(g,goal);losers=set(critical)
            for c in critical:
                if sum(x>1 for x in c)<=1:continue
                group=[]
                for source in range(g['n']):
                    d=[x%2 for x in c];d[source]+=sum(x-x%2 for x in c);losing=tuple(d) in losers;row=dict(graph=g['graph'],goal=goal,T=T,c=c,source=source,d=d,losing=losing)
                    if not losing:row.update(winning_trace(g,d,source,goal))
                    rows.append(row);group.append(row)
                    assert len(rows)<=300000
                groups.append(dict(graph=g['graph'],goal=goal,c=c,all_parity_class_AS_win=all(not r['losing'] for r in group)))
    (B/'certificates.json.xz').write_bytes(lzma.compress((json.dumps(dict(rows=rows,groups=groups),separators=(',',':'))+'\n').encode()));print(json.dumps(dict(cases=len(rows),critical_nonAS_inputs=len(groups),complete_parity_failures=sum(r['all_parity_class_AS_win'] for r in groups),literal_moves=sum(len(r.get('moves',[])) for r in rows))),flush=True)
if __name__=='__main__':main()
