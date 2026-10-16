"""Independent triangle enumeration, full failure sets, closures and split histories."""
import hashlib,itertools,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014')
def read(p):p=Path(p);return json.loads(lzma.decompress(p.read_bytes()) if p.suffix=='.xz' else p.read_bytes())
def main():
    for p,h in read(B/'split_inputs.json').items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    data=read(B/'split.json.xz');states=moves=0
    for g,tab,meta,row in zip(read('evidence/S013/precision_inputs.json'),read('evidence/S013/precision_tables.json.xz'),read('evidence/S013/precision.json'),data['rows']):
        n=g['n'];edges={frozenset(e) for e in g['edges']};adj=lambda u,v:frozenset([u,v]) in edges;degree=[sum(adj(u,v) for v in range(n)) for u in range(n)]
        triples=[z for z in itertools.combinations(range(n),3) if all(adj(u,v) for u,v in itertools.combinations(z,2))]
        triples=sorted((u,min(set(z)-{u}),max(set(z)-{u})) for z in triples for u in z);layers=[{tuple(c):m for c,m in lay} for lay in tab['layers']];expected=[];tests=0
        for mass,layer in enumerate(layers):
            losses=[c for c,m in layer.items() if not m[0]];q=max((sum(a*a for a in c) for c in losses),default=-1);p=min((sum(a*b for a,b in zip(c,degree)) for c in losses if sum(a*a for a in c)==q),default=-1)
            for c in sorted(losses):
                if layer[c][1]==0:continue
                for u,v,w in triples:
                    if c[u]<2:continue
                    tests+=1;d=tuple(c[z]-2 if z==u else c[z]+1 if z in [v,w] else c[z] for z in range(n));mask=layer[d]
                    if mask[1]:expected.append(dict(c=list(c),u=u,v=v,w=w,d=list(d),masks=mask,Qmax=sum(a*a for a in c)==q,QP=sum(a*a for a in c)==q and sum(a*b for a,b in zip(c,degree))==p,critical=mass==meta['thresholds']['clear']-1 if meta['thresholds']['clear'] else None))
        assert row==dict(graph=g['graph'],tests=tests,failures=expected)
        certs=[c for c in data['certificates'] if c['graph']==g['graph']];assert len(certs)==bool(expected)
        if not expected:continue
        cert=certs[0];assert cert['c']==expected[0]['c'];ss={tuple(c) for c in cert['states']};reachable={tuple(cert['c'])}
        assert len(ss)==len(cert['states'])<=300000
        for c in sorted(ss,key=lambda c:-sum(c)):
            assert c in reachable and sum(c)!=1
            for u in range(n):
                if c[u]<2:continue
                for v in range(n):
                    if not adj(u,v):continue
                    d=list(c);d[u]-=2;d[v]+=1;assert tuple(d) in ss;reachable.add(tuple(d))
        assert reachable==ss;states+=len(ss);assert [t['failure'] for t in cert['traces']]==[f for f in expected if f['c']==cert['c']]
        for trace in cert['traces']:
            x=trace['failure']['d'].copy()
            for u,v in trace['moves']:assert adj(u,v) and x[u]>=2;x[u]-=2;x[v]+=1;moves+=1
            assert x==trace['final'] and len([a for a in x if a])==1 and sum(x)>0
    result=dict(tests=sum(r['tests'] for r in data['rows']),failures=sum(len(r['failures']) for r in data['rows']),Qmax_failures=sum(f['Qmax'] for r in data['rows'] for f in r['failures']),QP_failures=sum(f['QP'] for r in data['rows'] for f in r['failures']),critical_failures=sum(bool(f['critical']) for r in data['rows'] for f in r['failures']),certificates=len(data['certificates']),negative_closure_states=states,literal_moves=moves,all_generated_sets_equal=True)
    raw=(json.dumps(result,indent=2)+'\n').encode();p=B/'split_verification.json'
    if '--check-only' in sys.argv:assert p.read_bytes()==raw
    else:p.write_bytes(raw)
    print(json.dumps(result),flush=True)
if __name__=='__main__':main()
