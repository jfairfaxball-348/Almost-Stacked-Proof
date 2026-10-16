import hashlib,json
from pathlib import Path
B=Path('evidence/S014/full_leaf_ascent');B.mkdir(exist_ok=True);assert not (B/'preflight.json').exists()
def write(p,t):
    p=Path(p)
    if not isinstance(t,str):t=json.dumps(t,indent=2)+'\n'
    assert not p.exists() or p.read_text(encoding='utf-8')==t,str(p)
    p.write_text(t,encoding='utf-8',newline='\n')
for suffix in ['produce','verify','run']:
    t=Path(f'tools/s014_c075_{suffix}.py').read_text(encoding='utf-8').replace('evidence/S014/leaf_ascent','evidence/S014/full_leaf_ascent').replace('s014_c075_','s014_c078_')
    if suffix=='produce':
        t=t.replace("    if not bip:out.append(dict(case=case['id'],bipartite=False));continue\n",'')
        t=t.replace("        if sum(a*e for a,e in zip(c,sign))%3:continue\n",'').replace('if a<2 or a%2:continue','if a<1:continue')
        t=t.replace("d=c.copy();d[v]-=1;d[w]+=2;y=int.from_bytes(bytes(d),'little');rows.append(dict(c=c,v=v,w=w,loses=y in S));records+=1;assert records<=1000000", "d=c.copy();d[v]-=1;d[w]+=2;y=int.from_bytes(bytes(d),'little');exception=sum(c)==2 and c[v]==c[w]==1;rows.append(dict(c=c,v=v,w=w,exception=exception,loses=y in S));records+=1;assert records<=2000000")
        t=t.replace("bipartite=True,states=len(S)","bipartite=bip,states=len(S)")
        t=t.replace("not x['loses']", "not x['loses'] and not x['exception']")
    elif suffix=='verify':
        t=t.replace("    if not bip:assert set(row)=={'case','bipartite'};continue\n",'').replace('bipcases+=1;sign=', 'bipcases+=bip;sign=')
        t=t.replace("        if sum(a*e for a,e in zip(c,sign))%3:continue\n",'').replace("if not(c[v]>0 and c[v]%2==0):continue", "if c[v]<1:continue")
        old="assert sum(d)==sum(c)+1 and sum(a*e for a,e in zip(d,sign))%3==0;expected[c,v,w]=d in S;extensions+=1;empty+=c[w]==0"
        new="assert sum(d)==sum(c)+1;exception=sum(c)==2 and c[v]==c[w]==1;expected[c,v,w]=[exception,d in S];extensions+=1;empty+=c[w]==0\n            if exception:assert d[w]==3 and sum(d)==3 and d not in S\n            if n>=3 and sum(c)==case['threshold']-1:raise AssertionError('critical leaf-neighbor positive')"
        assert old in t;t=t.replace(old,new).replace('if d not in S:fail.append','if d not in S and not exception:fail.append')
        t=t.replace(":r['loses'] for r in row['rows']", ":[r['exception'],r['loses']] for r in row['rows']")
        t=t.replace('assert extensions<=1000000','assert extensions<=2000000').replace("scope='Finite challenge only;114 written proof needed; universal ASH* OPEN'","scope='Finite all-graph challenge of117; exception is exactly two adjacent singletons; universal ASH* OPEN'")
    write(f'tools/s014_c078_{suffix}.py',t)
old=Path('evidence/S014/leaf_ascent');cfg=json.loads((old/'inputs.json').read_bytes());assert len(cfg['cases'])==142;write(B/'inputs.json',cfg);plan=Path('sessions/S014/PLAN_AMENDMENT_78.md');write(plan.with_suffix('.sha256'),hashlib.sha256(plan.read_bytes()).hexdigest()+'\n')
files=[B/'inputs.json',plan,plan.with_suffix('.sha256'),old/'inputs.json',old/'preflight.json',old/'verification.json',Path('research/S014_PRESCRIBED_SOURCE_AND_SAFE_LEAF.md'),Path('research/S014_UNIQUE_MARKERS_AND_LEAF_ESCAPE.md'),Path('research/S014_TRIVALENT_BOUNDARY_AND_BIPARTITE_PARITY.md'),Path('tools/s009_checks.py'),*Path('tools').glob('s014_c078_*.py')]
for c in cfg['cases']:files.extend([Path(c['certificate']),Path(c['summary'])])
write(B/'preflight.json',dict(files={p.as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}));print('CAM78 frozen; all142 cases, no parity filter')
