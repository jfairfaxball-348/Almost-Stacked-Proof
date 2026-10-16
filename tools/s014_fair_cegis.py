"""All mass-M input partitions share necessary graph clauses; no bare UNSAT."""
import itertools,json,lzma,sys,time
from pathlib import Path
from s014_master_encoding import build
B=Path('evidence/S014/fair_cegis')
def main():
    config=json.loads((B/('control_inputs.json' if sys.argv[1]=='N2_M4' else 'inputs.json')).read_bytes());case=next(c for c in config['cases'] if c['id']==sys.argv[1]);D=B/case['id'];D.mkdir(exist_ok=True);sys.path.insert(0,config['runtime']);from pysat.solvers import Glucose3
    n,M=case['n'],case['mass'];patterns=case['patterns'];pairs=list(itertools.combinations(range(n),2));vid={e:i+1 for i,e in enumerate(pairs)};units=[1<<(8*i) for i in range(n)];variables,selectors,fixed,blocks=build(n,patterns);assert len(fixed)<500000
    (D/'fixed_blocks.json').write_text(json.dumps(blocks)+'\n',encoding='utf-8',newline='\n');records=[];clauses=[];seen=set();started=time.monotonic();status='ITERATION_BOUND_UNKNOWN';iteration=0;c=patterns[0];closed=set();cursor=0;visits=[0]*len(patterns);conditional_unsat=[]
    def add(row):
        if len(records)>=50000 or len(fixed)+len(clauses)>=500000:raise RuntimeError('CLAUSE_CAP_UNKNOWN')
        C=tuple(sorted(set(row['clause'])));records.append(row)
        if C not in seen:seen.add(C);clauses.append(C);sat.add_clause(C)
    def oracle(E):
        arcs=sorted(E|{(v,u) for u,v in E});memo={};depth=0;top=None
        def put(x,k):
            if len(memo)>=300000 and x not in memo:raise RuntimeError('ORACLE_STATE_CAP_UNKNOWN')
            if len(memo)%10000==0 and time.monotonic()-started>540:raise RuntimeError('TIME_BOUND_UNKNOWN')
            memo[x]=k
        def raw(x):
            if x in memo:return memo[x]!=254
            if len(memo)>=300000:raise RuntimeError('ORACLE_STATE_CAP_UNKNOWN')
            if sum(bool((x>>(8*i))&255) for i in range(n))==1:put(x,255);return True
            for u,v in arcs:
                if ((x>>(8*u))&255)>=2 and win(x-2*units[u]+units[v]):put(x,u*n+v);return True
            put(x,254);return False
        def win(x):
            nonlocal depth,top
            if not depth:top=x
            depth+=1
            try:return raw(x)
            except RuntimeError as error:
                if depth==1:(D/'oracle_cap.json').write_text(json.dumps(dict(status=str(error),queried_graph=sorted(E),queried_input=[(top>>(8*i))&255 for i in range(n)],selected_pattern=c,scope='UNKNOWN query, may be temporary support graph'))+'\n',encoding='utf-8',newline='\n')
                raise
            finally:depth-=1
        def history(x):
            moves=[]
            while memo[x]!=255:
                u,v=divmod(memo[x],n);moves.append([u,v]);x=x-2*units[u]+units[v]
            return moves
        return arcs,memo,win,history
    def closure(path,x,arcs,memo):
        needed={x};todo=[x]
        for z in todo:
            assert memo[z]==254
            for u,v in arcs:
                if ((z>>(8*u))&255)<2:continue
                y=z-2*units[u]+units[v]
                if y not in needed:needed.add(y);todo.append(y)
        with lzma.open(path,'wb') as f:
            for x in sorted(needed):f.write(x.to_bytes(16,'little'))
        return len(needed)
    try:
        with Glucose3(bootstrap_with=fixed) as sat:
            for line in (D/'imports.jsonl').read_text(encoding='utf-8').splitlines():add(json.loads(line))
            for v in range(n):add(dict(kind='cut',vertices=[v],clause=[vid[e] for e in pairs if v in e]))
            k=(M+2)//3;assert 2<=k<=n
            for U in itertools.combinations(range(n),k):add(dict(kind='independent_set',vertices=list(U),clause=[vid[e] for e in itertools.combinations(U,2)]))
            for iteration in range(1,10001):
                if time.monotonic()-started>540:status='TIME_BOUND_UNKNOWN';break
                if len(closed)==len(patterns):
                    with Glucose3(bootstrap_with=fixed+clauses,with_proof=True) as fresh:
                        assert not fresh.solve();proof=fresh.get_proof()
                    (D/'proof.drup').write_text('\n'.join(proof)+'\n',encoding='ascii',newline='\n');status='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE' if len(proof)<=500000 else 'PROOF_SIZE_BOUND_UNKNOWN';break
                while cursor%len(patterns) in closed:cursor+=1
                requested=cursor%len(patterns);cursor+=1;visits[requested]+=1
                preferred=selectors[requested];sat.set_phases(list(range(1,len(pairs)+1)))
                if not sat.solve(assumptions=[preferred]):
                    closed.add(requested);conditional_unsat.append(dict(pattern=requested,iteration=iteration));continue
                model=set(sat.get_model());chosen=[i for i,s in enumerate(selectors) if s in model];assert chosen==[requested];index=requested;c=patterns[index];root=sum(z*units[i] for i,z in enumerate(c));E={e for e in pairs if vid[e] in model};reachable={0};todo=[0]
                for u in todo:
                    for v in range(n):
                        if v not in reachable and tuple(sorted((u,v))) in E:reachable.add(v);todo.append(v)
                if len(reachable)<n:add(dict(kind='cut',vertices=sorted(reachable),clause=[vid[e] for e in pairs if (e[0] in reachable)!=(e[1] in reachable)]));continue
                arcs,memo,win,history=oracle(E)
                if win(root):
                    moves=history(root);support={tuple(sorted((u,v))) for u,v in moves};complete=True
                    for e in sorted(support.copy()):
                        if e not in support:continue
                        try:
                            aa,mm,ww,hh=oracle(support-{e})
                            if ww(root):moves=hh(root);support={tuple(sorted((u,v))) for u,v in moves}
                        except RuntimeError as error:
                            if str(error)!='ORACLE_STATE_CAP_UNKNOWN':raise
                            complete=False;break
                    add(dict(kind='c_win',pattern=index,moves=moves,support_minimization_complete=complete,clause=sorted({-selectors[index]}|{-vid[e] for e in support})));continue
                starts=[root];bad=None;tested=0
                for mass in range(M,M+3):
                    for s in range(n):
                        off=[v for v in range(n) if v!=s]
                        for bits in range(1<<(n-1)):
                            x=(mass-bits.bit_count())*units[s]+sum(units[v] for i,v in enumerate(off) if bits>>i&1);starts.append(x);tested+=1
                            if not win(x):bad=x;break
                        if bad is not None:break
                    if bad is not None:break
                if bad is None:
                    P=D/'potential';P.mkdir(exist_ok=True);needed=set();stack=starts.copy()
                    while stack:
                        x=stack.pop()
                        if x in needed:continue
                        needed.add(x);kind=memo[x]
                        if kind==255:continue
                        if kind==254:stack.extend(x-2*units[u]+units[v] for u,v in arcs if ((x>>(8*u))&255)>=2)
                        else:u,v=divmod(kind,n);stack.append(x-2*units[u]+units[v])
                    with lzma.open(P/'candidate.bin.xz','wb') as f:
                        for x in sorted(needed):f.write(x.to_bytes(16,'little')+bytes([memo[x]]))
                    (P/'inputs.json').write_text(json.dumps(dict(graphs=[dict(id='candidate',n=n,edges=sorted(E),c=c)]))+'\n',encoding='utf-8',newline='\n');(P/'shard0_results.json').write_text(json.dumps([dict(graph='candidate',status='POTENTIAL_ACTUAL_COUNTEREXAMPLE',original_winning=False,AS_tested=tested,AS_bad=None,states=len(needed),memo_states=len(memo))])+'\n',encoding='utf-8',newline='\n');status='POTENTIAL_ACTUAL_COUNTEREXAMPLE';break
                badc=[(bad>>(8*i))&255 for i in range(n)];H=E.copy();ha,hm,hw,_=oracle(H);assert not hw(bad);complete=True
                for e in pairs:
                    if e in H:continue
                    try:
                        aa,mm,ww,_=oracle(H|{e})
                        if not ww(bad):H.add(e);ha,hm=aa,mm
                    except RuntimeError as error:
                        if str(error)!='ORACLE_STATE_CAP_UNKNOWN':raise
                        complete=False;break
                cert=f'AS_loss_{len(records):05d}.bin.xz';count=closure(D/cert,bad,ha,hm);add(dict(kind='AS_loss',input=badc,edges=sorted(H),certificate=cert,states=count,saturation_complete=complete,clause=[vid[e] for e in pairs if e not in H]))
                if iteration%25==0:(D/'progress.json').write_text(json.dumps(dict(iteration=iteration,records=len(records),graph_clauses=len(clauses),pattern=index,seconds=time.monotonic()-started,last_AS_mass=sum(badc)))+'\n',encoding='utf-8',newline='\n')
    except RuntimeError as error:
        assert str(error) in ['TIME_BOUND_UNKNOWN','ORACLE_STATE_CAP_UNKNOWN','CLAUSE_CAP_UNKNOWN'];status=str(error)
    (D/'constraints.jsonl').write_text(''.join(json.dumps(r,separators=(',',':'))+'\n' for r in records),encoding='utf-8',newline='\n')
    (D/'formula.cnf').write_text(f'p cnf {variables} {len(fixed)+len(clauses)}\n'+''.join(' '.join(map(str,C))+' 0\n' for C in fixed+clauses),encoding='ascii',newline='\n');(D/'fixed_formula.cnf').write_text(f'p cnf {variables} {len(fixed)}\n'+''.join(' '.join(map(str,C))+' 0\n' for C in fixed),encoding='ascii',newline='\n')
    (D/'scheduling.json').write_text(json.dumps(dict(visits=visits,conditional_unsat=conditional_unsat,untrusted_closed=sorted(closed),negative_selector_clauses_added=0,final_refutation_uses_no_assumptions=True))+'\n',encoding='utf-8',newline='\n')
    result=dict(case=case['id'],n=n,mass=M,patterns=len(patterns),status=status,iterations=iteration,graph_records=len(records),distinct_graph_clauses=len(clauses),fixed_encoding_clauses=len(fixed),variables=variables,seconds=time.monotonic()-started,scope='ONLY all mass-M inputs on n-vertex graphs; universal ASH* OPEN')
    (D/'result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
