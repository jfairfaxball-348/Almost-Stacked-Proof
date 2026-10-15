"""CAM-S013-01: historical exact threshold predicates, no new thresholds."""
import json,lzma,sys
from pathlib import Path

def main():
    rows=[]
    for r in json.loads(Path('evidence/S003/T2b_analysis.json').read_bytes()):rows.append((r['graph'],7,r['edges'],r['analysis']['stack']['threshold'],r['analysis']['clear'].get('threshold') if isinstance(r['analysis']['clear'],dict) else None))
    for r in json.loads(lzma.decompress(Path('evidence/S003/A3_n8_analysis.json.xz').read_bytes()))['graphs']:rows.append((r[0],8,r[1],r[3][0] if isinstance(r[3],list) else None,r[4][0] if isinstance(r[4],list) else None))
    counts={'records':len(rows),'both_exact':0,'unknown_pair':0,'gap1':0,'positive_gap':0,'vertex_triangular_positive':0,'component_criterion_positive':0}
    selected=[];eligible=[]
    for name,n,es,s,c in rows:
        edges=[tuple(map(int,e.split('-'))) for e in es.split(',')];adj=[set() for _ in range(n)]
        for a,b in edges:adj[a].add(b);adj[b].add(a)
        tri=[(a,b) for a,b in edges if adj[a]&adj[b]];tv={a for e in tri for a in e}
        if s is None or c is None:counts['unknown_pair']+=1;continue
        counts['both_exact']+=1;gap=c-s;assert gap>=0
        h=[set(a) for a in adj]
        for a,b in tri:h[a].remove(b);h[b].remove(a)
        seen=set();parts=[]
        for v in range(n):
            if v in seen:continue
            comp={v};todo=[v]
            for a in todo:
                for b in h[a]-comp:comp.add(b);todo.append(b)
            seen|=comp;parts.append(sorted(comp))
        crit=all(sum(v not in tv for v in part)<=1 for part in parts)
        tags=[]
        if gap==1:counts['gap1']+=1;tags.append('gap1')
        if gap>0:counts['positive_gap']+=1
        if gap>0 and len(tv)==n:counts['vertex_triangular_positive']+=1;tags.append('all_vertices_triangular')
        if gap>0 and crit:counts['component_criterion_positive']+=1;tags.append('component_criterion')
        eligible.append([name,n,s,c,len(tv),crit])
        if tags:selected.append({'graph':name,'n':n,'edges':es,'stack':s,'clear':c,'gap':gap,'triangle_vertices':sorted(tv),'H_components':parts,'tags':tags})
    out={'counts':counts,'eligible':eligible,'selected':selected,'assurance':'Historical computed exact thresholds only; no fresh reachability or universal inference.'}
    b=(json.dumps(out,separators=(',',':'))+'\n').encode();p=Path('evidence/S013/gap_scan.json')
    if '--check-only' in sys.argv:assert p.read_bytes()==b
    else:p.write_bytes(b)
    print(json.dumps(counts));print(json.dumps(selected[:3]))

if __name__=='__main__':main()
