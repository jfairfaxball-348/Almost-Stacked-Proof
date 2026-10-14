// Complete all-parent sparse losing recurrence, 8-bit fields in uint128.
// Usage: NAME N EDGES MODE CAP SECONDS OUTPUT.bin; max n=15, cap<=250.
#include <bits/stdc++.h>
using namespace std;using U=__uint128_t;
struct Hash {size_t operator()(U x)const {uint64_t a=x,b=x>>64; a^=b+0x9e3779b97f4a7c15ULL+(a<<6)+(a>>2);a^=a>>30;a*=0xbf58476d1ce4e5b9ULL;a^=a>>27;a*=0x94d049bb133111ebULL;return a^(a>>31);}};
using Set=unordered_set<U,Hash>;
int n;vector<pair<int,int>> arcs;U unit[16];
int f(U x,int i){return (x>>(8*i))&255;}
void terminal(int i,int left,U x,Set&out){if(left<0||left>n-i)return;if(i==n){if(!left)out.insert(x);return;}terminal(i+1,left,x,out);terminal(i+1,left-1,x+unit[i],out);}
void printstate(U x){cout<<"[";for(int i=0;i<n;i++){if(i)cout<<",";cout<<f(x,i);}cout<<"]";}
int main(int argc,char**argv){if(argc!=9)return 2;string name=argv[1],mode=argv[4];n=atoi(argv[2]);int cap=atoi(argv[5]),secs=atoi(argv[6]);if(n<2||n>15||cap>250)return 2;string es=argv[3];replace(es.begin(),es.end(),',',' ');stringstream in(es);string p;while(in>>p){int a,b;if(sscanf(p.c_str(),"%d-%d",&a,&b)!=2||a<0||b>=n||a==b)return 2;arcs.push_back({a,b});arcs.push_back({b,a});}for(int i=0;i<n;i++)unit[i]=U(1)<<(8*i);
ofstream bin(argv[7],ios::binary);ofstream meta(argv[8]);Set prev;auto start=chrono::steady_clock::now();string scope="MASS_CUTOFF";int threshold=0,last=0;vector<string>rows;
for(int t=1;t<=cap;t++){Set pool;if(t<=n)terminal(0,t,0,pool);bool stop=false;for(U d:prev){for(auto [u,v]:arcs)if(f(d,v)>0)pool.insert(d+2*unit[u]-unit[v]);if(pool.size()>5000000){scope="CANDIDATE_CUTOFF";stop=true;break;}}if(stop)break;Set cur;for(U c:pool){int support=0;for(int i=0;i<n;i++)support+=f(c,i)>0;if(mode=="stack"?support==1:t==1)continue;bool loss=true;for(auto [u,v]:arcs)if(f(c,u)>=2&&!prev.count(c-2*unit[u]+unit[v])){loss=false;break;}if(loss)cur.insert(c);}if(cur.size()>2000000){scope="LOSER_CUTOFF";break;}
uint32_t tt=t;uint64_t count=cur.size();bin.write((char*)&tt,4);bin.write((char*)&count,8);vector<U>sorted(cur.begin(),cur.end());sort(sorted.begin(),sorted.end());for(U c:sorted)bin.write((char*)&c,16);int Q=-1,as=0,nonasQ=0;U witness=0;for(U c:cur){int heavy=0,q=0;for(int i=0;i<n;i++){int a=f(c,i);heavy+=a>1;q+=a*a;}as+=heavy<=1;if(q>Q){Q=q;nonasQ=heavy>1;witness=c;}else if(q==Q)nonasQ+=heavy>1;}ostringstream s;s<<"{\"t\":"<<t<<",\"candidates\":"<<pool.size()<<",\"losers\":"<<cur.size()<<",\"as_losers\":"<<as<<",\"Qmax\":"<<Q<<",\"nonAS_Qmax\":"<<nonasQ<<"}";rows.push_back(s.str());last=t;prev=move(cur);if(t>n&&prev.empty()){scope="EXACT_THRESHOLD";threshold=t;break;}if(chrono::duration<double>(chrono::steady_clock::now()-start).count()>secs){scope="TIME_CUTOFF";break;}}
meta<<"{\"graph\":\""<<name<<"\",\"n\":"<<n<<",\"mode\":\""<<mode<<"\",\"cap\":"<<cap<<",\"field_bits\":8,\"scope\":\""<<scope<<"\",\"threshold\":"<<(threshold?to_string(threshold):"null")<<",\"last_layer\":"<<last<<",\"seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<",\"rows\":[";for(int i=0;i<(int)rows.size();i++){if(i)meta<<",";meta<<rows[i];}meta<<"]}\n";cout<<name<<" "<<mode<<" "<<scope<<" "<<threshold<<" "<<last<<endl;
}
