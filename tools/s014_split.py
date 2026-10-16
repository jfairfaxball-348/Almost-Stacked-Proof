"""Exact triangle-pair split challenge, distinct from adjacent single-receiver shifts."""
import hashlib,itertools,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014')
def read(p):p=Path(p);return json.loads(lzma.decompress(p.read_bytes()) if p.suffix=='.xz' else p.read_bytes())
def main():
    for p,h in read(B/'split_inputs.json').items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    rows=[];certs=[]
    for g,tab,meta in zip(read('evidence/S013/precision_inputs.json'),read('evidence/S013/precision_tables.json.xz'),read('evidence/S013/precision.json')):
        n=g['n'];arcs=sorted((u,v) for e in g['edges'] for u,v in [e,e[::-1]]);N=[{v for u,v in arcs if u==s} for s in range(n)]
        triangles=[(u,v,w) for u in range(n) for v,w in itertools.combinations(sorted(N[u]),2) if w in N[v]]
        layers=[{tuple(c):m for c,m in lay} for lay in tab['layers']];tests=0;failures=[]
        for mass,layer in enumerate(layers):
            losing=[c for c,m in layer.items() if not m[0]];Q=max((sum(a*a for a in c) for c in losing),default=-1);P=min((sum(len(N[v])*c[v] for v in range(n)) for c in losing if sum(a*a for a in c)==Q),default=-1)
            for c in sorted(losing):
                if not layer[c][1]:continue
                for u,v,w in triangles:
                    if c[u]<2:continue
                    tests+=1;d=list(c);d[u]-=2;d[v]+=1;d[w]+=1;dm=layer[tuple(d)]
                    if not dm[1]:continue
                    failures.append(dict(c=c,u=u,v=v,w=w,d=d,masks=dm,Qmax=sum(a*a for a in c)==Q,QP=sum(a*a for a in c)==Q and sum(len(N[v])*c[v] for v in range(n))==P,critical=mass==meta['thresholds']['clear']-1 if meta['thresholds']['clear'] else None))
        if failures:
            first=failures[0];start=tuple(first['c']);seen={start};todo=[start]
            for c in todo:
                if len(seen)>300000:raise RuntimeError('CLOSURE_STATE_CAP_UNKNOWN')
                assert sum(c)!=1
                for u,v in arcs:
                    if c[u]>=2:
                        d=list(c);d[u]-=2;d[v]+=1;d=tuple(d)
                        if d not in seen:seen.add(d);todo.append(d)
            traces=[]
            for f in failures:
                if f['c']!=first['c']:continue
                x=tuple(f['d']);moves=[]
                while sum(a>0 for a in x)!=1:
                    for u,v in arcs:
                        if x[u]<2:continue
                        d=list(x);d[u]-=2;d[v]+=1;d=tuple(d)
                        if layers[sum(d)][d][1]:break
                    else:raise AssertionError(x)
                    moves.append([u,v]);x=d
                traces.append(dict(failure=f,moves=moves,final=x))
            certs.append(dict(graph=g['graph'],c=start,states=sorted(seen),traces=traces))
        rows.append(dict(graph=g['graph'],tests=tests,failures=failures))
    out=dict(rows=rows,certificates=certs);raw=(json.dumps(out,separators=(',',':'))+'\n').encode();p=B/'split.json.xz'
    if '--check-only' in sys.argv:assert lzma.decompress(p.read_bytes())==raw
    else:p.write_bytes(lzma.compress(raw))
    print(json.dumps(dict(tests=sum(r['tests'] for r in rows),failures=sum(len(r['failures']) for r in rows),Qmax_failures=sum(f['Qmax'] for r in rows for f in r['failures']),QP_failures=sum(f['QP'] for r in rows for f in r['failures']),critical_failures=sum(bool(f['critical']) for r in rows for f in r['failures']),certificates=len(certs))),flush=True)
if __name__=='__main__':main()
