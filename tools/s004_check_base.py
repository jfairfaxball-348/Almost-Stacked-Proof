"""Cross-check frontier base layers against the cold full winning-set DP."""
import json,lzma,sys
from pathlib import Path
from s004_cold import full_layers

out=[]
for path in sorted(Path('evidence/S004').glob('*.json.xz')):
    d=json.loads(lzma.decompress(path.read_bytes()));n=d['n'];cap=min(n+1,len(d['layers'])-1)
    rows,B=full_layers(n,d['edges'],d['mode'],cap)
    for t,b in enumerate(B,1):
        assert b=={tuple(c) for c in d['layers'][t]},(str(path),t)
    out.append({'file':str(path),'full_reverse_layers_compared':len(B),'all_agree':True})
if '--check-only' not in sys.argv:
    Path('evidence/S004/base_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: complete reverse-winning base layers agree on',len(out),'cases')
