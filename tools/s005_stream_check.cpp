// Independent streamed replay: coordinate arrays, canonical parents, exact set equality.
#include <array>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstdint>
#include <stdexcept>
using C=std::array<uint16_t,16>;
struct H{size_t operator()(const C&c)const{size_t h=1469598103934665603ULL;for(auto a:c){h^=a;h*=1099511628211ULL;}return h;}};
using S=std::unordered_set<C,H>;
uint64_t readint(int b){uint64_t x=0;for(int i=0;i<b;i++){int a=std::cin.get();if(a<0)throw std::runtime_error("truncated header");x|=uint64_t(a)<<(8*i);}return x;}
int main(int argc,char**argv){
 if(argc!=4)return 2;int n=std::stoi(argv[1]);if(n<2||n>15)return 2;std::string mode=argv[3],es=argv[2];std::replace(es.begin(),es.end(),',',' ');std::stringstream ss(es);std::string p;std::vector<std::vector<int>>a(n);while(ss>>p){int u,v;auto split=p.find('-');u=std::stoi(p.substr(0,split));v=std::stoi(p.substr(split+1));if(u<0||u>=n||v<0||v>=n||u==v)return 2;a[u].push_back(v);a[v].push_back(u);}for(auto&z:a){std::sort(z.begin(),z.end());if(z.empty())return 2;}S old;int t=0;
 while(std::cin.peek()!=EOF){
  int mass=readint(4);uint64_t count=readint(8);if(mass!=++t)return 3;S cur;
  for(uint64_t k=0;k<count;k++){C c{};int sum=0;for(int i=0;i<16;i++){int z=std::cin.get();if(z<0)return 3;c[i]=z;if(i>=n&&z)return 3;sum+=z;}if(sum!=t||!cur.insert(c).second)return 3;}
  S pool;
  if(t<=n){for(uint64_t b=0;b<(1ULL<<n);b++)if(__builtin_popcountll(b)==t){C c{};for(int i=0;i<n;i++)c[i]=(b>>i)&1;pool.insert(c);}}
  for(const C&d:old)for(int u=0;u<n;u++){int v=a[u][0];if(!d[v])continue;C c=d;c[u]+=2;c[v]--;int first=-1;for(int i=0;i<n;i++)if(c[i]>=2){first=i;break;}if(first==u)pool.insert(c);}
  S expected;
  for(const C&c:pool){int support=0;for(int i=0;i<n;i++)support+=c[i]!=0;if(mode=="stack"?support==1:t==1)continue;bool losing=true;
   for(int u=0;u<n&&losing;u++)if(c[u]>=2)for(int v:a[u]){C d=c;d[u]-=2;d[v]++;if(!old.count(d)){losing=false;break;}}
   if(losing)expected.insert(c);
  }
  if(expected!=cur){std::cerr<<"layer mismatch "<<t<<" "<<expected.size()<<" "<<cur.size()<<std::endl;return 4;}
  uint64_t as=0,nonasq=0;int q=-1;
  for(const C&c:cur){int heavy=0,qq=0;for(int i=0;i<n;i++){heavy+=c[i]>1;qq+=c[i]*c[i];}as+=heavy<=1;if(qq>q){q=qq;nonasq=heavy>1;}else if(qq==q)nonasq+=heavy>1;}
  std::cout<<"{\"t\":"<<t<<",\"losers\":"<<cur.size()<<",\"as_losers\":"<<as<<",\"Qmax\":"<<q<<",\"nonAS_Qmax\":"<<nonasq<<"}"<<std::endl;old=std::move(cur);
 }
 return 0;
}
