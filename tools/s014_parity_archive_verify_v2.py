"""Separate streaming coordinate parser and exhaustive receiver regeneration."""
import hashlib,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/parity_archive')
def main():
    inp=json.loads((B/'inputs.json').read_bytes());saved=json.loads(lzma.decompress((B/'results.json.xz').read_bytes()));assert len(saved)==len(inp['cases'])==343;allfail=[];heavyfail=[];total=0
    for item,row in zip(inp['cases'],saved):
        assert item['id']==row['case'];meta=json.loads(Path(item['summary']).read_bytes());meta={**meta,**meta['case']['graph']} if 'n' not in meta else meta;n=meta['n'];T=meta['threshold'];critical=None
        with lzma.open(item['certificate'],'rb') as f:
            while header:=f.read(12):
                mass,count=struct.unpack('<IQ',header)
                if mass!=T-1:
                    remaining=count*16
                    while remaining:raw=f.read(min(remaining,1048576));assert raw;remaining-=len(raw)
                    continue
                if count>300000:break
                critical=set()
                for _ in range(count):raw=f.read(16);assert not any(raw[n:]);c=tuple(raw[:n]);assert sum(c)==T-1;critical.add(c)
                assert len(critical)==count;break
        if critical is None:assert row['status']=='CRITICAL_LAYER_CAP_UNKNOWN';continue
        expected={}
        for c in critical:
            heavy=[v for v in range(n) if c[v]>=2]
            if len(heavy)<2:continue
            losing=[]
            for root in range(n):
                d=tuple(T-1-sum(c[z]%2 for z in range(n) if z!=root) if v==root else c[v]%2 for v in range(n))
                assert sum(d)==T-1 and all(d[v]%2==c[v]%2 for v in range(n)) and sum(x>1 for x in d)<=1
                if d in critical:losing.append(root)
            expected[c]=dict(c=list(c),losing_sources=losing,losing_heavy_sources=[v for v in heavy if v in losing]);total+=1
        assert row['critical_losers']==len(critical) and {tuple(r['c']):r for r in row['nonAS']}==expected
        for c,r in expected.items():
            record=dict(case=item['id'],graph=meta['graph'],goal=item['goal'],n=n,edges=meta['edges'],threshold=T,c=list(c),losing_sources=r['losing_sources'],summary=item['summary'],certificate=item['certificate'])
            if not r['losing_sources']:allfail.append(record)
            if not r['losing_heavy_sources']:heavyfail.append(record)
    result=dict(cases=len(saved),nonAS_critical_inputs=total,all_receiver_failures=len(allfail),heavy_receiver_failures=len(heavyfail),first_all_receiver_failures=allfail[:4],first_heavy_receiver_failures=heavyfail[:4],all_complete_generated_memberships_equal=True)
    (B/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
