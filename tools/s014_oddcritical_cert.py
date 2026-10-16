"""Extract literal winners and full negative closures for registered failures."""
import json,lzma,struct,sys
from pathlib import Path
B=Path(sys.argv[1]) if len(sys.argv)>1 else Path('evidence/S014/oddcritical')
def main():
    out=[]
    for case in json.loads((B/'inputs.json').read_bytes())['cases']:
        g=case['graph'];f=case['failure'];n=g['n'];units=[1<<(8*i) for i in range(n)];arcs=sorted((u,v) for e in g['edges'] for u,v in [e,e[::-1]]);db={}
        with lzma.open(Path('evidence/S014/oddlarge_v2')/(g['graph']+'.bin.xz'),'rb') as src:
            while raw:=src.read(9):x,k=struct.unpack('<QB',raw);db[x]=k
        pack=lambda c:sum(z*units[i] for i,z in enumerate(c))
        unpack=lambda x:[(x>>(8*i))&255 for i in range(n)]
        root=pack(f['c']);closure={root};todo=[root]
        for x in todo:
            assert db[x]==254
            for u,v in arcs:
                if (x>>(8*u))&255<2:continue
                y=x-2*units[u]+units[v]
                if y not in closure:closure.add(y);todo.append(y)
        histories=[]
        for cand in f['candidates']:
            x=pack(cand['d']);moves=[]
            while db[x]!=255:
                u,v=divmod(db[x],n);assert u<n and v<n and (x>>(8*u))&255>=2
                moves.append([u,v]);x=x-2*units[u]+units[v]
            histories.append(dict(v=cand['v'],input=cand['d'],moves=moves,terminal=unpack(x)))
        report=json.loads((B/(g['graph']+'_stack_threshold.json')).read_bytes());critical=report['threshold']-1 if report['threshold'] else None
        row=next(row for row in report['rows'] if row['mass']==sum(f['c']));colors={0:1};todo=[0]
        for u in todo:
            for a,b in arcs:
                if a==u and b not in colors:colors[b]=-colors[u];todo.append(b)
        bip=all(colors[u]!=colors[v] for u,v in arcs)
        out.append(dict(graph=g,failure=f,closure=[unpack(x) for x in sorted(closure)],histories=histories,threshold=report['threshold'],critical_mass=critical,failure_mass=sum(f['c']),failure_is_critical=sum(f['c'])==critical,failure_layer_Q_max=row['Q'],failure_Q=sum(z*z for z in f['c']),bipartite=bip,signed_residue=sum(colors[v]*f['c'][v] for v in range(n))%3 if bip else None))
    (B/'certificates.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':main()
