"""Independent canonical-parent replay of C++ all-parent binary certificates.

Little-endian format: each layer uint32 mass, uint64 count, then count uint128
states. Eight-bit vertex fields. No producer import and no hash fingerprints
substituted for set equality. Optional full reverse-winning base cross-check.
"""
import json,lzma,itertools,struct,time,sys,hashlib
from pathlib import Path

def load(path):
 raw=lzma.decompress(Path(path).read_bytes());off=0;layers=[]
 while off<len(raw):
  t,count=struct.unpack_from('<IQ',raw,off);off+=12
  assert off+16*count<=len(raw)
  cur={int.from_bytes(raw[k:k+16],'little') for k in range(off,off+16*count,16)};off+=16*count
  assert len(cur)==count and t==len(layers)+1
  layers.append(cur)
 assert off==len(raw)
 return raw,layers

def verify(path,base=False):
 st=time.monotonic();path=Path(path);meta=json.loads(Path(str(path).replace('.bin.xz','.summary.json')).read_text())
 n=meta['n'];mode=meta['mode'];raw,layers=load(path);assert hashlib.sha256(raw).hexdigest()==meta['certificate_sha256']
 adj=[[] for _ in range(n)]
 for u,v in meta['edges']:adj[u].append(v);adj[v].append(u)
 for a in adj:a.sort();assert a
 units=[1<<(8*i) for i in range(n)]
 def fields(x):return [(x>>(8*i))&255 for i in range(n)]
 previous=set();critical=None;checked=0
 for t,current in enumerate(layers,1):
  assert all(sum(fields(x))==t and x>>(8*n)==0 for x in current)
  pool=set()
  if t<=n:
   for ss in itertools.combinations(range(n),t):pool.add(sum(units[i] for i in ss))
  for d in previous:
   f=fields(d)
   for u in range(n):
    v=adj[u][0]
    if not f[v]:continue
    x=d+2*units[u]-units[v];g=fields(x)
    if next((i for i in range(n) if g[i]>=2),None)==u:pool.add(x)
  expected=set()
  for x in pool:
   f=fields(x)
   if (sum(a>0 for a in f)==1 if mode=='stack' else t==1):continue
   if all(x-2*units[u]+units[v] in previous for u in range(n) if f[u]>=2 for v in adj[u]):expected.add(x)
  assert expected==current,(path,t,len(expected),len(current))
  row=meta['rows'][t-1];assert row['losers']==len(current)
  assert row['as_losers']==sum(sum(a>1 for a in fields(x))<=1 for x in current)
  qmax=max((sum(a*a for a in fields(x)) for x in current),default=-1)
  assert qmax==row['Qmax']
  nonas=sum(sum(a>1 for a in fields(x))>1 and sum(a*a for a in fields(x))==qmax for x in current)
  assert nonas==row['nonAS_Qmax']
  if current:critical=current
  previous=current;checked+=len(current)
 threshold=len(layers) if len(layers)>n and not previous else None
 assert threshold==meta['threshold']
 result={'file':str(path),'layers':len(layers),'threshold':threshold,'certified_losers':checked,'all_equal':True}
 if threshold:
  fs=[fields(x) for x in critical];asfs=[c for c in fs if sum(a>1 for a in c)<=1];q=max(sum(a*a for a in c) for c in fs)
  result.update(critical_AS_count=len(asfs),critical_AS_witness=min(asfs) if asfs else None,Qmax=q,nonAS_Qmax=sum(sum(a>1 for a in c)>1 and sum(a*a for a in c)==q for c in fs))
  lex=max(tuple(sorted(c,reverse=True)) for c in fs);result['lex_max_sorted_piles']=lex;result['lex_max_is_AS']=sum(a>1 for a in lex)<=1
 if base:
  from s004_cold import full_layers
  _,B=full_layers(n,meta['edges'],mode,min(n+1,len(layers)))
  for t,b in enumerate(B):assert {sum(c[i]*units[i] for i in range(n)) for c in b}==layers[t]
  result['reverse_winning_base_layers']=len(B)
 result['seconds']=time.monotonic()-st;print(json.dumps(result),flush=True);return result
if __name__=='__main__':
 paths=[x for x in sys.argv[1:] if not x.startswith('--')] or sorted(map(str,Path('evidence/S005').glob('*.bin.xz')))
 shard=next((x.split('=')[1] for x in sys.argv if x.startswith('--shard=')),None)
 if shard:
  index,total=map(int,shard.split('/'));assert 0<=index<total;paths=paths[index::total]
 out=[verify(p,'--base' in sys.argv) for p in paths]
 if '--check-only' not in sys.argv:Path('evidence/S005/verification.json').write_text(json.dumps(out,indent=2)+'\n')
