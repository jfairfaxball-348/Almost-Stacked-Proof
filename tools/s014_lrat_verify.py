"""Literal clause-id RUP hint replay; never imports or calls a SAT solver."""
import hashlib,json,sys,time
from pathlib import Path
B=Path('evidence/S014/lrat');P=Path('evidence/S014/cegis_orbits_v2')
def main():
    name=sys.argv[1];D=B/name
    for p,h in json.loads((D/'derived_preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    assert json.loads((P/name/'clause_verification.json').read_bytes())['all_clauses_necessary_for_fixed_input_counterexample']
    header,*lines=(P/name/'formula.cnf').read_text(encoding='ascii').splitlines();h=header.split();assert h[:2]==['p','cnf'];nv,number=map(int,h[2:]);assert number==len(lines)<=500000
    clauses={}
    for i,line in enumerate(lines,1):
        a=list(map(int,line.split()));assert a[-1]==0 and all(1<=abs(x)<=nv for x in a[:-1]);clauses[i]=frozenset(a[:-1])
    ever=set(clauses);added=deleted=hints=0;empty=False;start=time.monotonic();out=dict(case=name,fixed_input_class_exclusion_certified=False)
    try:
        with (D/'proof.lrat').open(encoding='ascii') as f:
            for lineno,line in enumerate(f,1):
                if lineno>1000000:raise RuntimeError('LINE_CAP_UNKNOWN')
                p=line.split()
                if not p or p[0]=='c':continue
                if p[0]=='d' or len(p)>1 and p[1]=='d':
                    ids=list(map(int,p[1:] if p[0]=='d' else p[2:]));assert ids[-1]==0
                    for i in ids[:-1]:clauses.pop(i,None);deleted+=1
                    continue
                a=list(map(int,p));cid=a[0];assert cid>0 and cid not in ever;zero=a.index(0,1);C=frozenset(a[1:zero]);hs=a[zero+1:];assert hs and hs[-1]==0 and all(x!=0 for x in hs[:-1]) and all(1<=abs(x)<=nv for x in C)
                if any(i<0 for i in hs[:-1]):raise RuntimeError('RAT_HINT_UNSUPPORTED_UNKNOWN')
                assignment={-x for x in C};conflict=any(-x in assignment for x in assignment)
                for ident in hs[:-1]:
                    hints+=1
                    if hints>100000000:raise RuntimeError('HINT_CAP_UNKNOWN')
                    if hints%100000==0 and time.monotonic()-start>540:raise RuntimeError('TIME_CAP_UNKNOWN')
                    assert ident in clauses
                    if conflict:continue
                    premise=clauses[ident]
                    if any(x in assignment for x in premise):continue
                    available=[x for x in premise if -x not in assignment]
                    if not available:conflict=True
                    elif len(available)==1:assignment.add(available[0])
                    else:raise RuntimeError('NON_UNIT_HINT_UNKNOWN')
                if not conflict:raise RuntimeError('NO_CONTRADICTION_UNKNOWN')
                clauses[cid]=C;ever.add(cid);added+=1;empty|=not C
                if added>500000:raise RuntimeError('ADDITION_CAP_UNKNOWN')
        assert empty;out.update(fixed_input_class_exclusion_certified=True,scope='ONLY exact fixed-c graph-class exclusion; universal ASH* OPEN')
    except RuntimeError as error:out.update(error=str(error),scope='UNKNOWN; no exclusion promoted')
    out.update(verified_RUP_additions=added,deleted_clause_ids=deleted,hint_visits=hints,seconds=time.monotonic()-start)
    (D/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
