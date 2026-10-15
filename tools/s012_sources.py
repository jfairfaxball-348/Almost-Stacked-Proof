"""Targeted primary refresh; temporary text only, metadata in S012."""
import concurrent.futures,json,tempfile
from pathlib import Path
import s009_sources

def main():
    s009_sources.TEMP=Path(tempfile.gettempdir())/'ash-s012-primary';s009_sources.TEMP.mkdir(exist_ok=True)
    ids=['2604.22341','2610.09650','2609.31811','1501.04245','https://archive.model.in.tum.de/um/bibdb/esparza/IPL11.pdf']
    results={}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        tasks={i:pool.submit(s009_sources.fetch,i) for i in ids}
        for ident,job in tasks.items():
            try:results[ident]=job.result()
            except Exception as e:results[ident]={'id':ident,'error':str(e),'access':'FETCH_FAILED_NO_UPGRADE'}
    Path('evidence/S012/source_refresh.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(results),flush=True)

if __name__=='__main__':main()
