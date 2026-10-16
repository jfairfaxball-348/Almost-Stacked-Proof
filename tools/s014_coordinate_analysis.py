"""Packed literal witnesses and complete losing-layer selected sets."""
import itertools,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/coordinate_maximal');units=[1<<(8*v) for v in range(4)];arcs=[(u,v) for u in range(4) for v in range(4) if abs(u-v)==1];d=(9,0,0,3)
def pack(c):return sum(a*u for a,u in zip(c,units))
def decode(x):return [(x>>(8*v))&255 for v in range(4)]
def search(c,root=None):
    memo={}
    def win(x):
        if x in memo:return memo[x] is not False
        assert len(memo)<5000
        if (sum(bool(a) for a in decode(x))==1 if root is None else x==units[root]):memo[x]=None;return True
        for u,v in arcs:
            if ((x>>(8*u))&255)>=2 and win(x-2*units[u]+units[v]):memo[x]=(u,v);return True
        memo[x]=False;return False
    start=pack(c);ok=win(start);history=[];x=start
    if ok:
        while memo[x] is not None:
            u,v=memo[x];history.append([u,v]);x=x-2*units[u]+units[v]
            assert len(history)<=100
    return dict(input=list(c),root=root,winning=ok,moves=history,final=decode(x)),memo
negative,memo=search(d);assert not negative['winning']
closed=sorted(memo);assert all(memo[x] is False for x in closed)
with lzma.open(B/'d_negative.bin.xz','wb') as f:
    for x in closed:f.write(x.to_bytes(16,'little'))
witnesses=[]
for k in [1,2]:
    for sites in itertools.combinations_with_replacement(range(4),k):
        c=list(d)
        for v in sites:c[v]+=1
        row,_=search(c);assert row['winning'];row['insertions']=list(sites);witnesses.append(row)
for s in range(4):
    c=list(d);c[s]+=1;row,_=search(c,s);assert row['winning'];witnesses.append(row)
losers=[]
with lzma.open(B/'P4_stack_threshold.bin.xz','rb') as f:
    while head:=f.read(12):
        mass,count=struct.unpack('<IQ',head)
        for _ in range(count):
            x=int.from_bytes(f.read(16),'little')
            if mass==12:losers.append(tuple(decode(x)))
h=min(sum(a>=2 for a in c) for c in losers);Q=max(sum(a*a for a in c) for c in losers);qm=[c for c in losers if sum(a*a for a in c)==Q];P=min(sum(deg*a for deg,a in zip([1,2,2,1],c)) for c in qm)
out=dict(negative_states=len(closed),d=list(d),mass12_losers=sorted(losers),minimum_heavy=h,Q=Q,P=P,Qmax=sorted(qm),QPmax=sorted(c for c in qm if sum(deg*a for deg,a in zip([1,2,2,1],c))==P),AS_losers=sum(sum(a>=2 for a in c)<=1 for c in losers),witnesses=witnesses)
(B/'analysis.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k not in ['mass12_losers','Qmax','QPmax','witnesses']}))
