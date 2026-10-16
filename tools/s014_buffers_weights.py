"""Independent edge-subset linear-forest enumeration for every path-cover DP."""
import itertools,json
from pathlib import Path
B=Path('evidence/S014/buffers')
def main():
    inp=json.loads((B/'threshold_inputs.json').read_bytes());seen={}
    for g in inp['graphs']:
        f=g['F'];n=f['n'];edges=f['edges'];key=(n,tuple(tuple(e) for e in edges))
        if key in seen:continue
        rows=[]
        for mask in range(1<<n):
            vertices=[z for z in range(n) if mask>>z&1];es=[(u,v) for u,v in edges if u in vertices and v in vertices];best=len(vertices)
            for flags in itertools.product([False,True],repeat=len(es)):
                deg=[0]*n;parent=list(range(n));count=0;valid=True
                def find(v):
                    while parent[v]!=v:v=parent[v]
                    return v
                for (u,v),flag in zip(es,flags):
                    if not flag:continue
                    deg[u]+=1;deg[v]+=1;x,y=find(u),find(v)
                    if deg[u]>2 or deg[v]>2 or x==y:valid=False;break
                    parent[x]=y;count+=1
                if valid:best=min(best,len(vertices)-count)
            rows.append(best)
        assert rows==f['theta'] and max(mask.bit_count()+2*t for mask,t in enumerate(rows))==f['W']
        seen[key]=dict(F=f['name'],theta=rows,W=f['W'])
    (B/'weights_verification.json').write_text(json.dumps(list(seen.values()),indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(full_labeled_F=len(seen),all_theta_and_W_equal=True)),flush=True)
if __name__=='__main__':main()
