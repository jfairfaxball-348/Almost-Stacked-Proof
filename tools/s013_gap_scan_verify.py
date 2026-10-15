"""Independent triple/union-find historical predicate classification."""
import itertools,json,lzma,sys
from pathlib import Path

def main():
    dataset=[]
    a=json.loads(Path('evidence/S003/T2b_analysis.json').read_bytes())
    b=json.loads(lzma.decompress(Path('evidence/S003/A3_n8_analysis.json.xz').read_bytes()))
    assert len(a)==853 and len(b['graphs'])==11117 and b['cap_t']==26
    for r in a:
        st=r['analysis']['stack'];cl=r['analysis']['clear']
        dataset.append((r['graph'],7,r['edges'],st.get('threshold'),cl.get('threshold') if isinstance(cl,dict) else None))
    for r in b['graphs']:dataset.append((r[0],8,r[1],r[3][0] if type(r[3])==list else None,r[4][0] if type(r[4])==list else None))
    tally=dict(records=len(dataset),both_exact=0,unknown_pair=0,gap1=0,positive_gap=0,vertex_triangular_positive=0,component_criterion_positive=0);kept=[];exact=[]
    for name,n,text,s,c in dataset:
        if s is None or c is None:tally['unknown_pair']+=1;continue
        tally['both_exact']+=1
        edges={frozenset(map(int,p.split('-'))) for p in text.split(',')}
        triples=[t for t in itertools.combinations(range(n),3) if all(frozenset(e) in edges for e in itertools.combinations(t,2))]
        covered={v for tri in triples for v in tri};covered_edges={frozenset(e) for tri in triples for e in itertools.combinations(tri,2)}
        parent=list(range(n))
        def find(v):
            while parent[v]!=v:v=parent[v]
            return v
        for edge in edges-covered_edges:
            u,v=tuple(edge);parent[find(u)]=find(v)
        parts=sorted([sorted(v for v in range(n) if find(v)==root) for root in set(find(v) for v in range(n))],key=lambda p:p[0])
        criterion=max(sum(v not in covered for v in part) for part in parts)<=1;d=c-s;assert d>=0
        tags=[]
        if d==1:tally['gap1']+=1;tags.append('gap1')
        tally['positive_gap']+=d>0
        if d>0 and len(covered)==n:tally['vertex_triangular_positive']+=1;tags.append('all_vertices_triangular')
        if d>0 and criterion:tally['component_criterion_positive']+=1;tags.append('component_criterion')
        exact.append([name,n,s,c,len(covered),criterion])
        if tags:kept.append(dict(graph=name,n=n,edges=text,stack=s,clear=c,gap=d,triangle_vertices=sorted(covered),H_components=parts,tags=tags))
    saved=json.loads(Path('evidence/S013/gap_scan.json').read_bytes());assert saved['counts']==tally and saved['eligible']==exact and saved['selected']==kept
    result={'all_records':len(dataset),'full_classification_equal':True,'counts':tally,'selected_rows':len(kept)}
    p=Path('evidence/S013/gap_scan_verification.json');raw=(json.dumps(result,indent=2)+'\n').encode()
    if '--check-only' in sys.argv:assert p.read_bytes()==raw
    else:p.write_bytes(raw)
    print(json.dumps(result))

if __name__=='__main__':main()
