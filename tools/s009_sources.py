"""Fetch primary text for local inspection; commit only metadata and digests."""
import concurrent.futures
import hashlib
import io
import json
import os
import re
import tempfile
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from pypdf import PdfReader

TEMP=Path(tempfile.gettempdir())/'ash-s009-primary'

def fetch(ident):
    direct=ident.startswith('https://')
    page=b'' if direct else urllib.request.urlopen(f'https://arxiv.org/abs/{ident}',timeout=60).read()
    versions=sorted(set(re.findall(rb'\[v(\d+)\]',page)),key=int)
    version=versions[-1].decode() if versions else '1'
    url=ident if direct else f'https://arxiv.org/pdf/{ident}v{version}'
    raw=urllib.request.urlopen(url,timeout=60).read()
    reader=PdfReader(io.BytesIO(raw))
    text='\n'.join(f'\n=== PDF PAGE {i+1} ===\n'+p.extract_text() for i,p in enumerate(reader.pages))
    basename=ident.rsplit('/',1)[-1] or 'Sjostrand_publisher'
    path=TEMP/((basename if direct else ident.replace('/','_'))+'.txt')
    path.write_text(text,encoding='utf-8',newline='\n')
    return {'id':ident,'versions':[v.decode() for v in versions],'current_version':None if direct else version,'pdf_url':url,
        'pdf_sha256':hashlib.sha256(raw).hexdigest(),'pdf_bytes':len(raw),'pages':len(reader.pages),
        'extracted_text_sha256':hashlib.sha256(text.encode()).hexdigest(),'abs_sha256':None if direct else hashlib.sha256(page).hexdigest(),
        'temporary_text_path':str(path),'utc':datetime.now(timezone.utc).isoformat(),'pdf_retained':False}

def main():
    import sys
    TEMP.mkdir(exist_ok=True)
    ids=sys.argv[1:] or ['2604.22341','2610.09650','2609.31811','math/0410129','2606.04659']
    dest=Path('evidence/S009/source_refresh.json')
    previous=json.loads(dest.read_text(encoding='utf-8')) if dest.exists() else {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        jobs={ident:pool.submit(fetch,ident) for ident in ids}
        for ident,job in jobs.items():
            try: result=job.result()
            except Exception as error: result={'id':ident,'error':str(error),'utc':datetime.now(timezone.utc).isoformat()}
            previous[ident]=result
            print(json.dumps(result))
    dest.write_text(json.dumps(previous,indent=2)+'\n',encoding='utf-8',newline='\n')

if __name__=='__main__':main()
