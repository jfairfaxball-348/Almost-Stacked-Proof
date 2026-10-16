"""Exact bounded dominated-pile transposition test; no theorem presumed."""
import hashlib,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014')
def load(p):p=Path(p);return json.loads(lzma.decompress(p.read_bytes()) if p.suffix=='.xz' else p.read_bytes())
def main():
    for p,h in load(B/'swap_inputs.json').items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    rows=[];certs=[]
    for g,tab,meta in zip(load('evidence/S013/precision_inputs.json'),load('evidence/S013/precision_tables.json.xz'),load('evidence/S013/precision.json')):
        n=g['n'];arcs=sorted((u,v) for e in g['edges'] for u,v in [e,e[::-1]]);N=[{v for u,v in arcs if u==s} for s in range(n)];pairs=[(s,t) for s,t in arcs if N[t]-{s}<=N[s]-{t}]
        layers=[{tuple(c):mask for c,mask in layer} for layer in tab['layers']];failures=[];tests=0
        for goal,j in [('stack',1),('clear',0)]:
            first=None
            for mass,layer in enumerate(layers):
                losing=[c for c,m in layer.items() if not m[j]];Q=max((sum(a*a for a in c) for c in losing),default=-1);P=min((sum(len(N[v])*c[v] for v in range(n)) for c in losing if sum(a*a for a in c)==Q),default=-1)
                for c in sorted(losing):
                    for s,t in pairs:
                        if c[s]<=c[t]:continue
                        tests+=1;d=list(c);d[s],d[t]=d[t],d[s]
                        if not layer[tuple(d)][j]:continue
                        isQ=sum(a*a for a in c)==Q;row=dict(goal=goal,c=c,d=d,s=s,t=t,mass=mass,Qmax=isQ,QP=isQ and sum(len(N[v])*c[v] for v in range(n))==P,critical=mass==meta['thresholds'][goal]-1 if meta['thresholds'][goal] else None)
                        failures.append(row)
                        if first is None:first=row
            if first:
                c=tuple(first['c']);seen={c};todo=[c]
                for x in todo:
                    if len(seen)>300000:raise RuntimeError('CLOSURE_STATE_CAP_UNKNOWN')
                    assert not (sum(x)==1 if goal=='clear' else sum(a>0 for a in x)==1)
                    for u,v in arcs:
                        if x[u]>=2:
                            y=list(x);y[u]-=2;y[v]+=1;y=tuple(y)
                            if y not in seen:seen.add(y);todo.append(y)
                x=tuple(first['d']);moves=[]
                while not (sum(x)==1 if goal=='clear' else sum(a>0 for a in x)==1):
                    for u,v in arcs:
                        if x[u]<2:continue
                        y=list(x);y[u]-=2;y[v]+=1;y=tuple(y)
                        if layers[sum(y)][y][j]:break
                    else:raise AssertionError(x)
                    moves.append([u,v]);x=y
                certs.append(dict(graph=g['graph'],failure=first,states=sorted(seen),moves=moves,final=x))
        rows.append(dict(graph=g['graph'],pairs=pairs,tests=tests,failures=failures))
    result=dict(rows=rows,certificates=certs);p=B/'swap.json.xz';raw=(json.dumps(result,separators=(',',':'))+'\n').encode()
    if '--check-only' in sys.argv:assert lzma.decompress(p.read_bytes())==raw
    else:p.write_bytes(lzma.compress(raw))
    print(json.dumps(dict(tests=sum(r['tests'] for r in rows),failures=sum(len(r['failures']) for r in rows),Qmax_failures=sum(f['Qmax'] for r in rows for f in r['failures']),critical_failures=sum(bool(f['critical']) for r in rows for f in r['failures']),certificates=len(certs))),flush=True)
if __name__=='__main__':main()
