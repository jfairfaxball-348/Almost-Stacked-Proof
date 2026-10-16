import hashlib,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/odd_leaf_contraction');start=time.monotonic()
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
out=[];states=records=failures=0;counts=[0,0,0]
for case in json.loads((B/'inputs.json').read_bytes())['cases']:
    n=case['n'];adj=[[] for _ in range(n)];unit=[1<<(8*i) for i in range(n)]
    for u,v in case['edges']:adj[u].append(v);adj[v].append(u)
    S=set()
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);assert count<=1000000
            for _ in range(count):z=f.read(16);assert len(z)==16;S.add(int.from_bytes(z,'little'))
    states+=len(S);assert states<=2000000;rows=[];bad=critical=0
    for x in sorted(S):
        c=list(x.to_bytes(16,'little')[:n])
        for w in range(n):
            if len(adj[w])!=1:continue
            v=adj[w][0];targets=[]
            if c[w]%2 and c[v]>=2:targets.append((0,x-unit[w]-unit[v]))
            if c[w]%2==0 and c[v]>=1:targets.append((1,x+unit[w]+unit[v]))
            if c[w]>=2 and c[w]%2==0:
                targets.append((2,x+3*unit[w]));critical+=sum(c)==case['threshold']-1
            for kind,y in targets:rows.append([c,w,kind,y in S]);counts[kind]+=1;bad+=y not in S;records+=1
        assert records<=2000000 and time.monotonic()-start<540
    file=B/(case['id']+'.json.xz');file.parent.mkdir(parents=True,exist_ok=True);file.write_bytes(lzma.compress(json.dumps(rows,separators=(',',':')).encode()));out.append(dict(case=case['id'],states=len(S),records=len(rows),failed_memberships=bad,critical_even_leafs=critical,file=file.as_posix()));failures+=bad
(B/'result.json').write_text(json.dumps(dict(cases=out,states=states,records=records,direction_counts=counts,failed_memberships=failures),indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(cases=len(out),states=states,records=records,direction_counts=counts,failed_memberships=failures)))
