"""Full independent layer replay; a proposed formula is not presumed exact."""
from pathlib import Path
source=Path('tools/s014_threshold_verify.py').read_text(encoding='utf-8')
old="assert L_AS==case['L_AS'] and report['threshold']-1>=case['L_AS']"
assert source.count(old)==1
source=source.replace(old,"assert report['threshold']-1>=L_AS")
old="assert report['last_complete_mass']==len(rows) and L_AS<=case['L_AS']"
assert source.count(old)==1
source=source.replace(old,"assert report['last_complete_mass']==len(rows)")
source=source.replace('L_AS_grammar=case[\'L_AS\']','proposed_L_AS=case[\'L_AS\']')
namespace={'__name__':'s014_buffers_independent_core','__file__':'tools/s014_threshold_verify.py'}
exec(compile(source,'tools/s014_threshold_verify.py','exec'),namespace)
namespace['B']=Path('evidence/S014/buffers')
if __name__=='__main__':namespace['main']()
