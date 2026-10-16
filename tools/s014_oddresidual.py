import json,lzma
from pathlib import Path
B=Path('evidence/S014/oddresidual')
def main():
    graphs={g['id']:g for g in json.loads(Path('evidence/S014/oddlarge_v2/inputs.json').read_bytes())['graphs']};data=json.loads(lzma.decompress(Path('evidence/S014/oddlarge_v2/results.json.xz').read_bytes()));out=[]
    for report in data:
        g=graphs[report['graph']];N=[set() for _ in range(g['n'])]
        for u,v in g['edges']:N[u].add(v);N[v].add(u)
        minimal=[not any(w<z for w in N) for z in N]
        color={0:0};todo=[0]
        for u in todo:
            for v in N[u]:
                if v not in color:color[v]=1-color[u];todo.append(v)
        bip=all(color[u]!=color[v] for u,v in g['edges'])
        for row in report['rows']:
            if not row['failed']:continue
            heavy=[i for i,z in enumerate(row['c']) if z>1];res=all(minimal[i] for i in heavy) and len({frozenset(N[i]) for i in heavy})==len(heavy)
            out.append(dict(graph=g['id'],row=row,minimal=minimal,residual=res,bipartite=bip))
    (B/'classification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    selected=[]
    for r in [next(r for r in out if r['row']['c'][r['row']['s']]==3),next((r for r in out if r['residual']),None)]:
        if r is not None and r['graph'] not in [x['graph']['graph'] for x in selected]:
            g=graphs[r['graph']];selected.append(dict(graph=dict(graph=g['id'],n=g['n'],edges=g['edges']),goal='stack',max_mass=64,candidate_cap=300000,loser_cap=300000,failure=dict(graph=g,**r['row'])))
    (B/'inputs.json').write_text(json.dumps(dict(cases=selected),indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(dict(failing_pairs=len(out),residual_failures=sum(r['residual'] for r in out),selected=[r['graph']['graph'] for r in selected])),flush=True)
if __name__=='__main__':main()
