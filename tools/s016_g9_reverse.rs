// S016 Gate 1 independent checker for the G9 STACK counterexample.
// Backward closure of all single piles under reverse moves, by mass layer.
// A forward move u->v (c_u>=2) gives c-2e_u+e_v and lowers mass by one, so
// a configuration of mass m is stackable iff it is a single pile or it is
// d-e_v+2e_u for a stackable d of mass m-1 with d_v>=1 and uv an edge.
// Usage: s016_g9_reverse [TOP]   (default TOP=16)
use std::collections::HashSet;

const N: usize = 9;
const B: u64 = 17; // digit base; every coordinate <= TOP <= 16

fn decode_g6(s: &str) -> (usize, Vec<(usize, usize)>) {
    let b: Vec<u8> = s.bytes().map(|x| x - 63).collect();
    let n = b[0] as usize;
    let mut bits = Vec::new();
    for x in &b[1..] {
        for k in (0..6).rev() {
            bits.push((x >> k) & 1);
        }
    }
    let mut edges = Vec::new();
    let mut p = 0;
    for j in 1..n {
        for i in 0..j {
            if bits[p] == 1 {
                edges.push((i, j));
            }
            p += 1;
        }
    }
    (n, edges)
}

fn enc(c: &[u64; N]) -> u64 {
    let mut x = 0;
    for v in (0..N).rev() {
        x = x * B + c[v];
    }
    x
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

// every composition of m into N nonnegative parts, odometer order
fn compositions(m: u64, f: &mut dyn FnMut(&[u64; N])) {
    let mut c = [0u64; N];
    c[N - 1] = m;
    loop {
        f(&c);
        // find rightmost position i<N-1 that can be incremented: move one unit
        // from the tail mass into position i, zeroing positions i+1..N-2
        let mut i = N - 1;
        loop {
            if i == 0 {
                return;
            }
            i -= 1;
            let tail: u64 = c[i + 1..].iter().sum();
            if tail > 0 {
                c[i] += 1;
                for k in i + 1..N {
                    c[k] = 0;
                }
                c[N - 1] = tail - 1;
                break;
            }
        }
    }
}

fn main() {
    let top: u64 = std::env::args().nth(1).map(|s| s.parse().unwrap()).unwrap_or(16);
    assert!(top <= 16);
    let (n, mut edges) = decode_g6("HCQTaXi");
    assert_eq!(n, N);
    edges.sort();
    let mut stated = vec![(0, 3), (0, 5), (0, 6), (1, 4), (1, 7), (1, 8), (2, 6), (2, 8), (3, 5), (3, 6), (4, 7), (4, 8), (5, 7), (6, 8)];
    stated.sort();
    assert_eq!(edges, stated, "graph6 decode differs from stated edge list");
    println!("graph6 HCQTaXi decodes to the stated 14-edge list: OK");
    let sigma = [1usize, 0, 2, 4, 3, 7, 8, 5, 6];
    let eset: HashSet<(usize, usize)> = edges.iter().cloned().collect();
    for &(a, b) in &edges {
        let (x, y) = (sigma[a].min(sigma[b]), sigma[a].max(sigma[b]));
        assert!(eset.contains(&(x, y)));
    }
    println!("map 0<->1,3<->4,5<->7,6<->8 (2 fixed) is an automorphism: OK");
    let mut adj: Vec<Vec<usize>> = vec![Vec::new(); N];
    for &(a, b) in &edges {
        adj[a].push(b);
        adj[b].push(a);
    }

    // W[m] = stackable configurations of mass m
    let mut w: Vec<HashSet<u64>> = vec![HashSet::new(); (top + 1) as usize];
    for m in 1..=top {
        let mut cur: HashSet<u64> = HashSet::new();
        for v in 0..N {
            let mut c = [0u64; N];
            c[v] = m;
            cur.insert(enc(&c));
        }
        if m >= 2 {
            for &x in &w[(m - 1) as usize] {
                let d = dec(x);
                for v in 0..N {
                    if d[v] == 0 {
                        continue;
                    }
                    for &u in &adj[v] {
                        let mut c = d;
                        c[v] -= 1;
                        c[u] += 2;
                        cur.insert(enc(&c));
                    }
                }
            }
        }
        w[m as usize] = cur;
    }

    let mut losers_by_mass: Vec<Vec<[u64; N]>> = vec![Vec::new(); (top + 1) as usize];
    println!("mass total stackable losers AS_losers");
    for m in 1..=top {
        let mut total = 0u64;
        let mut los = Vec::new();
        let wm = &w[m as usize];
        compositions(m, &mut |c: &[u64; N]| {
            total += 1;
            if !wm.contains(&enc(c)) {
                los.push(*c);
            }
        });
        // every member of W[m] must be a genuine mass-m configuration
        for &x in wm {
            assert_eq!(dec(x).iter().sum::<u64>(), m);
        }
        assert_eq!(total as usize, wm.len() + los.len());
        let mut binom = 1u64; // C(m+8, 8)
        for k in 1..=8u64 {
            binom = binom * (m + k) / k;
        }
        assert_eq!(total, binom);
        let asl = los.iter().filter(|c| is_as(c)).count();
        println!("{} {} {} {} {}", m, total, wm.len(), los.len(), asl);
        losers_by_mass[m as usize] = los;
    }
    for m in 13..=top {
        for c in &losers_by_mass[m as usize] {
            let s: Vec<String> = c.iter().map(|a| a.to_string()).collect();
            println!("loser {} ({}) AS={}", m, s.join(","), is_as(c));
        }
    }
    if top >= 15 {
        let cstar = [0u64, 0, 1, 0, 0, 5, 0, 8, 0];
        let image = [0u64, 0, 1, 0, 0, 8, 0, 5, 0];
        let l14 = &losers_by_mass[14];
        let k1 = l14.len() == 2 && l14.contains(&cstar) && l14.contains(&image) && !is_as(&cstar) && !is_as(&image);
        let k2 = losers_by_mass[15].is_empty();
        let k3 = l14.iter().all(|c| !is_as(c));
        let expect = [36usize, 128, 383, 930, 1862, 2887, 3280, 2510, 1301, 473, 124, 21, 2];
        let k4 = (2..=14).all(|m| losers_by_mass[m].len() == expect[m - 2]);
        let l_as = (1..=top as usize).filter(|&m| losers_by_mass[m].iter().any(is_as)).max().unwrap();
        println!("K1 {}", if k1 { "PASS" } else { "FAIL" });
        println!("K2 {}", if k2 { "PASS" } else { "FAIL" });
        println!("K3 {}", if k3 { "PASS" } else { "FAIL" });
        println!("K4 {}", if k4 { "PASS" } else { "FAIL" });
        println!("L_all=14 L_AS={} stack=15", l_as);
        if k1 && k2 && k3 && k4 && l_as == 13 {
            println!("G9_REVERSE_OK");
        }
    }
}
