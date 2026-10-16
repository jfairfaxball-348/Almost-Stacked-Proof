"""Fixed archived critical layers, all parity-class AS vertices."""
import hashlib,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/parity_archive')
def main():
    inp=json.loads((B/'inputs.json').read_bytes());results=[]
    for item in inp['cases']:
        meta=json.loads(Path(item['summary']).read_bytes());n=meta['n'];T=meta['threshold'];crit=None
        with lzma.open(item['certificate'],'rb') as f:
            while raw:=f.read(12):
                mass,count=struct.unpack('<IQ',raw)
                if mass==T-1:
                    if count>300000:break
                    crit={int.from_bytes(f.read(16),'little') for _ in range(count)};assert len(crit)==count;break
                remaining=count*16
                while remaining:chunk=f.read(min(remaining,65536));assert chunk;remaining-=len(chunk)
        if crit is None:results.append(dict(case=item['id'],status='CRITICAL_LAYER_CAP_UNKNOWN'));continue
        rows=[]
        for x in sorted(crit):
            c=[(x>>(8*v))&255 for v in range(n)]
            if sum(z>1 for z in c)<=1:continue
            parity=[z%2 for z in c];base=sum(z<<(8*v) for v,z in enumerate(parity));pairs=sum(c)-sum(parity);losing_sources=[s for s in range(n) if base+(pairs<<(8*s)) in crit]
            rows.append(dict(c=c,losing_sources=losing_sources,losing_heavy_sources=[s for s in losing_sources if c[s]>1]))
        assert len(rows)<=300000
        results.append(dict(case=item['id'],graph=meta['graph'],goal=item['goal'],threshold=T,n=n,status='COMPLETE_REGISTERED_CRITICAL_LAYER',critical_losers=len(crit),nonAS=rows))
    (B/'results.json.xz').write_bytes(lzma.compress((json.dumps(results,separators=(',',':'))+'\n').encode()));print(json.dumps(dict(cases=len(results),nonAS_inputs=sum(len(r.get('nonAS',[])) for r in results),all_receiver_failures=sum(not row['losing_sources'] for r in results for row in r.get('nonAS',[])),heavy_receiver_failures=sum(not row['losing_heavy_sources'] for r in results for row in r.get('nonAS',[])))),flush=True)
if __name__=='__main__':main()
