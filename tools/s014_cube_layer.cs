using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.IO.Compression;
using System.Numerics;
using System.Security.Cryptography;
using System.Text.Json;

public static class CubeLayers {
    static int D,N;
    static UInt128[] unit,lo,hi;
    static int[] shift;
    static Stopwatch clock;
    const int Cap=2000000;
    static void Setup(int d) {
        D=d;N=1<<d;unit=new UInt128[N];lo=new UInt128[D];hi=new UInt128[D];shift=new int[D];
        for(int u=0;u<N;u++)unit[u]=(UInt128)1<<(8*u);
        for(int b=0;b<D;b++) { shift[b]=8*(1<<b);for(int u=0;u<N;u++) { if((u&(1<<b))==0)lo[b]|=(UInt128)255<<(8*u);else hi[b]|=(UInt128)255<<(8*u); } }
    }
    static int Get(UInt128 x,int u) { return (int)((x>>(8*u))&255); }
    static UInt128 Swap(UInt128 x,int b) {return ((x&lo[b])<<shift[b])|((x&hi[b])>>shift[b]);}
    static UInt128 Canon(UInt128 x) {
        UInt128 y=x,best=x;int prior=0;
        for(int s=1;s<N;s++) {int gray=s^(s>>1);int b=BitOperations.TrailingZeroCount((uint)(gray^prior));y=Swap(y,b);if(y>best)best=y;prior=gray;}
        return best;
    }
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
    public static void Run(int d,int mass,string basePath) {
        if(d<1||d>4||mass<1||mass>31)throw new Exception("INPUT_SCOPE");Setup(d);clock=Stopwatch.StartNew();string folder=Path.Combine(basePath,"d"+d);Directory.CreateDirectory(folder);var previous=mass==1?new HashSet<UInt128>():Load(Path.Combine(folder,"mass"+(mass-1)+".bin.gz"),mass-1);var candidates=new HashSet<UInt128>();var losers=new HashSet<UInt128>();string status="COMPLETE_LAYER";string file=Path.Combine(folder,"mass"+mass+".bin.gz");long examined=0;
        try {
            int ticks=0;
            foreach(var z in previous) {
                if((ticks++&1023)==0)TimeCheck();
                for(int u=0;u<N;u++)for(int b=0;b<D;b++){int v=u^(1<<b);if(Get(z,v)>0)Add(candidates,Canon(z+2*unit[u]-unit[v]));}
            }
            if(mass<=N)for(uint bits=0;bits<(1u<<N);bits++) {if(BitOperations.PopCount(bits)!=mass)continue;UInt128 x=0;for(int v=0;v<N;v++)if((bits&(1u<<v))!=0)x+=unit[v];Add(candidates,Canon(x));}
            foreach(var x in candidates) {
                if((examined++&1023)==0)TimeCheck();if(Goal(x))continue;bool losing=true;
                for(int u=0;u<N&&losing;u++)if(Get(x,u)>=2)for(int b=0;b<D;b++){int v=u^(1<<b);if(!previous.Contains(Canon(x-2*unit[u]+unit[v]))){losing=false;break;}}
                if(losing){if(losers.Count>=Cap)throw new Exception("LOSER_CAP_UNKNOWN");losers.Add(x);}
            }
            Save(file,mass,losers);
        } catch(Exception e) when(e.Message.EndsWith("UNKNOWN")) {status=e.Message;file=Path.Combine(folder,"mass"+mass+"_partial_candidates.bin.gz");Save(file,mass,candidates);}
        string digest=Convert.ToHexString(SHA256.HashData(File.ReadAllBytes(file))).ToLowerInvariant();var report=new {dimension=d,n=N,mass=mass,status=status,candidates=candidates.Count,losers=status=="COMPLETE_LAYER"?losers.Count:(int?)null,examined=examined,certificate=Path.GetFileName(file),sha256=digest,seconds=clock.Elapsed.TotalSeconds,scope="Complete layer only after independent replay; caps UNKNOWN"};string json=JsonSerializer.Serialize(report);File.WriteAllText(Path.Combine(folder,"mass"+mass+".json"),json+"\n");Console.WriteLine(json);
    }
}
