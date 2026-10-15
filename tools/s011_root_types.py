"""CAM-S011-03 direct exact root-set normalization; no new reachability layers."""
import hashlib,json,lzma,sys
from pathlib import Path

def main():
    tables=json.loads(lzma.decompress(Path('evidence/S011/tree_tables.json.xz').read_bytes()))
    meta=json.loads(Path('evidence/S011/tree_summary.json').read_text(encoding='utf-8'));insertions=[];rows=[];clear_cases=[];checked=0
    for table,g in zip(tables,meta['graphs']):
        n=g['n'];edges=g['edges'];arcs=[a for u,v in edges for a in [(u,v),(v,u)]]
        def N(mask):return sum(1<<v for v in range(n) if any(mask>>u&1 and (u,v) in arcs for u in range(n)))
        layers=[{tuple(c):m for c,m in layer} for layer in table['layers']]
        for t in range(2,g['max_mass']+1):
            for c,m in layers[t].items():
                assert m[0]==N(m[2]) and m[1]==m[0]|m[2]|m[3];checked+=1
        for c,m in sorted(layers[g['stack_threshold']-1].items()):
            if m[1]:continue
            for w in range(n):
                d=list(c);d[w]+=1;mm=layers[sum(d)][tuple(d)];D=mm[2]
                assert D and not D>>w&1 and mm[3]==0 and mm[1]==D|N(D)
                assert bool(mm[1]>>w&1)==bool(mm[0]>>w&1)
                insertions.append({'graph':g['graph'],'c':c,'w':w,'D_two':D,'C_clear':mm[0],'S_stack':mm[1]})
        if g['clear_threshold'] is not None:
            gap=g['clear_threshold']-g['stack_threshold']
            for c,m in sorted(layers[g['clear_threshold']-1].items()):
                if m[0]==0:clear_cases.append({'graph':g['graph'],'c':c,'gap':gap,'already_stackable':bool(m[1])})
        rows.append({'graph':g['graph'],'checked_inputs':sum(len(layers[t]) for t in range(2,len(layers)))})
    model=[{'w':w,'D':[ (w+1)%5 ],'C':sorted([w,(w+2)%5]),'S':sorted([w,(w+1)%5,(w+2)%5])} for w in range(5)]
    assert not set.intersection(*[set(r['S']) for r in model])
    out={'campaign':'CAM-S011-03','checked_inputs':checked,'graphs':rows,'critical_insertions':insertions,
        'critical_clear_cases':clear_cases,'abstract_C5_model':model,'model_is_graph_configuration':False}
    dest=Path('evidence/S011/root_types.json')
    if '--check-only' in sys.argv:assert json.loads(dest.read_text(encoding='utf-8'))==json.loads(json.dumps(out))
    else:dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'checked_inputs':checked,'critical_insertions':len(insertions),'critical_clear_cases':len(clear_cases),'abstract_intersection':[]}))

if __name__=='__main__':main()
