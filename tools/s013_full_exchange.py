"""CAM-S013-04: zero/singleton receivers and global degree refinement."""
import json,lzma,sys
from pathlib import Path
BASE=Path('evidence/S013')
def read(name):
    p=BASE/name;b=p.read_bytes();return json.loads(lzma.decompress(b) if p.suffix=='.xz' else b)
def save(name,x):
    p=BASE/name;b=(json.dumps(x,separators=(',',':'))+'\n').encode()
    if '--check-only' in sys.argv:assert (lzma.decompress(p.read_bytes()) if p.suffix=='.xz' else p.read_bytes())==b
    else:p.write_bytes(lzma.compress(b) if p.suffix=='.xz' else b)
def main():
    rows=[];certs=[];failures=[];extrema=[]
    for g,tab,old in zip(read('precision_inputs.json'),read('precision_tables.json.xz'),read('precision.json')):
        n=g['n'];name=g['graph'];arcs=sorted((u,v) for a,b in g['edges'] for u,v in [(a,b),(b,a)]);idx={e:i for i,e in enumerate(arcs)}
        N=[{v for u,v in arcs if u==s} for s in range(n)];degree=list(map(len,N));layers=[{tuple(c):m for c,m in lay} for lay in tab['layers']]
        def get(c):return layers[sum(c)][tuple(c)]
        count=bad=certcount=0;branches={}
        for mass,lay in enumerate(layers):
            for c,mask in sorted(lay.items()):
                for s in range(n):
                    if c[s]<2:continue
                    for t in range(n):
                        if s==t or c[t]>1 or not N[t]<=N[s]:continue
                        for a in range(1,c[s]//2+1):
                            d=list(c);d[s]-=2*a;d[t]+=2*a;dm=get(d)
                            for goal,j in [('stack',1),('clear',0)]:
                                count+=1
                                if dm[j] and not mask[j]:
                                    assert goal=='stack' and a==1 and mass==3 and c[s]==2 and c[t]==1
                                    failures.append(dict(graph=name,c=c,d=d,s=s,t=t,a=a,goal=goal));bad+=1;continue
                                if not dm[j] or mass>8:continue
                                kind,q=next((kind,q) for kind in ([0] if goal=='clear' else [0,2,3]) for q in range(n) if dm[kind]>>q&1);k={0:1,2:2,3:3}[kind]
                                x=tuple(d);m=[0]*len(arcs)
                                while not (sum(x)==x[q] and x[q]==k):
                                    for z,(u,v) in enumerate(arcs):
                                        if x[u]>=2:
                                            y=list(x);y[u]-=2;y[v]+=1;y=tuple(y)
                                            if get(y)[kind]>>q&1:break
                                    else:raise AssertionError(x)
                                    m[z]+=1;x=y
                                mm=m.copy();root=q;reroot=None;branch='ordinary';out=sum(m[z] for z,e in enumerate(arcs) if e[0]==t)
                                if root==t and out<a:
                                    if k==2:
                                        assert mass==2 and a==1 and c[s]==2;root=s;mm=[0]*len(arcs);branch='pure_two'
                                    else:
                                        assert k==3 and c[t]==0
                                        z=next(z for z,(u,v) in enumerate(arcs) if v==t and mm[z]);u,v=arcs[z]
                                        assert mm[z]==1 and sum(mm[j] for j,e in enumerate(arcs) if e[1]==t)==1
                                        mm[z]-=1;mm[idx[(t,u)]]+=1;root=u;reroot=z;branch='reroot_three'
                                pre=mm.copy();path=[];redirect=[]
                                if branch!='pure_two':
                                    out=sum(mm[z] for z,e in enumerate(arcs) if e[0]==t)
                                    if root!=t and out>=a+1:
                                        paths={t:[]};todo=[t]
                                        for u in todo:
                                            if u==root:break
                                            for z,(v,w) in enumerate(arcs):
                                                if v==u and mm[z] and w not in paths:paths[w]=paths[u]+[z];todo.append(w)
                                        path=paths[root]
                                    protect=path[0] if path else None;left=a
                                    for z,(u,v) in enumerate(arcs):
                                        if u==t:
                                            used=min(left,pre[z]-(z==protect))
                                            if used:mm[z]-=used;mm[idx[(s,v)]]+=used;left-=used;redirect.append([z,used])
                                    assert left==0
                                    if not path and root!=t and branch=='ordinary':branch='disappearing_zero'
                                branches[branch]=branches.get(branch,0)+1
                                certs.append(dict(graph=name,c=c,d=d,s=s,t=t,a=a,goal=goal,q=q,k=k,m=m,root=root,modified=mm,branch=branch,reroot=reroot,path=path,redirect=redirect));certcount+=1;assert len(certs)<=300000
        for r in old['extrema']:
            qmax=r['maxima'];P=min(sum(degree[v]*c[v] for v in range(n)) for c in qmax);best=[c for c in qmax if sum(degree[v]*c[v] for v in range(n))==P]
            for c in best:
                if sum(c)<4:continue
                heavy=[v for v in range(n) if c[v]>=2]
                assert all(not N[t]<N[s] for s in heavy for t in range(n))
                assert all(not N[t]<=N[s] for s in heavy for t in heavy if s!=t)
            extrema.append(dict(graph=name,goal=r['goal'],Q=r['Qmax'],P=P,selected=best))
        rows.append(dict(graph=name,tests=count,exceptions=bad,certificates=certcount,branches=branches));print(json.dumps(rows[-1]),flush=True)
    save('full_exchange.json',rows);save('full_exchange_counts.json.xz',certs);save('full_exchange_exceptions.json',failures);save('minimal_extrema.json',extrema)
if __name__=='__main__':main()
