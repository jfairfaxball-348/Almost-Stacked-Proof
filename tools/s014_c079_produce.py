import hashlib,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/source_first');start=time.monotonic()
for p,h in json.loads((B/'preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
out=[];states=preds=tests=failures=0
for case in json.loads((B/'inputs.json').read_bytes())['cases']:
    n=case['n'];unit=[1<<(8*i) for i in range(n)];arcs=sorted([*map(tuple,case['edges']),*((v,u) for u,v in case['edges'])]);S=set()
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);assert count<=1000000
            for _ in range(count):z=f.read(16);assert len(z)==16;S.add(int.from_bytes(z,'little'))
    states+=len(S);assert states<=2000000;C=set()
    for x in S:
        for u,v in arcs:
            if (x>>(8*v))&255:C.add(x+2*unit[u]-unit[v])
        assert len(C)<=2000000 and time.monotonic()-start<540
    preds+=len(C);assert preds<=5000000;rows=heavy=failed=terminal=three=0;examples=[];file=B/(case['id']+'.bin.xz');file.parent.mkdir(parents=True,exist_ok=True)
    with lzma.open(file,'wb') as f:
        for c in sorted(C-S):
            counts=[(c>>(8*u))&255 for u in range(n)]
            if sum(a>0 for a in counts)==1:terminal+=1;three+=sum(counts)==3;continue
            mask=0
            for j,(u,v) in enumerate(arcs):
                if counts[u]>=2:
                    tests+=1
                    if c-2*unit[u]+unit[v] not in S:mask|=1<<j
            for u,a in enumerate(counts):
                if a<2:continue
                heavy+=1
                if not any(mask&(1<<j) for j,(v,w) in enumerate(arcs) if v==u):
                    failed+=1
                    if len(examples)<3:examples.append(dict(c=counts,u=u))
            f.write(c.to_bytes(16,'little')+struct.pack('<Q',mask));rows+=1
            assert tests<=20000000 and time.monotonic()-start<540
    failures+=failed;out.append(dict(case=case['id'],states=len(S),predecessors=len(C),winning_multioccupied=rows,heavy_sources=heavy,failed_sources=failed,terminal_predecessors=terminal,pure3_predecessors=three,examples=examples,file=file.as_posix()))
(B/'result.json').write_text(json.dumps(dict(cases=out,states=states,predecessors=preds,child_tests=tests,failed_sources=failures),indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(cases=len(out),states=states,predecessors=preds,child_tests=tests,failed_sources=failures)))
