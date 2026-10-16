"""Independent two-watched-literal RUP replay, without any native solver."""
import collections,hashlib,json,sys,time
from pathlib import Path
def main():
    directory=Path(sys.argv[1]);label=sys.argv[2];O=Path('evidence/S014/watched_drup')/label;O.mkdir(parents=True,exist_ok=True)
    paths=[directory/'formula.cnf',directory/'proof.drup',directory/'clause_verification.json',directory/'result.json',Path(__file__),Path('sessions/S014/PLAN_AMENDMENT_42.md')]
    files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths};(O/'preflight.json').write_text(json.dumps(dict(files=files),indent=2)+'\n',encoding='utf-8',newline='\n')
    assert json.loads((directory/'clause_verification.json').read_bytes())['all_clauses_necessary_for_fixed_input_counterexample']
    assert json.loads((directory/'result.json').read_bytes())['status']=='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE'
    clauses=[];active=[];watch=collections.defaultdict(list);units=[];empties=[];identities=collections.defaultdict(list);visits=0;started=time.monotonic()
    header,*lines=(directory/'formula.cnf').read_text(encoding='ascii').splitlines();h=header.split();assert h[:2]==['p','cnf'];variables,number=map(int,h[2:]);assert number==len(lines)<=500000
    def add(C):
        i=len(clauses);clauses.append(C);active.append(True);identities[frozenset(C)].append(i)
        if len(C)>1:watch[C[0]].append(i);watch[C[1]].append(i)
        elif C:units.append(i)
        else:empties.append(i)
    for line in lines:
        values=list(map(int,line.split()));assert values[-1]==0;C=values[:-1];assert len(C)==len(set(C)) and all(1<=abs(x)<=variables for x in C);add(C)
    def RUP(C):
        nonlocal visits
        values=[0]*(variables+1);queue=[]
        def assign(literal):
            u=abs(literal);sign=1 if literal>0 else -1
            if values[u]==-sign:return False
            if not values[u]:values[u]=sign;queue.append(-literal)
            return True
        def value(literal):return values[abs(literal)]*(1 if literal>0 else -1)
        if any(active[i] for i in empties):return True
        for x in C:
            if not assign(-x):return True
        for i in units:
            if active[i] and not assign(clauses[i][0]):return True
        for false in queue:
            bucket=watch[false];j=0
            while j<len(bucket):
                i=bucket[j]
                if not active[i]:bucket[j]=bucket[-1];bucket.pop();continue
                visits+=1
                if visits>500000000:raise RuntimeError('WATCH_VISIT_CAP_UNKNOWN')
                if visits%100000==0 and time.monotonic()-started>540:raise RuntimeError('TIME_CAP_UNKNOWN')
                clause=clauses[i]
                if clause[0]==false:clause[0],clause[1]=clause[1],clause[0]
                assert clause[1]==false
                other=clause[0]
                if value(other)>0:j+=1;continue
                replacement=next((k for k in range(2,len(clause)) if value(clause[k])>=0),None)
                if replacement is not None:
                    clause[1],clause[replacement]=clause[replacement],clause[1];watch[clause[1]].append(i);bucket[j]=bucket[-1];bucket.pop();continue
                if not assign(other):return True
                j+=1
        return False
    proof=(directory/'proof.drup').read_text(encoding='ascii').splitlines();assert len(proof)<=500000;added=deleted=0;empty=False;out=dict(case=label,fixed_input_class_exclusion_certified=False)
    try:
        for line in proof:
            p=line.split()
            if not p:continue
            deletion=p[0]=='d';values=list(map(int,p[1:] if deletion else p));assert values[-1]==0;C=list(dict.fromkeys(values[:-1]));assert all(1<=abs(x)<=variables for x in C)
            if deletion:
                ids=identities[frozenset(C)]
                while ids and not active[ids[-1]]:ids.pop()
                if ids:active[ids.pop()]=False
                deleted+=1;continue
            if not RUP(C):raise RuntimeError('NON_RUP_STEP_UNKNOWN')
            add(C);added+=1;empty|=not C
        assert empty
        if label=='control_C6':
            old=json.loads(Path('evidence/S014/cegis_orbits_v2/C6/proof_verification.json').read_bytes());assert old['fixed_input_class_exclusion_certified'] and added==old['added_RUP_steps']==37
        out.update(fixed_input_class_exclusion_certified=True,scope='ONLY this exact fixed input graph-class exclusion; universal ASH* OPEN')
    except RuntimeError as error:out.update(error=str(error),scope='UNKNOWN; no mathematical exclusion promoted')
    out.update(added_RUP_steps=added,deletions=deleted,active_watched_clause_visits=visits,seconds=time.monotonic()-started)
    for p,h in files.items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    (O/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
