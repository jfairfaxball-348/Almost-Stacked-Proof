"""CAM-S011-01 forward exact masks, tree alignment and ternary-root predicates."""
import hashlib,itertools,json,lzma,sys,time
from pathlib import Path

GRAPHS=[('K2',2,[(0,1)],3,3,None),('K3',3,[(0,1),(0,2),(1,2)],4,4,4),
 ('P4',4,[(0,1),(1,2),(2,3)],15,15,None),('C5',5,[(0,1),(1,2),(2,3),(3,4),(0,4)],10,8,10),
 ('triangle_tail2',5,[(0,1),(0,2),(1,2),(0,3),(3,4)],22,16,22),
 ('F2',5,[(0,1),(0,2),(1,2),(0,3),(0,4)],13,11,13),
 ('bowtie',5,[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)],8,8,8),
 ('diamond',4,[(0,1),(0,2),(0,3),(1,2),(2,3)],7,7,7)]

def comps(n,t):
    if n==1:yield (t,);return
    for x in range(t+1):
        for rest in comps(n-1,t-x):yield (x,)+rest

def properties(mask,n,edges):
    vertices={v for v in range(n) if mask>>v&1};colors={};components=0;bip=True
    for s in sorted(vertices):
        if s in colors:continue
        components+=1;colors[s]=0;queue=[s]
        for u in queue:
            for a,b in edges:
                if u not in (a,b):continue
                v=b if u==a else a
                if v not in vertices:continue
                if v in colors:bip &= colors[v]!=colors[u]
                else:colors[v]=1-colors[u];queue.append(v)
    return components<=1 and bool(vertices),bool(bip)

def classify(name,n,edges,M,gs,gc,layers):
    failures={'occupied_self_stack':[],'occupied_self_clear':[],'critical_common_clear':[],
              'critical_occupied_self_clear':[],'nonbipartite_ternary_clear_loser':[]}
    critical=[];ternary=[];insertions=deletions=0
    for t in range(2,M+1):
        for c,masks in sorted(layers[t].items()):
            cm,sm,two,three=masks
            if sm and not cm:
                assert three and all(three>>v&1 for v,a in enumerate(c) if a)
                connected,bip=properties(three,n,edges);assert connected
                for w,a in enumerate(c):
                    if a:
                        d=list(c);d[w]-=1;assert layers[t-1][tuple(d)][2]>>w&1;deletions+=1
                row={'c':c,'R3':three,'bipartite':bip,'critical_clear':t==gc-1 if gc else False}
                ternary.append(row)
                if not bip:failures['nonbipartite_ternary_clear_loser'].append(row)
            if not sm and t<M:
                roots=(1<<n)-1;all_win=True;rootrows=[]
                for w in range(n):
                    d=list(c);d[w]+=1;mm=layers[t+1][tuple(d)];rootrows.append(mm[0]);roots&=mm[0]
                    if mm[1]:
                        insertions+=1;assert mm[0]
                        if c[w] and not mm[1]>>w&1:failures['occupied_self_stack'].append({'c':c,'w':w})
                        if c[w] and not mm[0]>>w&1:
                            row={'c':c,'w':w};failures['occupied_self_clear'].append(row)
                            if t==gs-1:failures['critical_occupied_self_clear'].append(row)
                    else:all_win=False
                if t==gs-1:
                    assert all_win
                    row={'c':c,'AS':sum(a>1 for a in c)<=1,'Q':sum(a*a for a in c),
                         'clear_insertion_masks':rootrows,'common_clear_roots':roots}
                    critical.append(row)
                    if not roots:failures['critical_common_clear'].append(row)
    for goal,g,index in [('stack',gs,1),('clear',gc,0)]:
        if g:
            assert all(m[index] for m in layers[g].values()) and any(not m[index] for m in layers[g-1].values())
    return {'graph':name,'n':n,'edges':edges,'max_mass':M,'stack_threshold':gs,'clear_threshold':gc,
        'critical_stack':critical,'ternary_clear_losers':ternary,'failures':failures,
        'winning_insertions_checked':insertions,'occupied_deletions_checked':deletions}

def main():
    start=time.monotonic();tables=[];summaries=[]
    for name,n,edges,M,gs,gc in GRAPHS:
        arcs=[a for e in edges for a in (e,e[::-1])];layers=[];digests=[]
        for t in range(M+1):
            current={}
            for c in comps(n,t):
                occ=[v for v,a in enumerate(c) if a];pure=1<<occ[0] if len(occ)==1 else 0
                masks=[pure if t==1 else 0,pure,pure if t==2 else 0,pure if t==3 else 0]
                for u,v in arcs:
                    if c[u]>=2:
                        d=list(c);d[u]-=2;d[v]+=1;old=layers[t-1][tuple(d)]
                        masks=[a|b for a,b in zip(masks,old)]
                current[c]=masks
            assert len(current)<=300000;layers.append(current)
            digests.append(hashlib.sha256(json.dumps(sorted(current.items()),separators=(',',':')).encode()).hexdigest())
        summary=classify(name,n,edges,M,gs,gc,layers);summary['layer_hashes']=digests;summaries.append(summary)
        tables.append({'graph':name,'layers':[sorted(layer.items()) for layer in layers]})
        assert time.monotonic()-start<600
    raw=json.dumps(tables,separators=(',',':')).encode()
    out={'campaign':'CAM-S011-01','graphs':summaries,'layers':sum(len(x['layers']) for x in tables),
        'configurations':sum(len(layer) for x in tables for layer in x['layers']),
        'table_raw_sha256':hashlib.sha256(raw).hexdigest(),
        'failure_counts':{k:sum(len(g['failures'][k]) for g in summaries) for k in summaries[0]['failures']},
        'winning_insertions_checked':sum(g['winning_insertions_checked'] for g in summaries),
        'occupied_deletions_checked':sum(g['occupied_deletions_checked'] for g in summaries)}
    dest=Path('evidence/S011/tree_tables.json.xz');meta=Path('evidence/S011/tree_summary.json')
    if '--check-only' in sys.argv:assert lzma.decompress(dest.read_bytes())==raw and json.loads(meta.read_text(encoding='utf-8'))==json.loads(json.dumps(out))
    else:dest.write_bytes(lzma.compress(raw));meta.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v for k,v in out.items() if k!='graphs'}),flush=True)
    for g in summaries:print(json.dumps({'graph':g['graph'],'failures':{k:len(v) for k,v in g['failures'].items()},'first_failures':{k:v[:1] for k,v in g['failures'].items()}}),flush=True)

if __name__=='__main__':main()
