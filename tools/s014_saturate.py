"""Exact greedy loser-preserving edge saturation and AS-tail screen, CAM36."""
import json,lzma
from pathlib import Path
B=Path('evidence/S014/saturate');T=B/'tail'
def main():
    records=[];tailgraphs=[];tailrows=[]
    for case in json.loads((B/'inputs.json').read_bytes())['cases']:
        g=case['seed'];n=g['n'];units=[1<<(8*i) for i in range(n)];root=sum(z*units[i] for i,z in enumerate(g['c']));E={tuple(e) for e in g['edges']};excluded=[]
        def solver(es):
            arcs=sorted(es|{(v,u) for u,v in es});memo={}
            def put(x,k):
                if len(memo)>=300000 and x not in memo:raise RuntimeError('STATE_CAP_UNKNOWN')
                memo[x]=k
            def win(x):
                if x in memo:return memo[x]!=254
                if len(memo)>=300000:raise RuntimeError('STATE_CAP_UNKNOWN')
                if sum(bool((x>>(8*i))&255) for i in range(n))==1:put(x,255);return True
                for u,v in arcs:
                    if ((x>>(8*u))&255)>=2 and win(x-2*units[u]+units[v]):put(x,u*n+v);return True
                put(x,254);return False
            def history(x):
                moves=[]
                while memo[x]!=255:
                    u,v=divmod(memo[x],n);moves.append([u,v]);x=x-2*units[u]+units[v]
                return moves
            return arcs,memo,win,history
        try:
            _,_,win,_=solver(E);assert not win(root)
            for edge in case['order']:
                e=tuple(edge);arcs,memo,win,history=solver(E|{e})
                if win(root):excluded.append(dict(edge=edge,moves=history(root)))
                else:E.add(e)
            arcs,memo,win,history=solver(E);assert not win(root);starts=[root];tested=0;bad=None
            for mass in range(sum(g['c']),sum(g['c'])+3):
                for s in range(n):
                    off=[v for v in range(n) if v!=s]
                    for bits in range(1<<(n-1)):
                        x=(mass-bits.bit_count())*units[s]+sum(units[v] for i,v in enumerate(off) if bits>>i&1);starts.append(x);tested+=1
                        if not win(x):bad=dict(mass=mass,source=s,mask=bits);break
                    if bad:break
                if bad:break
            needed=set();todo=starts.copy()
            while todo:
                x=todo.pop()
                if x in needed:continue
                needed.add(x);k=memo[x]
                if k==255:continue
                if k==254:todo.extend(x-2*units[u]+units[v] for u,v in arcs if ((x>>(8*u))&255)>=2)
                else:u,v=divmod(k,n);todo.append(x-2*units[u]+units[v])
            with lzma.open(T/(case['id']+'.bin.xz'),'wb') as dst:
                for x in sorted(needed):dst.write(x.to_bytes(16,'little')+bytes([memo[x]]))
            final=dict(id=case['id'],n=n,edges=sorted(E),c=g['c']);status='AS_LOSER_FOUND' if bad else 'POTENTIAL_ACTUAL_COUNTEREXAMPLE';tailgraphs.append(final);tailrows.append(dict(graph=case['id'],status=status,original_winning=False,AS_tested=tested,AS_bad=bad,states=len(needed),memo_states=len(memo)));records.append(dict(case=case['id'],status='COMPLETE_SATURATION',final=final,excluded=excluded,tail_status=status))
            if not bad:break
        except RuntimeError as error:
            assert str(error)=='STATE_CAP_UNKNOWN';records.append(dict(case=case['id'],status='STATE_CAP_UNKNOWN'))
        if len(records)%10==0:(B/'results.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8',newline='\n')
    (B/'results.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8',newline='\n');(T/'inputs.json').write_text(json.dumps(dict(graphs=tailgraphs),indent=2)+'\n',encoding='utf-8',newline='\n');(T/'shard0_results.json').write_text(json.dumps(tailrows,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(cases=len(records),complete=len(tailgraphs),unknown=sum(r['status']=='STATE_CAP_UNKNOWN' for r in records),potentials=sum(r['tail_status']=='POTENTIAL_ACTUAL_COUNTEREXAMPLE' for r in records if r['status']=='COMPLETE_SATURATION'))),flush=True)
if __name__=='__main__':main()
