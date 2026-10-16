import hashlib,json,sys
from pathlib import Path
B=Path('evidence/S014/cube_pointwise');shard=int(sys.argv[1]);D=B/f'shard{shard}'
for pre in [B/'preflight.json',D/'derived_preflight.json']:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
assert (B/'inputs.json').read_bytes()==Path('evidence/S014/cube_general/inputs.json').read_bytes();cfg=json.loads((B/'inputs.json').read_bytes());selected=[c for c in cfg['candidates'] if c['id']%2==shard];rows=json.loads((D/'results.json').read_bytes());summary=json.loads((D/'result.json').read_bytes());assert len(rows)==summary['completed']<=len(selected) and sum(r['states'] for r in rows)==summary['cumulative_states']<=8000000;positives=unknown=moves=partialstates=0;potential=[]
for c,r in zip(selected,rows):
    assert c['id']==r['id'] and r['states']<=300000 and sum(c['c'])==c['mass'] and c['mass'] in [31,32,33]
    if r['winning'] is True:
        x=list(c['c']);assert len(r['moves'])<=100
        for code in r['moves']:u,v=divmod(code,16);assert 0<=u<16 and 0<=v<16 and (u^v).bit_count()==1 and x[u]>=2;x[u]-=2;x[v]+=1;moves+=1
        assert sum(z>0 for z in x)==1;positives+=1
    else:
        location=Path(r.get('partial',r.get('potential_certificate')));assert location.is_relative_to(D) and location.is_dir();data=json.loads((location/'result.json').read_bytes());local=json.loads((location/'inputs.json').read_bytes())['candidates'][0];assert local['c']==c['c'] and local['original_id']==c['id'] and local['id']==0;assert data['states']==r['states'];partialstates+=r['states']
        if r['winning'] is None:unknown+=1;assert r['status'] in ['QUERY_STATE_CAP_UNKNOWN','AGGREGATE_STATE_CAP_UNKNOWN','TIME_BOUND_UNKNOWN']
        else:potential.append(dict(case=c,path=location.as_posix()))
assert len(potential)<=1 and positives==summary['winning'] and unknown==summary['unknown'] and partialstates==summary['retained_partial_states']<=2000000
out=dict(shard=shard,status=summary['status'],candidate_prefix_checked=len(rows),literal_full_input_winners=positives,literal_moves=moves,unknown=unknown,potential=potential,all_positive_histories_verified=True,partial_states_retained_without_mathematical_promotion=partialstates,scope='Only pointwise winners, unknown suffix explicit; negative potential needs separate full DAG replay, no full threshold')
(D/'verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out))
