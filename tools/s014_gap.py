"""CAM-S014-01 historical positive-gap extrema; no threshold expansion."""
import hashlib,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014')

def traits(name,n,edges,s,g,losers):
    N=[set() for _ in range(n)]
    for u,v in edges:N[u].add(v);N[v].add(u)
    tri={v for u in range(n) for v in N[u] if N[u]&N[v]}
    Q=max(sum(x*x for x in c) for c in losers)
    qm=sorted(c for c in losers if sum(x*x for x in c)==Q)
    P=min(sum(len(N[v])*c[v] for v in range(n)) for c in qm)
    qp=[c for c in qm if sum(len(N[v])*c[v] for v in range(n))==P]
    avoid=lambda c:all(c[v]<2 for v in tri)
    AS=lambda c:sum(x>1 for x in c)<=1
    return dict(graph=name,n=n,edges=edges,stack=s,clear=g,gap=g-s,critical_losers=len(losers),triangle_vertices=sorted(tri),Q=Q,P=P,Qmax=qm,QPmin=qp,
        predicates={kind+suffix:op(fun(c) for c in values) for kind,values in [('Q',qm),('QP',qp)] for suffix,op,fun in [('_every_nontri',all,avoid),('_some_nontri',any,avoid),('_every_AS',all,AS),('_some_AS',any,AS)]})

def main():
    rows=[];status=[]
    for inp in json.loads((B/'gap_inputs.json').read_bytes()):
        for p,h in inp['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
        m=json.loads(Path(inp['clear']).read_bytes())
        sm=json.loads(Path(inp['stack']).read_bytes()) if inp['stack'] else {}
        if sm.get('scope')!='EXACT_THRESHOLD':status.append([m['graph'],'STACK_UNKNOWN']);continue
        g=m['threshold'];s=sm['threshold'];assert g>=s
        if g==s:status.append([m['graph'],'ZERO_GAP']);continue
        critical=None
        with lzma.open(inp['certificate'],'rb') as f:
            while hdr:=f.read(12):
                assert len(hdr)==12
                mass=int.from_bytes(hdr[:4],'little');count=int.from_bytes(hdr[4:],'little');size=count*16
                if mass==g-1:
                    if count>300000:break
                    raw=f.read(size);assert len(raw)==size
                    critical={tuple((int.from_bytes(raw[k:k+16],'little')>>(8*i))&255 for i in range(m['n'])) for k in range(0,size,16)}
                    assert len(critical)==count and all(sum(c)==g-1 for c in critical);break
                while size:
                    z=f.read(min(size,1048576));assert z;size-=len(z)
        if critical is None:status.append([m['graph'],'CRITICAL_LAYER_UNKNOWN']);continue
        rows.append(traits(m['graph'],m['n'],m['edges'],s,g,critical));status.append([m['graph'],'POSITIVE_GAP_COMPLETE'])
    tab=json.loads(lzma.decompress(Path('evidence/S013/precision_tables.json.xz').read_bytes()))
    metas=json.loads(Path('evidence/S013/precision.json').read_bytes());inputs=json.loads(Path('evidence/S013/precision_inputs.json').read_bytes())
    precision=[]
    for inp,t,meta in zip(inputs,tab,metas):
        s=meta['thresholds']['stack'];g=meta['thresholds']['clear']
        if not s or not g or g<=s:continue
        losers=[tuple(c) for c,m in t['layers'][g-1] if not m[0]]
        precision.append(traits(inp['graph'],inp['n'],inp['edges'],s,g,losers))
    witnesses=[]
    for row in rows+precision:
        bad=next((c for c in row['Qmax'] if any(c[v]>1 for v in row['triangle_vertices'])),None)
        if bad is None:continue
        arcs=sorted((u,v) for e in row['edges'] for u,v in [e,e[::-1]])
        seen={bad};todo=[bad]
        for c in todo:
            assert len(seen)<=300000
            assert sum(c)!=1
            for u,v in arcs:
                if c[u]>=2:
                    d=list(c);d[u]-=2;d[v]+=1;d=tuple(d)
                    if d not in seen:seen.add(d);todo.append(d)
        witnesses.append(dict(graph=row['graph'],c=bad,states=sorted(seen)))
    result=dict(campaign='CAM-S014-01',status=status,archive=rows,precision=precision,negative_witnesses=witnesses,threshold_claims=0)
    raw=(json.dumps(result,separators=(',',':'))+'\n').encode();p=B/'gap_extrema.json.xz'
    if '--check-only' in sys.argv:assert lzma.decompress(p.read_bytes())==raw
    else:p.write_bytes(lzma.compress(raw))
    print(json.dumps(dict(archive_cases=len(rows),precision_cases=len(precision),predicate_failures={k:[r['graph'] for r in rows+precision if not r['predicates'][k]] for k in rows[0]['predicates']} if rows else result['status'])))
if __name__=='__main__':main()
