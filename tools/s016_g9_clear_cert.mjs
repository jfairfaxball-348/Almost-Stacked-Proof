// S016 CAM-S016-04(ii) certificate producer (Node): for every AS configuration of mass 14
// and every configuration of mass 15 on G9, a legal move sequence ending at total mass 1.
// Output lines "c0.c1...c8 u>v u>v ..." (one per configuration), written to stdout.
// usage: node s016_g9_clear_cert.mjs > cert.txt   (then xz)
const edges = [[0,3],[0,5],[0,6],[1,4],[1,7],[1,8],[2,6],[2,8],[3,5],[3,6],[4,7],[4,8],[5,7],[6,8]];
const n = 9, nb = Array.from({length: n}, () => []);
for (const [a, b] of edges) { nb[a].push(b); nb[b].push(a); }
const memo = new Map();
function win(c, mass) {
  if (mass === 1) return [];
  const k = c.join('.');
  if (memo.has(k)) return memo.get(k);
  let res = null;
  for (let u = 0; u < n && !res; u++) if (c[u] >= 2) for (const v of nb[u]) {
    c[u] -= 2; c[v] += 1; const r = win(c, mass - 1); c[u] += 2; c[v] -= 1;
    if (r) { res = [`${u}>${v}`, ...r]; break; }
  }
  memo.set(k, res);
  return res;
}
const out = [];
function* comps(m, k) { if (k === 1) { yield [m]; return; } for (let a = 0; a <= m; a++) for (const r of comps(m - a, k - 1)) yield [a, ...r]; }
let fails = 0;
for (const m of [14, 15]) for (const c of comps(m, n)) {
  if (m === 14 && c.filter(x => x > 1).length > 1) continue;
  const s = win(c.slice(), m);
  if (!s) { fails++; process.stderr.write(`NO_SEQUENCE ${c.join('.')}\n`); continue; }
  out.push(`${c.join('.')} ${s.join(' ')}`);
}
process.stdout.write(out.join('\n') + '\n');
process.stderr.write(`lines ${out.length} fails ${fails}\n`);
