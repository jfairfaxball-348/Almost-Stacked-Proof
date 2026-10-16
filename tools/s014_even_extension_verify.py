import json
from pathlib import Path
B=Path('evidence/S014/even_extension');a=json.loads((B/'inputs.json').read_bytes());out=json.loads((B/'results.json').read_bytes());c=a['c'];n=a['n'];edges={frozenset(e) for e in a['edges']};colors=[1,-1,1,-1];assert all(colors[u]!=colors[v] for u,v in a['edges']) and sum(z*colors[i] for i,z in enumerate(c))%3==0;even=[i for i,z in enumerate(c) if z>0 and z%2==0];assert even==[a['source']];s=even[0];reachable={tuple(c)};todo=[tuple(c)]
for x in todo:
    assert len(reachable)<=300 and len([z for z in x if z])>1
    for u in range(n):
        if x[u]<2:continue
        for v in range(n):
            if frozenset([u,v]) not in edges:continue
            y=list(x);y[u]-=2;y[v]+=1;y=tuple(y)
            if y not in reachable:reachable.add(y);todo.append(y)
assert reachable=={tuple(x.to_bytes(16,'little')[:n]) for x in out['negative_states']};assert sorted(t['v'] for t in a['targets'])==list(range(n)) and len(a['targets'])==n;moves=0
for t,r in zip(a['targets'],out['targets']):
    d=c.copy();d[s]-=2;d[t['v']]+=3;assert t['c']==d and sum(d)==sum(c)+1
    for u,v in t['moves']:assert frozenset([u,v]) in edges and d[u]>1;d[u]-=2;d[v]+=1;moves+=1
    assert d==r['final'] and sum(z>0 for z in d)==1 and r['v']==t['v'] and r['moves']==len(t['moves'])
old=json.loads(Path('evidence/S003/cert_P4_stack_t12.json').read_bytes());assert tuple(reversed(old['losing_witness']['config']))==tuple(c) and {tuple(reversed(x)) for x in old['losing_witness']['reachable_set']}==reachable
ver=dict(original_negative_states=len(reachable),even_donors=len(even),all_vertices_tested=n,winning_candidates=n,literal_positive_moves=moves,E0='FALSE_ON_A_BIPARTITE_ZERO_IMBALANCE_LOSER',critical_status='BELOW_KNOWN_CRITICAL14',universal_no2='UNPROVED_NOT_REFUTED',universal_ASH='OPEN');(B/'verification.json').write_text(json.dumps(ver,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(ver),flush=True)
