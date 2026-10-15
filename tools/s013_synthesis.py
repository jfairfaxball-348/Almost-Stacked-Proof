"""CAM-S013-06 complete layer extrema, exact restricted maxima and conditional68."""
import hashlib,json,lzma,sys
from pathlib import Path
B=Path('evidence/S013')
def load(n):
    p=B/n;raw=p.read_bytes();return json.loads(lzma.decompress(raw) if p.suffix=='.xz' else raw)
def main():
    rows=[]
    for g,tab,meta in zip(load('precision_inputs.json'),load('precision_tables.json.xz'),load('precision.json')):
        n=g['n'];N=[set() for _ in range(n)]
        for u,v in g['edges']:N[u].add(v);N[v].add(u)
        minimal={s for s in range(n) if not any(N[t]<N[s] for t in range(n))}
        triangle_edges={tuple(e) for e in g['edges'] if N[e[0]]&N[e[1]]};tri={v for e in triangle_edges for v in e};H=[set() for _ in range(n)]
        for u,v in g['edges']:
            if (u,v) not in triangle_edges:H[u].add(v);H[v].add(u)
        seen=set();components=[]
        for v in range(n):
            if v in seen:continue
            todo=[v];component={v}
            for u in todo:
                for w in H[u]-component:component.add(w);todo.append(w)
            seen|=component;components.append(sorted(component))
        condition=all(all(N[s]<=N[t] or N[t]<=N[s] for s in comp if s not in tri for t in comp if t not in tri) for comp in components)
        extrema=[];maxima=[]
        for goal,j in [('stack',1),('clear',0)]:
            all_loss=[];as_loss=[];restricted=[];asminimal=[]
            for t,layer in enumerate(tab['layers']):
                losing=[tuple(c) for c,m in layer if not m[j]]
                for c in losing:
                    heavy=[v for v,a in enumerate(c) if a>1];AS=len(heavy)<=1;inR=all(s in minimal for s in heavy) and all(N[s]!=N[u] for s in heavy for u in heavy if s!=u)
                    all_loss.append(t)
                    if AS:as_loss.append(t)
                    if inR:restricted.append(t)
                    if AS and all(s in minimal for s in heavy):asminimal.append(t)
                if t<4 or not losing:continue
                Q=max(sum(a*a for a in c) for c in losing);qm=[c for c in losing if sum(a*a for a in c)==Q];P=min(sum(len(N[v])*c[v] for v in range(n)) for c in qm);selected=sorted(c for c in qm if sum(len(N[v])*c[v] for v in range(n))==P)
                for c in selected:
                    hv=[v for v,a in enumerate(c) if a>1];assert set(hv)<=minimal and all(not N[s]<=N[u] for s in hv for u in hv if s!=u)
                extrema.append(dict(goal=goal,mass=t,Q=Q,P=P,selected=selected))
            threshold=meta['thresholds'][goal]
            if n>=4 and threshold:
                m=[max(x) for x in [all_loss,as_loss,restricted,asminimal]];assert m[0]==m[2]==threshold-1 and m[1]==m[3]
                maxima.append(dict(goal=goal,L_all=m[0],L_AS=m[1],L_R=m[2],L_AS_minimal=m[3]))
        s,c=meta['thresholds']['stack'],meta['thresholds']['clear'];applicable=bool(c and c>=s+2 and condition)
        if applicable:
            cr=next(r for r in meta['extrema'] if r['goal']=='clear');assert all(sum(a>1 for a in x)<=1 for x in cr['maxima'])
        rows.append(dict(graph=g['graph'],minimal=sorted(minimal),H_components=components,condition68=condition,applicable68=applicable,extrema=extrema,maxima=maxima))
    p=B/'synthesis.json';b=(json.dumps(rows,separators=(',',':'))+'\n').encode()
    if '--check-only' in sys.argv:assert p.read_bytes()==b
    else:p.write_bytes(b)
    print(json.dumps(dict(graphs=len(rows),full_losing_layers=sum(len(r['extrema']) for r in rows),selected_extremizers=sum(len(e['selected']) for r in rows for e in r['extrema']),restricted_comparisons=sum(len(r['maxima']) for r in rows),applicable68=[r['graph'] for r in rows if r['applicable68']])))
if __name__=='__main__':main()
