"""Independent closure completeness, literal full-input winner, threshold scope."""
import itertools,json,sys
from pathlib import Path
B=Path(sys.argv[1]) if len(sys.argv)>1 else Path('evidence/S014/oddcritical')
def main():
    inputs=json.loads((B/'inputs.json').read_bytes())['cases'];certs=json.loads((B/'certificates.json').read_bytes());states=moves=0;rows=[]
    assert len(inputs)==len(certs)
    for case,cert in zip(inputs,certs):
        assert cert['graph']==case['graph'] and cert['failure']==case['failure'];g=case['graph'];f=case['failure'];n=g['n'];E={frozenset(e) for e in g['edges']};closure={tuple(c) for c in cert['closure']};seen={tuple(f['c'])}
        for c in sorted(closure,key=lambda c:-sum(c)):
            assert c in seen and sum(z>0 for z in c)>1
            for u,v in itertools.permutations(range(n),2):
                if c[u]<2 or frozenset([u,v]) not in E:continue
                d=list(c);d[u]-=2;d[v]+=1;assert tuple(d) in closure;seen.add(tuple(d))
        assert seen==closure
        assert len(cert['histories'])==len(f['candidates'])
        for cand,trace in zip(f['candidates'],cert['histories']):
            c=f['c'].copy();a=c[f['s']];c[f['s']]-=a;c[f['t']]+=a-1;c[cand['v']]+=1
            assert c==cand['d']==trace['input'] and trace['v']==cand['v']
            for u,v in trace['moves']:
                assert c[u]>=2 and frozenset([u,v]) in E;c[u]-=2;c[v]+=1;moves+=1
            assert c==trace['terminal'] and sum(z>0 for z in c)==1 and sum(c)>0
        independent=json.loads((B/(g['graph']+'_stack_threshold_verification.json')).read_bytes());T=independent['threshold'];assert independent['all_full_losing_layers_equal'] and independent['L_AS_exact']==T-1
        assert cert['threshold']==T and cert['critical_mass']==T-1 and cert['failure_mass']==sum(f['c']) and cert['failure_is_critical']==(sum(f['c'])==T-1)
        states+=len(closure);rows.append(dict(graph=g['graph'],mass=sum(f['c']),threshold=T,critical=cert['failure_is_critical'],Q=cert['failure_Q'],layer_Qmax=cert['failure_layer_Q_max']))
    result=dict(cases=rows,complete_negative_states=states,literal_winning_moves=moves,all_negative_closures_and_positive_histories_checked=True)
    (B/'certificate_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
