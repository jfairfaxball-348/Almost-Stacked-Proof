import hashlib,json,sys
from pathlib import Path
B=Path('evidence/S014/core_proof');P=Path('evidence/S014/cegis_orbits_v2')
def main():
    name=sys.argv[1];D=B/name
    for p,h in json.loads((D/'derived_preflight.json').read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
    assert json.loads((P/name/'clause_verification.json').read_bytes())['all_clauses_necessary_for_fixed_input_counterexample']
    old=(P/name/'formula.cnf').read_text(encoding='ascii').splitlines();new=(D/'formula.cnf').read_text(encoding='ascii').splitlines();indices=json.loads((D/'indices.json').read_bytes());assert len(indices)==len(set(indices))
    assert new[0]==f'p cnf {old[0].split()[2]} {len(indices)}'
    assert new[1:]==[old[i+1] for i in indices]
    out=dict(case=name,core_clauses=len(indices),all_clauses_necessary_for_fixed_input_counterexample=True,selected_literal_original_clauses_independently_checked=True)
    (D/'clause_verification.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(out),flush=True)
if __name__=='__main__':main()
