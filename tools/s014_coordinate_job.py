import contextlib,sys
from pathlib import Path
B=Path('evidence/S014/coordinate_maximal')
name,mode=sys.argv[1:3]
if mode=='produce':import s014_circulant_engine as engine
else:import s014_circulant_engine_verify as engine
engine.B=B
sys.argv=['engine',name,'stack']
with (B/(name+'_'+mode+'.log')).open('w',encoding='utf-8',newline='\n') as log,contextlib.redirect_stdout(log):engine.main()
print(name+' '+mode+' complete')
