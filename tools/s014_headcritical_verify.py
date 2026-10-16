"""Independent full layers and coordinate regeneration of critical head keys."""
import contextlib,itertools,json,lzma,struct,sys
from pathlib import Path
import s014_headcritical_engine_verify as engine
B=Path('evidence/S014/headcritical')
def main():
    cases=json.loads((B/'inputs.json').read_bytes())['cases'];reports=json.loads(lzma.decompress((B/'results.json.xz').read_bytes()));first=[];pairs=failed=states=nonASQ=complete=0;inputfail=[]
    assert len(cases)==len(reports)==252
    for case,row in zip(cases,reports):
        g=case['graph'];name=g['graph'];n=g['n'];E={frozenset(e) for e in g['edges']};sys.argv=['engine',name,'stack']
        with (B/(name+'_checker.log')).open('w',encoding='utf-8',newline='\n') as log,contextlib.redirect_stdout(log):engine.main()
        ver=json.loads((B/(name+'_stack_threshold_verification.json')).read_bytes());T=ver['threshold'];states+=ver['certified_losing_states']
        if T is None:assert row['status']!='EXACT_THRESHOLD';continue
        complete+=1;critical=set()
        with lzma.open(B/(name+'_stack_threshold.bin.xz'),'rb') as f:
            while hdr:=f.read(12):
                mass,count=struct.unpack('<IQ',hdr)
                if mass==T-1:
                    for _ in range(count):raw=f.read(16);assert not any(raw[n:]);critical.add(tuple(raw[:n]))
                    break
                left=count*16
                while left:data=f.read(min(left,1048576));assert data;left-=len(data)
        Q=max(sum(z*z for z in c) for c in critical);qm=[c for c in critical if sum(z*z for z in c)==Q];nonASQ+=sum(sum(z>1 for z in c)>1 for c in qm)
        assert row['threshold']==T and row['L_AS']==ver['L_AS_exact'] and row['Q']==Q and sorted(map(tuple,row['Qmax']))==sorted(qm)
        expected={};groups={}
        for c in critical:
            if sum(z>1 for z in c)<2:continue
            for s,t in itertools.permutations(range(n),2):
                if c[s]<3 or c[s]%2==0 or c[t]<c[s] or frozenset([s,t]) not in E:continue
                candidates=[]
                for v in range(n):
                    if v==t or c[v] or frozenset([s,v]) not in E or frozenset([t,v]) in E:continue
                    d=tuple(0 if i==s else c[t]+c[s]-1 if i==t else 1 if i==v else c[i] for i in range(n));assert sum(d)==T-1 and sum(z*z for z in d)-sum(z*z for z in c)==2*(c[s]-1)*(c[t]-1)>0
                    candidates.append(dict(v=v,d=list(d),losing=d in critical))
                if candidates:
                    rec=dict(c=list(c),s=s,t=t,candidates=candidates,failed=all(tuple(r['d']) not in critical for r in candidates));expected[c,s,t]=rec;groups.setdefault(c,[]).append(rec)
        assert {(tuple(r['c']),r['s'],r['t']):r for r in row['rows']}==expected
        pairs+=len(expected);failed+=sum(r['failed'] for r in expected.values())
        for r in sorted(expected.values(),key=lambda r:(r['c'],r['s'],r['t'])):
            if r['failed'] and len(first)<4:first.append(dict(graph=g,threshold=T,**r))
        for c,rs in groups.items():
            if all(r['failed'] for r in rs):inputfail.append(dict(graph=g,threshold=T,c=list(c)))
    out=dict(graphs=len(cases),complete_thresholds=complete,unknown=len(cases)-complete,full_losing_states=states,eligible_critical_pairs=pairs,failed_ordered_pairs=failed,failed_input_existence=len(inputfail),nonAS_global_Q_critical_inputs=nonASQ,all_complete_AS_comparisons_hold=all(r['L_AS']==r['threshold']-1 for r in reports if r['status']=='EXACT_THRESHOLD'),first_failures=first,first_input_failures=inputfail[:4],all_full_layers_and_critical_keys_equal=True)
    (B/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
