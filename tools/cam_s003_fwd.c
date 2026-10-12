/* CAM-S003-01 forward exact layered DP for stacking and clearing.
 *
 * Every pebbling move lowers the size by exactly one, so for t>=2
 *   winS_t(c) = [|supp c|==1] or exists legal move c->c' with winS_{t-1}(c')
 *   winC_t(c) = exists legal move c->c' with winC_{t-1}(c'),  winC_1 = all.
 * Each layer is the full set of compositions of t into n parts, ranked by the
 * combinatorial number system on divider positions p_j = (c_0+..+c_j)+j.
 * Output: one JSON line per layer with exact counts and order-free fingerprints
 * of the losing sets (h(c)=sum c_i B^i mod 2^61-1; fingerprint=(sum h, sum h^2)).
 *
 * usage: cam_s003_fwd NAME N "a-b,c-d,..." TMAX [--stop]
 *   --stop: stop one layer after both defined thresholds are found.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <omp.h>

#define MAXN 16
#define MAXT 1200
typedef unsigned __int128 u128;
static const uint64_t MOD = (1ULL << 61) - 1, HB = 1000003ULL;

static int n, tmax, nadj[MAXN], adj[MAXN][MAXN];
static uint64_t *BIN[MAXT + MAXN + 2]; /* BIN[a][b] = C(a,b), b<=MAXN */

static uint64_t C(int a, int b) { return (b < 0 || a < b) ? 0 : BIN[a][b]; }
static uint64_t mulmod(uint64_t a, uint64_t b) { u128 r = (u128)a * b; uint64_t lo = (uint64_t)(r & MOD), hi = (uint64_t)(r >> 61); uint64_t s = lo + hi; return s >= MOD ? s - MOD : s; }
static uint64_t addmod(uint64_t a, uint64_t b) { uint64_t s = a + b; return s >= MOD ? s - MOD : s; }
static uint64_t hcfg(const int *c) { uint64_t h = 0; for (int i = n - 1; i >= 0; i--) h = addmod(mulmod(h, HB), (uint64_t)c[i]); return h; }

static uint64_t rank_of(const int *c) {
    uint64_t r = 0; int P = 0;
    for (int j = 0; j < n - 1; j++) { P += c[j]; r += C(P + j, j + 1); }
    return r;
}
static int bipartite(void) {
    int col[MAXN], q[MAXN], h = 0, tl = 0; for (int i = 0; i < n; i++) col[i] = -1;
    col[0] = 0; q[tl++] = 0;
    while (h < tl) { int u = q[h++]; for (int k = 0; k < nadj[u]; k++) { int v = adj[u][k]; if (col[v] < 0) { col[v] = 1 - col[u]; q[tl++] = v; } else if (col[v] == col[u]) return 0; } }
    return 1;
}
static int connected(void) {
    int seen[MAXN] = {0}, q[MAXN], h = 0, tl = 0; seen[0] = 1; q[tl++] = 0;
    while (h < tl) { int u = q[h++]; for (int k = 0; k < nadj[u]; k++) { int v = adj[u][k]; if (!seen[v]) { seen[v] = 1; q[tl++] = v; } } }
    return tl == n;
}

typedef struct { uint64_t ls, las, lc, lac, as_total, total, s1, s2, c1, c2; uint64_t minS, minAS, minC, minAC; } Acc;

static uint8_t *prev, *cur; /* bit0 = stack win, bit1 = clear win */

/* Evaluate all compositions with c[0] fixed: recursive fill of positions 1..n-1. */
static void eval_rec(int *c, int pos, int rem, int t, Acc *A) {
    if (pos == n - 1) {
        c[pos] = rem;
        uint64_t r = rank_of(c);
        int supp = 0, heavy = 0; for (int i = 0; i < n; i++) { supp += c[i] > 0; heavy += c[i] > 1; }
        int w = 0;
        if (supp == 1) w |= 1;
        if (t == 1) w = 3;
        else {
            for (int u = 0; u < n && w != 3; u++) {
                if (c[u] < 2) continue;
                for (int k = 0; k < nadj[u] && w != 3; k++) {
                    int v = adj[u][k];
                    c[u] -= 2; c[v] += 1;
                    w |= prev[rank_of(c)];
                    c[u] += 2; c[v] -= 1;
                }
            }
        }
        cur[r] = (uint8_t)w;
        int as = heavy <= 1;
        A->total++; A->as_total += as;
        if (!(w & 1)) { uint64_t h = hcfg(c); A->ls++; A->as_total += 0; A->s1 = addmod(A->s1, h); A->s2 = addmod(A->s2, mulmod(h, h)); if (r < A->minS) A->minS = r; if (as) { A->las++; if (r < A->minAS) A->minAS = r; } }
        if (!(w & 2)) { uint64_t h = hcfg(c); A->lc++; A->c1 = addmod(A->c1, h); A->c2 = addmod(A->c2, mulmod(h, h)); if (r < A->minC) A->minC = r; if (as) { A->lac++; if (r < A->minAC) A->minAC = r; } }
        return;
    }
    for (int k = 0; k <= rem; k++) { c[pos] = k; eval_rec(c, pos + 1, rem - k, t, A); }
}

static void unrank(uint64_t r, int t, int *c) { /* inverse of rank_of, positions in [0,t+n-2] */
    int pos[MAXN];
    for (int j = n - 2; j >= 0; j--) { int p = j; while (C(p + 1, j + 1) <= r) p++; pos[j] = p; r -= C(p, j + 1); }
    int prevP = 0;
    for (int j = 0; j < n - 1; j++) { int P = pos[j] - j; c[j] = P - prevP; prevP = P; }
    c[n - 1] = t - prevP;
}
static void print_cfg(FILE *f, uint64_t r, int t) {
    if (r == UINT64_MAX) { fprintf(f, "null"); return; }
    int c[MAXN]; unrank(r, t, c); fprintf(f, "[");
    for (int i = 0; i < n; i++) fprintf(f, "%s%d", i ? "," : "", c[i]);
    fprintf(f, "]");
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage\n"); return 2; }
    const char *name = argv[1]; n = atoi(argv[2]); tmax = atoi(argv[4]);
    int stop = argc > 5 && !strcmp(argv[5], "--stop");
    if (n < 1 || n > MAXN || tmax > MAXT) return 2;
    int ne = 0; char *s = strdup(argv[3]); char *tok = strtok(s, ",");
    while (tok) { int a, b; if (sscanf(tok, "%d-%d", &a, &b) == 2 && a != b) { int dup = 0; for (int k = 0; k < nadj[a]; k++) dup |= adj[a][k] == b; if (!dup) { adj[a][nadj[a]++] = b; adj[b][nadj[b]++] = a; ne++; } } tok = strtok(NULL, ","); }
    for (int a = 0; a <= tmax + n + 1; a++) { BIN[a] = calloc(MAXN + 2, 8); BIN[a][0] = 1; for (int b = 1; b <= MAXN + 1 && b <= a; b++) BIN[a][b] = BIN[a - 1][b - 1] + (b <= a - 1 ? BIN[a - 1][b] : 0); }
    int bip = bipartite(), con = connected();
    printf("{\"graph\":\"%s\",\"n\":%d,\"edges\":%d,\"bipartite\":%s,\"connected\":%s,\"tmax\":%d}\n", name, n, ne, bip ? "true" : "false", con ? "true" : "false", tmax);
    if (!con) return 1;
    int stackT = -1, clearT = -1;
    prev = calloc(1, 1);
    for (int t = 1; t <= tmax; t++) {
        uint64_t L = C(t + n - 1, n - 1);
        cur = malloc(L);
        Acc tot = {0}; tot.minS = tot.minAS = tot.minC = tot.minAC = UINT64_MAX;
        if (n == 1) { int c[1] = {t}; eval_rec(c, 0, t, t, &tot); }
        else {
            #pragma omp parallel
            {
                Acc A = {0}; A.minS = A.minAS = A.minC = A.minAC = UINT64_MAX;
                #pragma omp for schedule(dynamic, 1)
                for (int c0 = 0; c0 <= t; c0++) { int c[MAXN]; c[0] = c0; eval_rec(c, 1, t - c0, t, &A); }
                #pragma omp critical
                {
                    tot.total += A.total; tot.as_total += A.as_total; tot.ls += A.ls; tot.las += A.las; tot.lc += A.lc; tot.lac += A.lac;
                    tot.s1 = addmod(tot.s1, A.s1); tot.s2 = addmod(tot.s2, A.s2); tot.c1 = addmod(tot.c1, A.c1); tot.c2 = addmod(tot.c2, A.c2);
                    if (A.minS < tot.minS) tot.minS = A.minS; if (A.minAS < tot.minAS) tot.minAS = A.minAS;
                    if (A.minC < tot.minC) tot.minC = A.minC; if (A.minAC < tot.minAC) tot.minAC = A.minAC;
                }
            }
        }
        if (tot.total != L) { fprintf(stderr, "count mismatch\n"); return 3; }
        printf("{\"t\":%d,\"total\":%llu,\"as_total\":%llu,\"nonstack\":%llu,\"as_nonstack\":%llu,\"nonclear\":%llu,\"as_nonclear\":%llu,\"fp_stack\":[%llu,%llu],\"fp_clear\":[%llu,%llu],\"ex_stack\":",
               t, (unsigned long long)L, (unsigned long long)tot.as_total, (unsigned long long)tot.ls, (unsigned long long)tot.las, (unsigned long long)tot.lc, (unsigned long long)tot.lac,
               (unsigned long long)tot.s1, (unsigned long long)tot.s2, (unsigned long long)tot.c1, (unsigned long long)tot.c2);
        print_cfg(stdout, tot.minS, t); printf(",\"ex_as_stack\":"); print_cfg(stdout, tot.minAS, t);
        printf(",\"ex_clear\":"); print_cfg(stdout, tot.minC, t); printf(",\"ex_as_clear\":"); print_cfg(stdout, tot.minAC, t); printf("}\n");
        fflush(stdout);
        if (t >= 2 && stackT < 0 && tot.ls == 0) stackT = t;
        if (t >= 2 && !bip && clearT < 0 && tot.lc == 0) clearT = t;
        free(prev); prev = cur;
        if (stop && stackT > 0 && (bip || clearT > 0) && t >= (stackT > clearT ? stackT : clearT) + 1) break;
    }
    printf("{\"summary\":true,\"graph\":\"%s\",\"stack_threshold\":%d,\"clear_threshold\":%d}\n", name, stackT, bip ? -2 : clearT);
    return 0;
}
