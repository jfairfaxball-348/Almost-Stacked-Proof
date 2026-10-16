"""Independent occurrence-list unit-propagation checker; no SAT/oracle imports."""
import collections,hashlib,json,sys,time
from pathlib import Path
B=Path('evidence/S014/cegis_orbits_v2');V=Path('evidence/S014/indexed_drup')
def main():
    name=sys.argv[1];D=B/name;O=V/name;O.mkdir(parents=True,exist_ok=True)
    files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in [D/'formula.cnf',D/'proof.drup',D/'clause_sources.bin',D/'constraints.jsonl',D/'clause_verification.json',D/'result.json',B/'inputs.json',Path(__file__),Path('sessions/S014/PLAN_AMENDMENT_39.md')]}
    (O/'preflight.json').write_text(json.dumps(dict(files=files),indent=2)+'\n',encoding='utf-8',newline='\n')
    necessity=json.loads((D/'clause_verification.json').read_bytes());assert necessity['all_clauses_necessary_for_fixed_input_counterexample']
    assert json.loads((D/'result.json').read_bytes())['status']=='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE'
    clauses=[];active=[];occ=collections.defaultdict(list);bykey=collections.defaultdict(list);units=[];empty=[];stamp=[];counts=[];residual=[];epoch=0;visits=0;start=time.monotonic()
    def insert(C):
        i=len(clauses);clauses.append(C);active.append(True);stamp.append(-1);counts.append(0);residual.append(0);bykey[frozenset(C)].append(i)
        for lit in C:occ[lit].append(i)
        if len(C)==1:units.append(i)
        if not C:empty.append(i)
    lines=(D/'formula.cnf').read_text(encoding='ascii').splitlines();h=lines[0].split();assert h[:2]==['p','cnf'];variables,number=map(int,h[2:]);assert number==len(lines)-1
    for line in lines[1:]:
        nums=list(map(int,line.split()));assert nums[-1]==0 and len(nums[:-1])==len(set(nums[:-1]));assert all(1<=abs(x)<=variables for x in nums[:-1]);insert(tuple(nums[:-1]))
    def rup(C):
        nonlocal epoch,visits
        epoch+=1;assignment=set();queue=[]
        def assign(lit):
            if -lit in assignment:return False
            if lit not in assignment:assignment.add(lit);queue.append(-lit)
            return True
        if any(active[i] for i in empty):return True
        for lit in C:
            if not assign(-lit):return True
        for i in units:
            if active[i] and not assign(clauses[i][0]):return True
        for false in queue:
            for i in occ[false]:
                if not active[i]:continue
                visits+=1
                if visits>500000000:raise RuntimeError('OCCURRENCE_CAP_UNKNOWN')
                if visits%100000==0 and time.monotonic()-start>540:raise RuntimeError('TIME_CAP_UNKNOWN')
                if stamp[i]!=epoch:
                    stamp[i]=epoch;counts[i]=len(clauses[i]);value=0
                    for lit in clauses[i]:value^=lit
                    residual[i]=value
                counts[i]-=1;residual[i]^=false
                if counts[i]==0:return True
                if counts[i]==1 and not assign(residual[i]):return True
        return False
    proof=(D/'proof.drup').read_text(encoding='ascii').splitlines();assert len(proof)<=500000;added=deleted=0;final=False;out=dict(case=name,fixed_input_class_exclusion_certified=False)
    try:
        for line in proof:
            p=line.split()
            if not p:continue
            deletion=p[0]=='d';nums=list(map(int,p[1:] if deletion else p));assert nums[-1]==0;C=tuple(dict.fromkeys(nums[:-1]));assert all(1<=abs(x)<=variables for x in C)
            if deletion:
                ids=bykey[frozenset(C)]
                while ids and not active[ids[-1]]:ids.pop()
                if ids:active[ids.pop()]=False
                deleted+=1;continue
            if not rup(C):raise RuntimeError('NON_RUP_STEP_UNKNOWN')
            insert(C);added+=1;final|=not C
        assert final;out.update(fixed_input_class_exclusion_certified=True,scope='ONLY exact fixed-input graph class; universal ASH* OPEN')
    except RuntimeError as error:out.update(error=str(error),scope='UNKNOWN; no mathematical exclusion promoted')
    out.update(added_RUP_steps=added,deletions=deleted,active_literal_occurrence_visits=visits,seconds=time.monotonic()-start)
    for p,digest in files.items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==digest,p
    (O/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
