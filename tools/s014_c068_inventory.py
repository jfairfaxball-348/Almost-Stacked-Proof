"""Independent full labeled weak-composition inventory and import provenance."""
import hashlib,json,os
from pathlib import Path
B=Path('evidence/S014/mass11_cegis');cfg=json.loads((B/'inputs.json').read_bytes());provided=[tuple(c['c']) for c in cfg['cases'] if not c['control']];complete=set();labeled=0
def rec(prefix,left,sites):
    global labeled
    if sites==1:
        c=prefix+[left];labeled+=1
        if sum(z>1 for z in c)>1:complete.add(tuple(sorted(c)))
        return
    for z in range(left+1):rec(prefix+[z],left-z,sites-1)
rec([],11,8);assert provided==sorted(complete) and len(provided)==len(set(provided)) and len(provided)<=256
D=B/'imported';records=(D/'constraints.jsonl').read_text(encoding='utf-8').splitlines();provenance=json.loads((D/'provenance.json').read_bytes());assert len(records)==len(provenance);AS=cuts=0
for line,origin in zip(records,provenance):
    source=Path(origin['source']);raw=source.read_text(encoding='utf-8').splitlines()[origin['line']-1];assert hashlib.sha256(raw.encode()).hexdigest()==origin['record_sha256'];r=json.loads(line);old=json.loads(raw)
    if r['kind']=='AS_loss':
        assert 11<=sum(r['input'])<=13 and (D/r['certificate']).resolve()==(source.parent/old['certificate']).resolve();r.pop('certificate');old.pop('certificate');AS+=1
    else:assert r['kind']=='cut';cuts+=1
    assert r==old
report=dict(whole_sorted_mass11_order8_inventory_equal=True,patterns=len(provided),labeled_compositions=labeled,AS_loss_imports=AS,connected_cut_imports=cuts,no_other_input_winning_records_imported=True)
(B/'inventory_verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(report))
