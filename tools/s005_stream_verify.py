"""Independent array-state streamed certificate replay plus reverse-winning bases."""
import json,lzma,subprocess,sys,time,hashlib,threading
from pathlib import Path

def verify(path,base=True):
 st=time.monotonic();path=Path(path);m=json.loads(Path(str(path).replace('.bin.xz','.summary.json')).read_text());n=m['n']
 cmd=['/tmp/s005_stream_check',str(n),','.join(f'{u}-{v}' for u,v in m['edges']),m['mode']]
 proc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=False)
 # Drain output concurrently so neither side can block when a layer completes.
 output=[]
 def drain():
  for line in proc.stdout:output.append(json.loads(line))
 th=threading.Thread(target=drain);th.start();h=hashlib.sha256()
 with lzma.open(path,'rb') as f:
  while chunk:=f.read(1024*1024):h.update(chunk);proc.stdin.write(chunk)
 proc.stdin.close();rc=proc.wait();th.join();assert rc==0,(path,rc);assert h.hexdigest()==m['certificate_sha256']
 assert len(output)==m['last_layer']
 for r,expected in zip(output,m['rows']):
  assert all(r[k]==expected[k] for k in ['t','losers','as_losers','Qmax','nonAS_Qmax']),(path,r,expected)
 threshold=len(output) if len(output)>n and output[-1]['losers']==0 else None;assert threshold==m['threshold']
 result={'file':str(path),'layers':len(output),'threshold':threshold,'certified_losers':sum(r['losers'] for r in output),'all_equal':True,'algorithm':'independent array-state streamed canonical replay'}
 # Only materialize the small critical layer, or small base layers when needed.
 def read_selected(want):
  selected={}
  with lzma.open(path,'rb') as f:
   while raw:=f.read(12):
    t=int.from_bytes(raw[:4],'little');count=int.from_bytes(raw[4:],'little')
    if t in want:
     selected[t]={tuple(f.read(16)[:n]) for _ in range(count)}
    else:
     left=16*count
     while left:
      chunk=f.read(min(left,1024*1024));assert chunk;left-=len(chunk)
  return selected
 want=set(range(1,min(n+1,len(output))+1)) if base else set()
 if threshold:want.add(threshold-1)
 selected=read_selected(want)
 if threshold:
  fs=selected[threshold-1];aas=[c for c in fs if sum(v>1 for v in c)<=1];q=max(sum(v*v for v in c) for c in fs);lex=max(tuple(sorted(c,reverse=True)) for c in fs)
  result.update(critical_AS_count=len(aas),critical_AS_witness=min(aas) if aas else None,Qmax=q,nonAS_Qmax=sum(sum(v>1 for v in c)>1 and sum(v*v for v in c)==q for c in fs),lex_max_sorted_piles=lex,lex_max_is_AS=sum(v>1 for v in lex)<=1)
 if base:
  from s004_cold import full_layers
  _,B=full_layers(n,m['edges'],m['mode'],min(n+1,len(output)))
  for t,b in enumerate(B,1):assert b==selected[t],(path,'full reverse base',t)
  result['reverse_winning_base_layers']=len(B)
 result['seconds']=time.monotonic()-st;print(json.dumps(result),flush=True);return result

if __name__=='__main__':
 paths=[a for a in sys.argv[1:] if not a.startswith('--')] or sorted(map(str,Path('evidence/S005').glob('*.bin.xz')))
 shard=next((x.split('=')[1] for x in sys.argv if x.startswith('--shard=')),None)
 if shard:
  i,n=map(int,shard.split('/'));paths=paths[i::n]
 out=[verify(p) for p in paths]
 if '--check-only' not in sys.argv:Path('evidence/S005/stream_verification.json').write_text(json.dumps(out,indent=2)+'\n')
