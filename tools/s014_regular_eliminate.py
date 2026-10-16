"""Batch complete layers for exactly the previously failing graphs."""
import contextlib,itertools,json,sys,lzma,struct
from pathlib import Path
import s014_regular_eliminate_engine as engine
B=Path('evidence/S014/regular_eliminate')
def main():
    results=[]
    for case in json.loads((B/'inputs.json').read_bytes())['cases']:
        name=case['graph']['graph'];sys.argv=['engine',name,'stack']
        with (B/(name+'_producer.log')).open('w',encoding='utf-8',newline='\n') as log,contextlib.redirect_stdout(log):engine.main()
        report=json.loads((B/(name+'_stack_threshold.json')).read_bytes());T=report['threshold'];n=case['graph']['n']
        if T is None:results.append(dict(graph=name,status=report['scope'],rows=[]));continue
        crit=set()
        with lzma.open(B/(name+'_stack_threshold.bin.xz'),'rb') as f:
            while hdr:=f.read(12):
                mass,count=struct.unpack('<IQ',hdr)
                if mass==T-1:crit={int.from_bytes(f.read(16),'little') for _ in range(count)};break
                left=count*16
                while left:data=f.read(min(left,65536));assert data;left-=len(data)
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
                            candidates.append([s,t,r,list(U),sum(z<<(8*v) for v,z in enumerate(d)) in crit])
            assert len(candidates)<=300000;rows.append(dict(c=c,candidates=candidates,failed=not any(r[-1] for r in candidates)))
        results.append(dict(graph=name,status='EXACT_THRESHOLD',threshold=T,L_AS=max(r['mass'] for r in report['rows'] if r['AS_losers']),Qmax=report['rows'][-2]['Qmax'],rows=rows))
    (B/'results.json.xz').write_bytes(lzma.compress((json.dumps(results,separators=(',',':'))+'\n').encode()))
    print(json.dumps(dict(graphs=len(results),complete=sum(r['status']=='EXACT_THRESHOLD' for r in results),nonAS_critical=sum(len(r['rows']) for r in results),H2r_failures=sum(t['failed'] for r in results for t in r['rows']))),flush=True)
if __name__=='__main__':main()
