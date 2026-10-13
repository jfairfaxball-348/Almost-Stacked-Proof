"""Finite challenge to the universal independent-set AS losing witness.

Every independent set and each root on every connected n=2..5 graph is tested
against the cold full winning DP. Does not substitute for the symbolic proof.
"""
import itertools,json,sys
from pathlib import Path
from s004_cold import atlas,full_layers

def main():
    out=[]
    for n in range(2,6):
        for edges in atlas(n):
            _,layers=full_layers(n,edges,'stack',32)
            edge_set={tuple(sorted(e)) for e in edges};tests=0
            for k in range(2,n+1):
                for independent in itertools.combinations(range(n),k):
                    if any(tuple(p) in edge_set for p in itertools.combinations(independent,2)):continue
                    for root in independent:
                        c=[int(v in independent and v!=root) for v in range(n)];c[root]=2*k+1
                        assert tuple(c) in layers[3*k-1],(n,edges,independent,root,c)
                        tests+=1
            out.append({'n':n,'edges':edges,'independent_set_root_tests':tests})
    if '--check-only' not in sys.argv:
        Path('evidence/S004/independent_witness_tests.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS:',sum(r['independent_set_root_tests'] for r in out),'witnesses on',len(out),'graphs')

if __name__=='__main__':main()
