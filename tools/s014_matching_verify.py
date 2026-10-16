"""Separate complete compositions and literal moves; reads full losing certs."""
import itertools,json,lzma,struct,sys
from pathlib import Path
B=Path('evidence/S014/matching')

def compositions(total,n):
    if n==1:yield (total,);return
    for x in range(total+1):
        for tail in compositions(total-x,n-1):yield (x,)+tail

def main():
    inp=json.loads((B/'threshold_inputs.json').read_bytes());results=[]
    for g in inp['graphs']:
        a,b,m,n=g['a'],g['b'],g['m'],g['n'];T=max(3*b+1,3*a+4*m+1);data=json.loads(lzma.decompress((B/(g['graph']+'_paths.json.xz')).read_bytes()));assert data['graph']==g
        E={tuple(sorted(e)) for e in g['edges']};wanted=set();seen=set();branches={};moves=0
        for total in [T,T+1,T+2]:
            for c in compositions(total,n):
                if sum(x>1 for x in c[:a])<=1 and sum(x>1 for x in c[a:a+b])<=1 and max(c[a+b:])<=1:wanted.add(c)
        for row in data['traces']:
            c=tuple(row['c']);assert c in wanted and c not in seen;seen.add(c);s=list(c)
            for u,v in row['moves']:
                assert tuple(sorted((u,v))) in E and s[u]>=2;s[u]-=2;s[v]+=1;moves+=1
            assert s==row['final'] and sum(x>0 for x in s)==1 and sum(s)>0
            label=row['branch'];branches[label]=branches.get(label,0)+1
        assert seen==wanted and branches==data['branches'] and len(seen)<=300000
        witnesses=[]
        if T-1==3*a+4*m:witnesses.append(tuple(2*a+2*m+1 if z==0 else 1 if 0<z<a or z>=a+b else 0 for z in range(n)))
        if b>=2 and T-1==3*b:witnesses.append(tuple(2*b+1 if z==a else 1 if a<z<a+b else 0 for z in range(n)))
        assert witnesses
        for goal in ['stack','clear']:
            cert=B/(g['graph']+'_'+goal+'_threshold.bin.xz');found=set()
            with lzma.open(cert,'rb') as handle:
                while raw:=handle.read(12):
                    mass,count=struct.unpack('<IQ',raw)
                    for _ in range(count):
                        rawc=handle.read(16)
                        if mass==T-1 and tuple(rawc[:n]) in witnesses:found.add(tuple(rawc[:n]))
            assert found==set(witnesses)
        row=dict(graph=g['graph'],traces=len(seen),literal_moves=moves,branches=branches,exact_AS_witnesses=[list(c) for c in witnesses],all_full_keys_equal=True);results.append(row);print(json.dumps(row),flush=True)
    (B/'paths_verification.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':main()
