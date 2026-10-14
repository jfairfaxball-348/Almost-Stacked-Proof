"""Preregistered all-parent C++ campaign; full 128-bit layers compressed intact."""
import json,lzma,subprocess,itertools,time,sys,hashlib,platform
from pathlib import Path

OUT=Path('evidence/S005');OUT.mkdir(exist_ok=True)
def jobs():
    atlas=json.loads(Path('evidence/S003/T2_analysis.json').read_text())
    for r in atlas:
        n=r['n']
        if n<2:continue
        e=[tuple(map(int,p.split('-'))) for p in r['edges'].split(',')]
        for mode in ['stack','clear']:
            if mode=='clear' and r['analysis']['bipartite']:continue
            yield r['graph'],n,e,mode,200,120
    gs=[r for r in json.loads(Path('evidence/S003/T2b_analysis.json').read_text()) if 7<=len(r['edges'].split(','))<=9][:24]
    for r in gs:
        e=[tuple(map(int,p.split('-'))) for p in r['edges'].split(',')]
        for mode in ['stack','clear']:
            if mode=='clear' and r['analysis']['bipartite']:continue
            yield r['graph'],7,e,mode,200,120
    old=json.loads(lzma.decompress(Path('evidence/S003/A3_n8_analysis.json.xz').read_bytes()))['graphs']
    selected=[]
    for r in old:
        e=[tuple(map(int,p.split('-'))) for p in r[1].split(',')]
        modes=[m for i,m in [(3,'stack'),(4,'clear')] if isinstance(r[i],list) and r[i][0] is None]
        if modes:selected.append((r[0],8,e,modes))
        if len(selected)==20:break
    for name,n,e,modes in selected:
        for mode in modes:yield name,n,e,mode,200,120
    named=[('C10',10,[(i,(i+1)%10) for i in range(10)],['stack'],70),
    ('triangle_tail5',8,[(0,1),(1,2),(0,2)]+[(i,i+1) for i in range(2,7)],['clear'],200),
    ('triangle_tail4',7,[(0,1),(1,2),(0,2)]+[(i,i+1) for i in range(2,6)],['stack','clear'],200),
    ('triangle_tail6',9,[(0,1),(1,2),(0,2)]+[(i,i+1) for i in range(2,8)],['stack','clear'],250),
    ('C5_tail3',8,[(i,(i+1)%5) for i in range(5)]+[(4,5),(5,6),(6,7)],['stack','clear'],200),
    ('two_triangles_path4',9,[(0,1),(1,2),(0,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(6,8)],['stack','clear'],200),
    ('C8_leaf',9,[(i,(i+1)%8) for i in range(8)]+[(7,8)],['stack','clear'],200)]
    for name,n,e,modes,cap in named:
        for mode in modes:yield name,n,e,mode,cap,180

def main():
    alljobs=list(jobs());(OUT/'graphs.json').write_text(json.dumps([dict(zip(['graph','n','edges','mode','cap','seconds_cap'],j)) for j in alljobs],indent=2)+'\n')
    start=time.monotonic();results=[]
    for name,n,e,mode,cap,secs in alljobs:
        base=OUT/(name+'_'+mode)
        if time.monotonic()-start>3600:break
        if base.with_suffix('.summary.json').exists() and base.with_suffix('.bin.xz').exists():
            try:
                d=json.loads(base.with_suffix('.summary.json').read_text())
                if 'certificate_sha256' in d:results.append(d);continue
            except json.JSONDecodeError:pass
        cmd=['/tmp/s005_sparse',name,str(n),','.join(f'{u}-{v}' for u,v in e),mode,str(cap),str(secs),str(base.with_suffix('.bin')),str(base.with_suffix('.summary.json'))]
        subprocess.run(cmd,check=True,timeout=secs+120)
        p=base.with_suffix('.bin');raw=p.read_bytes();base.with_suffix('.bin.xz').write_bytes(lzma.compress(raw));p.unlink()
        d=json.loads(base.with_suffix('.summary.json').read_text());d.update(edges=e,certificate_sha256=hashlib.sha256(raw).hexdigest());base.with_suffix('.summary.json').write_text(json.dumps(d,indent=2)+'\n');results.append(d)
    (OUT/'campaign_summary.json').write_text(json.dumps(results,indent=2)+'\n')
    (OUT/'environment.json').write_text(json.dumps({'python':sys.version,'platform':platform.platform(),'seconds':time.monotonic()-start},indent=2)+'\n')
if __name__=='__main__':main()
