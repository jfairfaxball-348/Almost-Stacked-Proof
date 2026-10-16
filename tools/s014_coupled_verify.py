import itertools,json,lzma
from pathlib import Path
B=Path('evidence/S014/coupled')
def main():
    inputs=json.loads((B/'inputs.json').read_bytes())['graphs'];out=json.loads((B/'results.json').read_bytes());complete=states=neg=steps=0;losers=[]
    assert len(inputs)==len(out)==252
    for g,row in zip(inputs,out):
        n=g['n'];E={frozenset(e) for e in g['edges']};db={}
        with lzma.open(B/(g['id']+'.bin.xz'),'rb') as src:
            while data:=src.read(17):
                assert len(data)==17 and not any(data[n:16]);c=tuple(data[:n]);assert c not in db;db[c]=data[16]
        if row['status']=='STATE_CAP_UNKNOWN':assert row['winning'] is None;continue
        assert row['status']=='COMPLETE_INPUT' and len(db)==row['states']<=300000;truth={}
        for c,k in sorted(db.items(),key=lambda kv:(sum(kv[0]),kv[0])):
            if k==255:assert sum(z>0 for z in c)==1;truth[c]=True
            elif k==254:
                assert sum(z>0 for z in c)>1
                for u,v in itertools.permutations(range(n),2):
                    if c[u]<2 or frozenset([u,v]) not in E:continue
                    d=list(c);d[u]-=2;d[v]+=1;assert tuple(d) in truth and not truth[tuple(d)];steps+=1
                truth[c]=False;neg+=1
            else:
                u,v=divmod(k,n);assert u<n and v<n and c[u]>=2 and frozenset([u,v]) in E;d=list(c);d[u]-=2;d[v]+=1;assert truth[tuple(d)];truth[c]=True;steps+=1
        assert tuple(g['c']) in truth and truth[tuple(g['c'])]==row['winning'];complete+=1;states+=len(db)
        if not row['winning']:losers.append(g)
    selected=sorted(losers,key=lambda g:(-g['cross_edges'],g['id']))[:2]
    result=dict(graphs=len(inputs),complete_inputs=complete,unknown=len(inputs)-complete,losing_inputs=len(losers),checked_states=states,negative_states=neg,legal_dependencies=steps,selected_for_AS_rays=selected,all_complete_DAGs_equal=True)
    (B/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
