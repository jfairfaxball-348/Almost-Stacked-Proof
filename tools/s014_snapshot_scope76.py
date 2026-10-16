"""Snapshot stable active files while CAM77 is still mutable."""
import datetime,hashlib,json,os
from pathlib import Path
exclude={'working_hashes.json','checkpoint_hashes.json','progress_checks.json','active_validation_checks.json'}
active=['evidence/S014/twofuel_cegis/','evidence/S014/twofuel_lrat/']
files={}
for folder in ['sessions/S014','evidence/S014']:
    for p in Path(folder).rglob('*'):
        if not p.is_file() or p.name in exclude or p.name.endswith('_validation_checks.json') or any(p.as_posix().startswith(x) for x in active):continue
        files[p.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
for p in [*Path('tools').glob('s014*'),*Path('research').glob('S014*.md')]:
    if p.is_file():files[p.as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
out=dict(status='ACTIVE_MUTABLE_CHECKPOINT_NOT_CLOSEOUT',utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),active_campaign_output_excluded=active,note='CAM77 frozen inputs/code are independently covered by its preflight; mutable outputs await case completion.',files=files)
p=Path('evidence/S014/working_hashes.json');tmp=p.with_name(p.name+'.76tmp');tmp.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');os.replace(tmp,p);print('Stable scope76 active hashes updated; CAM77 mutable outputs explicitly excluded')
