// S016 CAM-S016-04(i): bare-definition CLEAR truth table on G9, masses 1..TOP.
// Clearable configurations of mass m are the backward closure of the nine mass-1
// configurations e_v under reverse moves d -> d - e_v + 2e_u (uv an edge, d_v>=1):
// a forward move lowers mass by exactly one, so c (mass m>=2) is clearable iff some
// forward move leads to a clearable configuration of mass m-1.  No loser recursion,
// no candidate lemma, no single-pile winners (stacked != cleared above mass 1).
// Usage: s016_g9_clear_reverse [TOP]   (default 16)
use std::collections::HashSet;

const N: usize = 9;
const B: u64 = 17;

fn enc(c: &[u64; N]) -> u64 {
    c.iter().rev().fold(0, |x, &a| x * B + a)
}
fn dec(mut x: u64) -> [u64; N] {
    let mut c = [0u64; N];
    for v in 0..N {
        c[v] = x % B;
        x /= B;
    }
    c
}
fn is_as(c: &[u64; N]) -> bool {
    c.iter().filter(|&&a| a > 1).count() <= 1
}
// all compositions of m into N parts, by recursion (different from the Gate 1 odometer)
fn comps(m: u64, i: usize, c: &mut [u64; N], out: &mut Vec<[u64; N]>) {
    if i == N - 1 {
        c[i] = m;
        out.push(*c);
        return;
    }
    for a in 0..=m {
        c[i] = a;
        comps(m - a, i + 1, c, out);
    }
    c[i] = 0;
}

fn main() {
    let top: u64 = std::env::args().nth(1).map(|s| s.parse().unwrap()).unwrap_or(16);
    assert!(top <= 16);
    let edges = [(0, 3), (0, 5), (0, 6), (1, 4), (1, 7), (1, 8), (2, 6), (2, 8), (3, 5), (3, 6), (4, 7), (4, 8), (5, 7), (6, 8)];
    let mut adj = vec![Vec::new(); N];
    for &(a, b) in &edges {
        adj[a].push(b);
        adj[b].push(a);
    }
    // non-bipartite: 0-3-5 is a triangle
    assert!(adj[0].contains(&3) && adj[3].contains(&5) && adj[5].contains(&0));
    let mut w: Vec<HashSet<u64>> = vec![HashSet::new(); (top + 1) as usize];
    for v in 0..N {
        let mut c = [0u64; N];
        c[v] = 1;
        w[1].insert(enc(&c));
    }
    for m in 2..=top as usize {
        let mut cur = HashSet::new();
        for &x in &w[m - 1] {
            let d = dec(x);
            for v in 0..N {
                if d[v] >= 1 {
                    for &u in &adj[v] {
                        let mut c = d;
                        c[v] -= 1;
                        c[u] += 2;
                        cur.insert(enc(&c));
                    }
                }
            }
        }
        w[m] = cur;
    }
    let mut los: Vec<Vec<[u64; N]>> = vec![Vec::new(); (top + 1) as usize];
    println!("mass total clearable losers AS_losers");
    for m in 1..=top as usize {
        let mut all = Vec::new();
        comps(m as u64, 0, &mut [0; N], &mut all);
        for &x in &w[m] {
            assert_eq!(dec(x).iter().sum::<u64>(), m as u64);
        }
        let l: Vec<[u64; N]> = all.iter().filter(|c| !w[m].contains(&enc(c))).cloned().collect();
        assert_eq!(all.len(), w[m].len() + l.len());
        println!("{} {} {} {} {}", m, all.len(), w[m].len(), l.len(), l.iter().filter(|c| is_as(c)).count());
        los[m] = l;
    }
    for m in 13..=top as usize {
        for c in &los[m] {
            println!("loser {} {:?} AS={}", m, c, is_as(c));
        }
    }
    if top >= 15 {
        let cstar = [0u64, 0, 1, 0, 0, 5, 0, 8, 0];
        let image = [0u64, 0, 1, 0, 0, 8, 0, 5, 0];
        let k1 = los[14].len() == 2 && los[14].contains(&cstar) && los[14].contains(&image);
        let k2 = los[15].is_empty();
        let k3 = los[14].iter().all(|c| !is_as(c));
        let k4 = (2..=14).all(|m| !los[m].is_empty());
        let las = (1..=top as usize).filter(|&m| los[m].iter().any(is_as)).max().unwrap();
        println!("K1c {} K2c {} K3c {} K4c {} L_all=14 L_AS={} clear=15", k1, k2, k3, k4, las);
        if k1 && k2 && k3 && k4 && las == 13 {
            println!("G9_CLEAR_REVERSE_OK");
        }
    }
}
