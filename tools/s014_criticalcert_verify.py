import itertools,json,lzma
from pathlib import Path
B=Path('evidence/S014/criticalcert')
def main():
    inputs=json.loads((B/'inputs.json').read_bytes())['cases'];certs=json.loads(lzma.decompress((B/'certificates.json.xz').read_bytes()));states=moves=0
    for inp,cert in zip(inputs,certs):
        assert cert['case']==inp;n=inp['graph']['n'];E={frozenset(e) for e in inp['graph']['edges']};assert len(cert['negative'])==2
        for c,neg in zip([inp['c'],inp['AS']],cert['negative']):
            assert c==neg['c'] and sum(c)==15;ss={tuple(x) for x in neg['states']};assert len(ss)==len(neg['states'])<=300000;reach={tuple(c)}
            for x in sorted(ss,key=lambda x:-sum(x)):
                assert x in reach and sum(z>0 for z in x)>1
                for u,v in itertools.permutations(range(n),2):
                    if x[u]<2 or frozenset([u,v]) not in E:continue
                    y=list(x);y[u]-=2;y[v]+=1;assert tuple(y) in ss;reach.add(tuple(y))
            assert reach==ss;states+=len(ss)
        assert sum(z>1 for z in inp['AS'])<=1
        wanted=set();c=inp['c']
        for s,t,v in itertools.permutations(range(n),3):
            if c[s]<3 or c[s]%2==0 or c[t]<c[s] or c[v] or frozenset([s,t]) not in E or frozenset([s,v]) not in E or frozenset([t,v]) in E:continue
            wanted.add((s,t,v))
        assert wanted=={(r['s'],r['t'],r['v']) for r in cert['winners']}
        for row in cert['winners']:
            d=c.copy();a=d[row['s']];d[row['s']]=0;d[row['t']]+=a-1;d[row['v']]=1;assert d==row['d']
            for u,v in row['moves']:
                assert frozenset([u,v]) in E and d[u]>=2;d[u]-=2;d[v]+=1;moves+=1
            assert sum(z>0 for z in d)==1 and sum(d)>0
        report=json.loads(Path(inp['threshold_summary']).read_bytes());ver=json.loads(Path(inp['threshold_verification']).read_bytes());assert report['threshold']==ver['threshold']==16 and ver['all_full_losing_layers_equal'] and report['rows'][-2]['Q']==171 and inp['AS'] in report['rows'][-2]['Qmax']
    result=dict(graphs=len(inputs),negative_inputs=2*len(inputs),complete_negative_states=states,literal_winning_moves=moves,all_critical_candidates_win_but_AS_critical_losers_remain=True)
    (B/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
