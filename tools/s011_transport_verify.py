"""Independent complete fixed-count chronology and unrestricted closure checks."""
import hashlib,json,lzma,sys,time
from functools import lru_cache
from pathlib import Path

GRAPHS={'K2':[(0,1)],'P3':[(0,1),(0,2)],'K3':[(0,1),(0,2),(1,2)],
 'triangle_leaf':[(0,1),(0,2),(1,2),(0,3)],'bowtie':[(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)],
 'diamond':[(0,1),(0,2),(0,3),(1,2),(2,3)],'C5':[(0,1),(1,2),(2,3),(3,4),(0,4)]}

def chronology(c,f,m,arcs):
    @lru_cache(None)
    def search(rem):
        state=list(c)
        for (u,v),total,left in zip(arcs,m,rem):state[u]-=2*(total-left);state[v]+=total-left
        if not any(rem):return () if state==f else None
        for i,(u,v) in enumerate(arcs):
            if rem[i] and state[u]>=2:
                rest=list(rem);rest[i]-=1;tail=search(tuple(rest))
                if tail is not None:return (i,)+tail
        return None
    trace=search(tuple(m));assert search.cache_info().currsize<=300000
    assert trace is not None
    return trace

def closure(c,arcs):
    seen={tuple(c)};todo=[tuple(c)];clear=three=0
    for x in todo:
        occupied=[v for v,a in enumerate(x) if a]
        if len(occupied)==1:
            if sum(x)==1:clear|=1<<occupied[0]
            if sum(x)==3:three|=1<<occupied[0]
        for u,v in arcs:
            if x[u]>=2:
                y=list(x);y[u]-=2;y[v]+=1;y=tuple(y)
                if y not in seen:seen.add(y);todo.append(y)
        assert len(seen)<=300000
    return seen,clear,three

def main():
    start=time.monotonic();raw=lzma.decompress(Path('evidence/S011/transport_certificates.json.xz').read_bytes());certs=json.loads(raw)
    meta=json.loads(Path('evidence/S011/transport_summary.json').read_text(encoding='utf-8'));assert hashlib.sha256(raw).hexdigest()==meta['table_raw_sha256']
    sources=json.loads(lzma.decompress(Path('evidence/S010/count_traces.json.xz').read_bytes()))
    sources.append({'graph':'C5','c':[4,1,1,1,1],'m':[1,0,1,0,1,0,1,0,0,1],'q':0,'k':3})
    expected=set()
    for i,s in enumerate(sources):
        arcs=[a for e in GRAPHS[s['graph']] for a in (e,tuple(reversed(e)))];used={s['q']}|{v for v,a in enumerate(s['c']) if a}
        for j,(u,v) in enumerate(arcs):
            if s['m'][j]:used|={u,v}
        if s['k']==3:
            expected.update((i,'root',w) for w in used)
            expected.update((i,'edge',j) for j,a in enumerate(s['m']) if a)
        for u,v in arcs:
            if u==s['q']:
                for a in (1,2):
                    if s['c'][v]>=a and s['k']+a>=3:expected.add((i,'exchange',v,a))
    assert expected=={tuple(r['key']) for r in certs} and len(expected)==len(certs)
    traces=[];repairs=[];pair_checked=exception=0;closure_cache={}
    for r in certs:
        key=r['key'];s=sources[key[0]];assert r['graph']==s['graph'];edges=GRAPHS[r['graph']];arcs=[a for e in edges for a in (e,e[::-1])]
        n=len(s['c']);c=s['c'].copy();f=[0]*n;mm=s['m'].copy();at=key[2] if key[1]=='root' else (arcs[key[2]][1] if key[1]=='edge' else key[2]);visited={at}
        for j in r['path']:
            u,v=arcs[j];assert u==at and mm[j]>0 and v not in visited;visited.add(v);at=v;mm[j]-=1;mm[j^1]+=1
        assert at==s['q']
        if key[1]=='root':f[key[2]]=3
        elif key[1]=='edge':
            j=key[2];u,v=arcs[j];assert s['m'][j]>0 and mm[j]>0;mm[j]-=1;f[u]=f[v]=2
        else:
            t,a=key[2:];q=s['q'];c[q]+=a;c[t]-=a;f[q]=s['k']+a-3;f[t]=3-a
        assert c==r['c'] and f==r['f'] and mm==r['m'] and min(c)>=0
        trace=chronology(c,f,mm,arcs);state=c.copy();counts=[0]*len(mm)
        for j in trace:
            u,v=arcs[j];assert state[u]>=2;state[u]-=2;state[v]+=1;counts[j]+=1
        assert state==f and counts==mm
        traces.append({'key':key,'graph':r['graph'],'c':c,'f':f,'arc_indices':trace})
        if key[1]=='exchange':
            occupied=[v for v,a in enumerate(f) if a];pairarcs=[(s['q'],key[2]),(key[2],s['q'])]
            seen,_,_=closure(f,pairarcs);stack=any(sum(a>0 for a in x)==1 for x in seen)
            if key[3]==2 and s['k']==2:assert not stack;exception+=1
            else:assert stack
            pair_checked+=1
        if key[1]=='edge':
            u,v=arcs[key[2]];common=[z for z in range(n) if (u,z) in arcs and (v,z) in arcs]
            if common:
                z=common[0];moves=[(u,z),(v,z),(z,u)];state=f.copy()
                for a,b in moves:assert state[a]>=2;state[a]-=2;state[b]+=1
                assert state==[1 if w==u else 0 for w in range(n)]
                repairs.append({'key':key,'moves':moves,'final':state})
        assert time.monotonic()-start<600
    # Explicit whole odd-cycle3 support remains a CLEAR loser.
    c=[4,1,1,1,1];arcs=[a for e in GRAPHS['C5'] for a in (e,e[::-1])]
    cc,clear,three=closure(c,arcs);assert clear==0 and three==31
    c5={'graph':'C5','c':c,'clear_mask':clear,'three_mask':three,'closure':sorted(cc),
        'three_trace':chronology(c,[3,0,0,0,0],sources[-1]['m'],arcs)}
    tables=json.loads(lzma.decompress(Path('evidence/S011/tree_tables.json.xz').read_bytes()));sm=json.loads(Path('evidence/S011/tree_summary.json').read_text(encoding='utf-8'));cuts=[]
    for g,tab in zip(sm['graphs'],tables):
        gs,gc=g['stack_threshold'],g['clear_threshold']
        if gc is None or gc-gs<2:continue
        n=g['n'];edges=[tuple(e) for e in g['edges']];arcs=[a for e in edges for a in (e,e[::-1])]
        tri={u for u,v in arcs if any((u,z) in arcs and (v,z) in arcs for z in range(n))}
        prior={tuple(c):m for c,m in tab['layers'][gc-2]}
        for c,mask in tab['layers'][gc-1]:
            if mask[0]:continue
            assert all(c[v]<=1 for v in tri)
            for u,v in arcs:
                if c[u]>=2:
                    d=c.copy();d[u]-=2;d[v]+=1;assert prior[tuple(d)][1]
            cuts.append({'graph':g['graph'],'c':c,'triangular_vertices':sorted(tri)})
    assert cuts==meta['critical_clear_cuts']
    tr=json.dumps(traces,separators=(',',':')).encode();rp=json.dumps(repairs,separators=(',',':')).encode()
    out={'campaign':'CAM-S011-02','all_verified':True,'certificates':len(certs),'literal_moves':sum(len(x['arc_indices']) for x in traces),
        'adjacent_pair_checks':pair_checked,'exceptional_two_singletons':exception,'triangular_repairs':len(repairs),'critical_clear_cuts':len(cuts),
        'trace_raw_sha256':hashlib.sha256(tr).hexdigest(),'repair_raw_sha256':hashlib.sha256(rp).hexdigest(),'C5_closure_states':len(cc)}
    values={'transport_verification.json':out,'odd_cycle_failure.json':c5};compressed={'transport_traces.json.xz':tr,'triangle_repairs.json.xz':rp}
    for name,obj in values.items():
        p=Path('evidence/S011')/name
        if '--check-only' in sys.argv:assert json.loads(p.read_text(encoding='utf-8'))==json.loads(json.dumps(obj))
        else:p.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8',newline='\n')
    for name,data in compressed.items():
        p=Path('evidence/S011')/name
        if '--check-only' in sys.argv:assert lzma.decompress(p.read_bytes())==data
        else:p.write_bytes(lzma.compress(data))
    print(json.dumps(out),flush=True)

if __name__=='__main__':main()
