// S016 Gate 1 second fresh check (Node): forward closures and winning sequences on G9.
// (a) full forward reachable set from c* and its image; assert closed, no single pile.
// (b) for every AS configuration of mass 14 and every configuration of mass 15,
//     a forward DFS finds a legal move sequence to a single pile; each sequence is
//     replayed by a separate legality replayer.  Usage: node s016_g9_forward.mjs
const edges = [[0,3],[0,5],[0,6],[1,4],[1,7],[1,8],[2,6],[2,8],[3,5],[3,6],[4,7],[4,8],[5,7],[6,8]];
const n = 9;
const nb = Array.from({length: n}, () => []);
for (const [a, b] of edges) { nb[a].push(b); nb[b].push(a); }
const key = c => c.join(',');
const occupied = c => c.filter(x => x > 0).length;
function* successors(c) {
  for (let u = 0; u < n; u++) if (c[u] >= 2) for (const v of nb[u]) {
    const d = c.slice(); d[u] -= 2; d[v] += 1; yield [d, u, v];
  }
}
// (a)
function closure(c0) {
  const seen = new Map([[key(c0), c0]]); const stack = [c0];
  while (stack.length) {
    const c = stack.pop();
    for (const [d] of successors(c)) { const k = key(d); if (!seen.has(k)) { seen.set(k, d); stack.push(d); } }
  }
  return seen;
}
for (const c0 of [[0,0,1,0,0,5,0,8,0], [0,0,1,0,0,8,0,5,0]]) {
  const S = closure(c0);
  let piles = 0;
  for (const c of S.values()) {
    if (occupied(c) === 1) piles++;
    for (const [d] of successors(c)) if (!S.has(key(d))) throw new Error('not closed');
  }
  console.log(`closure of (${c0}) states=${S.size} single_piles=${piles} ${piles === 0 ? 'NONSTACKABLE' : 'STACKABLE'}`);
}
// (b) memoised win search; win(c) returns a move list or null
const memo = new Map();
function win(c) {
  if (occupied(c) === 1) return [];
  const k = key(c);
  if (memo.has(k)) return memo.get(k);
  let res = null;
  for (const [d, u, v] of successors(c)) { const r = win(d); if (r) { res = [[u, v], ...r]; break; } }
  memo.set(k, res);
  return res;
}
function replay(c, seq) {
  const d = c.slice();
  for (const [u, v] of seq) {
    if (!nb[u].includes(v) || d[u] < 2) return false;
    d[u] -= 2; d[v] += 1;
  }
  return occupied(d) === 1;
}
function* comps(m, k) {
  if (k === 1) { yield [m]; return; }
  for (let a = 0; a <= m; a++) for (const r of comps(m - a, k - 1)) yield [a, ...r];
}
const isAS = c => c.filter(x => x > 1).length <= 1;
let as14 = 0, all15 = 0, bad = 0;
for (const c of comps(14, n)) if (isAS(c)) { as14++; const s = win(c); if (!s || !replay(c, s)) bad++; }
for (const c of comps(15, n)) { all15++; const s = win(c); if (!s || !replay(c, s)) bad++; }
console.log(`AS mass14 checked=${as14}; all mass15 checked=${all15}; failures=${bad}`);
console.log(bad === 0 && as14 === 2304 && all15 === 490314 ? 'G9_FORWARD_OK' : 'G9_FORWARD_FAIL');
