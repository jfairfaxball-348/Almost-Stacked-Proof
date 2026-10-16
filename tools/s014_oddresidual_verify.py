import itertools,json,lzma
from pathlib import Path
B=Path('evidence/S014/oddresidual')
def main():
    gs=json.loads(Path('evidence/S014/oddlarge_v2/inputs.json').read_bytes())['graphs'];data=json.loads(lzma.decompress(Path('evidence/S014/oddlarge_v2/results.json.xz').read_bytes()));saved=json.loads((B/'classification.json').read_bytes());expected=[];counts={}
    for g,report in zip(gs,data):
        n=g['n'];A=[[0]*n for _ in range(n)]
        for u,v in g['edges']:A[u][v]=A[v][u]=1
        minimal=[not any(all(A[t][j]<=A[s][j] for j in range(n)) and any(A[t][j]<A[s][j] for j in range(n)) for t in range(n)) for s in range(n)]
        colorings=[bits for bits in itertools.product(range(2),repeat=n) if all(bits[u]!=bits[v] for u,v in g['edges'])];bip=bool(colorings)
        for row in report['rows']:
            if not row['failed']:continue
            heavy=[v for v in range(n) if row['c'][v]>=2];res=all(minimal[v] for v in heavy) and all(A[u]!=A[v] for u,v in itertools.combinations(heavy,2))
            expected.append(dict(graph=g['id'],row=row,minimal=minimal,residual=res,bipartite=bip));a=row['c'][row['s']];counts[a]=counts.get(a,0)+1
    assert expected==saved and len(saved)==583
    inputs=json.loads((B/'inputs.json').read_bytes())['cases'];choices=[next(r for r in saved if r['row']['c'][r['row']['s']]==3),next((r for r in saved if r['residual']),None)];wanted=[]
    for r in choices:
        if r and r['graph'] not in wanted:wanted.append(r['graph'])
    assert wanted==[c['graph']['graph'] for c in inputs]
    out=dict(failing_pairs=len(saved),donor_counts=counts,residual_failures=sum(r['residual'] for r in saved),bipartite_failures=sum(r['bipartite'] for r in saved),selected=wanted,independent_adjacency_classifier_equal=True)
    (B/'classification_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
