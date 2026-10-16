"""Independent full generated keys, whole negative certificates and moves."""
import hashlib,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/parity');R=Path('evidence/S014/regular')
def main():
    for p,h in json.loads((B/'inputs.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    data=json.loads(lzma.decompress((B/'certificates.json.xz').read_bytes()));graphs=json.loads((R/'ray_inputs.json').read_bytes())['graphs'];expected={};negatives={};edges={};groups={}
    for g in graphs:
        name=g['graph'];n=g['n'];edges[name]={frozenset(e) for e in g['edges']}
        for goal in ['clear','stack']:
            stem=name+'_'+goal+'_threshold';report=json.loads((R/(stem+'_verification.json')).read_bytes());T=report['threshold'];critical=set()
            with lzma.open(R/(stem+'.bin.xz'),'rb') as f:
                while raw:=f.read(12):
                    mass,count=struct.unpack('<IQ',raw)
                    for _ in range(count):
                        c=tuple(f.read(16)[:n])
                        if mass==T-1:critical.add(c)
            negatives[name,goal]=critical
            for c in critical:
                if len([v for v in c if v>1])<2:continue
                for source in range(n):
                    d=tuple(sum(c)-sum(c[v]%2 for v in range(n) if v!=source) if z==source else c[z]%2 for z in range(n));expected[name,goal,c,source]=(d,T)
    seen=set();moves=0
    for row in data['rows']:
        key=row['graph'],row['goal'],tuple(row['c']),row['source'];assert key not in seen;seen.add(key);d,T=expected[key];assert tuple(row['d'])==d and row['T']==T and sum(d)==T-1 and all(x%2==y%2 for x,y in zip(d,row['c'])) and sum(x>1 for x in d)<=1
        losing=d in negatives[key[:2]];assert losing==row['losing'];groups.setdefault(key[:3],[]).append(losing)
        if losing:continue
        s=list(d)
        for u,v in row['moves']:assert frozenset([u,v]) in edges[key[0]] and s[u]>=2;s[u]-=2;s[v]+=1;moves+=1
        assert s==row['final'] and sum(x>0 for x in s)==1 and (key[1]=='stack' or sum(s)==1)
    assert seen==set(expected) and len(seen)<=300000
    reported={(r['graph'],r['goal'],tuple(r['c'])):r['all_parity_class_AS_win'] for r in data['groups']};assert reported=={key:not any(values) for key,values in groups.items()}
    result=dict(cases=len(seen),critical_nonAS_inputs=len(groups),complete_parity_class_failures=sum(reported.values()),literal_moves=moves,all_generated_keys_negative_memberships_and_winning_traces_verified=True,example=next((r for r in data['groups'] if r['all_parity_class_AS_win']),None));(B/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
