"""Batch complete layers for exactly the previously failing graphs."""
import contextlib,json,sys,lzma,struct
from pathlib import Path
import s014_headcritical_engine as engine
B=Path('evidence/S014/headcritical')
def main():
    results=[]
    for case in json.loads((B/'inputs.json').read_bytes())['cases']:
        name=case['graph']['graph'];sys.argv=['engine',name,'stack']
        with (B/(name+'_producer.log')).open('w',encoding='utf-8',newline='\n') as log,contextlib.redirect_stdout(log):engine.main()
        report=json.loads((B/(name+'_stack_threshold.json')).read_bytes());T=report['threshold'];n=case['graph']['n'];N=[set() for _ in range(n)]
        for u,v in case['graph']['edges']:N[u].add(v);N[v].add(u)
        if T is None:results.append(dict(graph=name,status=report['scope'],rows=[]));continue
        critical=set()
        with lzma.open(B/(name+'_stack_threshold.bin.xz'),'rb') as f:
            while hdr:=f.read(12):
                mass,count=struct.unpack('<IQ',hdr)
                if mass==T-1:critical={int.from_bytes(f.read(16),'little') for _ in range(count)};break
                remaining=count*16
                while remaining:data=f.read(min(remaining,65536));assert data;remaining-=len(data)
        rows=[]
        for x in sorted(critical):
            c=[(x>>(8*v))&255 for v in range(n)]
            if sum(z>1 for z in c)<=1:continue
            for s in range(n):
                if c[s]<3 or c[s]%2!=1:continue
                for t in sorted(N[s]):
                    if c[t]<c[s]:continue
                    cs=[]
                    for v in sorted(N[s]-N[t]-{t}):
                        if c[v]:continue
                        d=c.copy();d[s]=0;d[t]+=c[s]-1;d[v]=1;y=sum(z<<(8*i) for i,z in enumerate(d));cs.append(dict(v=v,d=d,losing=y in critical))
                    if cs:rows.append(dict(c=c,s=s,t=t,candidates=cs,failed=all(not r['losing'] for r in cs)))
        results.append(dict(graph=name,status='EXACT_THRESHOLD',threshold=T,L_AS=max(r['mass'] for r in report['rows'] if r['AS_losers']),critical_losers=len(critical),Q=report['rows'][-2]['Q'],Qmax=report['rows'][-2]['Qmax'],rows=rows))
    (B/'results.json.xz').write_bytes(lzma.compress((json.dumps(results,separators=(',',':'))+'\n').encode()))
    print(json.dumps(dict(graphs=len(results),complete=sum(r['status']=='EXACT_THRESHOLD' for r in results),eligible_critical_pairs=sum(len(r['rows']) for r in results),failed_pairs=sum(t['failed'] for r in results for t in r['rows']))),flush=True)
if __name__=='__main__':main()
