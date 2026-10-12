/* CAM-S003-01 T3: AS-only exact stackability search below a known stacking number.
 *
 * For a connected graph with KNOWN stack(G)=S (trees: TreeStack theorem stack=estim),
 * the AS-gap reformulation says ASH-stack(G) holds iff every t with n<t<S admits an
 * almost-stacked configuration of size t that is NOT stackable.  For each such t this
 * program enumerates AS configurations (pile vertex r, 0/1 pattern on the other
 * vertices, pile = t - |pattern|), decides stackability exactly by memoised DFS over
 * the finite move DAG (win(c) = supp(c) singleton OR some child wins), and stops at the
 * first losing one.  A t for which every AS configuration wins is reported as a GAP.
 * Memo key: counts packed 12 bits per vertex into 128 bits (n<=10, t<=4095).
 *
 * usage: cam_s003_as NAME N "a-b,..." S [TFROM]
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define MAXN 10
typedef unsigned __int128 key_t128;
static int n, nadj[MAXN], adj[MAXN][MAXN];

static key_t128 *K; static uint8_t *Vv; static uint64_t cap = 1ULL << 22, used = 0;
static uint64_t hsh(key_t128 k) { uint64_t a = (uint64_t)k, b = (uint64_t)(k >> 64); uint64_t x = a * 0x9E3779B97F4A7C15ULL ^ (b + 0x632BE59BD9B4E019ULL) * 0xC2B2AE3D27D4EB4FULL; x ^= x >> 29; x *= 0xBF58476D1CE4E5B9ULL; x ^= x >> 32; return x; }
static void grow(void);
static int get(key_t128 k) { uint64_t i = hsh(k) & (cap - 1); while (Vv[i]) { if (K[i] == k) return Vv[i] - 1; i = (i + 1) & (cap - 1); } return -1; }
static void put(key_t128 k, int v) { if (2 * (used + 1) > cap) grow(); uint64_t i = hsh(k) & (cap - 1); while (Vv[i]) { if (K[i] == k) { Vv[i] = (uint8_t)(v + 1); return; } i = (i + 1) & (cap - 1); } K[i] = k; Vv[i] = (uint8_t)(v + 1); used++; }
static void grow(void) {
    key_t128 *oK = K; uint8_t *oV = Vv; uint64_t oc = cap; cap <<= 1;
    K = malloc(cap * sizeof *K); Vv = calloc(cap, 1); if (!K || !Vv) { fprintf(stderr, "oom\n"); exit(4); }
    used = 0;
    for (uint64_t i = 0; i < oc; i++) if (oV[i]) { uint64_t j = hsh(oK[i]) & (cap - 1); while (Vv[j]) j = (j + 1) & (cap - 1); K[j] = oK[i]; Vv[j] = oV[i]; used++; }
    free(oK); free(oV);
}
static key_t128 pack(const int *c) { key_t128 k = 0; for (int i = 0; i < n; i++) k = (k << 12) | (key_t128)c[i]; return k; }

static int win(int *c) {
    int supp = 0; for (int i = 0; i < n; i++) supp += c[i] > 0;
    if (supp == 1) return 1;
    key_t128 k = pack(c); int m = get(k); if (m >= 0) return m;
    int w = 0;
    for (int u = 0; u < n && !w; u++) {
        if (c[u] < 2) continue;
        for (int j = 0; j < nadj[u] && !w; j++) { int v = adj[u][j]; c[u] -= 2; c[v]++; w = win(c); c[u] += 2; c[v]--; }
    }
    put(k, w); return w;
}

int main(int argc, char **argv) {
    if (argc < 5) return 2;
    const char *name = argv[1]; n = atoi(argv[2]); int S = atoi(argv[4]);
    int tfrom = argc > 5 ? atoi(argv[5]) : n + 1;
    if (n > MAXN || S > 4095) return 2;
    char *s = strdup(argv[3]); char *tok = strtok(s, ",");
    while (tok) { int a, b; if (sscanf(tok, "%d-%d", &a, &b) == 2) { adj[a][nadj[a]++] = b; adj[b][nadj[b]++] = a; } tok = strtok(NULL, ","); }
    K = malloc(cap * sizeof *K); Vv = calloc(cap, 1);
    printf("{\"graph\":\"%s\",\"n\":%d,\"known_stack\":%d,\"tool\":\"as\"}\n", name, n, S);
    int gaps = 0;
    for (int t = tfrom; t < S; t++) {
        int found = 0, c[MAXN]; long tested = 0;
        /* order: pile vertex r, then 0/1 patterns by decreasing popcount (more singles first) */
        for (int pc = n - 1; pc >= 0 && !found; pc--)
            for (int r = 0; r < n && !found; r++)
                for (int mask = 0; mask < (1 << n) && !found; mask++) {
                    if (mask >> r & 1) continue;
                    if (__builtin_popcount(mask) != pc || pc > t) continue;
                    int pile = t - pc;
                    for (int i = 0; i < n; i++) c[i] = (mask >> i & 1);
                    c[r] = pile;
                    tested++;
                    if (!win(c)) {
                        found = 1;
                        printf("{\"t\":%d,\"as_loser\":[", t);
                        for (int i = 0; i < n; i++) printf("%s%d", i ? "," : "", c[i]);
                        printf("],\"tested\":%ld,\"memo\":%llu}\n", tested, (unsigned long long)used);
                    }
                }
        if (!found) { gaps++; printf("{\"t\":%d,\"GAP\":true,\"tested\":%ld,\"memo\":%llu}\n", t, tested, (unsigned long long)used); }
        fflush(stdout);
    }
    printf("{\"summary\":true,\"graph\":\"%s\",\"gaps\":%d,\"memo\":%llu}\n", name, gaps, (unsigned long long)used);
    return 0;
}
