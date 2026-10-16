"""CAM34 exact individual losers versus the finite complete AS tail."""
import json,lzma,sys
from pathlib import Path
B=Path('evidence/S014/tail_screen')
def main():
    shard=int(sys.argv[1]);graphs=json.loads((B/'inputs.json').read_bytes())['graphs'][shard*939:(shard+1)*939];out=[]
    for g in graphs:
        n=g['n'];arcs=sorted((u,v) for e in g['edges'] for u,v in [e,e[::-1]]);units=[1<<(8*i) for i in range(n)];memo={};T=sum(g['c']);tests=[];starts=[]
        def put(x,k):
            if len(memo)>=300000 and x not in memo:raise RuntimeError('STATE_CAP_UNKNOWN')
            memo[x]=k
        def win(x):
            if x in memo:return memo[x]!=254
            if len(memo)>=300000:raise RuntimeError('STATE_CAP_UNKNOWN')
            if sum(bool((x>>(8*i))&255) for i in range(n))==1:put(x,255);return True
            for u,v in arcs:
                if (x>>(8*u))&255<2:continue
                if win(x-2*units[u]+units[v]):put(x,u*n+v);return True
            put(x,254);return False
        root=sum(z*units[i] for i,z in enumerate(g['c']));starts.append(root);bad=None
        try:
            original=win(root)
            if original:status='ORIGINAL_WIN'
            else:
                for mass in range(T,T+3):
                    for s in range(n):
                        off=[v for v in range(n) if v!=s]
                        for bits in range(1<<(n-1)):
                            x=(mass-bits.bit_count())*units[s]+sum(units[v] for i,v in enumerate(off) if bits>>i&1);starts.append(x);answer=win(x);tests.append(answer)
                            if not answer:bad=dict(mass=mass,source=s,mask=bits);break
                        if bad:break
                    if bad:break
                status='AS_LOSER_FOUND' if bad else 'POTENTIAL_ACTUAL_COUNTEREXAMPLE'
            needed=set();todo=list(starts)
            while todo:
                x=todo.pop()
                if x in needed:continue
                needed.add(x);k=memo[x]
                if k==255:continue
                if k==254:todo.extend(x-2*units[u]+units[v] for u,v in arcs if ((x>>(8*u))&255)>=2)
                else:u,v=divmod(k,n);todo.append(x-2*units[u]+units[v])
        except RuntimeError as e:
            assert str(e)=='STATE_CAP_UNKNOWN';status='STATE_CAP_UNKNOWN';original=None;needed=set(memo)
        with lzma.open(B/(g['id']+'.bin.xz'),'wb') as f:
            for x in sorted(needed):f.write(x.to_bytes(16,'little')+bytes([memo[x]]))
        out.append(dict(graph=g['id'],status=status,original_winning=original,AS_tested=len(tests),AS_bad=bad,states=len(needed),memo_states=len(memo)))
        if len(out)%25==0 or status=='POTENTIAL_ACTUAL_COUNTEREXAMPLE':(B/f'shard{shard}_results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
        if status=='POTENTIAL_ACTUAL_COUNTEREXAMPLE':break
    (B/f'shard{shard}_results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(shard=shard,cases=len(out),original_winners=sum(r['status']=='ORIGINAL_WIN' for r in out),AS_rejections=sum(r['status']=='AS_LOSER_FOUND' for r in out),potentials=sum(r['status']=='POTENTIAL_ACTUAL_COUNTEREXAMPLE' for r in out),unknown=sum(r['status']=='STATE_CAP_UNKNOWN' for r in out))),flush=True)
if __name__=='__main__':main()
