import itertools,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/eliminate_residual')
def main():
    inputs=json.loads((B/'inputs.json').read_bytes())['cases'];saved=json.loads(lzma.decompress((B/'results.json.xz').read_bytes()));first=[];tests=nonAS=failures=0;maxheavy=0
    assert len(inputs)==len(saved)
    for inp,row in zip(inputs,saved):
        n,T=inp['n'],inp['threshold'];crit=set()
        with lzma.open(inp['certificate'],'rb') as src:
            while raw:=src.read(12):
                mass,count=struct.unpack('<IQ',raw)
                if mass==T-1:
                    assert count<=300000
                    for _ in range(count):data=src.read(16);assert not any(data[n:]);crit.add(tuple(data[:n]))
                    break
                left=count*16
                while left:data=src.read(min(left,1048576));assert data;left-=len(data)
        wanted={c for c in crit if sum(z>1 for z in c)>=2};assert wanted=={tuple(r['c']) for r in row['rows']}
        for rec in row['rows']:
            c=tuple(rec['c']);h=sum(z>1 for z in c);maxheavy=max(maxheavy,h);expected={}
            for s in range(n):
                if c[s]<2:continue
                for t in range(n):
                    if s==t or c[t]<2:continue
                    for r in [0,1]:
                        for bits in range(1<<n):
                            U=tuple(v for v in range(n) if bits>>v&1)
                            if len(U)>2 or len(U)+r>c[s] or any(c[v] for v in U):continue
                            d=tuple(r if v==s else c[t]+c[s]-r-len(U) if v==t else 1 if v in U else c[v] for v in range(n));assert sum(d)==sum(c) and sum(z>1 for z in d)==h-1
                            expected[s,t,r,U]=d in crit
            assert len(expected)<=300000 and {(s,t,r,tuple(U)):loss for s,t,r,U,loss in rec['candidates']}==expected
            failed=not any(expected.values());assert failed==rec['failed'];nonAS+=1;tests+=len(expected);failures+=failed
            if failed and len(first)<4:first.append(dict(case=inp,c=list(c),candidate_count=len(expected)))
    result=dict(cases=len(inputs),nonAS_critical_inputs=nonAS,candidates=tests,failed_H2r_inputs=failures,max_heavy_sites=maxheavy,first_failures=first,all_generated_keys_memberships_and_heavy_decreases_equal=True)
    (B/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
