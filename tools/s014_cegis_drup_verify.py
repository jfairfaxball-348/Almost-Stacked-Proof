"""Pure coordinate CNF/RUP proof replay; no SAT solver import or call."""
import collections,json,sys
from pathlib import Path
B=Path('evidence/S014/cegis')
def main():
    D=B/sys.argv[1];prior=json.loads((D/'clause_verification.json').read_bytes());result=json.loads((D/'result.json').read_bytes());out=dict(case=sys.argv[1],solver_status=result['status'],fixed_input_class_exclusion_certified=False)
    if result['status']!='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE':
        out['scope']='No UNSAT claim; bounded search/certificates only';(D/'proof_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out),flush=True);return
    lines=(D/'formula.cnf').read_text(encoding='ascii').splitlines();header=lines[0].split();variables=int(header[2]);F=collections.Counter()
    for line in lines[1:]:nums=list(map(int,line.split()));assert nums[-1]==0;F[frozenset(nums[:-1])]+=1
    scans=0
    def rup(C):
        nonlocal scans
        assignment=set()
        for x in C:
            v=-x
            if -v in assignment:return True
            assignment.add(v)
        changed=True
        while changed:
            changed=False
            for clause,count in F.items():
                if not count:continue
                scans+=1
                if scans>200000000:raise RuntimeError('UNIT_SCAN_CAP_UNKNOWN')
                if any(x in assignment for x in clause):continue
                pending=[x for x in clause if -x not in assignment]
                if not pending:return True
                if len(pending)==1:
                    v=pending[0]
                    if -v in assignment:return True
                    if v not in assignment:assignment.add(v);changed=True
        return False
    added=deleted=0;empty=False;proof=(D/'proof.drup').read_text(encoding='ascii').splitlines();assert len(proof)<=500000
    try:
        for line in proof:
            parts=line.split()
            if not parts:continue
            deletion=parts[0]=='d';nums=list(map(int,parts[1:] if deletion else parts));assert nums[-1]==0;C=frozenset(nums[:-1]);assert all(1<=abs(v)<=variables for v in C)
            if deletion:
                if F[C]:F[C]-=1
                deleted+=1;continue
            if not rup(C):raise RuntimeError('NON_RUP_STEP_UNKNOWN')
            F[C]+=1;added+=1;empty|=not C
        assert empty and prior['all_clauses_necessary_for_fixed_input_counterexample'];out.update(fixed_input_class_exclusion_certified=True,added_RUP_steps=added,deletions=deleted,unit_clause_scans=scans,scope='ONLY this exact labeled fixed-input graph class; NOT universal ASH*')
    except RuntimeError as error:out.update(error=str(error),scope='UNKNOWN; solver UNSAT not promoted')
    (D/'proof_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
