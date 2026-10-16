"""Separate base-certificate replay and literal permutation expansion validation."""
import hashlib,itertools,json,struct,sys
from pathlib import Path
import s014_cegis_clauses_verify as basecheck
B=Path('evidence/S014/cegis_orbits')
def main():
    D=B/sys.argv[1]
    for p,h in json.loads((D/'derived_preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    basecheck.B=D/'base';basecheck.main()
    case=next(c for c in json.loads((B/'inputs.json').read_bytes())['cases'] if c['id']==sys.argv[1]);n=case['n'];perms=case['permutations'];edges=list(itertools.combinations(range(n),2));var={frozenset(e):i+1 for i,e in enumerate(edges)}
    assert len({tuple(p) for p in perms})==len(perms)
    for p in perms:assert sorted(p)==list(range(n)) and all(case['c'][i]==case['c'][p[i]] for i in range(n))
    rows=[json.loads(line) for line in (D/'constraints.jsonl').read_text(encoding='utf-8').splitlines()]
    br=[json.loads(line) for line in (D/'base'/case['id']/'constraints.jsonl').read_text(encoding='utf-8').splitlines()]
    assert len(rows)==len(br)
    for a,b in zip(rows,br):
        ac=a.copy();bc=b.copy()
        if a['kind']=='AS_loss':
            assert (D/a['certificate']).resolve()==(D/'base'/case['id']/b['certificate']).resolve();ac.pop('certificate');bc.pop('certificate')
        assert ac==bc
    lines=(D/'formula.cnf').read_text(encoding='ascii').splitlines();source=(D/'clause_sources.bin').read_bytes();assert len(source)==8*(len(lines)-1)
    assert lines[0]==f'p cnf {len(edges)} {len(lines)-1}'
    for k,line in enumerate(lines[1:]):
        i,j=struct.unpack_from('<II',source,k*8);assert i<len(rows) and j<len(perms);p=perms[j];expected=[]
        for x in rows[i]['clause']:
            u,v=edges[abs(x)-1];value=var[frozenset([p[u],p[v]])];expected.append(value if x>0 else -value)
        assert line==' '.join(map(str,sorted(expected)))+' 0'
    out=dict(case=case['id'],base_clauses=len(rows),stabilizer_size=len(perms),expanded_clauses=len(lines)-1,all_clauses_necessary_for_fixed_input_counterexample=True,scope='Only fixed input graph class, independent literal clause provenance')
    (D/'clause_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
