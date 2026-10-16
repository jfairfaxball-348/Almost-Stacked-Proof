"""Complete tuple-coordinate canonical-parent replay, without producer imports."""
import hashlib,itertools,json,lzma,struct,sys
from pathlib import Path
B=Path('evidence/S014')
def main():
    name,goal=sys.argv[1:3];stem=name+'_'+goal+'_threshold';report=json.loads((B/(stem+'.json')).read_bytes());case=report['case'];g=case['graph'];n=g['n']
    inputs=json.loads((B/'threshold_inputs.json').read_bytes());assert case==next(c for c in inputs['cases'] if c['graph']['graph']==name and c['goal']==goal)
    path=B/(stem+'.bin.xz');assert hashlib.sha256(path.read_bytes()).hexdigest()==report['certificate_sha256']
    neighbors=[sorted(v for a,b in g['edges'] for u,v in [(a,b),(b,a)] if u==s) for s in range(n)]
    prev=set();L_AS=-1;last_losers=None;rows=[];total=0
    with lzma.open(path,'rb') as handle:
        for saved in report['rows']:
            mass,count=struct.unpack('<IQ',handle.read(12));assert mass==saved['mass'] and mass==len(rows)+1 and count<=case['loser_cap']
            wanted=set();order=[]
            for _ in range(count):
                raw=handle.read(16);assert len(raw)==16 and not any(raw[n:]);c=tuple(raw[:n]);assert sum(c)==mass;wanted.add(c);order.append(raw)
            assert len(wanted)==count and order==sorted(order,key=lambda raw:int.from_bytes(raw,'little'))
            computed=set()
            if mass<=n:
                for sites in itertools.combinations(range(n),mass):
                    c=tuple(int(v in sites) for v in range(n))
                    if mass!=1:computed.add(c)
            generated=set()
            for d in prev:
                for u in range(n):
                    for v in neighbors[u]:
                        if not d[v]:continue
                        c=list(d);c[u]+=2;c[v]-=1;c=tuple(c)
                        # Unique canonical first move is the lowest heavy source, then its least neighbor.
                        if any(c[w]>=2 for w in range(u)) or v!=neighbors[u][0]:continue
                        assert c not in generated;generated.add(c)
                        if goal=='stack' and sum(a>0 for a in c)==1:continue
                        losing=True
                        for s in range(n):
                            if c[s]<2:continue
                            for t in neighbors[s]:
                                child=list(c);child[s]-=2;child[t]+=1
                                if tuple(child) not in prev:losing=False;break
                            if not losing:break
                        if losing:computed.add(c)
            assert computed==wanted,(name,goal,mass,len(computed),len(wanted))
            Q=max((sum(v*v for v in c) for c in wanted),default=None);qm=sorted(c for c in wanted if sum(v*v for v in c)==Q);AS=sum(sum(a>1 for a in c)<=1 for c in wanted)
            assert len(wanted)==saved['losers'] and AS==saved['AS_losers'] and Q==saved['Q'] and qm==sorted(tuple(c) for c in saved['Qmax'])
            if AS:L_AS=mass
            total+=count;rows.append(dict(mass=mass,losers=count,AS_losers=AS,Q=Q));prev=wanted
            if wanted:last_losers=wanted
        assert not handle.read(1)
    assert report['last_complete_mass']==len(rows) and L_AS<=case['L_AS']
    if report['scope']=='EXACT_THRESHOLD':
        assert report['threshold']==len(rows)>n and not prev and last_losers and max(sum(c) for c in last_losers)==len(rows)-1
        assert L_AS==case['L_AS'] and report['threshold']-1>=case['L_AS']
    else:assert report['threshold'] is None
    result=dict(graph=name,goal=goal,scope=report['scope'],threshold=report['threshold'],last_complete_mass=len(rows),certified_losing_states=total,L_AS_seen=L_AS,L_AS_grammar=case['L_AS'],all_full_losing_layers_equal=True)
    (B/(stem+'_verification.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
