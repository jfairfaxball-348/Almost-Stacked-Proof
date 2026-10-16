"""Direct finite search on two coupled critical-hole gadgets, CAM30."""
import json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/coupled')
def main():
    out=[]
    for g in json.loads((B/'inputs.json').read_bytes())['graphs']:
        n=g['n'];arcs=sorted((u,v) for e in g['edges'] for u,v in [e,e[::-1]]);units=[1<<(8*i) for i in range(n)];memo={};cap=False
        def win(x):
            if x in memo:return memo[x]!=254
            if len(memo)>=300000:raise RuntimeError('STATE_CAP_UNKNOWN')
            if sum(bool((x>>(8*i))&255) for i in range(n))==1:memo[x]=255;return True
            for u,v in arcs:
                if (x>>(8*u))&255<2:continue
                if win(x-2*units[u]+units[v]):memo[x]=u*n+v;return True
            memo[x]=254;return False
        x=sum(z*units[i] for i,z in enumerate(g['c']))
        try:winner=win(x)
        except RuntimeError as e:assert str(e)=='STATE_CAP_UNKNOWN';cap=True;winner=None
        with lzma.open(B/(g['id']+'.bin.xz'),'wb') as dst:
            for x,k in sorted(memo.items()):dst.write(x.to_bytes(16,'little')+bytes([k]))
        out.append(dict(graph=g['id'],status='STATE_CAP_UNKNOWN' if cap else 'COMPLETE_INPUT',winning=winner,states=len(memo)))
    (B/'results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(dict(graphs=len(out),losing=sum(r['winning'] is False for r in out),winning=sum(r['winning'] is True for r in out),unknown=sum(r['winning'] is None for r in out))),flush=True)
if __name__=='__main__':main()
