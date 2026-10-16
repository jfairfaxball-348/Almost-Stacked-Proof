"""Independent edge-order reconstruction and exact missing-edge histories."""
import itertools,json
from pathlib import Path
B=Path('evidence/S014/saturate')
def main():
    cases=json.loads((B/'inputs.json').read_bytes())['cases'];rows=json.loads((B/'results.json').read_bytes());tail=json.loads((B/'tail/shard0_verification.json').read_bytes());assert tail['all_complete_DAGs_and_AS_tail_keys_checked'];graphs=json.loads((B/'tail/inputs.json').read_bytes())['graphs'];mapped={g['id']:g for g in graphs};moves=edges=0
    assert len(cases)==len(rows) or rows[-1].get('tail_status')=='POTENTIAL_ACTUAL_COUNTEREXAMPLE'
    for case,row in zip(cases,rows):
        assert row['case']==case['id']
        if row['status']=='STATE_CAP_UNKNOWN':continue
        assert row['final']==mapped[case['id']];g=case['seed'];n=g['n'];actual={frozenset(e) for e in g['edges']};final={frozenset(e) for e in row['final']['edges']};missing={frozenset(e) for e in itertools.combinations(range(n),2)}-actual;order=[frozenset(e) for e in case['order']];assert set(order)==missing and len(order)==len(missing)
        proofs={frozenset(r['edge']):r['moves'] for r in row['excluded']};assert len(proofs)==len(row['excluded'])
        for edge in order:
            if edge in final:actual.add(edge);continue
            assert edge in proofs;c=g['c'].copy();used=False
            for u,v in proofs[edge]:
                e=frozenset([u,v]);assert e in actual|{edge} and c[u]>=2;c[u]-=2;c[v]+=1;used|=e==edge;moves+=1
            assert used and sum(z>0 for z in c)==1 and sum(c)>0;edges+=1
        assert actual==final and set(proofs)==({frozenset(e) for e in itertools.combinations(range(n),2)}-final)
    out=dict(cases=len(rows),complete_saturations=len(graphs),unknown=len(rows)-len(graphs),missing_edge_winning_histories=edges,literal_edge_moves=moves,AS_tail_verification=tail,all_greedy_decisions_and_saturation_certificates_checked=True)
    (B/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k!='AS_tail_verification'}),flush=True)
if __name__=='__main__':main()
