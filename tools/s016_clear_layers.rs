// S016 Gate 2 producer: exact losing-layer recursion for CLEAR (default) or STACK.
// Lemmas C4-C6 of research/S016_CLEAR.md.  Lose(1)=empty; Cand(t) = 0/1 vectors of
// mass t (t<=n) plus s+2e_u-e_v for s in Lose(t-1), uv an edge, s_v>=1; c in Cand(t)
// loses iff it has no legal move (and, for STACK, is not a single pile) or every
// legal successor lies in Lose(t-1).  Halts at the first empty layer (t>n by C1).
//
// usage: s016_clear_layers MODE THREADS SECONDS LAYERCAP CRITFILE < graphs
//   MODE clear|stack; graphs lines "name n a-b,c-d,..." ; one output line per graph:
//   name n MODE status Lall LAS crit critAS maxlayer total fingerprint
//   status: ASH_OK | ASH_FAIL | BIPARTITE_SKIP | DISCONNECTED_SKIP | CAP_UNKNOWN | OVERFLOW_UNKNOWN
// Coordinates are packed in a u128 with w=floor(128/n) bits each (2<=n<=16); a coordinate
// that would exceed 2^w-2 aborts the graph as OVERFLOW_UNKNOWN.
use std::collections::HashSet;
use std::hash::{BuildHasherDefault, Hasher};
use std::io::{BufRead, Write};
use std::sync::{Arc, Mutex};
use std::time::Instant;

#[derive(Default)]
struct Fx(u64);
impl Hasher for Fx {
    fn finish(&self) -> u64 {
        self.0
    }
    fn write(&mut self, _: &[u8]) {
        unreachable!()
    }
    fn write_u128(&mut self, x: u128) {
        let a = (x as u64) ^ ((x >> 64) as u64).rotate_left(29);
        self.0 = (a ^ (a >> 31)).wrapping_mul(0x9E37_79B9_7F4A_7C15);
        self.0 ^= self.0 >> 29;
    }
}
type Set = HashSet<u128, BuildHasherDefault<Fx>>;

struct G {
    n: usize,
    w: u32,
    mask: u128,
    adj: Vec<Vec<usize>>,
    edges: Vec<(usize, usize)>,
}

impl G {
    #[inline]
    fn get(&self, k: u128, i: usize) -> u128 {
        (k >> (self.w * i as u32)) & self.mask
    }
    #[inline]
    fn unit(&self, i: usize) -> u128 {
        1u128 << (self.w * i as u32)
    }
    fn is_as(&self, k: u128) -> bool {
        (0..self.n).filter(|&i| self.get(k, i) > 1).count() <= 1
    }
    fn fmt(&self, k: u128) -> String {
        (0..self.n).map(|i| self.get(k, i).to_string()).collect::<Vec<_>>().join(".")
    }
}

enum Outcome {
    Done { lall: usize, las: usize, crit: Vec<u128>, maxlayer: usize, total: usize },
    Cap,
    Overflow,
}

fn run(g: &G, stack: bool, secs: f64, cap: usize) -> Outcome {
    let n = g.n;
    let maxc = g.mask - 1;
    let t0 = Instant::now();
    let mut prev: Set = Set::default();
    let mut las = 0usize;
    let mut maxlayer = 0usize;
    let mut total = 0usize;
    let mut t = 2usize;
    loop {
        let mut cand: Set = Set::default();
        if t <= n {
            for m in 0u32..(1u32 << n) {
                if m.count_ones() as usize == t {
                    let mut k = 0u128;
                    for i in 0..n {
                        if m >> i & 1 == 1 {
                            k += g.unit(i);
                        }
                    }
                    cand.insert(k);
                }
            }
        }
        for &s in &prev {
            for &(a, b) in &g.edges {
                for &(u, v) in &[(a, b), (b, a)] {
                    if g.get(s, v) >= 1 {
                        if g.get(s, u) + 2 > maxc {
                            return Outcome::Overflow;
                        }
                        cand.insert(s + 2 * g.unit(u) - g.unit(v));
                    }
                }
            }
        }
        let mut cur: Set = Set::default();
        for &c in &cand {
            let occ = (0..n).filter(|&i| g.get(c, i) > 0).count();
            if stack && occ == 1 {
                continue; // single pile: stacked, a winner
            }
            let mut lose = true;
            'mv: for u in 0..n {
                if g.get(c, u) >= 2 {
                    for &v in &g.adj[u] {
                        if !prev.contains(&(c - 2 * g.unit(u) + g.unit(v))) {
                            lose = false;
                            break 'mv;
                        }
                    }
                }
            }
            if lose {
                cur.insert(c);
            }
        }
        if cur.is_empty() {
            let mut crit: Vec<u128> = prev.into_iter().collect();
            crit.sort();
            return Outcome::Done { lall: t - 1, las, crit, maxlayer, total };
        }
        if cur.iter().any(|&c| g.is_as(c)) {
            las = t;
        }
        maxlayer = maxlayer.max(cur.len());
        total += cur.len();
        if cur.len() > cap || t0.elapsed().as_secs_f64() > secs {
            return Outcome::Cap;
        }
        prev = cur;
        t += 1;
    }
}

fn bipartite_connected(g: &G) -> (bool, bool) {
    let mut col = vec![-1i32; g.n];
    col[0] = 0;
    let mut q = vec![0usize];
    let mut bip = true;
    while let Some(x) = q.pop() {
        for &y in &g.adj[x] {
            if col[y] < 0 {
                col[y] = 1 - col[x];
                q.push(y);
            } else if col[y] == col[x] {
                bip = false;
            }
        }
    }
    (col.iter().all(|&c| c >= 0), bip)
}

fn main() {
    let a: Vec<String> = std::env::args().collect();
    let stack = match a[1].as_str() {
        "clear" => false,
        "stack" => true,
        _ => panic!("MODE"),
    };
    let threads: usize = a[2].parse().unwrap();
    let secs: f64 = a[3].parse().unwrap();
    let cap: usize = a[4].parse().unwrap();
    let critfile = a[5].clone();
    let lines: Vec<String> = std::io::stdin().lock().lines().map(|l| l.unwrap()).filter(|l| !l.trim().is_empty()).collect();
    let lines = Arc::new(lines);
    let next = Arc::new(Mutex::new(0usize));
    let results: Arc<Mutex<Vec<Option<(String, String)>>>> = Arc::new(Mutex::new(vec![None; lines.len()]));
    let mut hs = Vec::new();
    for _ in 0..threads {
        let (lines, next, results) = (lines.clone(), next.clone(), results.clone());
        hs.push(std::thread::spawn(move || loop {
            let i = {
                let mut g = next.lock().unwrap();
                let i = *g;
                *g += 1;
                i
            };
            if i >= lines.len() {
                break;
            }
            let f: Vec<&str> = lines[i].split_whitespace().collect();
            let name = f[0];
            let n: usize = f[1].parse().unwrap();
            assert!(n >= 2 && n <= 16);
            let mut edges = Vec::new();
            if f.len() > 2 {
                for e in f[2].split(',') {
                    let p: Vec<usize> = e.split('-').map(|x| x.parse().unwrap()).collect();
                    assert!(p[0] != p[1] && p[0] < n && p[1] < n);
                    edges.push((p[0], p[1]));
                }
            }
            let mut adj = vec![Vec::new(); n];
            for &(x, y) in &edges {
                adj[x].push(y);
                adj[y].push(x);
            }
            let w = (128 / n) as u32;
            let mask = if w >= 64 { u64::MAX as u128 } else { (1u128 << w) - 1 };
            let g = G { n, w: w.min(64), mask, adj, edges };
            let (conn, bip) = bipartite_connected(&g);
            let mode = if stack { "stack" } else { "clear" };
            let (line, crit) = if !conn {
                (format!("{} {} {} DISCONNECTED_SKIP", name, n, mode), String::new())
            } else if bip && !stack {
                (format!("{} {} {} BIPARTITE_SKIP", name, n, mode), String::new())
            } else {
                match run(&g, stack, secs, cap) {
                    Outcome::Cap => (format!("{} {} {} CAP_UNKNOWN", name, n, mode), String::new()),
                    Outcome::Overflow => (format!("{} {} {} OVERFLOW_UNKNOWN", name, n, mode), String::new()),
                    Outcome::Done { lall, las, crit, maxlayer, total } => {
                        let cas = crit.iter().filter(|&&c| g.is_as(c)).count();
                        let mut strs: Vec<String> = crit.iter().map(|&c| g.fmt(c)).collect();
                        strs.sort();
                        let mut h: u64 = 1469598103934665603;
                        for s in &strs {
                            for b in s.bytes().chain(std::iter::once(b' ')) {
                                h ^= b as u64;
                                h = h.wrapping_mul(1099511628211);
                            }
                        }
                        let st = if las == lall { "ASH_OK" } else { "ASH_FAIL" };
                        (
                            format!("{} {} {} {} {} {} {} {} {} {} {:016x}", name, n, mode, st, lall, las, crit.len(), cas, maxlayer, total, h),
                            format!("{} {} {}\n", name, lall, strs.join(" ")),
                        )
                    }
                }
            };
            results.lock().unwrap()[i] = Some((line, crit));
        }));
    }
    for h in hs {
        h.join().unwrap();
    }
    let res = results.lock().unwrap();
    let out = std::io::stdout();
    let mut o = out.lock();
    let mut cf = std::fs::File::create(&critfile).unwrap();
    for r in res.iter() {
        let (l, c) = r.as_ref().unwrap();
        writeln!(o, "{}", l).unwrap();
        cf.write_all(c.as_bytes()).unwrap();
    }
}
