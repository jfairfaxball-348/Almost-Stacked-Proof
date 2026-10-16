"""Separate full-group source; refuse to overwrite any different file."""
from pathlib import Path
def save(name,t):
    p=Path('tools')/name;raw=t.encode('utf-8')
    if p.exists():assert p.read_bytes()==raw,'Refuse source collision: '+str(p)
    else:p.write_bytes(raw)
t=Path('tools/s014_cube_layer.cs').read_text(encoding='utf-8').replace('public static class CubeLayers','public static class CubeLayers64').replace('static int[] shift;','static int[] shift;\n    static List<int[]> maps;').replace('D=d;N=1<<d;','D=d;N=1<<d;maps=new List<int[]>();BuildPermutations(0,new int[D],new bool[D]);')
a=t.index('    static UInt128 Canon(');b=t.index('    static bool Goal',a)
t=t[:a]+'''    static void BuildPermutations(int depth,int[] perm,bool[] used) {
        if(depth==D) {var map=new int[N];for(int v=0;v<N;v++){int w=0;for(int j=0;j<D;j++)if((v&(1<<j))!=0)w|=1<<perm[j];map[v]=w;}maps.Add(map);return;}
        for(int j=0;j<D;j++)if(!used[j]){used[j]=true;perm[depth]=j;BuildPermutations(depth+1,perm,used);used[j]=false;}
    }
    static UInt128 Canon(UInt128 x) {
        int biggest=0;for(int v=0;v<N;v++)biggest=Math.Max(biggest,Get(x,v));UInt128 best=0;
        for(int p=0;p<N;p++)if(Get(x,p)==biggest){int s=(N-1)^p;foreach(var map in maps){UInt128 y=0;for(int v=0;v<N;v++)y|=(UInt128)Get(x,map[v]^s)<<(8*v);if(y>best)best=y;}}
        return best;
    }
'''+t[b:];save('s014_c064_layer.cs',t)
for old,new in [('s014_cube_layer_build.ps1','s014_c064_build.ps1'),('s014_cube_layer_job.ps1','s014_c064_job.ps1')]:
    t=Path('tools/'+old).read_text(encoding='utf-8').replace('s014_cube_layer.cs','s014_c064_layer.cs').replace('cube_layers','cube_layers_full').replace('[CubeLayers]','[CubeLayers64]');save(new,t)
t=Path('tools/s014_cube_layer_verify.py').read_text(encoding='utf-8').replace('evidence/S014/cube_layers','evidence/S014/cube_layers_full')
a=t.index('def translate(');b=t.index('def read(',a)
t=t[:a]+'''maps=[]
for perm in itertools.permutations(range(d)):
    coords=[sum(((v>>j)&1)<<perm[j] for j in range(d)) for v in range(n)]
    for s in range(n):maps.append(tuple(v^s for v in coords))
mapset=set(maps);assert len(mapset)==n*__import__('math').factorial(d) and tuple(range(n)) in mapset
bylast=[[f for f in maps if f[-1]==p] for p in range(n)]
generators=[tuple(v^(1<<j) for v in range(n)) for j in range(d)]
for j in range(d-1):generators.append(tuple(v if ((v>>j)&1)==((v>>(j+1))&1) else v^(1<<j)^(1<<(j+1)) for v in range(n)))
edges={frozenset([u,v]) for u in range(n) for v in adj[u]}
for f in maps:
    assert len(set(f))==n and {frozenset([f[u],f[v]]) for u in range(n) for v in adj[u]}==edges
    for g in generators:assert tuple(f[g[v]] for v in range(n)) in mapset
def canonical(x):
    data=x.to_bytes(16,'little')[:n];biggest=max(data)
    return max(int.from_bytes(bytes(data[v] for v in f),'little') for p,a in enumerate(data) if a==biggest for f in bylast[p])
def orbit(x):
    data=x.to_bytes(16,'little')[:n];return {int.from_bytes(bytes(data[v] for v in f),'little') for f in maps}
'''+t[b:]
t=t.replace('        for s in range(n):\n            child=translate(z,s);counts=', '        for child in orbit(z):\n            counts=')
a=t.index('try:\n');b=t.index('except RuntimeError',a);body=t[a+5:b]
prefix='''refined=None
old=Path('evidence/S014/cube_layers')/f'd{d}'
oldv=old/f'mass{mass}_verification.json'
if oldv.exists() and json.loads(oldv.read_bytes())['all_full_orbit_losing_sets_equal']:
    refined=set()
    with gzip.open(old/f'mass{mass}.bin.gz','rb') as handle:
        om,oc=struct.unpack('<IQ',handle.read(12));assert om==mass
        for _ in range(oc):raw=handle.read(16);assert len(raw)==16 and not any(raw[n:]) and sum(raw[:n])==mass;refined.add(canonical(int.from_bytes(raw,'little')))
        assert not handle.read(1)
try:
    if d==4 and mass<=13:
        assert refined is not None;computed=refined;assert computed==provided
    else:
'''
t=t[:a]+prefix+''.join('    '+line if line.strip() else line for line in body.splitlines(keepends=True))+"    if refined is not None:assert computed==refined\n"+t[b:]
t=t.replace("out=dict(dimension=d,n=n,mass=mass,", "out=dict(group_size=len(maps),method='REFINED_PREVIOUS_COMPLETE_LAYER' if d==4 and mass<=13 else 'FULL_CANONICAL_FIRST_PARENT',dimension=d,n=n,mass=mass,")
save('s014_c064_verify.py',t)
t=Path('tools/s014_cube_layer_run.py').read_text(encoding='utf-8').replace('evidence/S014/cube_layers','evidence/S014/cube_layers_full').replace('s014_cube_layer_build.ps1','s014_c064_build.ps1').replace('s014_cube_layer_job.ps1','s014_c064_job.ps1').replace('s014_cube_layer_verify.py','s014_c064_verify.py').replace('s014_cube_layer.cs','s014_c064_layer.cs');save('s014_c064_run.py',t);print('CAM64 distinct full384-group sources generated without overwrites')
