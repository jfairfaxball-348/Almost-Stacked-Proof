"""Freeze separate fair-selector continuation; never edits old evidence."""
import hashlib,json,os
from pathlib import Path
B=Path('evidence/S014/fair_cegis');B.mkdir(exist_ok=True);cases=[];files=[]
oldcfg=json.loads(Path('evidence/S014/master_cegis/inputs.json').read_bytes())
spec=[(2,4,None),(8,10,'even_cegis/E8'),(9,11,'master_cegis/N9_M11'),(10,12,'master_cegis/N10_M12'),(10,17,'master_cegis/N10_M17'),(12,13,'master_cegis/N12_M13'),(12,16,'master_cegis/N12_M16')]
import itertools
def partitions(total,slots,largest):
    if not slots:
        if not total:yield ()
        return
    for first in range(min(total,largest),-1,-1):
        if total-first>(slots-1)*first:continue
        for rest in partitions(total-first,slots-1,first):yield (first,)+rest
for n,M,source in spec:
    patterns=[list(p) for p in partitions(M,n,M) if sum(x>=2 for x in p)>=2];patterns.sort(key=lambda p:(sum(x>=2 for x in p),sum(x>=2 and x%2==0 for x in p),max(p)-min(x for x in p if x>=2),tuple(p)));name=f'N{n}_M{M}';D=B/name;D.mkdir(exist_ok=True);imports=[]
    if source:
        old=Path('evidence/S014')/source;v=json.loads((old/'clause_verification.json').read_bytes());assert v.get('all_graph_clauses_necessary') or v.get('counterexample_exists_implies_formula_satisfiable') or v.get('all_clauses_necessary_for_fixed_input_counterexample')
        if n==8:
            oc=next(c for c in json.loads((old.parent/'inputs.json').read_bytes())['cases'] if c['id']=='E8');order=sorted(range(n),key=lambda i:(-oc['c'][i],i));mapping={v:i for i,v in enumerate(order)};idx=patterns.index([oc['c'][i] for i in order]);edges=list(itertools.combinations(range(n),2));vid={e:i+1 for i,e in enumerate(edges)};selector=len(edges)+1+idx
        else:assert patterns==next(c for c in oldcfg['cases'] if c['id']==name)['patterns']
        for line in (old/'constraints.jsonl').read_text(encoding='utf-8').splitlines():
            r=json.loads(line)
            if n==8 and r['kind']=='c_win':r['pattern']=idx;r['moves']=[[mapping[u],mapping[v]] for u,v in r['moves']];r['clause']=sorted({-selector}|{-vid[tuple(sorted(e))] for e in r['moves']})
            if r['kind']=='AS_loss':r['certificate']=Path(os.path.relpath((old/r['certificate']).resolve(),D)).as_posix()
            imports.append(r)
        files.extend(p for p in old.rglob('*') if p.is_file());files.append(old.parent/'inputs.json')
    dest=D/'imports.jsonl';dest.write_text(''.join(json.dumps(r,separators=(',',':'))+'\n' for r in imports),encoding='utf-8',newline='\n');files.append(dest);cases.append(dict(id=name,n=n,mass=M,patterns=patterns,control=n==2,source=source))
cfg=dict(cases=cases,runtime=oldcfg['runtime']);(B/'inputs.json').write_text(json.dumps(cfg,indent=2)+'\n',encoding='utf-8',newline='\n');(B/'control_inputs.json').write_text(json.dumps(dict(cases=cases[:1],runtime=cfg['runtime']),indent=2)+'\n',encoding='utf-8',newline='\n')
plan=Path('sessions/S014/PLAN_AMENDMENT_51.md');plan.with_suffix('.sha256').write_text(hashlib.sha256(plan.read_bytes()).hexdigest()+'\n',encoding='ascii',newline='\n');files.extend([plan,plan.with_suffix('.sha256'),B/'inputs.json',B/'control_inputs.json',Path('research/S014_FAIR_SELECTOR_CERTIFICATION.md'),Path('research/S014_SHARED_INPUT_REDUCTION.md'),Path('research/S014_PROVED_GRAPH_SYMMETRY.md'),Path('tools/s014_master_encoding.py'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_fair*.py')])
pre=dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files},native_binary='C:/Earth-Moon-problem/artifacts/tmp/S004/drat-trim-mingw.exe',native_sha256='970caaea97a15c8a27d4747e0e92e058ac1b1d9d4e04a95e3fc58b069ed4c03e');(B/'preflight.json').write_text(json.dumps(pre,indent=2)+'\n',encoding='utf-8',newline='\n');(B/'control_preflight.json').write_text(json.dumps(pre,indent=2)+'\n',encoding='utf-8',newline='\n');print('CAM51 frozen',[(c['id'],len(c['patterns'])) for c in cases])
