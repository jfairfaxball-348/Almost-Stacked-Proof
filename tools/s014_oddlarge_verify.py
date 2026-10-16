"""Independent coordinate DAG proof check and exhaustive required box keys."""
import itertools,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/oddlarge')
def main():
    graphs=json.loads((B/'inputs.json').read_bytes())['graphs'];saved=json.loads(lzma.decompress((B/'results.json.xz').read_bytes())); total=steps=neg=0;failures=[];pairs=0
    assert len(graphs)==len(saved)==len(graphs)
    for g,report in zip(graphs,saved):
        n=g['n'];E={frozenset(e) for e in g['edges']};records={}
        with lzma.open(B/(g['id']+'.bin.xz'),'rb') as f:
            while data:=f.read(9):
                assert len(data)==9;raw,kind=struct.unpack('<QB',data);c=tuple(data[:n]);assert not any(data[n:8]) and c not in records;records[c]=kind
        assert len(records)==report['states']<=300000
        truth={}
        for c,k in sorted(records.items(),key=lambda kv:(sum(kv[0]),kv[0])):
            pure=sum(z!=0 for z in c)==1
            if k==255:assert pure;truth[c]=True
            elif k==254:
                assert not pure
                for u,v in itertools.permutations(range(n),2):
                    if c[u]<2 or frozenset([u,v]) not in E:continue
                    d=list(c);d[u]-=2;d[v]+=1;assert tuple(d) in truth and not truth[tuple(d)];steps+=1
                truth[c]=False;neg+=1
            else:
                u,v=divmod(k,n);assert 0<=u<n and 0<=v<n and c[u]>=2 and frozenset([u,v]) in E
                d=list(c);d[u]-=2;d[v]+=1;assert truth[tuple(d)];truth[c]=True;steps+=1
        expected=[];count=losers=0
        if report['status']!='COMPLETE_REGISTERED_BOX':continue
        for a,b in itertools.product([3,5,7],[3,5,7,9]):
            if a>b:continue
            for tail in itertools.product(range(2),repeat=n-3):
                c=(a,b,0)+tail;count+=1;assert c in truth
                if truth[c]:continue
                losers+=1
                for s,t in [(0,1),(1,0)]:
                    if c[s]>c[t]:continue
                    candidates=[]
                    for v in range(n):
                        if v==t or c[v] or frozenset([s,v]) not in E or frozenset([t,v]) in E:continue
                        d=tuple(0 if i==s else c[t]+c[s]-1 if i==t else 1 if i==v else c[i] for i in range(n))
                        assert sum(d)==sum(c) and sum(z*z for z in d)-sum(z*z for z in c)==2*(c[s]-1)*(c[t]-1)
                        candidates.append(dict(v=v,d=list(d),losing=not truth[d]))
                    if candidates:
                        r=dict(c=list(c),s=s,t=t,candidates=candidates,failed=all(truth[tuple(r['d'])] for r in candidates));expected.append(r)
                        if r['failed']:failures.append(dict(graph=g,**r))
        assert expected==report['rows'] and count==report['inputs'] and losers==report['losing_inputs'];pairs+=len(expected);total+=len(records)
    result=dict(graphs=len(graphs),independently_checked_states=total,negative_states=neg,legal_dependency_moves=steps,eligible_pairs=pairs,failed_pairs=len(failures),first_failures=failures[:4],all_complete_keys_and_certificates_equal=True)
    (B/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
