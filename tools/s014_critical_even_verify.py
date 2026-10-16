import json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/critical_even');inputs=json.loads((B/'inputs.json').read_bytes())['cases'];out=json.loads((B/'results.json').read_bytes());assert len(inputs)==len(out)
for case,row in zip(inputs,out):
    assert row['case']==case['id'];n=case['n'];parent=list(range(n));parity=[0]*n
    def find(v):
        if parent[v]!=v:
            p=parent[v];parent[v]=find(p);parity[v]^=parity[p]
        return parent[v]
    bip=True
    for u,v in case['edges']:
        a,b=find(u),find(v);p=parity[u]^parity[v]
        if a==b:bip&=p==1
        else:parent[a]=b;parity[a]=p^1
    assert row['bipartite']==bip;states=None
    with lzma.open(case['certificate'],'rb') as f:
        while h:=f.read(12):
            mass,count=struct.unpack('<IQ',h)
            if mass+1==case['threshold']:
                assert count<=1000000;states=set()
                for _ in range(count):
                    data=f.read(16);assert len(data)==16 and not any(data[n:]);c=tuple(data[:n]);assert sum(c)==mass;states.add(c)
                assert len(states)==count;break
            for _ in range(count):assert len(f.read(16))==16
    assert states and row['critical']==len(states)
    nonAS={c for c in states if len([z for z in c if z>1])>=2};even={c for c in nonAS if any(z>1 and not z%2 for z in c)}
    assert row['nonAS']==len(nonAS) and row['nonAS_with2']==sum(2 in c for c in nonAS) and row['even_heavy_inputs']==[list(c) for c in sorted(even)]
outcome=dict(cases=len(out),critical=sum(r['critical'] for r in out),nonAS=sum(r['nonAS'] for r in out),nonAS_with2=sum(r['nonAS_with2'] for r in out),even_heavy_inputs=sum(len(r['even_heavy_inputs']) for r in out),bipartite_even_heavy_inputs=sum(len(r['even_heavy_inputs']) for r in out if r['bipartite']),all_selected_labeled_inputs_equal=True,universal_no2='REFUTED_IN_THIS_DATA' if any(r['nonAS_with2'] for r in out) else 'UNPROVED_FINITE_AGREEMENT_ONLY')
(B/'verification.json').write_text(json.dumps(outcome,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(outcome),flush=True)
