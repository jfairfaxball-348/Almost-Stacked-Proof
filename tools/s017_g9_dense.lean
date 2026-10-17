/-
S017 Milestone 1: independent cold re-check of the G9 CLEAR (and STACK) layers.
Dense forward dynamic programme over ALL configurations of masses 0..16 on 9 vertices.
Each mass layer is a flat array indexed by the lexicographic stars-and-bars rank.
No hash set, no candidate generation, no backward closure, no DFS.
Run: lean --run tools/s017_g9_dense.lean
-/

def N : Nat := 9
def MAXM : Nat := 16

/-- independent graph6 decoder (order < 63) -/
def decodeG6 (s : String) : Nat × List (Nat × Nat) := Id.run do
  let cs := s.toList.map (fun ch => ch.toNat - 63)
  let n := cs.head!
  let bits : Array Bool := Id.run do
    let mut b : Array Bool := #[]
    for x in cs.tail! do
      for k in [0:6] do
        b := b.push ((x >>> (5 - k)) % 2 == 1)
    return b
  let mut es : List (Nat × Nat) := []
  let mut idx := 0
  for j in [1:n] do
    for i in [0:j] do
      if bits[idx]! then es := es ++ [(i, j)]
      idx := idx + 1
  return (n, es)

def stated : List (Nat × Nat) :=
  [(0,3),(0,5),(0,6),(1,4),(1,7),(1,8),(2,6),(2,8),(3,5),(3,6),(4,7),(4,8),(5,7),(6,8)]

/-- binom table C(a,b) for a <= 40 by Pascal -/
def binom (a b : Nat) : Nat := Id.run do
  if b > a then return 0
  let mut row : Array Nat := #[1]
  for _ in [0:a] do
    let mut nr : Array Nat := #[1]
    for k in [1:row.size] do
      nr := nr.push (row[k-1]! + row[k]!)
    nr := nr.push 1
    row := nr
  return row[b]!

/-- number of compositions of r into k parts (k >= 1) -/
def comps (tbl : Array (Array Nat)) (r k : Nat) : Nat :=
  if k == 0 then (if r == 0 then 1 else 0) else tbl[r + k - 1]![k - 1]!

/-- lexicographic rank of a composition c (Array of length N) of mass m -/
def rank (tbl : Array (Array Nat)) (c : Array Nat) (m : Nat) : Nat := Id.run do
  let mut r := 0
  let mut rem := m
  for i in [0:N-1] do
    for x in [0:c[i]!] do
      r := r + comps tbl (rem - x) (N - 1 - i)
    rem := rem - c[i]!
  return r

/-- all compositions of m into k parts in lexicographic order -/
partial def enumComps (m k : Nat) : Array (Array Nat) :=
  if k == 1 then #[#[m]] else Id.run do
    let mut out : Array (Array Nat) := #[]
    for x in [0:m+1] do
      for rest in enumComps (m - x) (k - 1) do
        out := out.push (#[x] ++ rest)
    return out

def isAS (c : Array Nat) : Bool :=
  -- exists v0 with c u <= 1 for all u != v0  <=>  at most one entry >= 2
  (c.toList.filter (· ≥ 2)).length ≤ 1

def isPile (c : Array Nat) : Bool := (c.toList.filter (· ≠ 0)).length == 1

def showC (c : Array Nat) : String := "(" ++ ",".intercalate (c.toList.map toString) ++ ")"

def main : IO Unit := do
  let (n, es) := decodeG6 "HCQTaXi"
  if n != N then throw (IO.userError "order")
  -- graph6 lists edges column by column; compare as sets (same length, mutual inclusion)
  if !(es.length == stated.length && es.all (stated.contains ·) && stated.all (es.contains ·)) then
    throw (IO.userError s!"edges differ {es}")
  let adj : List (Nat × Nat) := es ++ es.map (fun (a, b) => (b, a))
  -- automorphism 0<->1, 3<->4, 5<->7, 6<->8, 2 fixed
  let perm : Array Nat := #[1,0,2,4,3,7,8,5,6]
  let es' := es.map (fun (a, b) => let x := perm[a]!; let y := perm[b]!; if x < y then (x, y) else (y, x))
  if !(es'.all (fun e => es.contains e)) || es'.length != es.length then throw (IO.userError "automorphism")
  let tbl : Array (Array Nat) := (List.range 41).toArray.map (fun a => (List.range 41).toArray.map (fun b => binom a b))
  IO.println s!"graph HCQTaXi decoded, n={n}, edges={es.length}, stated edges match, automorphism OK"
  -- win arrays per mass
  let mut stackPrev : Array Bool := #[]
  let mut clearPrev : Array Bool := #[]
  let mut stackLoseCnt : Array Nat := #[]
  let mut clearLoseCnt : Array Nat := #[]
  let mut stackASLoseCnt : Array Nat := #[]
  let mut clearASLoseCnt : Array Nat := #[]
  let mut clearLosers : Array (Nat × Array (Array Nat)) := #[]
  let mut stackLosers : Array (Nat × Array (Array Nat)) := #[]
  let mut as14 := 0
  for m in [0:MAXM+1] do
    let layer := enumComps m N
    if layer.size != comps tbl m N then throw (IO.userError s!"layer size {m}")
    let mut sw : Array Bool := Array.mkEmpty layer.size
    let mut cw : Array Bool := Array.mkEmpty layer.size
    let mut sl := 0; let mut cl := 0; let mut sal := 0; let mut cal := 0
    let mut cls : Array (Array Nat) := #[]
    let mut sls : Array (Array Nat) := #[]
    for j in [0:layer.size] do
      let c := layer[j]!
      if rank tbl c m != j then throw (IO.userError s!"rank {m} {j}")
      let mut s := isPile c
      let mut w := m == 1
      for (u, v) in adj do
        if c[u]! ≥ 2 then
          let d := (c.set! u (c[u]! - 2)).set! v (c[v]! + 1)
          let rd := rank tbl d (m - 1)
          if stackPrev[rd]! then s := true
          if clearPrev[rd]! then w := true
      sw := sw.push s
      cw := cw.push w
      if m == 14 && isAS c then as14 := as14 + 1
      if !s then
        sl := sl + 1
        if isAS c then sal := sal + 1
        if m ≥ 12 then sls := sls.push c
      if !w then
        cl := cl + 1
        if isAS c then cal := cal + 1
        if m ≥ 12 then cls := cls.push c
    stackPrev := sw; clearPrev := cw
    stackLoseCnt := stackLoseCnt.push sl; clearLoseCnt := clearLoseCnt.push cl
    stackASLoseCnt := stackASLoseCnt.push sal; clearASLoseCnt := clearASLoseCnt.push cal
    if m ≥ 12 then
      clearLosers := clearLosers.push (m, cls)
      stackLosers := stackLosers.push (m, sls)
    IO.println s!"mass {m}: total {layer.size} clear_losers {cl} clear_AS_losers {cal} stack_losers {sl} stack_AS_losers {sal}"
  for (m, l) in clearLosers do
    for c in l do IO.println s!"CLEAR_LOSER mass {m} {showC c} AS={isAS c}"
  for (m, l) in stackLosers do
    for c in l do IO.println s!"STACK_LOSER mass {m} {showC c} AS={isAS c}"
  let cstar : Array Nat := #[0,0,1,0,0,5,0,8,0]
  let cimg : Array Nat := #[0,0,1,0,0,8,0,5,0]
  let crit14 := (clearLosers.find? (·.1 == 14)).map (·.2) |>.getD #[]
  let scrit14 := (stackLosers.find? (·.1 == 14)).map (·.2) |>.getD #[]
  let k1c := crit14.size == 2 && crit14.contains cstar && crit14.contains cimg && !(isAS cstar) && !(isAS cimg)
  let k2c := clearLoseCnt[15]! == 0 && clearLoseCnt[16]! == 0
  let k3c := clearASLoseCnt[14]! == 0
  let expC : List Nat := [36,137,384,932,1863,2887,3280,2510,1301,473,124,21,2]
  let expCA : List Nat := [36,137,375,791,1185,1331,1116,734,391,177,60,10,0]
  let expS : List Nat := [36,128,383,930,1862,2887,3280,2510,1301,473,124,21,2]
  let k4c := (List.range 13).map (fun i => clearLoseCnt[i+2]!) == expC && (List.range 13).map (fun i => clearASLoseCnt[i+2]!) == expCA
  let k1 := scrit14.size == 2 && scrit14.contains cstar && scrit14.contains cimg
  let k2 := stackLoseCnt[15]! == 0 && stackLoseCnt[16]! == 0
  let k3 := stackASLoseCnt[14]! == 0
  let k4 := (List.range 13).map (fun i => stackLoseCnt[i+2]!) == expS
  IO.println s!"AS configurations of mass 14: {as14}"
  IO.println s!"CLEAR: K1c={k1c} K2c={k2c} K3c={k3c} K4c={k4c} clear=15:{k2c && clearLoseCnt[14]! > 0} L_all=14 L_AS=13:{clearASLoseCnt[13]! > 0 && k3c}"
  IO.println s!"STACK: K1={k1} K2={k2} K3={k3} K4={k4} stack=15:{k2 && stackLoseCnt[14]! > 0} L_AS=13:{stackASLoseCnt[13]! > 0 && k3}"
