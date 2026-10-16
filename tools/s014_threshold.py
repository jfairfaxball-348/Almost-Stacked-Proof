"""Complete all-predecessor sparse losing layers, four exact registered cases."""
import hashlib,itertools,json,lzma,struct,sys
from pathlib import Path
B=Path('evidence/S014')
def main():
    name,goal=sys.argv[1:3];inp=json.loads((B/'threshold_inputs.json').read_bytes());case=next(c for c in inp['cases'] if c['graph']['graph']==name and c['goal']==goal)
    g=case['graph'];n=g['n'];units=[1<<(8*v) for v in range(n)];arcs=sorted((u,v) for e in g['edges'] for u,v in [e,e[::-1]]);delta=[2*units[u]-units[v] for u,v in arcs]
    stem=name+'_'+goal+'_threshold';dest=B/(stem+'.bin.xz');prev=set();rows=[];threshold=None;status='COMPLETE_TO_REGISTERED_MASS'
    with lzma.open(dest,'wb') as cert:
        for mass in range(1,case['max_mass']+1):
            candidates=set()
            for d in prev:
                for (u,v),change in zip(arcs,delta):
                    if (d>>(8*v))&255:candidates.add(d+change)
                if len(candidates)>case['candidate_cap']:status='CANDIDATE_CAP_UNKNOWN';break
            if status.endswith('UNKNOWN'):break
            if mass<=n:
                candidates.update(sum(units[v] for v in vs) for vs in itertools.combinations(range(n),mass))
            if len(candidates)>case['candidate_cap']:status='CANDIDATE_CAP_UNKNOWN';break
            pure={mass*u for u in units} if goal=='stack' or mass==1 else set();losers=set()
            for c in candidates:
                if c in pure:continue
                if all(c-change in prev for (u,v),change in zip(arcs,delta) if ((c>>(8*u))&255)>=2):losers.add(c)
                if len(losers)>case['loser_cap']:status='LOSING_LAYER_CAP_UNKNOWN';break
            if status.endswith('UNKNOWN'):break
            ordered=sorted(losers);cert.write(struct.pack('<IQ',mass,len(ordered)))
            for c in ordered:cert.write(c.to_bytes(16,'little'))
            configs=[tuple((c>>(8*v))&255 for v in range(n)) for c in ordered]
            assert all(sum(c)==mass for c in configs) and mass<256
            Q=max((sum(a*a for a in c) for c in configs),default=None);maxima=[c for c in configs if sum(a*a for a in c)==Q]
            row=dict(mass=mass,candidates=len(candidates),losers=len(losers),AS_losers=sum(sum(a>1 for a in c)<=1 for c in configs),Q=Q,Qmax=maxima);rows.append(row)
            print(json.dumps({k:v for k,v in row.items() if k!='Qmax'}),flush=True)
            if not losers and mass>n:threshold=mass;status='EXACT_THRESHOLD';break
            prev=losers
    summary=dict(case=case,scope=status,threshold=threshold,last_complete_mass=rows[-1]['mass'] if rows else 0,rows=rows,certificate_sha256=hashlib.sha256(dest.read_bytes()).hexdigest())
    (B/(stem+'.json')).write_text(json.dumps(summary,separators=(',',':'))+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in summary.items() if k not in ['case','rows']}),flush=True)
if __name__=='__main__':main()
