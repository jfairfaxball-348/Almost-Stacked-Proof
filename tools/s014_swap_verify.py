"""Independent full labeled SWAP predicate and certificate verifier."""
import hashlib,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014')
def get(p):p=Path(p);return json.loads(lzma.decompress(p.read_bytes()) if p.suffix=='.xz' else p.read_bytes())
def main():
    for p,h in get(B/'swap_inputs.json').items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    data=get(B/'swap.json.xz');moves=states=0
    for g,table,meta,row in zip(get('evidence/S013/precision_inputs.json'),get('evidence/S013/precision_tables.json.xz'),get('evidence/S013/precision.json'),data['rows']):
        n=g['n'];E={frozenset(e) for e in g['edges']};adj=lambda u,v:frozenset([u,v]) in E
        pairs=[(s,t) for s in range(n) for t in range(n) if adj(s,t) and all(not adj(t,w) or adj(s,w) for w in range(n) if w!=s and w!=t)]
        assert row['graph']==g['graph'] and row['pairs']==[list(e) for e in pairs]
        layers=[{tuple(c):m for c,m in layer} for layer in table['layers']];fail=[];tests=0;degree=[sum(adj(v,w) for w in range(n)) for v in range(n)]
        for goal,j in [('stack',1),('clear',0)]:
            for mass,layer in enumerate(layers):
                losses=[c for c,m in layer.items() if m[j]==0];sq=lambda c:sum(a*a for a in c);weight=lambda c:sum(a*b for a,b in zip(c,degree));q=max(map(sq,losses),default=-1);p=min((weight(c) for c in losses if sq(c)==q),default=-1)
                for c in sorted(losses):
                    for s,t in pairs:
                        if c[s]<=c[t]:continue
                        tests+=1;d=tuple(c[t] if v==s else c[s] if v==t else c[v] for v in range(n))
                        if layer[d][j]:fail.append(dict(goal=goal,c=list(c),d=list(d),s=s,t=t,mass=mass,Qmax=sq(c)==q,QP=sq(c)==q and weight(c)==p,critical=mass==meta['thresholds'][goal]-1 if meta['thresholds'][goal] else None))
        assert row['tests']==tests and row['failures']==fail
        for goal in ['stack','clear']:
            fs=[f for f in fail if f['goal']==goal];certs=[c for c in data['certificates'] if c['graph']==g['graph'] and c['failure']['goal']==goal];assert len(certs)==bool(fs)
            if not fs:continue
            cert=certs[0];assert cert['failure']==fs[0];ss={tuple(c) for c in cert['states']};reachable={tuple(fs[0]['c'])};assert len(ss)==len(cert['states'])<=300000
            for c in sorted(ss,key=lambda c:-sum(c)):
                assert c in reachable and not (sum(c)==1 if goal=='clear' else len([a for a in c if a])==1)
                for u in range(n):
                    for v in range(n):
                        if not adj(u,v) or c[u]<2:continue
                        d=list(c);d[u]-=2;d[v]+=1;assert tuple(d) in ss;reachable.add(tuple(d))
            assert reachable==ss;states+=len(ss);x=fs[0]['d'].copy()
            for u,v in cert['moves']:assert adj(u,v) and x[u]>=2;x[u]-=2;x[v]+=1;moves+=1
            assert x==cert['final'] and (sum(x)==1 if goal=='clear' else len([a for a in x if a])==1)
    summary=dict(tests=sum(r['tests'] for r in data['rows']),failures=sum(len(r['failures']) for r in data['rows']),Qmax_failures=sum(f['Qmax'] for r in data['rows'] for f in r['failures']),critical_failures=sum(bool(f['critical']) for r in data['rows'] for f in r['failures']),certificates=len(data['certificates']),negative_closure_states=states,literal_moves=moves,all_labeled_failures_equal=True)
    raw=(json.dumps(summary,indent=2)+'\n').encode();p=B/'swap_verification.json'
    if '--check-only' in sys.argv:assert p.read_bytes()==raw
    else:p.write_bytes(raw)
    print(json.dumps(summary),flush=True)
if __name__=='__main__':main()
