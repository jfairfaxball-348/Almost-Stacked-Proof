"""Separate coordinate enumeration and complete critical-state membership."""
import itertools,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/oddshift');A=Path('evidence/S014/parity_archive')
def main():
    items=json.loads((A/'inputs.json').read_bytes())['cases'];saved=json.loads(lzma.decompress((B/'results.json.xz').read_bytes()));total=losing=0;failures=[];pairsfail=[];inputcount=0
    for item,row in zip(items,saved):
        meta=json.loads(Path(item['summary']).read_bytes());meta={**meta,**meta['case']['graph']} if 'n' not in meta else meta;n=meta['n'];T=meta['threshold'];E={frozenset(e) for e in meta['edges']};critical=set()
        with lzma.open(item['certificate'],'rb') as f:
            while raw:=f.read(12):
                mass,count=struct.unpack('<IQ',raw)
                if mass==T-1:
                    if count>300000:break
                    for _ in range(count):raw=f.read(16);assert not any(raw[n:]);critical.add(tuple(raw[:n]))
                    break
                size=count*16
                while size:raw=f.read(min(size,1048576));assert raw;size-=len(raw)
        if row['status']=='INHERITED_UNKNOWN':assert not critical;continue
        expected={};groups={};ordered={}
        for c in sorted(critical):
            if sum(x>1 for x in c)<2:continue
            for s,t,v in itertools.permutations(range(n),3):
                if c[s]<3 or c[s]%2!=1 or c[t]<2 or c[v] or frozenset([s,t]) not in E or frozenset([s,v]) not in E:continue
                d=tuple(0 if z==s else c[z]+c[s]-1 if z==t else 1 if z==v else c[z] for z in range(n));assert sum(d)==T-1 and sum(x*x for x in d)-sum(x*x for x in c)==2*(c[s]-1)*(c[t]-1)>0
                rec=dict(c=list(c),s=s,t=t,v=v,d=list(d),private=frozenset([t,v]) not in E,losing=d in critical);expected[c,s,t,v]=rec;groups.setdefault(c,[]).append(rec);ordered.setdefault((c,s,t),[]).append(rec)
        assert {(tuple(r['c']),r['s'],r['t'],r['v']):r for r in row['rows']}==expected and len(expected)<=300000
        total+=len(expected);losing+=sum(r['losing'] for r in expected.values());inputcount+=len(groups)
        for c,rs in groups.items():
            if not any(r['losing'] for r in rs):failures.append(dict(case=item['id'],graph=meta['graph'],goal=item['goal'],n=n,edges=meta['edges'],threshold=T,c=list(c),candidates=rs,summary=item['summary'],certificate=item['certificate']))
        for (c,s,t),rs in ordered.items():
            if not any(r['losing'] for r in rs):pairsfail.append((item['id'],c,s,t))
    result=dict(cases=len(saved),tests=total,losing_transforms=losing,eligible_critical_inputs=inputcount,all_transformations_win_failures=len(failures),ordered_pair_failures=len(pairsfail),first_failures=failures[:4],all_complete_keys_Q_identities_and_memberships_equal=True);(B/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
