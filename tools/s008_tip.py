"""CAM-S008-01 exact tree/forest buffer optimizer; independent checker separate."""
import itertools
import json
import lzma
import time
from pathlib import Path
from s006_grammar import solve

def forest(clear):
    cells=clear['cells']; index={(c['vertex'],tuple(c['off']),c['kind']):i for i,c in enumerate(cells)}
    values=[c['value'] for c in cells]; nodes=[]; roots=[]
    for i,c in enumerate(cells):
        roots.append(None if c['value'] is None else len(nodes))
        if c['value'] is not None: nodes.append({'cell':i,'clear_node':c['witness'],'children':None})
    rules=[]
    for i,a in enumerate(cells):
        for j,b in enumerate(cells):
            if a['vertex']!=b['vertex']:continue
            d=tuple(x+y for x,y in zip(a['off'],b['off']))
            if any(x>y for x,y in zip(d,clear['box'])):continue
            k=3 if a['kind']==b['kind']==3 else (a['kind']%3+b['kind']%3)%3
            rules.append((index[a['vertex'],d,k],i,j))
    for rounds in range(len(cells)+1):
        changed=False
        for p,a,b in rules:
            if values[a] is None or values[b] is None:continue
            v=values[a]+values[b]
            if values[p] is None or v<values[p]:
                values[p]=v; roots[p]=len(nodes)
                nodes.append({'cell':p,'clear_node':None,'children':[roots[a],roots[b]]});changed=True
        if not changed:break
    else:raise AssertionError('forest bound')
    return {'values':values,'roots':roots,'nodes':nodes,'rounds':rounds+1}

def main():
    start=time.monotonic();rows=[]
    for l in range(9):
        n=l+3;s=0 if l==0 else n-1
        edges=[[0,1],[0,2],[1,2]]+[[0 if v==3 else v-1,v] for v in range(3,n)]
        c=solve(n,edges,s,[int(v in (1,2)) for v in range(n) if v!=s]);c['graph']=f'triangle_tail{l}'
        f=forest(c); b=tuple(c['box']);N=4*2**l-3
        minima=[min(f['values'][i] for i,x in enumerate(c['cells']) if tuple(x['off'])==b and x['kind']==r and f['values'][i] is not None) for r in range(3)]
        assert N<minima[N%3]
        rows.append({'length':l,'clear':c,'forest':f,'candidate_source':N,'unrooted_minima':minima})
        print(l,minima,'loser',N,flush=True)
        assert time.monotonic()-start<600
    raw=json.dumps(rows,separators=(',',':')).encode()
    Path('evidence/S008/tip_certificates.json.xz').write_bytes(lzma.compress(raw))

if __name__=='__main__':main()
