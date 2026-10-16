using System;
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
    static bool Goal(UInt128 x) {int p=0;for(int u=0;u<N;u++)if(Get(x,u)>0)p++;return p==1;}
    static void TimeCheck() {if(clock.Elapsed.TotalSeconds>540)throw new Exception("TIME_BOUND_UNKNOWN");}
    static void Add(HashSet<UInt128> set,UInt128 x) {if(set.Count>=Cap&&!set.Contains(x))throw new Exception("CANDIDATE_CAP_UNKNOWN");set.Add(x);}
    static HashSet<UInt128> Load(string path,int expected) {
        var result=new HashSet<UInt128>();using(var fs=File.OpenRead(path))using(var gz=new GZipStream(fs,CompressionMode.Decompress))using(var br=new BinaryReader(gz)) {
            if(br.ReadInt32()!=expected)throw new Exception("PREVIOUS_MASS_MISMATCH");ulong count=br.ReadUInt64();if(count>Cap)throw new Exception("PREVIOUS_CAP_MISMATCH");
            for(ulong i=0;i<count;i++) {ulong a=br.ReadUInt64(),b=br.ReadUInt64();if(!result.Add((UInt128)a|((UInt128)b<<64)))throw new Exception("PREVIOUS_DUPLICATE");}
            if(gz.ReadByte()!=-1)throw new Exception("PREVIOUS_TRAILING_BYTES");
        }return result;
    }
    static void Save(string path,int mass,HashSet<UInt128> values) {
        var ordered=new UInt128[values.Count];values.CopyTo(ordered);Array.Sort(ordered);
        using(var fs=File.Create(path))using(var gz=new GZipStream(fs,CompressionLevel.Fastest))using(var bw=new BinaryWriter(gz)) {bw.Write(mass);bw.Write((ulong)ordered.Length);foreach(var x in ordered){bw.Write((ulong)x);bw.Write((ulong)(x>>64));}}
    }
    public static void Run(string name,int mass,string basePath){
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
        string digest=Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(file))).ToLowerInvariant();var report=new{graph=name,n=N,mass=mass,status=status,candidates=candidates.Count,losers=status=="COMPLETE_LAYER"?losers.Count:(int?)null,examined=examined,certificate=Path.GetFileName(file),sha256=digest,seconds=clock.Elapsed.TotalSeconds,scope="Complete layer only after independent replay; caps UNKNOWN"};string json=JsonSerializer.Serialize(report);File.WriteAllText(Path.Combine(folder,"mass"+mass+".json"),json+"\n");Console.WriteLine(json);
    }
}
