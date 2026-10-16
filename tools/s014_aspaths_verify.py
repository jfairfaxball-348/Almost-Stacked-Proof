"""Independent full generated inputs, literal arithmetic and exact grammar membership."""
import hashlib,itertools,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014')
def main():
    for p,h in json.loads((B/'aspaths_inputs.json').read_bytes()).items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    data=json.loads(lzma.decompress((B/'aspaths.json.xz').read_bytes()));graphs=json.loads((B/'balanced/ray_inputs.json').read_bytes())['graphs'];expected=set();seen=set();branches={};count=0
    for g in graphs:
        n=g['n'];a=g['a'];x=n-2;y=n-1;E={frozenset(e) for e in g['edges']};gram=json.loads(lzma.decompress((B/'balanced'/(g['graph']+'_binary_s0_rays.json.xz')).read_bytes()));ix={tuple(d):i for i,d in enumerate(gram['vectors'])}
        for goal,base in [('clear',3*a+7),('stack',3*a+5)]:
            vertices=[v for v in range(1,n) if goal=='stack' or v<n-2]
            for size in range(len(vertices)+1):
                for sites in itertools.combinations(vertices,size):
                    for mass in [base,base+1,base+2]:
                        c=tuple(mass-size if v==0 else int(v in sites) for v in range(n));expected.add((g['graph'],goal,c))
        for trace in (r for r in data['traces'] if r['graph']==g['graph']):
            c=tuple(trace['c']);key=(g['graph'],trace['goal'],c);assert key not in seen;seen.add(key);assert c[0]>=4 and all(z in [0,1] for z in c[1:]);state=list(c)
            if trace['goal']=='clear':assert c[x]==c[y]==0
            for u,v in trace['moves']:assert frozenset([u,v]) in E and state[u]>=2;state[u]-=2;state[v]+=1;count+=1
            assert state==trace['final']
            if trace['goal']=='clear':assert sum(state)==1
            else:assert len([v for v in state if v])==1 and sum(state)>0
            V=gram['C'] if trace['goal']=='clear' else gram['S'];di=ix[c[1:]];k=c[0]%3;minima=[V[di][4*q+k] for q in range(n) if V[di][4*q+k] is not None];assert minima and min(minima)<=c[0]
            label=trace['goal']+':'+trace['branch'];branches[label]=branches.get(label,0)+1
    assert seen==expected and branches==data['branches'] and len(data['traces'])==len(seen)<=300000
    result=dict(traces=len(seen),literal_moves=count,branches=branches,all_generated_inputs_and_grammar_predictions_equal=True)
    raw=(json.dumps(result,indent=2)+'\n').encode();p=B/'aspaths_verification.json'
    if '--check-only' in sys.argv:assert p.read_bytes()==raw
    else:p.write_bytes(raw)
    print(json.dumps(result),flush=True)
if __name__=='__main__':main()
