"""Separate graph provenance replay, local truth tables and full CNF coverage."""
import hashlib,itertools,json,sys
from pathlib import Path
import s014_cegis_clauses_verify as basecheck
B=Path('evidence/S014/mass11_cegis')
def main():
    name=sys.argv[1];D=B/name
    for p,h in json.loads((D/'derived_preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    basecheck.B=D/'base';basecheck.main()
    case=next(c for c in json.loads((B/'inputs.json').read_bytes())['cases'] if c['id']==name);n=case['n'];edges=list(itertools.combinations(range(n),2));vid={frozenset(e):i+1 for i,e in enumerate(edges)};m=len(edges)
    records=[json.loads(line) for line in (D/'constraints.jsonl').read_text(encoding='utf-8').splitlines()];base=[json.loads(line) for line in (D/'base'/name/'constraints.jsonl').read_text(encoding='utf-8').splitlines()];assert len(records)==len(base)
    for a,b in zip(records,base):
        ac=a.copy();bc=b.copy()
        if a['kind']=='AS_loss':assert (D/a['certificate']).resolve()==(D/'base'/name/b['certificate']).resolve();ac.pop('certificate');bc.pop('certificate')
        assert ac==bc
    graph=[];seen=set()
    for r in records:
        C=tuple(sorted(r['clause']))
        if C not in seen:seen.add(C);graph.append(C)
    gl=(D/'graph_formula.cnf').read_text(encoding='ascii').splitlines();assert gl[0]==f'p cnf {m} {len(graph)}' and gl[1:]==[' '.join(map(str,C))+' 0' for C in graph]
    full=(D/'formula.cnf').read_text(encoding='ascii').splitlines();h=full[0].split();assert h[:2]==['p','cnf'] and int(h[3])==len(full)-1;F=[]
    for line in full[1:]:a=list(map(int,line.split()));assert a[-1]==0;F.append(a[:-1])
    assert F[:len(graph)]==[list(C) for C in graph];cursor=len(graph);metadata=json.loads((D/'lex_blocks.json').read_bytes());blocks=metadata['blocks'];comparisons=metadata['comparisons'];swaps=[]
    for value in sorted(set(case['c'])):
        g=[v for v,z in enumerate(case['c']) if z==value];swaps.extend(zip(g,g[1:]))
    assert len(comparisons)==len(swaps) and len(blocks)==m*len(swaps);nv=m;truth_rows=0
    for j,((u,v),comparison) in enumerate(zip(swaps,comparisons)):
        assert comparison['swap']==[u,v] and case['c'][u]==case['c'][v];nv+=1;prev=nv;assert comparison['prefix0']==prev and comparison['first_block']==j*m;assert F[cursor]==[prev];cursor+=1
        p=list(range(n));p[u],p[v]=v,u
        for i,e in enumerate(edges):
            nv+=1;cur=nv;a=i+1;b=vid[frozenset(p[x] for x in e)];r=blocks[j*m+i];assert r['previous']==prev and r['current']==cur and r['a']==a and r['b']==b
            count=r['count'];assert 0<=count<=6;local=F[cursor:cursor+count];cursor+=count;variables=sorted({prev,cur,a,b});assert all(len(C)==len(set(C)) and all(abs(x) in variables for x in C) for C in local)
            for bits in itertools.product([False,True],repeat=len(variables)):
                assignment=dict(zip(variables,bits));actual=all(any(assignment[abs(x)]==(x>0) for x in C) for C in local);expected=(assignment[cur]==(assignment[prev] and assignment[a]==assignment[b])) and (not assignment[prev] or not assignment[a] or assignment[b]);assert actual==expected;truth_rows+=1
            prev=cur
    assert cursor==len(F) and int(h[2])==nv
    out=dict(case=name,graph_certificate_records=len(records),distinct_graph_clauses=len(graph),representative_comparisons=len(swaps),local_truth_rows=truth_rows,all_graph_clauses_necessary=True,exact_lex_existential_extension_checked=True,counterexample_exists_implies_formula_satisfiable=True,scope='Proposition94 gives a representative; lex clauses not claimed necessary for every labeling')
    (D/'clause_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
