import contextlib,sys
from pathlib import Path
B=Path('evidence/S014/metric_gap');mode=sys.argv[1]
if mode=='produce':import s014_circulant_engine as engine
else:import s014_circulant_engine_verify as engine
engine.B=B;sys.argv=['engine','A182fresh','stack']
with (B/('threshold_'+mode+'.log')).open('w',encoding='utf-8',newline='\n') as log,contextlib.redirect_stdout(log):engine.main()
print('A182fresh '+mode+' complete')
