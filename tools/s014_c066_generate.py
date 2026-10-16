from pathlib import Path
def save(name,t):
    p=Path('tools')/name;raw=t.encode('utf-8')
    if p.exists():assert p.read_bytes()==raw,'Refuse differing source collision'
    else:p.write_bytes(raw)
old=Path('tools/s014_cube_layer.cs').read_text(encoding='utf-8');common=old[old.index('    static bool Goal'):old.index('    public static void Run')]
header='''using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.IO.Compression;
using System.Numerics;
using System.Security.Cryptography;
using System.Text.Json;
public static class GraphLayers66 {
    static int N;static UInt128[] unit;static List<int[]> maps;static int[][] adj;static Stopwatch clock;const int Cap=2000000;
    static int Get(UInt128 x,int u){return (int)((x>>(8*u))&255);}
    static void Setup(JsonElement g){
        N=g.GetProperty("n").GetInt32();if(N<2||N>16)throw new Exception("N_SCOPE");unit=new UInt128[N];var lists=new List<int>[N];for(int u=0;u<N;u++){unit[u]=(UInt128)1<<(8*u);lists[u]=new List<int>();}
        foreach(var e in g.GetProperty("edges").EnumerateArray()){int u=e[0].GetInt32(),v=e[1].GetInt32();lists[u].Add(v);lists[v].Add(u);}adj=new int[N][];for(int u=0;u<N;u++){lists[u].Sort();adj[u]=lists[u].ToArray();}
        maps=new List<int[]>();foreach(var f in g.GetProperty("maps").EnumerateArray()){var p=new int[N];for(int v=0;v<N;v++)p[v]=f[v].GetInt32();maps.Add(p);}
    }
    static UInt128 Canon(UInt128 x){int biggest=0;for(int v=0;v<N;v++)biggest=Math.Max(biggest,Get(x,v));UInt128 best=0;foreach(var f in maps){if(Get(x,f[N-1])!=biggest)continue;UInt128 y=0;for(int v=0;v<N;v++)y|=(UInt128)Get(x,f[v])<<(8*v);if(y>best)best=y;}return best;}
'''
body='''    public static void Run(string name,int mass,string basePath){
        using(var input=JsonDocument.Parse(File.ReadAllText(Path.Combine(basePath,"inputs.json")))){
            JsonElement graph=default;bool found=false;foreach(var g in input.RootElement.GetProperty("cases").EnumerateArray())if(g.GetProperty("id").GetString()==name){graph=g;found=true;break;}
            if(!found||mass<1||mass>graph.GetProperty("max_mass").GetInt32())throw new Exception("CASE_SCOPE");Setup(graph);
        }
        clock=Stopwatch.StartNew();string folder=Path.Combine(basePath,name);Directory.CreateDirectory(folder);var previous=mass==1?new HashSet<UInt128>():Load(Path.Combine(folder,"mass"+(mass-1)+".bin.gz"),mass-1);var candidates=new HashSet<UInt128>();var losers=new HashSet<UInt128>();string status="COMPLETE_LAYER";string file=Path.Combine(folder,"mass"+mass+".bin.gz");long examined=0;
        try{int ticks=0;foreach(var z in previous){if((ticks++&1023)==0)TimeCheck();for(int u=0;u<N;u++)foreach(int v in adj[u])if(Get(z,v)>0)Add(candidates,Canon(z+2*unit[u]-unit[v]));}
            if(mass<=N)for(uint bits=0;bits<(1u<<N);bits++){if(BitOperations.PopCount(bits)!=mass)continue;UInt128 x=0;for(int v=0;v<N;v++)if((bits&(1u<<v))!=0)x+=unit[v];Add(candidates,Canon(x));}
            foreach(var x in candidates){if((examined++&1023)==0)TimeCheck();if(Goal(x))continue;bool losing=true;for(int u=0;u<N&&losing;u++)if(Get(x,u)>=2)foreach(int v in adj[u])if(!previous.Contains(Canon(x-2*unit[u]+unit[v]))){losing=false;break;}if(losing){if(losers.Count>=Cap)throw new Exception("LOSER_CAP_UNKNOWN");losers.Add(x);}}
            Save(file,mass,losers);
        }catch(Exception e)when(e.Message.EndsWith("UNKNOWN")){status=e.Message;file=Path.Combine(folder,"mass"+mass+"_partial_candidates.bin.gz");Save(file,mass,candidates);}
        string digest=Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(file))).ToLowerInvariant();var report=new{graph=name,n=N,mass=mass,status=status,candidates=candidates.Count,losers=status=="COMPLETE_LAYER"?losers.Count:(int?)null,examined=examined,certificate=Path.GetFileName(file),sha256=digest,seconds=clock.Elapsed.TotalSeconds,scope="Complete layer only after independent replay; caps UNKNOWN"};string json=JsonSerializer.Serialize(report);File.WriteAllText(Path.Combine(folder,"mass"+mass+".json"),json+"\\n");Console.WriteLine(json);
    }
}
'''
save('s014_c066_layer.cs',header+common+body)
save('s014_c066_build.ps1',"$ErrorActionPreference = 'Stop'\nAdd-Type -Path (Join-Path $PWD 'tools/s014_c066_layer.cs') -OutputAssembly (Join-Path $PWD 'evidence/S014/fano_layers/producer.dll')\nWrite-Output 'Untrusted generic graph producer compiled; controls pending.'\n")
save('s014_c066_job.ps1',"param([string]$Graph,[int]$Mass)\n$ErrorActionPreference = 'Stop'\n$layerBase = Join-Path $PWD 'evidence/S014/fano_layers'\n[void][System.Reflection.Assembly]::LoadFrom((Join-Path $layerBase 'producer.dll'))\n[GraphLayers66]::Run($Graph,$Mass,$layerBase)\n")
t=Path('tools/s014_cube_layer_verify.py').read_text(encoding='utf-8');a=t.index("B=Path(");b=t.index('def read(',a)
new='''B=Path('evidence/S014/fano_layers');name=sys.argv[1];mass=int(sys.argv[2]);cfg=json.loads((B/'inputs.json').read_bytes());case=next(c for c in cfg['cases'] if c['id']==name);n=case['n'];D=B/name;stem=D/f'mass{mass}';start=time.monotonic()
for pre in [B/'preflight.json',B/'binary_preflight.json',Path(str(stem)+'_derived_preflight.json')]:
    for p,h in json.loads(pre.read_bytes())['files'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h,p
report=json.loads(stem.with_suffix('.json').read_bytes());assert report['status']=='COMPLETE_LAYER' and report['graph']==name and report['n']==n and report['mass']==mass;units=[1<<(8*v) for v in range(n)];edges={frozenset(e) for e in case['edges']};adj=[[v for v in range(n) if frozenset([u,v]) in edges] for u in range(n)];first=[min(vs) for vs in adj];maps={tuple(f) for f in case['maps']};assert tuple(range(n)) in maps
for f in maps:
    assert set(f)==set(range(n)) and {frozenset([f[u],f[v]]) for u,v in case['edges']}==edges
    for g in maps:assert tuple(f[g[v]] for v in range(n)) in maps
bylast=[[f for f in maps if f[-1]==p] for p in range(n)]
def canonical(x):
    data=x.to_bytes(16,'little')[:n];biggest=max(data)
    return max(int.from_bytes(bytes(data[v] for v in f),'little') for p,a in enumerate(data) if a==biggest for f in bylast[p])
def orbit(x):
    data=x.to_bytes(16,'little')[:n];return {int.from_bytes(bytes(data[v] for v in f),'little') for f in maps}
'''
t=t[:a]+new+t[b:];t=t.replace("(d,mass,len(computed),len(provided),len(computed-provided),len(provided-computed))","(name,mass,len(computed),len(provided),len(computed-provided),len(provided-computed))")
t=t.replace('        for s in range(n):\n            child=translate(z,s);counts=','        for child in orbit(z):\n            counts=')
t=t.replace("oracle=json.loads(Path('evidence/S014/cube_dag/choices.json').read_bytes()) if d==4 else None", "oracle=json.loads(Path('evidence/S014/fano_AS/choices.json').read_bytes()) if name=='FanoInc14' else None")
t=t.replace("if d==4:assert json.loads(Path('evidence/S014/cube_lower/verification.json').read_bytes())['exact_binary_buffer_AS_oracle_certified']", "if name=='FanoInc14':assert json.loads(Path('evidence/S014/fano_AS/verification.json').read_bytes())['exact_binary_buffer_AS_oracle_certified']")
t=t.replace('if d==4 and len(heavy)==1:','if name==\'FanoInc14\' and len(heavy)==1:').replace("s=heavy[0];N=data[s];mask=sum(1<<((v^s)-1) for v in occupied if v!=s);losing=N<oracle[mask][N%3][0];AS_calls+=1", "s=heavy[0];N=data[s];f=case['source_maps'][s];mask=sum(1<<(q-1) for q in range(1,n) if data[f[q]]);losing=N<oracle[mask][N%3][0];AS_calls+=1")
t=t.replace("out=dict(dimension=d,n=n,mass=mass,", "out=dict(graph=name,group_size=len(maps),n=n,mass=mass,")
marker='    assert computed==provided,(name,mass,len(computed),len(provided),len(computed-provided),len(provided-computed))'
assert t.count(marker)==1;t=t.replace(marker,marker+"\n    if name in ['Q1','Q3']:\n        old=Path('evidence/S014/cube_layers_full')/('d1' if name=='Q1' else 'd3');assert json.loads((old/f'mass{mass}_verification.json').read_bytes())['all_full_orbit_losing_sets_equal'];assert computed==read(old/f'mass{mass}.bin.gz',mass)")
save('s014_c066_verify.py',t);print('CAM66 separate generic native producer and independent group/parent checker generated')
