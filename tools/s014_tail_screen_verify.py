import itertools,json,lzma,sys
from pathlib import Path
B=Path('evidence/S014/tail_screen')
def main():
    shard=int(sys.argv[1]);inputs=json.loads((B/'inputs.json').read_bytes())['graphs'][shard*939:(shard+1)*939];rows=json.loads((B/f'shard{shard}_results.json').read_bytes());negative=positive=states=0;potential=[]
    assert len(rows)==len(inputs) or rows[-1]['status']=='POTENTIAL_ACTUAL_COUNTEREXAMPLE'
    for g,row in zip(inputs,rows):
        assert row['graph']==g['id'];n=g['n'];T=sum(g['c']);assert T>=n+1;E={frozenset(e) for e in g['edges']};db={}
        with lzma.open(B/(g['id']+'.bin.xz'),'rb') as f:
            while data:=f.read(17):
                assert len(data)==17 and not any(data[n:16]);c=tuple(data[:n]);assert c not in db;db[c]=data[16]
        assert len(db)==row['states']<=row['memo_states']<=300000
        if row['status']=='STATE_CAP_UNKNOWN':continue
        truth={}
        for c,k in sorted(db.items(),key=lambda kv:(sum(kv[0]),kv[0])):
            if k==255:assert sum(z>0 for z in c)==1;truth[c]=True
            elif k==254:
                assert sum(z>0 for z in c)>1
                for u,v in itertools.permutations(range(n),2):
                    if c[u]<2 or frozenset([u,v]) not in E:continue
                    d=list(c);d[u]-=2;d[v]+=1;assert tuple(d) in truth and not truth[tuple(d)]
                truth[c]=False;negative+=1
            else:
                u,v=divmod(k,n);assert u<n and v<n and c[u]>=2 and frozenset([u,v]) in E;d=list(c);d[u]-=2;d[v]+=1;assert truth[tuple(d)];truth[c]=True;positive+=1
        assert truth[tuple(g['c'])]==row['original_winning'];states+=len(db)
        if row['status']=='ORIGINAL_WIN':assert truth[tuple(g['c'])] and not row['AS_tested'];continue
        assert not truth[tuple(g['c'])];count=0;bad=None
        for mass in range(T,T+3):
            for s in range(n):
                off=[v for v in range(n) if v!=s]
                for bits in range(1<<(n-1)):
                    U=[v for i,v in enumerate(off) if bits&(1<<i)];c=tuple(mass-len(U) if v==s else int(v in U) for v in range(n));assert sum(c)==mass and c[s]>=2;count+=1
                    assert c in truth
                    if not truth[c]:bad=dict(mass=mass,source=s,mask=bits);break
                if bad:break
            if bad:break
        assert count==row['AS_tested'] and bad==row['AS_bad']
        if row['status']=='AS_LOSER_FOUND':assert bad is not None
        else:assert row['status']=='POTENTIAL_ACTUAL_COUNTEREXAMPLE' and bad is None and count==3*n*2**(n-1);potential.append(g)
    out=dict(shard=shard,cases=len(rows),complete_cases=sum(r['status']!='STATE_CAP_UNKNOWN' for r in rows),unknown=sum(r['status']=='STATE_CAP_UNKNOWN' for r in rows),checked_states=states,negative_states=negative,positive_dependencies=positive,potential_counterexamples=potential,all_complete_DAGs_and_AS_tail_keys_checked=True)
    (B/f'shard{shard}_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
