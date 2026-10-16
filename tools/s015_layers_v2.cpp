// CAM-S015-83 producer v2 (derived from CAM-S015-82 v1; adds full critical-layer
// output, per-graph wall/state caps and timing).  Original v1 header follows.
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
// usage: s015_layers_v2 LAYERCAP SECONDS TOTALCAP CRITFILE < graphs (lines: name n a-b,c-d,...)
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cstdint>
#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>
#include <chrono>

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
    double tcap = argc > 2 ? atof(argv[2]) : 60.0;
    long long totcap = argc > 3 ? atoll(argv[3]) : 200000000LL;
    FILE *cf = argc > 4 ? fopen(argv[4], "w") : NULL;
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
        auto t0 = std::chrono::steady_clock::now();
        std::vector<Cfg> crit;
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
            double el = std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
            if (el > tcap || totalStates > totcap) { capped = true; break; }
            if ((long long)cur.size() > maxlayer) maxlayer = cur.size();
            if (!cur.empty()) {
                Lall = m; critCount = cur.size(); critAS = 0; critNonAS = "-";
                crit.assign(cur.begin(), cur.end());
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
        double ms = 1000.0 * std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
        if (!capped && cf) {
            std::vector<std::vector<int>> rows;
            for (const Cfg &c : crit) { std::vector<int> r(n); for (int i = 0; i < n; i++) r[i] = c.x[i]; rows.push_back(r); }
            std::sort(rows.begin(), rows.end());
            fprintf(cf, "%s %d", name, Lall);
            for (auto &r : rows) { fputc(' ', cf); for (int i = 0; i < n; i++) fprintf(cf, i ? ".%d" : "%d", r[i]); }
            fputc('\n', cf); fflush(cf);
        }
        if (capped) printf("%s %d CAPPED_AT_MASS %d cap %lld ms %.0f\n", name, n, m, cap, ms);
        else printf("%s %d Lall %d LAS %d crit %lld critAS %lld maxlayer %lld total %lld nonAS %s %s ms %.0f\n",
                    name, n, Lall, LAS, critCount, critAS, maxlayer, totalStates, critNonAS.c_str(),
                    (LAS == Lall) ? "ASH_OK" : "ASH_FAIL", ms);
        fflush(stdout);
    }
    return 0;
}
