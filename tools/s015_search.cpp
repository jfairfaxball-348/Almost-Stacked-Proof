// CAM-S015-87 heuristic counterexample search (NOT a completeness claim).
// Local search over connected simple graphs of fixed order n (<=12) for
//     gap(G) = L_nonAS(G) - L_AS(G),
// where L_nonAS is the largest mass of a STACK loser with >=2 heavy sites and
// L_AS the largest mass of an AS loser, both from the exact loser-layer recursion
// (same lemmas as tools/s015_layers.cpp).  ASH*-STACK fails on G iff gap>0.
// Score = (gap, fraction of non-AS losers in the critical layer).  Moves toggle a
// random vertex pair keeping connectivity; sideways moves accepted; restart on
// stagnation.  Every evaluated graph with gap>=0 is logged with its edge list;
// gap>0 graphs are logged as CANDIDATE for separate dual certification.
// Evaluations exceeding the per-graph wall cap or a 16-bit coordinate are
// scored as invalid (never as evidence).
//
// usage: s015_search N SEED SECONDS_TOTAL SECONDS_PER_GRAPH LOGFILE
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cstdint>
#include <vector>
#include <unordered_set>
#include <chrono>
#include <random>
#include <string>

static const int MAXN = 12;
struct Cfg { uint16_t x[MAXN]; };
struct H { size_t operator()(const Cfg &c) const { uint64_t h = 1469598103934665603ULL; for (int i = 0; i < MAXN; i++) { h ^= c.x[i]; h *= 1099511628211ULL; h ^= h >> 29; } return h; } };
struct E { bool operator()(const Cfg &a, const Cfg &b) const { return memcmp(a.x, b.x, sizeof a.x) == 0; } };
typedef std::unordered_set<Cfg, H, E> Set;

static int n;
struct Res { bool ok; int Lall, LAS, LnonAS; double frac; };

static Res evaluate(const std::vector<std::vector<int>> &adj, double tcap) {
    auto t0 = std::chrono::steady_clock::now();
    Set prev, cur, seen; Res r{true, -1, -1, -1, 0};
    for (int m = 2;; m++) {
        cur.clear(); seen.clear();
        if (m <= n) for (uint32_t mask = 0; mask < (1u << n); mask++) if (__builtin_popcount(mask) == m) { Cfg c{}; for (int i = 0; i < n; i++) c.x[i] = (mask >> i) & 1; cur.insert(c); }
        for (const Cfg &s : prev) for (int v = 0; v < n; v++) if (s.x[v]) for (int u : adj[v]) {
            Cfg c = s; c.x[v]--; c.x[u] += 2;
            if (c.x[u] > 60000) { r.ok = false; return r; }
            if (!seen.insert(c).second) continue;
            int occ = 0; for (int i = 0; i < n; i++) occ += c.x[i] > 0; if (occ < 2) continue;
            bool lose = true; Cfg d = c;
            for (int a = 0; a < n && lose; a++) if (c.x[a] >= 2) for (int b : adj[a]) { d.x[a] -= 2; d.x[b]++; bool in = prev.count(d); d.x[a] += 2; d.x[b]--; if (!in) { lose = false; break; } }
            if (lose) cur.insert(c);
        }
        if (!cur.empty()) {
            r.Lall = m; long nonas = 0;
            for (const Cfg &c : cur) { int h = 0; for (int i = 0; i < n; i++) h += c.x[i] > 1; if (h <= 1) r.LAS = m; else { r.LnonAS = m; nonas++; } }
            r.frac = (double)nonas / cur.size();
        }
        if (cur.empty() && m >= n) break;
        std::swap(prev, cur);
        if (std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count() > tcap) { r.ok = false; return r; }
    }
    return r;
}

static bool connected(const std::vector<std::vector<int>> &adj) {
    std::vector<int> seen(n, 0), st{0}; seen[0] = 1; int c = 1;
    while (!st.empty()) { int u = st.back(); st.pop_back(); for (int w : adj[u]) if (!seen[w]) { seen[w] = 1; c++; st.push_back(w); } }
    return c == n;
}

int main(int argc, char **argv) {
    n = atoi(argv[1]); unsigned seed = atoi(argv[2]); double ttot = atof(argv[3]), tg = atof(argv[4]);
    FILE *lf = fopen(argv[5], "a");
    std::mt19937 rng(seed);
    auto T0 = std::chrono::steady_clock::now();
    std::vector<std::vector<char>> A(n, std::vector<char>(n, 0));
    auto build = [&](std::vector<std::vector<char>> &M) { std::vector<std::vector<int>> adj(n); for (int i = 0; i < n; i++) for (int j = 0; j < n; j++) if (i != j && M[i][j]) adj[i].push_back(j); return adj; };
    auto randomGraph = [&]() { double p = 0.25 + 0.35 * (rng() % 1000) / 1000.0; do { for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) A[i][j] = A[j][i] = (rng() % 1000) < p * 1000; } while (!connected(build(A))); };
    auto edges = [&](std::vector<std::vector<char>> &M) { std::string s; for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) if (M[i][j]) { if (!s.empty()) s += ','; s += std::to_string(i) + "-" + std::to_string(j); } return s; };
    randomGraph();
    Res cur = evaluate(build(A), tg); long evals = 1, stagn = 0, cands = 0;
    while (std::chrono::duration<double>(std::chrono::steady_clock::now() - T0).count() < ttot) {
        if (!cur.ok || stagn > 400) { randomGraph(); cur = evaluate(build(A), tg); evals++; stagn = 0; continue; }
        auto B = A; int i = rng() % n, j = rng() % n; if (i == j) continue;
        B[i][j] = B[j][i] = !B[i][j];
        if (!connected(build(B))) continue;
        Res r = evaluate(build(B), tg); evals++;
        if (!r.ok) { stagn++; continue; }
        int g = r.LnonAS - r.LAS, g0 = cur.LnonAS - cur.LAS;
        if (g >= 0) { fprintf(lf, "%s n %d Lall %d LAS %d LnonAS %d frac %.4f edges %s\n", g > 0 ? "CANDIDATE" : "TIE", n, r.Lall, r.LAS, r.LnonAS, r.frac, edges(B).c_str()); fflush(lf); if (g > 0) cands++; }
        if (g > g0 || (g == g0 && r.frac >= cur.frac)) { if (g > g0 || r.frac > cur.frac) stagn = 0; else stagn++; A = B; cur = r; } else stagn++;
    }
    fprintf(lf, "END seed %u n %d evals %ld candidates %ld\n", seed, n, evals, cands); fclose(lf);
    printf("seed %u n %d evals %ld candidates %ld\n", seed, n, evals, cands);
    return 0;
}
