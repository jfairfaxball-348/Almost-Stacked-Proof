"""Consolidate complete producer/replay pairs; never promote a missing replay."""
import json,lzma,hashlib,sys,platform
from pathlib import Path
P=Path('evidence/S005')
def eligible(r):
 if r['mode']=='stack':return True
 colour={0:0};todo=[0];adj=[[] for _ in range(r['n'])]
 for u,v in r['edges']:adj[u].append(v);adj[v].append(u)
 for u in todo:
  for v in adj[u]:
   if v in colour:
    if colour[v]==colour[u]:return True
   else:colour[v]=1-colour[u];todo.append(v)
 return False
def main():
 jobs=json.loads((P/'graphs.json').read_text());done={}
 for f in [P/'verification.json']+list(P.glob('resume_verify_*.jsonl')):
  if not f.exists():continue
  rows=json.loads(f.read_text()) if f.suffix=='.json' else [json.loads(x) for x in f.read_text().splitlines() if x]
  done.update({r['file']:r for r in rows})
 rows=[];verified=[]
 for j in jobs:
  path=P/(j['graph']+'_'+j['mode']+'.bin.xz')
  assert path.exists(),path
  m=json.loads(Path(str(path).replace('.bin.xz','.summary.json')).read_text())
  assert 'certificate_sha256' in m and str(path) in done,(path,'missing producer/replay')
  v=done[str(path)];assert m['threshold']==v['threshold'] and m['last_layer']==v['layers'] and v['all_equal']
  m['eligible']=eligible(m);m['ash_scope']='ELIGIBLE_GOAL' if m['eligible'] else 'BIPARTITE_REACHABILITY_ONLY'
  if not m['eligible']:assert m['threshold'] is None
  rows.append(m);verified.append(v)
 (P/'campaign_summary.json').write_text(json.dumps(rows,indent=2)+'\n')
 (P/'verification.json').write_text(json.dumps(verified,indent=2)+'\n')
 exact=[r for r in rows if r['eligible'] and r['threshold']]
 analysis={'total_cases':len(rows),'eligible_cases':sum(r['eligible'] for r in rows),
 'exact_threshold_cases':len(exact),'cutoff_cases':[{'graph':r['graph'],'mode':r['mode'],'last_complete_mass':r['last_layer'],'scope':r['scope']} for r in rows if r['eligible'] and not r['threshold']],
 'ineligible_cases':[{'graph':r['graph'],'mode':r['mode'],'last_complete_mass':r['last_layer'],'scope':r['ash_scope']} for r in rows if not r['eligible']],
 'certified_losing_states':sum(v['certified_losers'] for v in verified),
 'completed_critical_Q_cases':len(exact),'Q_counterexamples':sum(v.get('nonAS_Qmax',0)>0 for v in verified if v['threshold']),
 'lex_counterexamples':sum(not v.get('lex_max_is_AS',True) for v in verified if v['threshold']),
 'ASHstar_counterexamples':sum(v.get('critical_AS_count',1)==0 for v in verified if v['threshold']),
 'producer_compute_seconds':sum(r['seconds'] for r in rows),'replay_seconds':sum(v['seconds'] for v in verified)}
 (P/'analysis.json').write_text(json.dumps(analysis,indent=2)+'\n')
 env=json.loads((P/'environment.json').read_text()) if (P/'environment.json').exists() else {}
 env.update(continuation_python=sys.version,continuation_platform=platform.platform(),compiler='g++13.3.0 Ubuntu24.04',
 producer_source_versions={'original_reconstructed_after_eligibility_insertion':hashlib.sha256(Path('tools/s005_sparse_original.cpp').read_bytes()).hexdigest(),'eligibility_detection_version':hashlib.sha256(Path('tools/s005_sparse.cpp').read_bytes()).hexdigest()},
 binary_format='little endian uint32 mass / uint64 count / uint128 states, 8-bit vertex fields',
 original_run_date='2026-10-13',continuation_date='2026-10-14')
 (P/'environment.json').write_text(json.dumps(env,indent=2)+'\n')
 for f in P.glob('*.bin'):
  xz=Path(str(f)+'.xz')
  assert xz.exists() and hashlib.sha256(f.read_bytes()).hexdigest()==hashlib.sha256(lzma.decompress(xz.read_bytes())).hexdigest()
  f.unlink()
 print(json.dumps(analysis,indent=2))
if __name__=='__main__':main()
