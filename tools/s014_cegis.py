"""Necessary-clause CEGIS over every graph edge, no bare UNSAT promotion."""
import itertools,json,lzma,sys,time
from pathlib import Path
B=Path('evidence/S014/cegis')
def main():
    config=json.loads((B/'inputs.json').read_bytes());case=next(c for c in config['cases'] if c['id']==sys.argv[1]);D=B/case['id'];D.mkdir(exist_ok=True);sys.path.insert(0,config['runtime']);from pysat.solvers import Glucose3
    n=case['n'];c=case['c'];T=sum(c);pairs=list(itertools.combinations(range(n),2));vid={e:i+1 for i,e in enumerate(pairs)};units=[1<<(8*i) for i in range(n)];root=sum(z*units[i] for i,z in enumerate(c));clauses=[];records=[];start=time.monotonic();status='ITERATION_BOUND_UNKNOWN';iteration=0
    def add(record):
        clauses.append(record['clause']);records.append(record);sat.add_clause(record['clause'])
        with (D/'constraints.jsonl').open('a',encoding='utf-8',newline='\n') as f:f.write(json.dumps(record,separators=(',',':'))+'\n')
    def oracle(E):
        arcs=sorted(E|{(v,u) for u,v in E});memo={}
        def put(x,k):
            if len(memo)>=300000 and x not in memo:raise RuntimeError('ORACLE_STATE_CAP_UNKNOWN')
            memo[x]=k
        def win(x):
            if x in memo:return memo[x]!=254
            if len(memo)>=300000:raise RuntimeError('ORACLE_STATE_CAP_UNKNOWN')
            if sum(bool((x>>(8*i))&255) for i in range(n))==1:put(x,255);return True
            for u,v in arcs:
                if ((x>>(8*u))&255)>=2 and win(x-2*units[u]+units[v]):put(x,u*n+v);return True
            put(x,254);return False
        def history(x):
            moves=[]
            while memo[x]!=255:
                u,v=divmod(memo[x],n);moves.append([u,v]);x=x-2*units[u]+units[v]
            return moves
        return arcs,memo,win,history
    def closure(path,x,arcs,memo):
        ss={x};todo=[x]
        for z in todo:
            assert memo[z]==254
            for u,v in arcs:
                if ((z>>(8*u))&255)<2:continue
                y=z-2*units[u]+units[v]
                if y not in ss:ss.add(y);todo.append(y)
        with lzma.open(path,'wb') as f:
            for z in sorted(ss):f.write(z.to_bytes(16,'little'))
        return len(ss)
    (D/'constraints.jsonl').write_bytes(b'')
    try:
        with Glucose3() as sat:
            for v in range(n):add(dict(kind='cut',vertices=[v],clause=[vid[e] for e in pairs if v in e]))
            for iteration in range(1,5001):
                if time.monotonic()-start>540:status='TIME_BOUND_UNKNOWN';break
                sat.set_phases(list(range(1,len(pairs)+1)))
                if not sat.solve():
                    status='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE'
                    with Glucose3(bootstrap_with=clauses,with_proof=True) as fresh:
                        assert not fresh.solve();proof=fresh.get_proof()
                    if len(proof)>500000:status='PROOF_SIZE_BOUND_UNKNOWN'
                    (D/'proof.drup').write_text('\n'.join(proof)+'\n',encoding='ascii',newline='\n');break
                model=set(sat.get_model());E={e for e in pairs if vid[e] in model};seen={0};todo=[0]
                for u in todo:
                    for v in range(n):
                        if v not in seen and tuple(sorted((u,v))) in E:seen.add(v);todo.append(v)
                if len(seen)<n:
                    add(dict(kind='cut',vertices=sorted(seen),clause=[vid[e] for e in pairs if (e[0] in seen)!=(e[1] in seen)]));continue
                arcs,memo,win,history=oracle(E)
                if win(root):
                    moves=history(root);add(dict(kind='c_win',moves=moves,clause=sorted({-vid[tuple(sorted((u,v)))] for u,v in moves})));continue
                starts=[root];bad=None;tested=0
                for mass in range(T,T+3):
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
                        needed.add(x);k=memo[x]
                        if k==255:continue
                        if k==254:stack.extend(x-2*units[u]+units[v] for u,v in arcs if ((x>>(8*u))&255)>=2)
                        else:u,v=divmod(k,n);stack.append(x-2*units[u]+units[v])
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
                        assert str(error)=='ORACLE_STATE_CAP_UNKNOWN';complete=False;break
                cert=f'AS_loss_{len(records):05d}.bin.xz';count=closure(D/cert,bad,ha,hm)
                add(dict(kind='AS_loss',input=badc,edges=sorted(H),certificate=cert,states=count,saturation_complete=complete,clause=[vid[e] for e in pairs if e not in H]))
                if iteration%25==0:(D/'progress.json').write_text(json.dumps(dict(iteration=iteration,clauses=len(clauses),seconds=time.monotonic()-start,last_AS_mass=sum(badc)))+'\n',encoding='utf-8',newline='\n')
    except RuntimeError as error:
        assert str(error)=='ORACLE_STATE_CAP_UNKNOWN';status=str(error)
    cnf=f'p cnf {len(pairs)} {len(clauses)}\n'+''.join(' '.join(map(str,C))+' 0\n' for C in clauses);(D/'formula.cnf').write_text(cnf,encoding='ascii',newline='\n')
    result=dict(case=case,status=status,iterations=iteration,clauses=len(clauses),seconds=time.monotonic()-start,scope='ALL connected labeled graphs with THIS fixed input only; universal ASH* remains OPEN')
    (D/'result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
