/* CAM-S003-01 independent reverse-predecessor exact solver (cold check of cam_s003_fwd).
 *
 * Win sets are built upward: W_1 = all size-1 configurations (both goals);
 * stack:  W_t = {singleton-support size t} U {d + 2e_u - e_v : d in W_{t-1}, uv edge, d(v)>=1}
 * clear:  W_t = {d + 2e_u - e_v : d in W_{t-1}, uv edge, d(v)>=1}
 * (p = d + 2e_u - e_v is exactly the configuration with p(u)>=2 whose move u=>v gives d).
 * Ranking is lexicographic with a count table N[k][m] built by the recurrence
 * N[1][m]=1, N[k][m]=sum_{j<=m} N[k-1][m-j]; no binomial formula and no shared code.
 * Same output fingerprint definition as the forward tool, computed independently.
 *
 * usage: cam_s003_rev NAME N "a-b,..." TMAX
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define MAXN 16
#define MAXT 1200
static int n, tmax, E, eu[256], ev[256];
static uint64_t N[MAXN + 1][MAXT + 2], CUM[MAXN + 1][MAXT + 2]; /* CUM[k][m] = sum_{j<=m} N[k][j] */
static const uint64_t P61 = 2305843009213693951ULL;

static uint64_t mm(uint64_t a, uint64_t b) { unsigned __int128 r = (unsigned __int128)a * b; r = (r & P61) + (r >> 61); r = (r & P61) + (r >> 61); return (uint64_t)(r >= P61 ? r - P61 : r); }

/* lexicographic rank among compositions of t into n parts (first coordinate most significant, larger first coordinate later) */
static uint64_t lexrank(const int *c, int t) {
    uint64_t r = 0; int rem = t;
    for (int i = 0; i < n - 1; i++) {
        int k = n - 1 - i;           /* parts remaining after position i */
        /* compositions with smaller value x<c[i] at position i: sum_{x<c[i]} N[k][rem-x] */
        if (c[i] > 0) r += CUM[k][rem] - (rem - c[i] >= 0 ? CUM[k][rem - c[i]] : 0);
        rem -= c[i];
    }
    return r;
}
static int next_comp(int *c, int t) { /* advance in lexicographic order; return 0 when done */
    /* find rightmost i<n-1 such that c[n-1]>0 among suffix: standard: move one unit from tail to position i */
    int tail = c[n - 1];
    if (n == 1) return 0;
    int i = n - 2;
    while (i >= 0 && tail == 0) { tail += c[i]; c[i] = 0; i--; /* unreachable when c[n-1]>0 */ }
    /* now c[n-1] (stored in tail) > 0 or i<0 */
    if (i < 0) return 0;
    /* increment c[i], put remaining tail-1 at last position */
    c[n - 1] = 0;
    c[i] += 1; c[n - 1] = tail - 1;
    (void)t; return 1;
}

int main(int argc, char **argv) {
    if (argc < 5) return 2;
    const char *name = argv[1]; n = atoi(argv[2]); tmax = atoi(argv[4]);
    char *s = strdup(argv[3]); char *tok = strtok(s, ",");
    while (tok) { int a, b; if (sscanf(tok, "%d-%d", &a, &b) == 2 && a != b) { int dup = 0; for (int k = 0; k < E; k++) dup |= (eu[k] == a && ev[k] == b) || (eu[k] == b && ev[k] == a); if (!dup) { eu[E] = a; ev[E] = b; E++; } } tok = strtok(NULL, ","); }
    for (int m = 0; m <= tmax + 1; m++) N[1][m] = 1;
    for (int k = 2; k <= n; k++) for (int m = 0; m <= tmax + 1; m++) { uint64_t sum = 0; for (int j = 0; j <= m; j++) sum += N[k - 1][m - j]; N[k][m] = sum; }
    for (int k = 1; k <= n; k++) { uint64_t sum = 0; for (int m = 0; m <= tmax + 1; m++) { sum += N[k][m]; CUM[k][m] = sum; } }
    printf("{\"graph\":\"%s\",\"n\":%d,\"edges\":%d,\"tool\":\"rev\"}\n", name, n, E);
    uint8_t *prevS = NULL, *prevC = NULL;
    for (int t = 1; t <= tmax; t++) {
        uint64_t L = N[n][t];
        uint8_t *S = calloc(L, 1), *Cl = calloc(L, 1);
        int c[MAXN];
        if (t == 1) { memset(S, 1, L); memset(Cl, 1, L); }
        else {
            for (int v = 0; v < n; v++) { memset(c, 0, sizeof c); c[v] = t; S[lexrank(c, t)] = 1; }
            uint64_t Lp = N[n][t - 1];
            memset(c, 0, sizeof c); c[n - 1] = t - 1; /* lexicographically first: all mass at the end */
            uint64_t idx = 0;
            do {
                uint64_t r = lexrank(c, t - 1);
                if (r != idx) { fprintf(stderr, "rank/enumeration mismatch\n"); return 3; }
                if (prevS[r] || prevC[r]) {
                    for (int k = 0; k < E; k++) for (int o = 0; o < 2; o++) {
                        int u = o ? ev[k] : eu[k], v = o ? eu[k] : ev[k];
                        if (c[v] < 1) continue;
                        c[u] += 2; c[v] -= 1;
                        uint64_t pr = lexrank(c, t);
                        if (prevS[r]) S[pr] = 1;
                        if (prevC[r]) Cl[pr] = 1;
                        c[u] -= 2; c[v] += 1;
                    }
                }
                idx++;
            } while (next_comp(c, t - 1));
            if (idx != Lp) { fprintf(stderr, "layer size mismatch\n"); return 3; }
        }
        /* count losers and fingerprints on layer t */
        uint64_t ls = 0, las = 0, lc = 0, lac = 0, ast = 0, s1 = 0, s2 = 0, c1 = 0, c2 = 0, idx = 0;
        memset(c, 0, sizeof c); c[n - 1] = t;
        do {
            uint64_t r = lexrank(c, t);
            int heavy = 0; for (int i = 0; i < n; i++) heavy += c[i] > 1;
            int as = heavy <= 1; ast += as;
            uint64_t h = 0; for (int i = n - 1; i >= 0; i--) { h = mm(h, 1000003ULL) + (uint64_t)c[i]; if (h >= P61) h -= P61; }
            if (!S[r]) { ls++; las += as; s1 = (s1 + h) % P61; s2 = (s2 + mm(h, h)) % P61; }
            if (!Cl[r]) { lc++; lac += as; c1 = (c1 + h) % P61; c2 = (c2 + mm(h, h)) % P61; }
            idx++;
        } while (next_comp(c, t));
        if (idx != L) { fprintf(stderr, "count mismatch\n"); return 3; }
        printf("{\"t\":%d,\"total\":%llu,\"as_total\":%llu,\"nonstack\":%llu,\"as_nonstack\":%llu,\"nonclear\":%llu,\"as_nonclear\":%llu,\"fp_stack\":[%llu,%llu],\"fp_clear\":[%llu,%llu]}\n",
               t, (unsigned long long)L, (unsigned long long)ast, (unsigned long long)ls, (unsigned long long)las, (unsigned long long)lc, (unsigned long long)lac,
               (unsigned long long)s1, (unsigned long long)s2, (unsigned long long)c1, (unsigned long long)c2);
        fflush(stdout);
        free(prevS); free(prevC); prevS = S; prevC = Cl;
    }
    return 0;
}
