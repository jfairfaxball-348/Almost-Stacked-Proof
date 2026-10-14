"""Replay only certificate pairs missing from previously completed replay logs."""
import json,sys,time
from pathlib import Path
from s005_verify import verify
p=Path('evidence/S005');done={}
for f in [p/'verification.json']+list(p.glob('resume_verify_*.jsonl')):
 if not f.exists():continue
 rows=json.loads(f.read_text()) if f.suffix=='.json' else [json.loads(x) for x in f.read_text().splitlines() if x]
 done.update({r['file']:r for r in rows})
paths=[]
for f in sorted(p.glob('*.bin.xz')):
 if str(f) in done:continue
 m=json.loads(Path(str(f).replace('.bin.xz','.summary.json')).read_text())
 if 'certificate_sha256' in m:paths.append(f)
group,total=map(int,sys.argv[1].split('/'));paths=paths[group::total]
print('pending group',group,'cases',len(paths),file=sys.stderr,flush=True)
for f in paths:verify(f,True)
