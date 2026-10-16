"""Independent Floyd/tuple/all-edge hypothesis and finite negative audit."""
import gzip,hashlib,json,time
from pathlib import Path
B=Path('evidence/S014/shell_witness');start=time.monotonic()
for pre in [B/'preflight.json',B/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
def read(p):return json.loads(Path(p).read_bytes())
cfg=read(B/'inputs.json');out=read(B/'result.json');provided={(r['graph'],r['source'],r['ell']):r for r in cfg['rows']};assert len(provided)==len(cfg['rows']);results={r['id']:r for r in out['rows']};assert set(results)==set(range(len(cfg['rows'])))
cube_choices=read('evidence/S014/cube_dag/choices.json');fano_choices=read('evidence/S014/fano_AS/choices.json');fano=read('evidence/S014/fano_AS/inputs.json');assert read('evidence/S014/cube_lower/verification.json')['exact_binary_buffer_AS_oracle_certified'] and read('evidence/S014/fano_AS/verification.json')['exact_binary_buffer_AS_oracle_certified']
inventory=set();oracle_calls=edges_checked=dependencies=states=forward=unknown=0
for g in cfg['graphs']:
    n=g['n'];E={tuple(sorted(e)) for e in g['edges']};assert len(E)==len(g['edges']) and all(0<=u<v<n for u,v in E)
    D=[[0 if u==v else 1 if tuple(sorted((u,v))) in E else 999 for v in range(n)] for u in range(n)]
    for k in range(n):
        for u in range(n):
            for v in range(n):D[u][v]=min(D[u][v],D[u][k]+D[k][v])
    assert all(x<999 for row in D for x in row)
    for s in range(n):
        for ell in range(1,max(D[s])+1):
            key=(g['id'],s,ell);inventory.add(key);row=provided[key];U={v for v in range(n) if D[s][v]==ell};k=len(U);H=2**ell;N=H//2*(k+3)-3
            assert set(row['U'])==U and len(row['U'])==k and row['N']==N>=1 and row['forward_check']==(g['small'] and ell<=3)
            R=[2**d if d<=ell else H//2 for d in D[s]];assert R[s]==1 and all(R[u]==H for u in U)
            for u,v in E:
                assert (D[s][u]-D[s][v])%2 and R[u]<=2*R[v] and R[v]<=2*R[u];edges_checked+=2
                if u in U:assert 2*R[v]==R[u]
                if v in U:assert 2*R[u]==R[v]
            assert (N+(-1)**ell*k)%3==0 and N+k*H==3*H*(k+1)//2-3
            if g['id'] in ['Q4','FanoInc14']:
                f=[v^s for v in range(n)] if g['id']=='Q4' else fano['source_maps'][s];assert len(set(f))==n and f[0]==s and {tuple(sorted((f[u],f[v]))) for u,v in E}==E
                mask=sum(1<<(u-1) for u in range(1,n) if f[u] in U);choices=cube_choices if g['id']=='Q4' else fano_choices;assert N<choices[mask][N%3][0];oracle_calls+=1
            result=results[row['id']]
            if not row['forward_check']:assert result['status']=='VALUATION_ONLY';continue
            if result['status']!='COMPLETE_NEGATIVE_CLOSURE':unknown+=1;assert result['status'] in ['TIME_CAP_UNKNOWN','STATE_CAP_UNKNOWN','UNEXECUTED_AFTER_CAP'];continue
            path=Path(result['certificate']);assert hashlib.sha256(path.read_bytes()).hexdigest()==result['sha256'];raw=gzip.decompress(path.read_bytes());assert len(raw)%n==0;S={tuple(raw[j:j+n]) for j in range(0,len(raw),n)};assert len(S)==result['states'] and len(S)*n==len(raw)
            initial=tuple(N if v==s else int(v in U) for v in range(n));assert initial in S
            for c in S:
                if states%4096==0:assert time.monotonic()-start<540
                states+=1;assert 0<sum(c)<=N+k and sum(a>0 for a in c)>1
                for u,a in enumerate(c):
                    if a>=2:
                        for v in range(n):
                            if tuple(sorted((u,v))) in E:
                                d=list(c);d[u]-=2;d[v]+=1;assert tuple(d) in S;dependencies+=1
            forward+=1
assert inventory==set(provided) and states==sum(r.get('states',0) for r in out['rows'] if r['status']=='COMPLETE_NEGATIVE_CLOSURE')
report=dict(all_shell_hypotheses_verified=True,graphs=len(cfg['graphs']),shell_rows=len(inventory),oriented_edges_checked=edges_checked,exact_AS_oracle_queries=oracle_calls,complete_negative_queries=forward,states=states,dependencies=dependencies,unknown_queries=unknown,scope='Finite parameter/closure challenge only;109 symbolic proof required, universal ASH* OPEN',seconds=time.monotonic()-start)
(B/'verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(report))
