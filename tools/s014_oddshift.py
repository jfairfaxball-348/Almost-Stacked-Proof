"""Fixed critical odd-concentration diagnostic, all empty actual heads."""
import json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/oddshift');A=Path('evidence/S014/parity_archive')
def main():
    items=json.loads((A/'inputs.json').read_bytes())['cases'];archive=json.loads(lzma.decompress((A/'results.json.xz').read_bytes()));results=[]
    for item,ar in zip(items,archive):
        if ar['status']!='COMPLETE_REGISTERED_CRITICAL_LAYER':results.append(dict(case=item['id'],status='INHERITED_UNKNOWN'));continue
        meta=json.loads(Path(item['summary']).read_bytes());meta={**meta,**meta['case']['graph']} if 'n' not in meta else meta;n=meta['n'];T=meta['threshold'];N=[{v for e in meta['edges'] for u,v in [e,e[::-1]] if u==z} for z in range(n)];critical=set()
        with lzma.open(item['certificate'],'rb') as f:
            while raw:=f.read(12):
                mass,count=struct.unpack('<IQ',raw)
                if mass==T-1:critical={int.from_bytes(f.read(16),'little') for _ in range(count)};break
                size=count*16
                while size:raw=f.read(min(size,65536));assert raw;size-=len(raw)
        rows=[]
        for rec in ar['nonAS']:
            c=rec['c']
            for s in range(n):
                if c[s]<3 or c[s]%2==0:continue
                for t in sorted(N[s]):
                    if c[t]<2:continue
                    for v in sorted(N[s]-{t}):
                        if c[v]:continue
                        d=c.copy();d[s]=0;d[t]+=c[s]-1;d[v]=1;x=sum(z<<(8*i) for i,z in enumerate(d));rows.append(dict(c=c,s=s,t=t,v=v,d=d,private=v not in N[t],losing=x in critical))
        assert len(rows)<=300000;results.append(dict(case=item['id'],graph=meta['graph'],goal=item['goal'],n=n,edges=meta['edges'],threshold=T,status='COMPLETE_FIXED_DIAGNOSTIC',rows=rows))
    (B/'results.json.xz').write_bytes(lzma.compress((json.dumps(results,separators=(',',':'))+'\n').encode()));print(json.dumps(dict(cases=len(results),tests=sum(len(r.get('rows',[])) for r in results),losing_transforms=sum(t['losing'] for r in results for t in r.get('rows',[])))),flush=True)
if __name__=='__main__':main()
