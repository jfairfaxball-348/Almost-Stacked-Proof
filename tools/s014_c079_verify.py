import hashlib,json,lzma,struct,time
from pathlib import Path
B=Path('evidence/S014/source_first');start=time.monotonic()
for pre in [B/'preflight.json',B/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
cfg=json.loads((B/'inputs.json').read_bytes())['cases'];saved=json.loads((B/'result.json').read_bytes());assert len(cfg)==len(saved['cases'])==142
states=preds=tests=failures=rowsall=heavies=threeall=0
for case,row in zip(cfg,saved['cases']):
    assert case['id']==row['case'];n=case['n'];arcs=sorted((u,v) for u in range(n) for v in range(n) if [u,v] in case['edges'] or [v,u] in case['edges']);assert len(arcs)==2*len(case['edges']);S=set()
    with lzma.open(case['certificate'],'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);assert count<=1000000
            for _ in range(count):z=f.read(16);assert len(z)==16 and not any(z[n:]) and sum(z[:n])==mass;S.add(tuple(z[:n]))
    states+=len(S);assert len(S)==row['states'] and states<=2000000;C=set()
    for x in S:
        for u,v in arcs:
            if x[v]:C.add(tuple(a+2*int(i==u)-int(i==v) for i,a in enumerate(x)))
        assert len(C)<=2000000 and time.monotonic()-start<540
    preds+=len(C);assert len(C)==row['predecessors'] and preds<=5000000;actual={}
    with lzma.open(row['file'],'rb') as f:
        while raw:=f.read(24):
            assert len(raw)==24 and not any(raw[n:16]);c=tuple(raw[:n]);assert c not in actual;actual[c]=struct.unpack('<Q',raw[16:])[0]
    expected={c for c in C-S if sum(a>0 for a in c)>=2};assert set(actual)==expected;heavy=failed=terminal=three=0
    for c in C-S:
        if sum(a>0 for a in c)==1:terminal+=1;three+=sum(c)==3;continue
        assert sum(c)<=case['threshold'];mask=0
        for j,(u,v) in enumerate(arcs):
            if c[u]>=2:
                child=tuple(a-2*int(i==u)+int(i==v) for i,a in enumerate(c));tests+=1
                if child not in S:mask|=1<<j
        assert mask==actual[c]
        for u,a in enumerate(c):
            if a<2:continue
            heavy+=1
            if all(not(mask&(1<<j)) for j,(v,w) in enumerate(arcs) if v==u):failed+=1
        assert tests<=20000000 and time.monotonic()-start<540
    assert len(expected)==row['winning_multioccupied'] and heavy==row['heavy_sources'] and failed==row['failed_sources'] and terminal==row['terminal_predecessors'] and three==row['pure3_predecessors'];failures+=failed;rowsall+=len(expected);heavies+=heavy;threeall+=three
assert states==saved['states'] and preds==saved['predecessors'] and tests==saved['child_tests'] and failures==saved['failed_sources']
out=dict(complete_predecessor_inventory_and_all_child_masks_equal=True,cases=142,states=states,predecessors=preds,winning_multioccupied_inputs=rowsall,heavy_sources=heavies,child_tests=tests,pure3_terminal_predecessors=threeall,failed_sources=failures,scope='Complete source-first challenge on precisely142 old graphs;116 symbolic proof separate; universal ASH* OPEN',seconds=time.monotonic()-start)
(B/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
