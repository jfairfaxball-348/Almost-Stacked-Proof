// CAM-S015-88 producer v4: v3 with unsigned __int128 keys, B=min(16,floor(128/n))
// bits per coordinate (n<=16).  Everything else identical.  Original v3 header:
// CAM-S015-85 producer v3: same exact loser-layer recursion as v1/v2
// (see tools/s015_layers.cpp header for the two lemmas), engineered for speed:
// configurations packed into ONE uint64 with B=floor(64/n) bits per coordinate,
// flat open-addressing hash tables, a per-layer "seen" table so every
// candidate is tested once.  If any coordinate would reach 2^B-1 the graph is
// reported OVERFLOW (no claim; rerun with v2).  Output format identical to v2
// (stdout line + sorted critical layer line in CRITFILE).
//
// usage: s015_layers_v3 SECONDS TOTALCAP CRITFILE < graphs
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cstdint>
#include <vector>
#include <string>
#include <algorithm>
#include <chrono>

typedef unsigned __int128 K;
struct Table {
    std::vector<K> a; uint64_t mask = 0; size_t cnt = 0;
    void init(size_t cap) { size_t s = 16; while (s < 2 * cap + 16) s <<= 1; a.assign(s, 0); mask = s - 1; cnt = 0; }
    static inline uint64_t mix(K k) { uint64_t x = (uint64_t)k ^ ((uint64_t)(k >> 64) * 0x9E3779B97F4A7C15ULL); x ^= x >> 33; x *= 0xff51afd7ed558ccdULL; x ^= x >> 33; x *= 0xc4ceb9fe1a85ec53ULL; x ^= x >> 33; return x; }
    inline bool has(K k) const { size_t i = mix(k) & mask; while (a[i]) { if (a[i] == k) return true; i = (i + 1) & mask; } return false; }
    inline bool insert(K k) { // returns true if newly inserted
        if (2 * (cnt + 1) > a.size()) grow();
        size_t i = mix(k) & mask; while (a[i]) { if (a[i] == k) return false; i = (i + 1) & mask; }
        a[i] = k; cnt++; return true; }
    void grow() { std::vector<K> old; old.swap(a); a.assign(old.size() * 2, 0); mask = a.size() - 1; cnt = 0; for (K k : old) if (k) insert(k); }
};

static int n, B; static K M1;
static std::vector<int> adj[16];
static inline int get(K k, int i) { return (int)((k >> (B * i)) & M1); }

int main(int argc, char **argv) {
    double tcap = atof(argv[1]); long long totcap = atoll(argv[2]);
    FILE *cf = fopen(argv[3], "w");
    char name[256], es[4096];
    while (scanf("%255s %d %4095s", name, &n, es) == 3) {
        B = 128 / n; if (B > 16) B = 16; M1 = (((K)1) << B) - 1;
        for (int i = 0; i < 16; i++) adj[i].clear();
        if (strcmp(es, "-") != 0) { char *tok = strtok(es, ","); while (tok) { int a, b; if (sscanf(tok, "%d-%d", &a, &b) == 2) { adj[a].push_back(b); adj[b].push_back(a); } tok = strtok(NULL, ","); } }
        auto t0 = std::chrono::steady_clock::now();
        std::vector<K> prevL, curL, crit; Table prevT, curT, seen; prevT.init(1);
        int Lall = -1, LAS = -1, m; bool capped = false, overflow = false; long long total = 0, maxlayer = 0;
        long long critAS = 0;
        K one[16]; for (int i = 0; i < n; i++) one[i] = ((K)1) << (B * i);
        for (m = 2;; m++) {
            curL.clear(); curT.init(prevL.size() + 64); seen.init(prevL.size() * 2 + 64);
            if (m <= n) for (uint32_t mask = 0; mask < (1u << n); mask++) if (__builtin_popcount(mask) == m) {
                K k = 0; for (int i = 0; i < n; i++) if (mask >> i & 1) k += one[i];
                if (curT.insert(k)) curL.push_back(k); seen.insert(k);
            }
            for (K s : prevL) {
                for (int v = 0; v < n; v++) {
                    if (get(s, v) < 1) continue;
                    for (int u : adj[v]) {
                        if (get(s, u) + 2 >= (int)M1) { overflow = true; break; }
                        K c = s - one[v] + 2 * one[u];
                        if (!seen.insert(c)) continue;
                        int occ = 0; for (int i = 0; i < n; i++) occ += get(c, i) > 0;
                        if (occ < 2) continue;
                        bool lose = true;
                        for (int a = 0; a < n && lose; a++) {
                            if (get(c, a) < 2) continue;
                            for (int b : adj[a]) { if (!prevT.has(c - 2 * one[a] + one[b])) { lose = false; break; } }
                        }
                        if (lose && curT.insert(c)) curL.push_back(c);
                    }
                    if (overflow) break;
                }
                if (overflow) break;
            }
            if (overflow) break;
            total += curL.size(); if ((long long)curL.size() > maxlayer) maxlayer = curL.size();
            if (!curL.empty()) {
                Lall = m; crit = curL; critAS = 0;
                for (K c : curL) { int h = 0; for (int i = 0; i < n; i++) h += get(c, i) > 1; if (h <= 1) critAS++; }
                if (critAS) LAS = m;
            }
            if (curL.empty() && m >= n) break;
            std::swap(prevL, curL); std::swap(prevT, curT);
            double el = std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
            if (el > tcap || total > totcap) { capped = true; break; }
        }
        double ms = 1000.0 * std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
        if (overflow) { printf("%s %d OVERFLOW_AT_MASS %d ms %.0f\n", name, n, m, ms); fflush(stdout); continue; }
        if (capped) { printf("%s %d CAPPED_AT_MASS %d cap 0 ms %.0f\n", name, n, m, ms); fflush(stdout); continue; }
        std::vector<std::vector<int>> rows; long long nonAS = 0; std::string rep = "-";
        for (K c : crit) { std::vector<int> r(n); int h = 0; for (int i = 0; i < n; i++) { r[i] = get(c, i); h += r[i] > 1; } rows.push_back(r); nonAS += h > 1; }
        std::sort(rows.begin(), rows.end());
        fprintf(cf, "%s %d", name, Lall);
        for (auto &r : rows) { fputc(' ', cf); for (int i = 0; i < n; i++) fprintf(cf, i ? ".%d" : "%d", r[i]); }
        fputc('\n', cf); fflush(cf);
        for (auto &r : rows) { int h = 0; for (int x : r) h += x > 1; if (h > 1) { rep.clear(); for (int i = 0; i < n; i++) { rep += std::to_string(r[i]); if (i + 1 < n) rep += '.'; } break; } }
        printf("%s %d Lall %d LAS %d crit %zu critAS %lld maxlayer %lld total %lld nonAS %s %s ms %.0f\n",
               name, n, Lall, LAS, crit.size(), critAS, maxlayer, total, rep.c_str(), LAS == Lall ? "ASH_OK" : "ASH_FAIL", ms);
        fflush(stdout);
    }
    return 0;
}
