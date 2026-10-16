/* CAM-S015-88 checker v3: s015_check.c with B=min(16,floor(128/n)) bits per coordinate,
 * OVERFLOW detection and LSD radix sort (8 passes of 16 bits) instead of qsort.
 * Original header follows.
 * CAM-S015-83 second compiled checker, written separately from the C++ producer.
 * Data structure: each losing layer is a SORTED, DEDUPLICATED array of packed
 * unsigned __int128 keys (12 bits per coordinate, n<=10, coordinate <=4095),
 * membership by binary search.  Candidates for mass t: all 0/1 vectors of
 * weight t (t<=n) and every p=q+2e_a-e_b with q losing at mass t-1, a~b, q_b>=1,
 * generated edge-by-edge over an explicit edge list (not adjacency lists).
 * p is kept iff >=2 sites occupied and every legal move of p lands in layer t-1.
 * Stop at the first empty layer with t>=n.  Prints per graph:
 *   name n Lall LAS crit critAS FNV64(sorted critical layer as text)  OK|OVER
 * and, with a third argument, writes the critical layer in the same text
 * format as the producer for set comparison.
 * usage: s015_check MAXSTATES SECONDS [critfile] < graphs
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
typedef unsigned __int128 K;
static int BB; static K MM;
static int n, E, ea[64], eb[64];

static int get(K k, int i) { return (int)((k >> (BB * i)) & MM); }
static K add(K k, int i, int d) { return d >= 0 ? k + ((K)d << (BB * i)) : k - ((K)(-d) << (BB * i)); }
static void rsort(K *a, long len) { K *t = malloc(sizeof(K) * (len ? len : 1)); static long cnt[65537]; for (int sh = 0; sh < 128; sh += 16) { memset(cnt, 0, sizeof cnt); for (long i = 0; i < len; i++) cnt[(int)((a[i] >> sh) & 0xFFFF) + 1]++; for (int j = 0; j < 65536; j++) cnt[j + 1] += cnt[j]; for (long i = 0; i < len; i++) t[cnt[(int)((a[i] >> sh) & 0xFFFF)]++] = a[i]; memcpy(a, t, sizeof(K) * len); } free(t); }
static int cmpk(const void *x, const void *y) { K a = *(const K *)x, b = *(const K *)y; return a < b ? -1 : a > b; }
static int has(const K *A, long len, K k) { long lo = 0, hi = len - 1; while (lo <= hi) { long m = (lo + hi) / 2; if (A[m] == k) return 1; if (A[m] < k) lo = m + 1; else hi = m - 1; } return 0; }
static int occ(K k) { int s = 0; for (int i = 0; i < n; i++) s += get(k, i) > 0; return s; }
static int heavy(K k) { int s = 0; for (int i = 0; i < n; i++) s += get(k, i) > 1; return s; }

int main(int argc, char **argv) {
    long cap = atol(argv[1]); double tcap = atof(argv[2]);
    FILE *cf = argc > 3 ? fopen(argv[3], "w") : NULL;
    char name[256], es[4096];
    while (scanf("%255s %d %4095s", name, &n, es) == 3) {
        E = 0;
        if (strcmp(es, "-")) { char *tok = strtok(es, ","); while (tok) { sscanf(tok, "%d-%d", &ea[E], &eb[E]); E++; tok = strtok(NULL, ","); } }
        BB = 128 / n; if (BB > 16) BB = 16; MM = (((K)1) << BB) - 1; int ovf = 0;
        clock_t t0 = clock();
        K *prev = NULL; long plen = 0; K *crit = NULL; long clen = 0;
        int Lall = -1, LAS = -1, t, over = 0;
        for (t = 2;; t++) {
            long cmax = plen * 2 * E + (1L << n) + 1, len = 0;
            if (cmax > cap) { over = 1; break; }
            K *cand = malloc(sizeof(K) * (cmax > 0 ? cmax : 1));
            if (t <= n) for (long mask = 0; mask < (1L << n); mask++) if (__builtin_popcountl(mask) == t) { K k = 0; for (int i = 0; i < n; i++) if (mask >> i & 1) k = add(k, i, 1); cand[len++] = k; }
            for (long j = 0; j < plen; j++) for (int e = 0; e < E; e++) for (int o = 0; o < 2; o++) {
                int a = o ? eb[e] : ea[e], b = o ? ea[e] : eb[e];
                if (get(prev[j], b) < 1) continue;
                if (get(prev[j], a) + 2 >= (int)MM) { ovf = 1; continue; }
                cand[len++] = add(add(prev[j], a, 2), b, -1);
            }
            if (ovf) { free(cand); over = 2; break; }
            rsort(cand, len);
            long u = 0; for (long j = 0; j < len; j++) if (u == 0 || cand[j] != cand[u - 1]) cand[u++] = cand[j];
            long keep = 0;
            for (long j = 0; j < u; j++) {
                K p = cand[j]; if (occ(p) < 2) continue;
                int ok = 1;
                for (int e = 0; e < E && ok; e++) for (int o = 0; o < 2 && ok; o++) {
                    int a = o ? eb[e] : ea[e], b = o ? ea[e] : eb[e];
                    if (get(p, a) < 2) continue;
                    if (!has(prev, plen, add(add(p, a, -2), b, 1))) ok = 0;
                }
                if (ok) cand[keep++] = p;
            }
            free(prev); prev = cand; plen = keep;
            if (plen) {
                Lall = t; free(crit); crit = malloc(sizeof(K) * plen); memcpy(crit, prev, sizeof(K) * plen); clen = plen;
                for (long j = 0; j < plen; j++) if (heavy(prev[j]) <= 1) { LAS = t; break; }
            }
            if (!plen && t >= n) break;
            if ((double)(clock() - t0) / CLOCKS_PER_SEC > tcap) { over = 1; break; }
        }
        if (over) { printf("%s %d %s %d\n", name, n, over == 2 ? "OVERFLOW" : "OVER", t); fflush(stdout); free(prev); free(crit); continue; }
        /* text of critical layer in numeric-lexicographic order of coordinate tuples */
        long cas = 0; unsigned long long h = 1469598103934665603ULL;
        /* sort by coordinate tuple: coordinate 0 most significant */
        for (long i = 1; i < clen; i++) { K x = crit[i]; long j = i - 1;
            while (j >= 0) { int lt = 0, d = 0; for (int c = 0; c < n && !d; c++) { int A = get(crit[j], c), B = get(x, c); if (A != B) { d = 1; lt = B < A; } } if (!lt) break; crit[j + 1] = crit[j]; j--; }
            crit[j + 1] = x; }
        if (cf) fprintf(cf, "%s %d", name, Lall);
        for (long j = 0; j < clen; j++) {
            if (heavy(crit[j]) <= 1) cas++;
            char buf[128]; int L = 0;
            for (int i = 0; i < n; i++) L += sprintf(buf + L, i ? ".%d" : " %d", get(crit[j], i));
            for (int i = 0; i < L; i++) { h ^= (unsigned char)buf[i]; h *= 1099511628211ULL; }
            if (cf) fputs(buf, cf);
        }
        if (cf) fputc('\n', cf);
        printf("%s %d %d %d %ld %ld %016llx %s\n", name, n, Lall, LAS, clen, cas, h, LAS == Lall ? "ASH_OK" : "ASH_FAIL");
        fflush(stdout); free(prev); free(crit);
    }
    return 0;
}
