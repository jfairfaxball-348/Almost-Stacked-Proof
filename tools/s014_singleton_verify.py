import json,lzma
from pathlib import Path
B=Path('evidence/S014/singleton')
def main():
    gs=json.loads(Path('evidence/S013/precision_inputs.json').read_bytes());tables=json.loads(lzma.decompress(Path('evidence/S013/precision_tables.json.xz').read_bytes()));saved=json.loads(lzma.decompress((B/'results.json.xz').read_bytes()));total=0;first=[]
    for g,table,row in zip(gs,tables,saved):
        layers=[{tuple(c):m for c,m in layer} for layer in table['layers']];wanted={}
        for mass,layer in enumerate(layers):
            if mass==0:continue
            for d,m in layer.items():
                if m[1]:continue
                for s,a in enumerate(d):
                    if a!=2:continue
                    c=list(d);c[s]=1;c=tuple(c)
                    if layers[mass-1][c][1]:wanted[c,s]=dict(c=list(c),s=s,d=list(d))
        actual={(tuple(r['c']),r['s']):r for r in row['failures']};assert wanted==actual;total+=len(wanted)
        for r in sorted(wanted.values(),key=lambda r:(r['c'],r['s'])):
            if len(first)<4:first.append(dict(graph=g,**r))
    result=dict(graphs=len(saved),failures=total,first_failures=first,independent_forward_inverse_failure_keys_equal=True)
    (B/'verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
