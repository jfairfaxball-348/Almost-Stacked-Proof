"""Fresh read-only primary inspection metadata; no copyrighted mirror."""
import concurrent.futures,json,tempfile
from pathlib import Path
import s009_sources

def main():
    s009_sources.TEMP=Path(tempfile.gettempdir())/'ash-s014-primary';s009_sources.TEMP.mkdir(exist_ok=True)
    ids=['1501.04245','2610.09650','2604.22341','2609.31811']
    out={}
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        jobs={ident:pool.submit(s009_sources.fetch,ident) for ident in ids}
        for ident,job in jobs.items():
            try:out[ident]=job.result()
            except Exception as error:out[ident]=dict(id=ident,error=str(error))
            print(json.dumps(out[ident]),flush=True)
    Path('evidence/S014/source_refresh.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':main()
