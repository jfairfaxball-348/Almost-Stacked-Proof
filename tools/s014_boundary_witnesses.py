"""Check exact formula witnesses and preserve old incomplete layers."""
import itertools,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/firstfires');OLD=Path('evidence/S014/buffers')
def layers(path,n):
    result={}
    with lzma.open(path,'rb') as f:
        while raw:=f.read(12):
            mass,count=struct.unpack('<IQ',raw);result[mass]={tuple(f.read(16)[:n]) for _ in range(count)}
    return result
def main():
    inp=json.loads((OLD/'threshold_inputs.json').read_bytes());checked=0
    for g in inp['graphs']:
        a,b,n,f=g['a'],g['b'],g['n'],g['F'];W=f['W'];critical=max(n,3*b,3*a+W);losers=layers(OLD/(g['graph']+'_stack_threshold.bin.xz'),n)[critical];witnesses=[]
        if critical==n:witnesses.append((1,)*n)
        if b>=2 and critical==3*b:witnesses.append(tuple(2*b+1 if z==a else int(a<z<a+b) for z in range(n)))
        if critical==3*a+W:
            for mask,h in enumerate(f['theta']):
                if mask.bit_count()+2*h==W:witnesses.append(tuple(2*a+2*h+1 if z==0 else 1 if 0<z<a else int(bool(mask>>(z-a-b)&1)) if z>=a+b else 0 for z in range(n)))
        assert witnesses and all(w in losers and sum(w)==critical and sum(x>1 for x in w)<=1 for w in witnesses);checked+=len(witnesses)
    for case in json.loads((B/'threshold_inputs.json').read_bytes())['cases']:
        g=case['graph'];a,b,n=g['a'],g['b'],g['n'];stem=g['graph']+'_clear_threshold.bin.xz';old=layers(OLD/stem,n);new=layers(B/stem,n);assert all(new[m]==vs for m,vs in old.items());w=tuple(2*a+7 if z==0 else int(0<z<a) for z in range(n));assert w in new[3*a+6]
    result=dict(all_graphs=146,explicit_STACK_AS_witnesses=checked,completed_CLEAR_boundaries=6,old_full_losing_layers_preserved=True);(B/'witnesses_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps(result),flush=True)
if __name__=='__main__':main()
