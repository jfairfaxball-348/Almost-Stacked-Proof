"""Exact upward losing recurrence, all inverse moves + terminal seeds."""
import itertools,json,lzma,time,hashlib
from pathlib import Path

def run(name,n,edges,mode,cap=140):
    start=time.monotonic();arcs=[(a,b) for u,v in edges for a,b in [(u,v),(v,u)]]
    bad=set();layers=[[]];rows=[];scope='MASS_CUTOFF';witness=None
    for t in range(1,cap+1):
        candidates=set()
        if t<=n:
            for ss in itertools.combinations(range(n),t):
                c=[0]*n
                for u in ss:c[u]=1
                candidates.add(tuple(c))
        for d in bad:
            for u,v in arcs:
                if d[v]:
                    c=list(d);c[u]+=2;c[v]-=1;candidates.add(tuple(c))
            if len(candidates)>2000000:break
        if len(candidates)>2000000:scope='CANDIDATE_CUTOFF';break
        new=set()
        for c in candidates:
            if (sum(x>0 for x in c)==1 if mode=='stack' else t==1):continue
            losing=True
            for u,v in arcs:
                if c[u]>=2:
                    d=list(c);d[u]-=2;d[v]+=1
                    if tuple(d) not in bad:losing=False;break
            if losing:new.add(c)
        if len(new)>1000000:scope='LOSER_CUTOFF';break
        asbad=[c for c in new if sum(x>=2 for x in c)<=1]
        rows.append({'t':t,'candidates':len(candidates),'losers':len(new),'as_losers':len(asbad)})
        layers.append(sorted(new));bad=new
        if asbad:witness=min(asbad)
        if t>n and not new:scope='EXACT_THRESHOLD';break
        if time.monotonic()-start>120:scope='TIME_CUTOFF';break
    result={'graph':name,'n':n,'edges':edges,'mode':mode,'scope':scope,
            'threshold':rows[-1]['t'] if scope=='EXACT_THRESHOLD' else None,
            'critical_as_witness':witness if scope=='EXACT_THRESHOLD' else None,
            'rows':rows,'seconds':time.monotonic()-start}
    base=Path('evidence/S004')/(name+'_'+mode)
    raw=json.dumps({'n':n,'edges':edges,'mode':mode,'layers':layers},separators=(',',':')).encode()
    base.with_suffix('.json.xz').write_bytes(lzma.compress(raw))
    result['layer_sha256']=hashlib.sha256(raw).hexdigest()
    base.with_suffix('.summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['graph','mode','scope','threshold','critical_as_witness','seconds']}),flush=True)
    return result

def campaign():
    old=json.loads(Path('evidence/S003/T2b_analysis.json').read_text());results=[]
    for r in old:
        for mode in ['stack','clear']:
            a=r['analysis'][mode]
            if isinstance(a,dict) and a['threshold'] is None:
                e=[list(map(int,p.split('-'))) for p in r['edges'].split(',')]
                results.append(run(r['graph'],7,e,mode))
    named=[('C8',8,[(i,(i+1)%8) for i in range(8)]),
           ('C9',9,[(i,(i+1)%9) for i in range(9)]),
           ('C10',10,[(i,(i+1)%10) for i in range(10)]),
           ('triangle_tail5',8,[(0,1),(1,2),(2,0)]+[(i,i+1) for i in range(2,7)]),
           ('two_triangles_path3',8,[(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,6),(6,7),(7,5)]),
           ('C8_chord04',8,[(i,(i+1)%8) for i in range(8)]+[(0,4)])]
    for name,n,e in named:
        for mode in ['stack','clear']:
            if mode=='clear' and name in ['C8','C10']:continue
            results.append(run(name,n,e,mode))
    Path('evidence/S004/frontier_summary.json').write_text(json.dumps(results,indent=2)+'\n')

if __name__=='__main__':campaign()
