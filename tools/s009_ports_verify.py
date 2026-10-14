"""Independent complete closures and reverse rooted membership; no producer import."""
import hashlib
import json
import lzma
import sys
import time
from collections import deque
from pathlib import Path

def complete(n,edges,c):
    arcs=[(a,b) for e in edges for a,b in (e,e[::-1])]
    start=tuple(c);seen={start};queue=deque([start]);parents={start:None}
    while queue:
        x=queue.popleft()
        for a,b in arcs:
            if x[a]<2:continue
            y=list(x);y[a]-=2;y[b]+=1;y=tuple(y)
            if y not in seen:
                seen.add(y);queue.append(y);parents[y]=(x,(a,b))
        assert len(seen)<=300000
    bymass={m:[] for m in range(sum(c)+1)}
    masks={x:[0,0] for x in seen};goals={}
    for x in sorted(seen):
        bymass[sum(x)].append(x)
        occupied=[i for i,v in enumerate(x) if v]
        if len(occupied)==1:
            bit=1<<occupied[0];masks[x][1]=bit;goals.setdefault(('stack',occupied[0]),x)
            if sum(x)==1:masks[x][0]=bit;goals.setdefault(('clear',occupied[0]),x)
    direct=[sum(1<<q for goal,q in goals if goal==g) for g in ('clear','stack')]
    # Reverse predecessors seeded by ALL rooted goals in the complete closure.
    for m in range(1,sum(c)+1):
        for x in bymass[m-1]:
            if not any(masks[x]):continue
            for a,b in arcs:
                if not x[b]:continue
                y=list(x);y[a]+=2;y[b]-=1;y=tuple(y)
                if y in seen:
                    masks[y][0]|=masks[x][0];masks[y][1]|=masks[x][1]
    assert masks[start]==direct
    traces=[]
    for (goal,q),x in sorted(goals.items()):
        moves=[];at=x
        while parents[at] is not None:
            prior,move=parents[at];moves.append(move);at=prior
        moves.reverse();at=list(start)
        for a,b in moves:
            assert (a,b) in arcs and at[a]>=2
            at[a]-=2;at[b]+=1
        assert at[q]>0 and all(v==0 for i,v in enumerate(at) if i!=q)
        if goal=='clear':assert sum(at)==1
        traces.append({'goal':goal,'root':q,'moves':moves,'final':at})
    return {'clear_mask':direct[0],'stack_mask':direct[1],'closure_states':len(seen),
        'closure_sha256':hashlib.sha256(json.dumps(sorted(seen),separators=(',',':')).encode()).hexdigest(),
        'rooted_traces':traces}

def marked():
    edges={frozenset((0,1)),frozenset((0,2))};tokens=[[],[],[]]
    for i in range(3):tokens[1].extend([{'v':1,'leaf':f'o1_{i}','children':None},{'v':1,'leaf':f'x{i}','children':None}])
    tokens[2]=[{'v':2,'leaf':f'o2_{i}','children':None} for i in range(3)]
    moves=[]
    def move(u,v,indices):
        assert frozenset((u,v)) in edges and len(indices)==2
        a,b=(tokens[u][i] for i in indices)
        for i in sorted(indices,reverse=True):tokens[u].pop(i)
        tokens[v].append({'v':v,'leaf':None,'children':[a,b]});moves.append([u,v])
    for _ in range(3):move(1,0,(0,1))
    move(2,0,(0,1));move(0,2,(0,3));move(2,0,(0,1))
    assert [len(t) for t in tokens]==[3,0,0]
    def leaves(tree):
        if tree['children'] is None:return {tree['leaf']}
        a,b=tree['children'];assert a['v']==b['v'] and frozenset((a['v'],tree['v'])) in edges
        la,lb=leaves(a),leaves(b);assert not la&lb
        return la|lb
    parts=[leaves(t) for t in tokens[0]];marks={f'x{i}' for i in range(3)}
    assert all(len(part&marks)==1 for part in parts)
    assert len(set.union(*parts))==9 and sum(map(len,parts))==9
    return {'configuration':[0,6,3],'removed_marks':sorted(marks),'moves':moves,
        'final_forest':tokens[0],'affected_components':3,'old_configuration':[0,3,3],
        'verdict':'REFUTES_AT_MOST_TWO_AFFECTED_COMPONENTS_ONLY'}

def main():
    start=time.monotonic();raw=Path('evidence/S009/port_inputs.json').read_bytes();rows=json.loads(raw)
    produced=json.loads(Path('evidence/S009/port_results.json').read_text(encoding='utf-8'))
    assert hashlib.sha256(raw).hexdigest()==produced['input_sha256'] and len(rows)==318
    registered={'P3':(3,{(0,1),(0,2)}),'triangle_leaf':(4,{(0,1),(0,2),(1,2),(0,3)}),
        'triangle_tail2':(5,{(0,1),(0,2),(1,2),(0,3),(3,4)}),'F2':(5,{(0,1),(0,2),(1,2),(0,3),(0,4)}),
        'bowtie':(5,{(0,1),(0,2),(1,2),(0,3),(0,4),(3,4)}),'diamond':(4,{(0,1),(0,2),(1,2),(1,3),(2,3)}),
        'K3':(3,{(0,1),(0,2),(1,2)})}
    for j,row in enumerate(rows):
        n,edges=registered[row['graph']];assert row['n']==n and {tuple(e) for e in row['edges']}==edges and row['port']==0
        c=row['configuration'];assert len(c)==n and min(c)>=0 and sum(c)<=18
        if j<312:
            index=j%52;N=index//4;b=index%4;x,y=(0,1) if row['graph']=='P3' else (1,2)
            expected=[0]*n;expected[-1]=N
            if b>=1:expected[x]+=3 if b==3 else 1
            if b>=2:expected[y]+=3 if b==3 else 1
            assert c==expected
        else:assert c==[[0,1,1,7,1],[0,0,0,11,1],[0,3,3],[0,6,3],[5,0,0],[6,0,0]][j-312]
    checked=[]
    for j,(row,prod) in enumerate(zip(rows,produced['cases'])):
        result=complete(row['n'],row['edges'],row['configuration'])
        assert prod['id']==row['id'] and (prod['clear_mask'],prod['stack_mask'])==(result['clear_mask'],result['stack_mask']),(row,prod,result)
        checked.append({'id':row['id'],**result})
        if j%40==0:print(json.dumps({'independent_cases':j+1,'seconds':time.monotonic()-start}),flush=True)
        assert time.monotonic()-start<600
    assert checked[312]['stack_mask']==checked[313]['clear_mask']==checked[314]['stack_mask']==0
    assert checked[315]['stack_mask']&1 and not checked[316]['clear_mask']&1 and checked[316]['clear_mask']>0
    mark=marked()
    out={'campaign':'CAM-S009-01','all_verified':True,'cases':checked,'complete_cases':len(checked),
        'total_closure_states':sum(r['closure_states'] for r in checked),'maximum_closure_states':max(r['closure_states'] for r in checked),
        'rooted_winning_traces':sum(len(r['rooted_traces']) for r in checked),'marked_forest':mark,'seconds':time.monotonic()-start}
    dest=Path('evidence/S009/port_verification.json.xz')
    if '--check-only' in sys.argv:
        saved=json.loads(lzma.decompress(dest.read_bytes()))
        actual=json.loads(json.dumps(out))
        assert {k:v for k,v in actual.items() if k!='seconds'}=={k:v for k,v in saved.items() if k!='seconds'}
    else:dest.write_bytes(lzma.compress(json.dumps(out,separators=(',',':')).encode()))
    print(json.dumps({k:v for k,v in out.items() if k not in ('cases','marked_forest')}),flush=True)

if __name__=='__main__':main()
