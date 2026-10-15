"""CAM-S012-03 actual critical donor exceptions, table producer."""
import json,lzma,sys
from pathlib import Path

def read(p):
    b=Path(p).read_bytes();return json.loads(lzma.decompress(b) if p.endswith('.xz') else b)

def main():
    meta=read('evidence/S012/analysis.json');tables=read('evidence/S011/tree_tables.json.xz')+read('evidence/S012/extra_tables.json.xz')
    pairs=[];extrema=[];traces=[];controls=[]
    for g,t in zip(meta['rows'],tables):
        n=g['n'];name=g['graph'];arcs=[(u,v) for a,b in g['edges'] for u,v in [(a,b),(b,a)]]
        layers=[{tuple(c):m for c,m in layer} for layer in t['layers']]
        def get(c):return layers[sum(c)][tuple(c)]
        def delta(c,s,t,a=1):x=list(c);x[s]-=a;x[t]+=a;return x
        def literal(c,q,j):
            x=list(c);moves=[]
            while not (sum(x)==x[q] and x[q]==[1,0,2,3][j]):
                for u,v in arcs:
                    if x[u]>=2:
                        d=delta(x,u,v);d[u]-=1
                        if get(d)[j]>>q&1:break
                else:raise AssertionError((name,x,q,j))
                moves.append([u,v]);x=d
            traces.append({'graph':name,'c':c,'q':q,'kind':j,'moves':moves,'final':x})
        for goal,j in [('stack',1),('clear',0)]:
            threshold=g['thresholds'][goal]
            if not threshold:continue
            losers=[c for c,m in sorted(layers[threshold-1].items()) if not m[j]]
            Q=max(sum(a*a for a in c) for c in losers);maxima=[c for c in losers if sum(a*a for a in c)==Q]
            asmax=[c for c in maxima if sum(a>1 for a in c)<=1]
            extrema.append({'graph':name,'goal':goal,'threshold':threshold,'losers':len(losers),'Qmax':Q,'maximizers':maxima,'AS_maximizers':len(asmax),'nonAS_maximizers':len(maxima)-len(asmax)})
            if asmax:controls.append({'graph':name,'goal':goal,'c':asmax[0]})
            if goal!='stack':continue
            for c in losers:
                if sum(a>=2 for a in c)<2:continue
                controls.append({'graph':name,'goal':'stack','c':c})
                for s in range(n):
                    for receiver in range(n):
                        if s==receiver or c[s]<2 or c[receiver]<c[s]:continue
                        for a in (1,2,3):
                            if a>c[s]:continue
                            d=delta(c,s,receiver,a);dm=get(d);deletion=list(c);deletion[s]-=1
                            inserted=list(c);inserted[s]+=1
                            donor=[bool(dm[j]>>s&1) for j in (0,2,3)]
                            D=bool(get(inserted)[2]>>receiver&1);deleted_clear=bool(get(deletion)[0]>>receiver&1)
                            if a==1:assert donor[0]==D and not donor[1]
                            if a==2:assert not donor[0] and donor[1]==deleted_clear
                            if (s,receiver) in arcs:
                                if a==1:assert not donor[1] and not donor[2]
                                if a==2:assert not donor[0] and not donor[2]
                            pairs.append({'graph':name,'c':c,'s':s,'t':receiver,'a':a,'d':d,'donor_1_2_3':donor,'stackable':bool(dm[1]),'AS':sum(x>1 for x in d)<=1,'Q_increase':sum(x*x for x in d)-sum(x*x for x in c),'D_edge':D,'deletion_clear_at_t':deleted_clear})
                            for j in (0,2):
                                if dm[j]>>s&1:literal(d,s,j)
    traces=list({(r['graph'],tuple(r['c']),r['q'],r['kind']):r for r in traces}.values())
    controls=list({(r['graph'],r['goal'],tuple(r['c'])):r for r in controls}.values())
    out={'campaign':'CAM-S012-03','pairs':pairs,'extrema':extrema,'controls':controls}
    for name,obj in [('exceptions.json',out),('exception_traces.json.xz',traces)]:
        p=Path('evidence/S012')/name;b=(json.dumps(obj,separators=(',',':'))+'\n').encode()
        if '--check-only' in sys.argv:assert (lzma.decompress(p.read_bytes()) if p.suffix=='.xz' else p.read_bytes())==b
        else:p.write_bytes(lzma.compress(b) if p.suffix=='.xz' else b)
    print(json.dumps({'pairs':len(pairs),'increasing_losing_transfers':sum(not r['stackable'] for r in pairs),'literal_traces':len(traces),'literal_moves':sum(len(r['moves']) for r in traces),'global_extrema':len(extrema),'nonAS_global_Qmax':sum(r['nonAS_maximizers'] for r in extrema)}),flush=True)

if __name__=='__main__':main()
