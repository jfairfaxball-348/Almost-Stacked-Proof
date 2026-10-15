"""CAM-S013-03: actual root-connected count redirection and gap1 certificates."""
import json,lzma,sys
from pathlib import Path

ROOT=Path('evidence/S013')
def read(name):
    p=ROOT/name;b=p.read_bytes();return json.loads(lzma.decompress(b) if p.suffix=='.xz' else b)
def save(name,obj):
    p=ROOT/name;b=(json.dumps(obj,separators=(',',':'))+'\n').encode()
    if '--check-only' in sys.argv:assert (lzma.decompress(p.read_bytes()) if p.suffix=='.xz' else p.read_bytes())==b
    else:p.write_bytes(lzma.compress(b) if p.suffix=='.xz' else b)
def main():
    inputs=read('precision_inputs.json');tabs=read('precision_tables.json.xz');reports=read('precision.json')
    certs=[];failed=[];gaps=[];rows=[]
    for g,tab,report in zip(inputs,tabs,reports):
        n=g['n'];name=g['graph'];edges=g['edges'];arcs=sorted((u,v) for a,b in edges for u,v in [(a,b),(b,a)]);index={e:i for i,e in enumerate(arcs)}
        N=[{v for u,v in arcs if u==s} for s in range(n)];layers=[{tuple(c):m for c,m in lay} for lay in tab['layers']]
        def get(c):return layers[sum(c)][tuple(c)]
        def literal(c,kind,q=None):
            m=get(c)
            if q is None:q=next(v for v in range(n) if m[kind]>>v&1)
            x=tuple(c);moves=[];need={0:1,2:2,3:3}.get(kind)
            while not (x[q]>0 and sum(x)==x[q] and (need is None or x[q]==need)):
                for u,v in arcs:
                    if x[u]>=2:
                        d=list(x);d[u]-=2;d[v]+=1;d=tuple(d)
                        if get(d)[kind]>>q&1:break
                else:raise AssertionError(x)
                moves.append([u,v]);x=d
            return dict(c=c,q=q,kind=kind,moves=moves,final=x)
        def closure(c,j):
            seen={tuple(c)};todo=[tuple(c)]
            for x in todo:
                assert len(seen)<=300000 and not get(x)[j]
                for u,v in arcs:
                    if x[u]>=2:
                        d=list(x);d[u]-=2;d[v]+=1;d=tuple(d)
                        if d not in seen:seen.add(d);todo.append(d)
            return sorted(seen)
        open_tests=closed_tests=closed_bad=0;first={};generated=0
        for mass,lay in enumerate(layers):
            for c,mask in sorted(lay.items()):
                for s in range(n):
                    if c[s]<2:continue
                    for t in range(n):
                        if s==t or c[t]<2:continue
                        opened=N[t]<=N[s];closed=(s,t) in index and N[t]-{s}<=N[s]-{t}
                        if not opened and not closed:continue
                        for a in range(1,c[s]//2+1):
                            d=list(c);d[s]-=2*a;d[t]+=2*a;dm=get(d)
                            for goal,j in [('stack',1),('clear',0)]:
                                if opened:
                                    open_tests+=1;assert not dm[j] or mask[j],(name,c,s,t,a,goal)
                                    if mass<=8 and dm[j]:
                                        kind,q=next((kind,q) for kind in ([0] if j==0 else [0,2,3]) for q in range(n) if dm[kind]>>q&1)
                                        k={0:1,2:2,3:3}[kind];trace=literal(d,kind,q);m=[0]*len(arcs)
                                        for e in trace['moves']:m[index[tuple(e)]]+=1
                                        protect=None;P=[]
                                        if q!=t:
                                            queue=[t];paths={t:[]}
                                            for u in queue:
                                                if u==q:break
                                                for z,e in enumerate(arcs):
                                                    if e[0]==u and m[z] and e[1] not in paths:paths[e[1]]=paths[u]+[z];queue.append(e[1])
                                            P=paths[q];protect=P[0]
                                        mm=m.copy();left=a;redirect=[]
                                        for z,(u,v) in enumerate(arcs):
                                            if u!=t:continue
                                            used=min(left,m[z]-(z==protect))
                                            if used:mm[z]-=used;mm[index[(s,v)]]+=used;left-=used;redirect.append([z,used])
                                        assert left==0
                                        certs.append(dict(graph=name,c=c,d=d,s=s,t=t,a=a,goal=goal,q=q,k=k,m=m,modified=mm,path=P,redirect=redirect))
                                        generated+=1;assert len(certs)<=300000
                                if closed:
                                    closed_tests+=1
                                    if dm[j] and not mask[j]:
                                        closed_bad+=1
                                        if goal not in first:
                                            diagnostic=dict(graph=name,c=c,d=d,s=s,t=t,a=a,goal=goal)
                                            first[goal]=diagnostic
                                            failed.append(dict(diagnostic=diagnostic,positive=literal(d,j),negative=closure(c,j)))
        for sh in report['gap1_shadows']:
            c=sh['c'];assert not get(c)[0];successors=[]
            for u,v in arcs:
                if c[u]>=2:
                    d=list(c);d[u]-=2;d[v]+=1;assert get(d)[1]
                    successors.append(dict(move=[u,v],trace=literal(d,1)))
            gaps.append(dict(graph=name,c=c,negative=closure(c,0),successors=successors))
        row=dict(graph=name,open_tests=open_tests,closed_tests=closed_tests,closed_failures=closed_bad,first=list(first.values()),count_certificates=generated)
        rows.append(row);print(json.dumps(row),flush=True)
    save('concentration.json',rows);save('concentration_counts.json.xz',certs);save('concentration_failures.json.xz',failed);save('gap1_certificates.json.xz',gaps)
if __name__=='__main__':main()
