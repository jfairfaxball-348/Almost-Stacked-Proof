"""Separate tuple replay followed by exact criticality/Q audit of all failures."""
import contextlib,json,sys
from pathlib import Path
import s014_oddbulk_engine_verify as engine
B=Path('evidence/S014/oddbulk')
def main():
    result=[];critical=globalQ=failures=0;allstates=0
    for case in json.loads((B/'inputs.json').read_bytes())['cases']:
        name=case['graph']['graph'];sys.argv=['engine',name,'stack']
        with (B/(name+'_checker.log')).open('w',encoding='utf-8',newline='\n') as log,contextlib.redirect_stdout(log):engine.main()
        verified=json.loads((B/(name+'_stack_threshold_verification.json')).read_bytes());report=json.loads((B/(name+'_stack_threshold.json')).read_bytes());T=verified['threshold'];out=[]
        for f in case['failures']:
            mass=sum(f['c']);row=next(r for r in report['rows'] if r['mass']==mass);Q=sum(z*z for z in f['c']);iscrit=mass==T-1 if T else None;isQ=Q==row['Q'];critical+=bool(iscrit);globalQ+=isQ;failures+=1
            out.append(dict(c=f['c'],s=f['s'],t=f['t'],mass=mass,Q=Q,layer_Qmax=row['Q'],critical=iscrit,global_layer_Q=isQ))
        result.append(dict(graph=name,threshold=T,L_AS=verified['L_AS_exact'],failures=out,all_full_layers_independently_checked=True));allstates+=verified['certified_losing_states']
    summary=dict(graphs=len(result),failed_pairs=failures,critical_failures=critical,layer_global_Q_failures=globalQ,full_losing_states=allstates,all_AS_comparisons_hold=all(r['threshold']==r['L_AS']+1 for r in result),graphs_detail=result)
    (B/'verification.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in summary.items() if k!='graphs_detail'}),flush=True)
if __name__=='__main__':main()
