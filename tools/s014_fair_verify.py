"""Independent all-pattern coverage, graph certificates and selector/lex CNF."""
import hashlib,itertools,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014/fair_cegis')
def main():
    name=sys.argv[1];D=B/name
    for pre in [B/('control_preflight.json' if name=='N2_M4' else 'preflight.json'),D/'derived_preflight.json']:
        for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    case=next(c for c in json.loads((B/('control_inputs.json' if name=='N2_M4' else 'inputs.json')).read_bytes())['cases'] if c['id']==name);n,M=case['n'],case['mass'];patterns=case['patterns'];assert len(patterns)<=300
    # Independent unbounded-knapsack partition DP, by allowed part value.
    dp={(0,0):{()}}
    for value in range(1,M+1):
        updated={key:set(items) for key,items in dp.items()}
        for (mass,length),items in dp.items():
            for copies in range(1,min(n-length,(M-mass)//value)+1):
                target=(mass+copies*value,length+copies);updated.setdefault(target,set()).update(p+(value,)*copies for p in items)
        dp=updated
    wanted={tuple(reversed(p))+(0,)*(n-length) for (mass,length),items in dp.items() if mass==M for p in items if sum(z>=2 for z in p)>=2};assert len(wanted)==len(patterns)==len({tuple(p) for p in patterns}) and wanted=={tuple(p) for p in patterns}
    edges=list(itertools.combinations(range(n),2));vid={frozenset(e):i+1 for i,e in enumerate(edges)};m=len(edges);selectors=list(range(m+1,m+1+len(patterns)));records=[json.loads(line) for line in (D/'constraints.jsonl').read_text(encoding='utf-8').splitlines()];assert len(records)<=50000
    graph=[];seen=set();negative=positive=states=moves=independent=0
    for r in records:
        C=r['clause'];assert len(C)==len(set(C)) and all(1<=abs(x)<=m+len(patterns) for x in C)
        if r['kind']=='cut':
            U=set(r['vertices']);assert U and U<set(range(n));assert C==[vid[frozenset(e)] for e in edges if (e[0] in U)!=(e[1] in U)]
        elif r['kind']=='independent_set':
            U=r['vertices'];k=(M+2)//3;assert 2<=k<=n and len(U)==len(set(U))==k and sorted(U)==U and all(0<=u<n for u in U) and M<=3*k<=M+2
            assert C==[vid[frozenset(e)] for e in itertools.combinations(U,2)];independent+=1
        elif r['kind']=='c_win':
            j=r['pattern'];assert 0<=j<len(patterns);x=patterns[j].copy();used=set()
            for u,v in r['moves']:
                assert 0<=u<n and 0<=v<n and u!=v and x[u]>=2;x[u]-=2;x[v]+=1;used.add(vid[frozenset([u,v])]);moves+=1
            assert sum(z>0 for z in x)==1 and sum(x)>0 and C==sorted({-selectors[j]}|{-i for i in used});negative+=1
        else:
            assert r['kind']=='AS_loss';x=r['input'];assert len(x)==n and all(isinstance(z,int) and z>=0 for z in x) and M<=sum(x)<=M+2 and sum(z>1 for z in x)<=1
            E={frozenset(e) for e in r['edges']};assert len(E)==len(r['edges']) and all(len(e)==2 and all(0<=v<n for v in e) for e in E);assert C==[vid[frozenset(e)] for e in edges if frozenset(e) not in E]
            ss=set()
            with lzma.open(D/r['certificate'],'rb') as f:
                while data:=f.read(16):assert len(data)==16 and not any(data[n:]);ss.add(tuple(data[:n]))
            assert len(ss)==r['states']<=300000;reachable={tuple(x)}
            for z in sorted(ss,key=lambda z:-sum(z)):
                assert z in reachable and sum(v>0 for v in z)>1
                for u,v in itertools.permutations(range(n),2):
                    if z[u]<2 or frozenset([u,v]) not in E:continue
                    child=list(z);child[u]-=2;child[v]+=1;assert tuple(child) in ss;reachable.add(tuple(child))
            assert reachable==ss;states+=len(ss);positive+=1
        key=tuple(sorted(C))
        if key not in seen:seen.add(key);graph.append(list(key))
    lines=(D/'formula.cnf').read_text(encoding='ascii').splitlines();h=lines[0].split();assert h[:2]==['p','cnf'] and int(h[3])==len(lines)-1<=500000;F=[]
    for line in lines[1:]:a=list(map(int,line.split()));assert a[-1]==0;F.append(a[:-1])
    fixed_meta=json.loads((D/'fixed_blocks.json').read_bytes());fixed_count=1+len(selectors)*(len(selectors)-1)//2;expected=[selectors]+[[-a,-b] for a,b in itertools.combinations(selectors,2)];assert F[:fixed_count]==expected and fixed_meta['selector_clause_count']==fixed_count;cursor=fixed_count;nv=m+len(selectors);blocks=fixed_meta['blocks'];comparisons=fixed_meta['comparisons'];required=[]
    for j,p in enumerate(patterns):
        for value in sorted(set(p)):
            group=[v for v,z in enumerate(p) if z==value]
            if len(group)>=2:required.append((j,group[0],group[1]))
    assert len(comparisons)==len(required) and len(blocks)==m*len(required);truth_rows=0
    for ci,((j,u,v),meta) in enumerate(zip(required,comparisons)):
        assert meta['pattern']==j and meta['swap']==[u,v] and patterns[j][u]==patterns[j][v];perm=list(range(n));perm[u],perm[v]=v,u;nv+=1;prev=nv;assert meta['prefix0']==prev and meta['first_block']==ci*m and F[cursor]==[prev];cursor+=1;sel=selectors[j]
        for i,(s,t) in enumerate(edges):
            nv+=1;cur=nv;a=i+1;b=vid[frozenset([perm[s],perm[t]])];r=blocks[ci*m+i];assert r==dict(pattern=j,selector=sel,previous=prev,current=cur,a=a,b=b,count=r['count']);count=r['count'];assert 0<=count<=6;local=F[cursor:cursor+count];cursor+=count;vs=sorted({sel,prev,cur,a,b});assert all(len(C)==len(set(C)) and all(abs(x) in vs for x in C) for C in local)
            for bits in itertools.product([False,True],repeat=len(vs)):
                assignment=dict(zip(vs,bits));actual=all(any(assignment[abs(x)]==(x>0) for x in C) for C in local);logical=(assignment[cur]==(assignment[prev] and assignment[a]==assignment[b])) and (not assignment[sel] or not assignment[prev] or not assignment[a] or assignment[b]);assert actual==logical;truth_rows+=1
            prev=cur
    assert F[cursor:]==graph and int(h[2])==nv
    fixed=(D/'fixed_formula.cnf').read_text(encoding='ascii').splitlines();assert fixed[0]==f'p cnf {nv} {cursor}' and fixed[1:]==lines[1:cursor+1]
    out=dict(case=name,n=n,mass=M,patterns=len(patterns),all_mass_M_nonAS_patterns_covered=True,certificate_records=len(records),c_winning_clauses=negative,AS_negative_clauses=positive,AS_closure_states=states,literal_c_moves=moves,independent_set_instances=independent,local_truth_rows=truth_rows,all_conditional_graph_clauses_necessary=True,exact_selector_and_lex_extension_checked=True,counterexample_exists_implies_formula_satisfiable=True,scope='ONLY n-vertex mass-M countermodels; universal ASH* OPEN')
    (D/'clause_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
