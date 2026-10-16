"""Independent necessity check for every CEGIS input clause."""
import itertools,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014/cegis')
def main():
    case=next(c for c in json.loads((B/'inputs.json').read_bytes())['cases'] if c['id']==sys.argv[1]);D=B/case['id'];n=case['n'];T=sum(case['c']);pairs=list(itertools.combinations(range(n),2));vid={frozenset(e):i+1 for i,e in enumerate(pairs)};rows=[json.loads(x) for x in (D/'constraints.jsonl').read_text(encoding='utf-8').splitlines()];neg=pos=states=moves=0;clauses=[]
    for row in rows:
        C=row['clause'];assert all(1<=abs(v)<=len(pairs) for v in C) and len(C)==len(set(C));clauses.append(C)
        if row['kind']=='cut':
            U=set(row['vertices']);assert U and U<set(range(n));assert C==[vid[frozenset(e)] for e in pairs if (e[0] in U)!=(e[1] in U)]
        elif row['kind']=='c_win':
            c=case['c'].copy();used=set()
            for u,v in row['moves']:
                assert 0<=u<n and 0<=v<n and u!=v and c[u]>=2;c[u]-=2;c[v]+=1;used.add(vid[frozenset([u,v])]);moves+=1
            assert sum(z>0 for z in c)==1 and sum(c)>0 and C==sorted(-v for v in used);neg+=1
        else:
            assert row['kind']=='AS_loss';c=row['input'];assert len(c)==n and all(isinstance(z,int) and z>=0 for z in c) and T<=sum(c)<=T+2 and sum(z>1 for z in c)<=1
            E={frozenset(e) for e in row['edges']};assert len(E)==len(row['edges']) and all(len(e)==2 and all(0<=v<n for v in e) for e in E);assert C==[vid[frozenset(e)] for e in pairs if frozenset(e) not in E]
            ss=set()
            with lzma.open(D/row['certificate'],'rb') as f:
                while raw:=f.read(16):assert len(raw)==16 and not any(raw[n:]);ss.add(tuple(raw[:n]))
            assert len(ss)==row['states']<=300000;reachable={tuple(c)}
            for x in sorted(ss,key=lambda x:-sum(x)):
                assert x in reachable and sum(z>0 for z in x)>1
                for u,v in itertools.permutations(range(n),2):
                    if x[u]<2 or frozenset([u,v]) not in E:continue
                    y=list(x);y[u]-=2;y[v]+=1;assert tuple(y) in ss;reachable.add(tuple(y))
            assert reachable==ss;pos+=1;states+=len(ss)
    text=(D/'formula.cnf').read_text(encoding='ascii').splitlines();assert text[0]==f'p cnf {len(pairs)} {len(clauses)}';parsed=[]
    for line in text[1:]:nums=list(map(int,line.split()));assert nums[-1]==0;parsed.append(nums[:-1])
    assert parsed==clauses
    out=dict(case=case['id'],clauses=len(clauses),c_winning_trace_clauses=neg,AS_negative_clauses=pos,AS_closure_states=states,literal_c_winning_moves=moves,all_clauses_necessary_for_fixed_input_counterexample=True)
    (D/'clause_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
