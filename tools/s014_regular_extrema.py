"""Complete critical-layer metrics, every labeled Q/P maximum, no extrapolation."""
import collections,hashlib,json,lzma,struct
from pathlib import Path
B=Path('evidence/S014/regular')
def main():
    inp=json.loads((B/'threshold_inputs.json').read_bytes());results=[]
    for g in json.loads((B/'ray_inputs.json').read_bytes())['graphs']:
        n=g['n'];N=[{v for e in g['edges'] for u,v in [e,e[::-1]] if u==s} for s in range(n)];visited={0};todo=[0]
        while todo:
            u=todo.pop()
            for v in N[u]-visited:visited.add(v);todo.append(v)
        assert len(visited)==n and all(not any(N[v]<N[u] for v in range(n)) for u in range(n))
        colors={0:0};todo=[0];odd=False
        while todo:
            u=todo.pop()
            for v in N[u]:
                if v in colors:odd|=colors[u]==colors[v]
                else:colors[v]=1-colors[u];todo.append(v)
        assert odd
        triangle={u for u in range(n) if any(v in N[w] for v in N[u] for w in N[u] if v!=w)};goals={}
        for goal in ['stack','clear']:
            report=json.loads((B/(g['graph']+'_'+goal+'_threshold.json')).read_bytes());verified=json.loads((B/(g['graph']+'_'+goal+'_threshold_verification.json')).read_bytes());T=verified['threshold'];assert verified['all_full_losing_layers_equal']
            if T is None:goals[goal]=dict(status='UNKNOWN_BEYOND_REGISTERED_MASS',critical=None);continue
            cert=B/(g['graph']+'_'+goal+'_threshold.bin.xz');critical=[]
            with lzma.open(cert,'rb') as stream:
                while raw:=stream.read(12):
                    mass,count=struct.unpack('<IQ',raw)
                    for _ in range(count):
                        c=tuple(stream.read(16)[:n])
                        if mass==T-1:critical.append(c)
            Q=max(sum(x*x for x in c) for c in critical);qm=[c for c in critical if sum(x*x for x in c)==Q];assert set(qm)=={tuple(c) for c in report['rows'][T-2]['Qmax']}
            P=min(sum(len(N[v])*c[v] for v in range(n)) for c in qm);qp=[c for c in qm if sum(len(N[v])*c[v] for v in range(n))==P]
            AS=lambda c:sum(x>1 for x in c)<=1;triheavy=lambda c:any(c[v]>1 for v in triangle)
            goals[goal]=dict(status='EXACT_THRESHOLD',threshold=T,L_AS=verified['L_AS_seen'],critical_losers=len(critical),critical_AS=sum(AS(c) for c in critical),Q=Q,P=P,Qmax=qm,QPmax=qp,every_Q_AS=all(AS(c) for c in qm),every_QP_AS=all(AS(c) for c in qp),every_Q_avoids_triangle_heavy=all(not triheavy(c) for c in qm),every_QP_avoids_triangle_heavy=all(not triheavy(c) for c in qp))
        row=dict(graph=g['graph'],n=n,all_open_neighborhoods_minimal=True,triangle_vertices=sorted(triangle),goals=goals);results.append(row);print(json.dumps({k:v for k,v in row.items() if k!='goals'})+' '+json.dumps({goal:{k:v for k,v in r.items() if k not in ['Qmax','QPmax']} for goal,r in goals.items()}),flush=True)
    (B/'extrema.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8',newline='\n')
if __name__=='__main__':main()
