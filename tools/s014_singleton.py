import json,lzma
from pathlib import Path
B=Path('evidence/S014/singleton')
def main():
    gs=json.loads(Path('evidence/S013/precision_inputs.json').read_bytes());tables=json.loads(lzma.decompress(Path('evidence/S013/precision_tables.json.xz').read_bytes()));out=[]
    for g,table in zip(gs,tables):
        layers=[{tuple(c):m for c,m in layer} for layer in table['layers']];tested=0;fail=[]
        for mass,layer in enumerate(layers[:-1]):
            for c,m in sorted(layer.items()):
                if not m[1]:continue
                for s,a in enumerate(c):
                    if a!=1:continue
                    d=list(c);d[s]+=1;d=tuple(d);tested+=1
                    if not layers[mass+1][d][1]:fail.append(dict(c=c,s=s,d=d))
        assert len(fail)<=300000;out.append(dict(graph=g['graph'],tested=tested,failures=fail))
    (B/'results.json.xz').write_bytes(lzma.compress((json.dumps(out,separators=(',',':'))+'\n').encode()));print(json.dumps(dict(graphs=len(out),tested=sum(r['tested'] for r in out),failures=sum(len(r['failures']) for r in out))),flush=True)
if __name__=='__main__':main()
