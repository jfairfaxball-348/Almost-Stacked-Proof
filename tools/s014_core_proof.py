import hashlib,json,sys,time
from pathlib import Path
B=Path('evidence/S014/core_proof');P=Path('evidence/S014/cegis_orbits_v2')
def main():
    name=sys.argv[1];D=B/name;D.mkdir(exist_ok=True);cfg=json.loads((P/'inputs.json').read_bytes());sys.path.insert(0,cfg['runtime']);from pysat.solvers import Glucose3
    assert json.loads((P/name/'clause_verification.json').read_bytes())['all_clauses_necessary_for_fixed_input_counterexample']
    text=(P/name/'formula.cnf').read_text(encoding='ascii').splitlines();h=text[0].split();nv=int(h[2]);clauses=[list(map(int,l.split()))[:-1] for l in text[1:]];assert len(clauses)==int(h[3])<=500000
    start=time.monotonic();calls=0;status='SAT_SUBSET_UNKNOWN';chosen=[]
    def checktime():
        if time.monotonic()-start>540:raise RuntimeError('TIME_CAP_UNKNOWN')
    try:
        with Glucose3(bootstrap_with=clauses) as direct:is_sat=direct.solve()
        if not is_sat:
            with Glucose3(bootstrap_with=[C+[-(nv+i+1)] for i,C in enumerate(clauses)]) as sat:
                candidate=list(range(len(clauses)));assert not sat.solve(assumptions=[nv+i+1 for i in candidate]);candidate=sorted(v-nv-1 for v in sat.get_core());calls+=1
                for _ in range(4):
                    before=len(candidate);chunks=[candidate[i::32] for i in range(32)]
                    for chunk in chunks:
                        checktime()
                        if not chunk or calls>=128:continue
                        removing=set(chunk);attempt=[i for i in candidate if i not in removing]
                        if len(attempt)==len(candidate):continue
                        calls+=1
                        if not sat.solve(assumptions=[nv+i+1 for i in attempt]):candidate=sorted(v-nv-1 for v in sat.get_core())
                    if len(candidate)==before or calls>=128:break
                chosen=candidate
            checktime()
            with Glucose3(bootstrap_with=[clauses[i] for i in chosen],with_proof=True) as fresh:
                assert not fresh.solve();proof=fresh.get_proof()
            (D/'proof.drup').write_text('\n'.join(proof)+'\n',encoding='ascii',newline='\n');status='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE' if len(proof)<=500000 else 'PROOF_SIZE_BOUND_UNKNOWN'
    except RuntimeError as error:status=str(error)
    (D/'formula.cnf').write_text(f'p cnf {nv} {len(chosen)}\n'+''.join(' '.join(map(str,clauses[i]))+' 0\n' for i in chosen),encoding='ascii',newline='\n')
    (D/'indices.json').write_text(json.dumps(chosen)+'\n',encoding='utf-8',newline='\n')
    out=dict(case=name,status=status,original_clauses=len(clauses),core_clauses=len(chosen),tightening_calls=calls,seconds=time.monotonic()-start,scope='Fixed input only, provisional until subset and complete fresh proof independently checked')
    (D/'result.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
