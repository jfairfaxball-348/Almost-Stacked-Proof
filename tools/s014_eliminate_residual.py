"""Finite test of precisely stated critical heavy elimination H2."""
import itertools,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/eliminate_residual')
def main():
    out=[]
    for item in json.loads((B/'inputs.json').read_bytes())['cases']:
        n,T=item['n'],item['threshold'];crit=set()
        with lzma.open(item['certificate'],'rb') as f:
            while hdr:=f.read(12):
                mass,count=struct.unpack('<IQ',hdr)
                if mass==T-1:
                    if count>300000:raise RuntimeError('CRITICAL_CAP_UNKNOWN')
                    crit={int.from_bytes(f.read(16),'little') for _ in range(count)};break
                left=count*16
                while left:part=f.read(min(left,65536));assert part;left-=len(part)
        rows=[]
        for x in sorted(crit):
            c=[(x>>(8*v))&255 for v in range(n)];heavy=[v for v in range(n) if c[v]>1]
            if len(heavy)<2:continue
            empty=[v for v in range(n) if c[v]==0];candidates=[]
            for s,t in itertools.permutations(heavy,2):
                for r in [0,1]:
                    for k in range(min(2,c[s]-r)+1):
                        for U in itertools.combinations(empty,k):
                            d=c.copy();d[s]=r;d[t]+=c[s]-r-k
                            for v in U:d[v]=1
                            y=sum(z<<(8*v) for v,z in enumerate(d));candidates.append([s,t,r,list(U),y in crit])
            assert len(candidates)<=300000
            rows.append(dict(c=c,candidates=candidates,failed=not any(r[-1] for r in candidates)))
        out.append(dict(case=item['id'],rows=rows))
    (B/'results.json.xz').write_bytes(lzma.compress((json.dumps(out,separators=(',',':'))+'\n').encode()));print(json.dumps(dict(cases=len(out),critical_nonAS=sum(len(r['rows']) for r in out),failed_inputs=sum(t['failed'] for r in out for t in r['rows']))),flush=True)
if __name__=='__main__':main()
