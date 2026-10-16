"""Distinct closure verifier, literal traces and whole same-mass neighbor sets."""
import itertools,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/obstruction')
def main():
    data=json.loads(lzma.decompress((B/'certificates.json.xz').read_bytes()));assert len(data)==2;reports=[]
    for row in data:
        g=row['graph'];n=g['n'];E={frozenset(e) for e in g['edges']};c=row['c'];T=json.loads((B/(g['graph']+'_stack_threshold_verification.json')).read_bytes())['threshold'];assert T==9 and sum(c)==8;critical=set()
        with lzma.open(B/(g['graph']+'_stack_threshold.bin.xz'),'rb') as f:
            while raw:=f.read(12):
                mass,count=struct.unpack('<IQ',raw)
                for _ in range(count):
                    d=tuple(f.read(16)[:n])
                    if mass==8:critical.add(d)
        for start,field in [(c,'negative'),(row['AS_critical'],'AS_negative')]:
            states={tuple(s) for s in row[field]};assert len(states)==len(row[field])<=300000;reached={tuple(start)}
            for s in sorted(states,key=lambda s:-sum(s)):
                assert s in reached and sum(x>0 for x in s)!=1
                for u in range(n):
                    if s[u]<2:continue
                    for v in range(n):
                        if frozenset([u,v]) in E:d=list(s);d[u]-=2;d[v]+=1;d=tuple(d);assert d in states;reached.add(d)
            assert reached==states and tuple(start) in critical
        assert sum(x>1 for x in row['AS_critical'])<=1 and [x%2 for x in row['AS_critical']]!=[x%2 for x in c]
        seen=set();moves=0
        for trace in row['same_parity_AS_winners']:
            source=trace['source'];assert source not in seen;seen.add(source);d=[8-sum(c[v]%2 for v in range(n) if v!=source) if z==source else c[z]%2 for z in range(n)];assert d==trace['d'] and tuple(d) not in critical;s=d.copy()
            for u,v in trace['moves']:assert frozenset([u,v]) in E and s[u]>=2;s[u]-=2;s[v]+=1;moves+=1
            assert s==trace['final'] and sum(x>0 for x in s)==1
        assert seen==set(range(n));expected={}
        for s,t in itertools.permutations(range(n),2):
            if not c[s]:continue
            d=c.copy();d[s]-=1;d[t]+=1;expected[s,t]=dict(s=s,t=t,d=d,losing=tuple(d) in critical)
        assert {(r['s'],r['t']):r for r in row['unit_redistributions']}==expected
        alpha=max(sum(bits) for bits in itertools.product([0,1],repeat=n) if all(not(bits[u] and bits[v]) for u,v in g['edges']));assert alpha==row['alpha']==2
        increasing=[r for r in expected.values() if r['losing'] and sum(x*x for x in r['d'])>sum(x*x for x in c)]
        reports.append(dict(graph=g['graph'],threshold=T,c=c,AS_critical=row['AS_critical'],alpha=alpha,complete_negative_states=len(row['negative'])+len(row['AS_negative']),all_parity_AS_winners=n,literal_moves=moves,increasing_Q_losing_unit_neighbors=increasing,all_complete_closures_moves_and_keys_verified=True))
    (B/'verification.json').write_text(json.dumps(reports,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(reports),flush=True)
if __name__=='__main__':main()
