// CAM-S015-82 producer: exact STACK losing layers by downward-closed recursion.
//
// For a finite connected simple graph G (n<=12) and mass m>=1:
//   L_1 = {} (every mass-1 input is already a single pile);
//   c (|c|=m>=2) loses STACK iff |supp c|>=2 and EVERY legal successor
//   (two removed at u, one created at a true neighbour v) is in L_{m-1}.
// Candidate completeness: a loser with no legal move is binary (all <=1);
// a loser with a move u->v has successor s in L_{m-1} and c=s+2e_u-e_v, s_v>=1.
// Termination: if L_m is empty and m>=n, no binary input has mass >m and no
// inverse image exists, so every larger layer is empty: L_all=last nonempty m.
// Output one line per graph: graph6-like name, n, L_all, L_AS, layer counts of
// the critical layer, number of AS critical losers, max layer size, and a
// lexicographically smallest critical non-AS loser (if any).
//
// usage: s015_layers STATECAP < graphs (lines: name n a-b,c-d,...)
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cstdint>
#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>

static const int MAXN = 12;
struct Cfg { uint16_t x[MAXN]; };
struct H {
    size_t operator()(const Cfg &c) const {
        uint64_t h = 1469598103934665603ULL;
        for (int i = 0; i < MAXN; i++) { h ^= c.x[i]; h *= 1099511628211ULL; h ^= h >> 29; }
        return (size_t)h;
    }
};
struct E { bool operator()(const Cfg &a, const Cfg &b) const { return memcmp(a.x, b.x, sizeof a.x) == 0; } };
typedef std::unordered_set<Cfg, H, E> Set;

static int n;
static std::vector<int> adj[MAXN];

static bool isAS(const Cfg &c) { int h = 0; for (int i = 0; i < n; i++) if (c.x[i] > 1) h++; return h <= 1; }
static int support(const Cfg &c) { int s = 0; for (int i = 0; i < n; i++) if (c.x[i]) s++; return s; }

static bool loses(const Cfg &c, const Set &prev) {
    if (support(c) <= 1) return false;
    Cfg d = c;
    for (int u = 0; u < n; u++) {
        if (c.x[u] < 2) continue;
        for (int v : adj[u]) {
            d.x[u] -= 2; d.x[v] += 1;
            bool in = prev.count(d) > 0;
            d.x[u] += 2; d.x[v] -= 1;
            if (!in) return false;
        }
    }
    return true;
}

int main(int argc, char **argv) {
    long long cap = argc > 1 ? atoll(argv[1]) : 3000000;
    char name[256], es[4096];
    while (scanf("%255s %d %4095s", name, &n, es) == 3) {
        for (int i = 0; i < MAXN; i++) adj[i].clear();
        if (strcmp(es, "-") != 0) {
            char *s = es, *tok = strtok(s, ",");
            while (tok) { int a, b; if (sscanf(tok, "%d-%d", &a, &b) == 2) { adj[a].push_back(b); adj[b].push_back(a); } tok = strtok(NULL, ","); }
        }
        Set prev, cur;
        int Lall = -1, LAS = -1, m = 1; long long maxlayer = 0; bool capped = false;
        long long critCount = 0, critAS = 0; std::string critNonAS = "-";
        long long totalStates = 0;
        for (m = 2;; m++) {
            cur.clear();
            // binary inputs of mass m
            if (m <= n) {
                for (uint32_t mask = 0; mask < (1u << n); mask++) if (__builtin_popcount(mask) == m) {
                    Cfg c; memset(&c, 0, sizeof c);
                    for (int i = 0; i < n; i++) c.x[i] = (mask >> i) & 1;
                    cur.insert(c);
                }
            }
            // inverse images of previous losers
            for (const Cfg &s : prev) {
                for (int v = 0; v < n; v++) {
                    if (s.x[v] < 1) continue;
                    for (int u : adj[v]) {
                        Cfg c = s; c.x[v] -= 1; c.x[u] += 2;
                        if (cur.count(c)) continue;
                        if (loses(c, prev)) cur.insert(c);
                    }
                }
                if ((long long)cur.size() > cap) { capped = true; break; }
            }
            if (capped) break;
            totalStates += cur.size();
            if ((long long)cur.size() > maxlayer) maxlayer = cur.size();
            if (!cur.empty()) {
                Lall = m; critCount = cur.size(); critAS = 0; critNonAS = "-";
                std::vector<std::string> nonAS;
                for (const Cfg &c : cur) {
                    if (isAS(c)) critAS++;
                    else {
                        std::string t;
                        for (int i = 0; i < n; i++) { t += std::to_string(c.x[i]); if (i + 1 < n) t += '.'; }
                        nonAS.push_back(t);
                    }
                }
                if (critAS > 0) LAS = m;
                if (!nonAS.empty()) critNonAS = *std::min_element(nonAS.begin(), nonAS.end());
            }
            if (cur.empty() && m >= n) break;
            std::swap(prev, cur);
        }
        if (capped) printf("%s %d CAPPED_AT_MASS %d cap %lld\n", name, n, m, cap);
        else printf("%s %d Lall %d LAS %d crit %lld critAS %lld maxlayer %lld total %lld nonAS %s %s\n",
                    name, n, Lall, LAS, critCount, critAS, maxlayer, totalStates, critNonAS.c_str(),
                    (LAS == Lall) ? "ASH_OK" : "ASH_FAIL");
        fflush(stdout);
    }
    return 0;
}
