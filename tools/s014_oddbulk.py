"""Batch complete layers for exactly the previously failing graphs."""
import contextlib,json,sys
from pathlib import Path
import s014_oddbulk_engine as engine
B=Path('evidence/S014/oddbulk')
def main():
    for case in json.loads((B/'inputs.json').read_bytes())['cases']:
        name=case['graph']['graph'];sys.argv=['engine',name,'stack']
        with (B/(name+'_producer.log')).open('w',encoding='utf-8',newline='\n') as log,contextlib.redirect_stdout(log):engine.main()
    print('Finished every registered failing graph; per-graph complete layers retained.',flush=True)
if __name__=='__main__':main()
