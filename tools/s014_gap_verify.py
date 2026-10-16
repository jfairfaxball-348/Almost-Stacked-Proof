"""Separate streamed-byte/triple-enumeration verifier for CAM-S014-01."""
import hashlib,itertools,json,lzma,struct
from pathlib import Path

def inspect(n,edges,configurations):
    adj=[[False]*n for _ in range(n)];degree=[0]*n
    for a,b in edges:adj[a][b]=adj[b][a]=True;degree[a]+=1;degree[b]+=1
    triangles=set()
    for a,b,c in itertools.combinations(range(n),3):
        if adj[a][b] and adj[a][c] and adj[b][c]:triangles.update([a,b,c])
    ranked=sorted((sum(v*v for v in c),-sum(a*b for a,b in zip(degree,c)),tuple(c)) for c in configurations)
    q=ranked[-1][0];qm=sorted(c for a,b,c in ranked if a==q);p=-max(b for a,b,c in ranked if a==q)
    qp=sorted(c for a,b,c in ranked if a==q and -b==p)
    predicates={}
    for name,values in [('Q',qm),('QP',qp)]:
        bad=sum(any(c[v]>=2 for v in triangles) for c in values);not_as=sum(len([v for v in c if v>=2])>=2 for c in values)
        predicates.update({name+'_every_nontri':bad==0,name+'_some_nontri':bad<len(values),name+'_every_AS':not_as==0,name+'_some_AS':not_as<len(values)})
    return sorted(triangles),q,p,qm,qp,predicates

def main():
    root=Path('evidence/S014');expected=json.loads(lzma.decompress((root/'gap_extrema.json.xz').read_bytes()))
    byname={r['graph']:r for r in expected['archive']};statuses=[]
    for item in json.loads((root/'gap_inputs.json').read_bytes()):
        for filename,sha in item['files'].items():assert hashlib.sha256(Path(filename).read_bytes()).hexdigest()==sha
        clear=json.loads(Path(item['clear']).read_bytes());stack=json.loads(Path(item['stack']).read_bytes()) if item['stack'] else {}
        if stack.get('scope')!='EXACT_THRESHOLD':statuses.append([clear['graph'],'STACK_UNKNOWN']);continue
        if clear['threshold']==stack['threshold']:statuses.append([clear['graph'],'ZERO_GAP']);continue
        found=None
        with lzma.open(item['certificate'],'rb') as handle:
            while header:=handle.read(12):
                mass,count=struct.unpack('<IQ',header)
                if mass!=clear['threshold']-1:
                    remaining=16*count
                    while remaining:
                        part=handle.read(min(remaining,65536));assert part;remaining-=len(part)
                    continue
                if count>300000:break
                found=[]
                for _ in range(count):
                    chunk=handle.read(16);assert len(chunk)==16 and not any(chunk[clear['n']:])
                    c=tuple(chunk[:clear['n']]);assert sum(c)==mass;found.append(c)
                assert len(set(found))==count
                break
        if found is None:statuses.append([clear['graph'],'CRITICAL_LAYER_UNKNOWN']);continue
        statuses.append([clear['graph'],'POSITIVE_GAP_COMPLETE']);r=byname.pop(clear['graph'])
        assert r['critical_losers']==len(found) and r['gap']==clear['threshold']-stack['threshold']
        vals=inspect(clear['n'],clear['edges'],found)
        assert json.loads(json.dumps(vals))==[r[k] for k in ['triangle_vertices','Q','P','Qmax','QPmin','predicates']]
    assert not byname and statuses==expected['status']
    tables=json.loads(lzma.decompress(Path('evidence/S013/precision_tables.json.xz').read_bytes()))
    inputs=json.loads(Path('evidence/S013/precision_inputs.json').read_bytes());meta=json.loads(Path('evidence/S013/precision.json').read_bytes())
    eligible=[]
    for inp,t,m in zip(inputs,tables,meta):
        s=m['thresholds']['stack'];g=m['thresholds']['clear']
        if not g or not s or g<=s:continue
        eligible.append(inp['graph']);r=next(z for z in expected['precision'] if z['graph']==inp['graph'])
        values=inspect(inp['n'],inp['edges'],[c for c,mask in t['layers'][g-1] if mask[0]==0])
        assert json.loads(json.dumps(values))==[r[k] for k in ['triangle_vertices','Q','P','Qmax','QPmin','predicates']]
    assert eligible==[r['graph'] for r in expected['precision']]
    for witness in expected['negative_witnesses']:
        r=next(r for r in expected['archive']+expected['precision'] if r['graph']==witness['graph'])
        states={tuple(c) for c in witness['states']};assert len(states)==len(witness['states'])<=300000
        start=tuple(witness['c']);assert start in states and witness['c'] in r['Qmax'] and any(start[v]>=2 for v in r['triangle_vertices'])
        reachable={start}
        for c in sorted(states,key=lambda c:-sum(c)):
            assert c in reachable and sum(c)!=1
            for a,b in r['edges']:
                for u,v in [(a,b),(b,a)]:
                    if c[u]<2:continue
                    d=list(c);d[u]-=2;d[v]+=1;d=tuple(d);assert d in states;reachable.add(d)
        assert reachable==states
    assert expected['threshold_claims']==0
    print(json.dumps(dict(archive_cases=len(expected['archive']),precision_cases=len(expected['precision']),complete_negative_closures=len(expected['negative_witnesses']),all_selected_sets_and_predicates_equal=True)))
if __name__=='__main__':main()
