"""Independent complete general layers and all H2r coordinate choices."""
import contextlib,itertools,json,lzma,struct,sys
from pathlib import Path
import s014_regular_eliminate_engine_verify as engine
B=Path('evidence/S014/regular_eliminate')
def main():
    cases=json.loads((B/'inputs.json').read_bytes())['cases'];rows=json.loads(lzma.decompress((B/'results.json.xz').read_bytes()));total=nonAS=tests=failures=nonASQ=0;first=[];summary=[]
    for case,row in zip(cases,rows):
        g=case['graph'];name=g['graph'];n=g['n'];sys.argv=['engine',name,'stack']
        with (B/(name+'_checker.log')).open('w',encoding='utf-8',newline='\n') as log,contextlib.redirect_stdout(log):engine.main()
        verified=json.loads((B/(name+'_stack_threshold_verification.json')).read_bytes());T=verified['threshold'];total+=verified['certified_losing_states']
        if T is None:assert row['status']!='EXACT_THRESHOLD';summary.append(dict(graph=name,status=row['status']));continue
        crit=set()
        with lzma.open(B/(name+'_stack_threshold.bin.xz'),'rb') as src:
            while raw:=src.read(12):
                mass,count=struct.unpack('<IQ',raw)
                if mass==T-1:
                    for _ in range(count):data=src.read(16);assert not any(data[n:]);crit.add(tuple(data[:n]))
                    break
                left=count*16
                while left:data=src.read(min(left,1048576));assert data;left-=len(data)
        wanted={c for c in crit if sum(z>1 for z in c)>=2};assert wanted=={tuple(r['c']) for r in row['rows']};q=max(sum(z*z for z in c) for c in crit);qm={c for c in crit if sum(z*z for z in c)==q};assert qm==set(map(tuple,row['Qmax']));nonASQ+=sum(sum(z>1 for z in c)>1 for c in qm)
        for rec in row['rows']:
            c=tuple(rec['c']);h=sum(z>1 for z in c);expected={}
            for s,t in itertools.permutations(range(n),2):
                if min(c[s],c[t])<2:continue
                empty=tuple(v for v in range(n) if c[v]==0)
                for r in range(2):
                    for U in [()]+[(v,) for v in empty]+list(itertools.combinations(empty,2)):
                        if len(U)+r>c[s]:continue
                        d=tuple(r if v==s else c[t]+c[s]-r-len(U) if v==t else 1 if v in U else c[v] for v in range(n));assert sum(d)==T-1 and sum(z>1 for z in d)==h-1;expected[s,t,r,U]=d in crit
            assert len(expected)<=300000 and expected=={(s,t,r,tuple(U)):losing for s,t,r,U,losing in rec['candidates']};failed=not any(expected.values());assert failed==rec['failed'];nonAS+=1;tests+=len(expected);failures+=failed
            if failed and len(first)<4:first.append(dict(graph=g,threshold=T,c=list(c),candidates=len(expected)))
        assert row['L_AS']==verified['L_AS_exact'];summary.append(dict(graph=name,status='EXACT_THRESHOLD',threshold=T,L_AS=verified['L_AS_exact']))
    out=dict(graphs=len(cases),complete=sum(r['status']=='EXACT_THRESHOLD' for r in summary),unknown=sum(r['status']!='EXACT_THRESHOLD' for r in summary),full_losing_states=total,nonAS_critical_inputs=nonAS,candidates=tests,H2r_failures=failures,nonAS_global_Q=nonASQ,all_complete_AS_comparisons_hold=all(r['L_AS']==r['threshold']-1 for r in summary if r['status']=='EXACT_THRESHOLD'),first_failures=first,graphs_detail=summary,all_full_layers_and_H2r_keys_equal=True)
    (B/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k!='graphs_detail'}),flush=True)
if __name__=='__main__':main()
