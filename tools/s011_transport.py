"""CAM-S011-02 exact count/terminal-support certificates, no chronological solver."""
import hashlib,json,lzma,sys,time
from pathlib import Path

EDGES={'K2':[(0,1)],'P3':[(0,1),(0,2)],'K3':[(0,1),(0,2),(1,2)],
 'triangle_leaf':[(0,1),(0,2),(1,2),(0,3)],'bowtie':[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)],
 'diamond':[(0,1),(0,2),(0,3),(1,2),(2,3)],'C5':[(0,1),(1,2),(2,3),(3,4),(0,4)]}

def path(arcs,m,start,end):
    queue=[start];paths={start:[]}
    for u in queue:
        if u==end:return paths[u]
        for j,(a,b) in enumerate(arcs):
            if a==u and m[j] and b not in paths:paths[b]=paths[u]+[j];queue.append(b)
    raise AssertionError((start,end,m))

def check(c,f,m,arcs):
    value=f.copy();used={v for v,a in enumerate(c) if a}|{v for v,a in enumerate(f) if a};rev={v:[] for v in range(len(c))}
    for j,(u,v) in enumerate(arcs):
        assert m[j]>=0
        if m[j]:used|={u,v};rev[v].append(u)
        value[u]+=2*m[j];value[v]-=m[j]
    assert value==list(c) and sum(f)>0 and min(f)>=0
    seen={v for v,a in enumerate(f) if a};queue=sorted(seen)
    for v in queue:
        for u in rev[v]:
            if u not in seen:seen.add(u);queue.append(u)
    assert used<=seen

def derive(index,source):
    name=source['graph'];edges=EDGES[name];arcs=[a for e in edges for a in (e,e[::-1])]
    d=source['c'];n=len(d);m=source['m'];q=source['q'];k=source['k'];rows=[]
    def reverse(start):
        P=path(arcs,m,start,q);mm=m.copy()
        for j in P:mm[j]-=1;mm[j^1]+=1
        return mm,P
    def add(key,c,f,mm,P):
        check(c,f,mm,arcs);rows.append({'key':[index]+key,'graph':name,'c':c,'f':f,'m':mm,'path':P})
    if k==3:
        used={q}|{v for v,a in enumerate(d) if a}
        for j,(u,v) in enumerate(arcs):
            if m[j]:used|={u,v}
        for w in sorted(used):
            mm,P=reverse(w);f=[0]*n;f[w]=3;add(['root',w],d,f,mm,P)
        for j,(u,v) in enumerate(arcs):
            if m[j]:
                mm,P=reverse(v);assert mm[j];mm[j]-=1;f=[0]*n;f[u]=f[v]=2;add(['edge',j],d,f,mm,P)
    for j,(s,t) in enumerate(arcs):
        if s!=q:continue
        for a in (1,2):
            if d[t]<a or k+a<3:continue
            c=d.copy();c[s]+=a;c[t]-=a;mm,P=reverse(t);f=[0]*n;f[s]=k+a-3;f[t]=3-a
            add(['exchange',t,a],c,f,mm,P)
    return rows

def main():
    start=time.monotonic();sources=json.loads(lzma.decompress(Path('evidence/S010/count_traces.json.xz').read_bytes()))
    explicit={'graph':'C5','c':[4,1,1,1,1],'m':[1,0,1,0,1,0,1,0,0,1],'q':0,'k':3}
    sources.append(explicit);rows=[]
    for i,source in enumerate(sources):rows.extend(derive(i,source))
    pergraph={name:sum(r['graph']==name for r in rows) for name in EDGES};assert max(pergraph.values())<=300000
    summary=json.loads(Path('evidence/S011/tree_summary.json').read_text(encoding='utf-8'))
    tables=json.loads(lzma.decompress(Path('evidence/S011/tree_tables.json.xz').read_bytes()));cuts=[]
    for meta,table in zip(summary['graphs'],tables):
        gs,gc=meta['stack_threshold'],meta['clear_threshold']
        if gc is None or gc<gs+2:continue
        n=meta['n'];edges=meta['edges'];adj={u:{v for a,b in edges for v in ([b] if a==u else ([a] if b==u else []))} for u in range(n)}
        triangular={u for u in range(n) for v in adj[u] if adj[u]&adj[v]}
        for c,masks in table['layers'][gc-1]:
            if masks[0]==0:
                assert all(c[v]<=1 for v in triangular)
                cuts.append({'graph':meta['graph'],'c':c,'triangular_vertices':sorted(triangular)})
    raw=json.dumps(rows,separators=(',',':')).encode()
    out={'campaign':'CAM-S011-02','certificates':len(rows),'per_graph':pergraph,'roots':sum(r['key'][1]=='root' for r in rows),
        'edges':sum(r['key'][1]=='edge' for r in rows),'exchanges':sum(r['key'][1]=='exchange' for r in rows),
        'table_raw_sha256':hashlib.sha256(raw).hexdigest(),'critical_clear_cuts':cuts,'explicit_C5':explicit}
    assert time.monotonic()-start<600
    dest=Path('evidence/S011/transport_certificates.json.xz');mp=Path('evidence/S011/transport_summary.json')
    if '--check-only' in sys.argv:assert lzma.decompress(dest.read_bytes())==raw and json.loads(mp.read_text(encoding='utf-8'))==out
    else:dest.write_bytes(lzma.compress(raw));mp.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:v if k!='critical_clear_cuts' else len(v) for k,v in out.items() if k!='explicit_C5'}),flush=True)

if __name__=='__main__':main()
