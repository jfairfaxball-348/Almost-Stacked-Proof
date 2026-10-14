"""Independent optimality/legality and full candidate closures; no producer import."""
import hashlib
import itertools
import json
import lzma
import sys
import time
from pathlib import Path
from s006_verify import check

def verify(row):
    c=row['clear'];f=row['forest'];cells=c['cells'];n=c['n'];s=c['source']
    edges={frozenset(e) for e in c['edges']};decoded=[]
    # Reconstruct tree input/output vectors independently from the retained DAG.
    for node in c['nodes']:
        x=cells[node['cell']]
        if node['children'] is None:d=tuple(int(v==node['leaf']) for v in range(n))
        else:
            a,b=(decoded[j] for j in node['children']);assert a[1]==b[1]
            d=tuple(u+v for u,v in zip(a[0],b[0]))
        decoded.append((d,x['vertex']))
    forests=[]
    for i,node in enumerate(f['nodes']):
        cell=cells[node['cell']]
        if node['clear_node'] is not None:
            d,q=decoded[node['clear_node']];trees=[node['clear_node']]
        else:
            a,b=node['children'];assert a<i and b<i
            da,qa,ta=forests[a];db,qb,tb=forests[b];assert qa==qb
            d=tuple(x+y for x,y in zip(da,db));q=qa;trees=ta+tb
        assert q==cell['vertex'] and tuple(d[v] for v in c['off_vertices'])==tuple(cell['off'])
        assert cell['kind']==(d[s]%3 if d[s]>0 else 3)
        forests.append((d,q,trees))
    values={(x['vertex'],tuple(x['off']),x['kind']):f['values'][i] for i,x in enumerate(cells)}
    inequalities=0;finite=0;moves=0
    for i,cell in enumerate(cells):
        v=f['values'][i];cv=cell['value']
        if cv is not None:assert v is not None and v<=cv
        if v is None:assert f['roots'][i] is None;continue
        d,q,trees=forests[f['roots'][i]];assert d[s]==v
        assert q==cell['vertex'] and tuple(d[w] for w in c['off_vertices'])==tuple(cell['off'])
        current=list(d)
        for tree in trees:
            todo=[(tree,False)]
            while todo:
                j,ready=todo.pop();node=c['nodes'][j]
                if node['children'] is None:continue
                if not ready:todo.append((j,True));todo.extend((k,False) for k in node['children'])
                else:
                    u=cells[c['nodes'][node['children'][0]]['cell']]['vertex'];w=cells[node['cell']]['vertex']
                    assert frozenset((u,w)) in edges and current[u]>=2
                    current[u]-=2;current[w]+=1;moves+=1
        assert sum(current)>0 and all(current[w]==0 for w in range(n) if w!=q)
        finite+=1
    for a in cells:
        for b in cells:
            if a['vertex']!=b['vertex']:continue
            va=values[a['vertex'],tuple(a['off']),a['kind']];vb=values[b['vertex'],tuple(b['off']),b['kind']]
            if va is None or vb is None:continue
            d=tuple(x+y for x,y in zip(a['off'],b['off']))
            if any(x>y for x,y in zip(d,c['box'])):continue
            r=(va+vb)%3 if va+vb else 3
            vp=values[a['vertex'],d,r];assert vp is not None and vp<=va+vb;inequalities+=1
    N=row['candidate_source'];b=tuple(c['box'])
    candidate_min=min(values[q,b,N%3] for q in range(n) if values[q,b,N%3] is not None)
    assert N<candidate_min
    return {'length':row['length'],'forest_finite':finite,'forest_inequalities':inequalities,'forest_replay_moves':moves,'candidate_source':N,'candidate_minimum':candidate_min}

def closure(l):
    n=l+3;s=0 if l==0 else n-1;N=4*2**l-3
    edges=[(0,1),(0,2),(1,2)]+[(0 if v==3 else v-1,v) for v in range(3,n)]
    start=tuple(N if v==s else int(v in (1,2)) for v in range(n))
    seen={start};todo=[start]
    while todo:
        c=todo.pop()
        for a,b in edges:
            for u,v in ((a,b),(b,a)):
                if c[u]<2:continue
                d=list(c);d[u]-=2;d[v]+=1;d=tuple(d)
                if d not in seen:seen.add(d);todo.append(d)
        assert len(seen)<=300000
    # Distinct backward goal recurrence over the complete reachable domain.
    wins={c for c in seen if sum(x>0 for x in c)==1}
    for t in range(1,sum(start)+1):
        previous=[c for c in wins if sum(c)==t-1]
        for c in previous:
            for a,b in edges:
                for u,v in ((a,b),(b,a)):
                    if not c[v]:continue
                    d=list(c);d[u]+=2;d[v]-=1;d=tuple(d)
                    if d in seen:wins.add(d)
    assert start not in wins and not wins
    return {'length':l,'configuration':start,'complete_reachable_states':len(seen),'stack_goals':len(wins),'closure_sha256':hashlib.sha256(json.dumps(sorted(seen),separators=(',',':')).encode()).hexdigest()}

def main():
    start=time.monotonic();rows=json.loads(lzma.decompress(Path('evidence/S008/tip_certificates.json.xz').read_bytes()))
    assert len(rows)==9
    out={'grammar':[],'forest':[],'closures':[]}
    for row in rows:
        l=row['length'];c=row['clear'];assert l==len(out['grammar']) and c['n']==l+3
        assert c['source']==(0 if l==0 else l+2)
        assert row['candidate_source']==4*2**l-3
        assert c['box']==[int(v in (1,2)) for v in c['off_vertices']]
        assert c['edges']==[[0,1],[0,2],[1,2]]+[[0 if v==3 else v-1,v] for v in range(3,l+3)]
        out['grammar'].append(check(c));out['forest'].append(verify(row));assert time.monotonic()-start<600
    out['closures']=[closure(l) for l in range(4)];out['all_verified']=True
    if '--check-only' not in sys.argv:Path('evidence/S008/tip_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'all_verified':True,'grammar_cases':len(rows),'closures':out['closures'],'forest_finite':sum(x['forest_finite'] for x in out['forest']),'seconds':time.monotonic()-start}))

if __name__=='__main__':main()
