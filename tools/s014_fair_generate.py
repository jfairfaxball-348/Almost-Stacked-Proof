"""Derive a separate bounded scheduler without changing any frozen producer."""
from pathlib import Path
def save(name,t):Path('tools/'+name+'.py').write_text(t,encoding='utf-8',newline='\n')
def one(t,a,b):assert t.count(a)==1,a;return t.replace(a,b)
t=Path('tools/s014_master_cegis.py').read_text(encoding='utf-8').replace('evidence/S014/master_cegis','evidence/S014/fair_cegis')
t=one(t,"c=patterns[0]","c=patterns[0];closed=set();cursor=0;visits=[0]*len(patterns);conditional_unsat=[]")
a="""                preferred=selectors[(iteration-1)%len(selectors)];sat.set_phases(list(range(1,len(pairs)+1))+[-s for s in selectors if s!=preferred]+[preferred])
                if not sat.solve():
                    with Glucose3(bootstrap_with=fixed+clauses,with_proof=True) as fresh:
                        assert not fresh.solve();proof=fresh.get_proof()
                    (D/'proof.drup').write_text('\\n'.join(proof)+'\\n',encoding='ascii',newline='\\n');status='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE' if len(proof)<=500000 else 'PROOF_SIZE_BOUND_UNKNOWN';break
                model=set(sat.get_model());chosen=[i for i,s in enumerate(selectors) if s in model];assert len(chosen)==1;index=chosen[0];c=patterns[index];"""
b="""                if len(closed)==len(patterns):
                    with Glucose3(bootstrap_with=fixed+clauses,with_proof=True) as fresh:
                        assert not fresh.solve();proof=fresh.get_proof()
                    (D/'proof.drup').write_text('\\n'.join(proof)+'\\n',encoding='ascii',newline='\\n');status='UNSAT_AWAITING_INDEPENDENT_CERTIFICATE' if len(proof)<=500000 else 'PROOF_SIZE_BOUND_UNKNOWN';break
                while cursor%len(patterns) in closed:cursor+=1
                requested=cursor%len(patterns);cursor+=1;visits[requested]+=1
                preferred=selectors[requested];sat.set_phases(list(range(1,len(pairs)+1)))
                if not sat.solve(assumptions=[preferred]):
                    closed.add(requested);conditional_unsat.append(dict(pattern=requested,iteration=iteration));continue
                model=set(sat.get_model());chosen=[i for i,s in enumerate(selectors) if s in model];assert chosen==[requested];index=requested;c=patterns[index];"""
t=one(t,a,b)
t=one(t,"    result=dict(case=case['id']", "    (D/'scheduling.json').write_text(json.dumps(dict(visits=visits,conditional_unsat=conditional_unsat,untrusted_closed=sorted(closed),negative_selector_clauses_added=0,final_refutation_uses_no_assumptions=True))+'\\n',encoding='utf-8',newline='\\n')\n    result=dict(case=case['id']")
save('s014_fair_cegis',t)
for stem in ['verify','potential','lrat_verify','run']:
    t=Path('tools/s014_master_'+stem+'.py').read_text(encoding='utf-8').replace('evidence/S014/master_cegis','evidence/S014/fair_cegis').replace('evidence/S014/master_lrat','evidence/S014/fair_lrat').replace('s014_master_cegis','s014_fair_cegis').replace('s014_master_verify','s014_fair_verify').replace('s014_master_potential','s014_fair_potential').replace('s014_master_lrat_verify','s014_fair_lrat_verify')
    save('s014_fair_'+stem,t)
print('Separate fair scheduler and independent verifier wrappers written')
