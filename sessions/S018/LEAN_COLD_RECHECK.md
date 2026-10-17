# S018 Milestone 3 - Lean cold re-check of the Challenge statements

Reviewed file: formal/Challenge.lean (197 lines; reviewed at its S017 bytes, then at the F1-fixed bytes, both sha256 in evidence/S018/HASHES.md), line by line, against research/ASH_SPEC.md (model, printed and critical forms), research/S003_AS_GAP_AND_ATTACKS.md (Lemma 2, Prop. 3, Thm 4) and research/S016_CLEAR.md. This is the human semantic check (do the Lean statements say what the programme claims?). Whether the Solution proves exactly these statements is the Comparator's job (Milestone 2, sessions/S018/LEAN_ASSURANCE.md), not this review. The S017 stand-in `tools/s017_challenge_bridge.py` is not relied on.

## Definitions (Challenge lines 41-109)

| item | Lean | spec | verdict |
|---|---|---|---|
| D1 universe | `V` a `Fintype` with `DecidableEq`; theorems on `Fin 9` / `Fin n` | finite simple graph | OK |
| D2 size | `size c = ∑ v, c v` | ‖c‖ | OK |
| D3 move | `∃ u v, G.Adj u v ∧ 2 ≤ c u ∧ d = update (update c u (c u - 2)) v (c v + 1)` | u⇒v along an edge, c(u)≥2, c(u)-=2, c(v)+=1 | OK: `SimpleGraph.Adj` is irreflexive, so u≠v and the outer update reads the original `c v`; size drops by exactly 1 |
| D4 stacked | `∃ v, ∀ w, c w ≠ 0 ↔ w = v` | \|supp\|=1 | OK (the zero configuration is not stacked) |
| D5 stackable / clearable | `∃ d, ReflTransGen (Move G) c d ∧ IsStacked d` / `∧ size d = 1` | some finite (possibly empty) legal sequence reaches stacked / total mass exactly 1 | OK |
| D6 almost stacked | `∃ v₀, ∀ u, u ≠ v₀ → c u ≤ 1` | ∃v0 ∀u≠v0, c(u)≤1 | OK |
| D7 stack / clear number | `IsLeast {s ∣ 2 ≤ s ∧ ∀ c, size c = s → Stackable G c} t` (resp. Clearable) | least t≥2 such that every configuration of size exactly t is g-able | OK: exact size, `t ≥ 2` convention; connectivity / non-bipartiteness is imposed where the number is used (universal statements), not in the definition, which only widens it |
| D8 ASH* (critical form) | `∀ t, IsStackNumber G t → IsLeast {t₀ ∣ 2 ≤ t₀ ∧ ∀ s, t₀ ≤ s → ∀ c, size c = s → IsAlmostStacked c → Stackable G c} t` (resp. clear) | stack(G) = least t₀≥2 such that every AS configuration of every size ≥ t₀ is stackable | OK. Note R1 below |
| D9 G9 | `SimpleGraph.fromRel` of the 14 pairs `g9Edges` on `Fin 9` | graph6 `HCQTaXi` | OK: decoded independently in this session from the graph6 string (Python, upper-triangle column order) to exactly the same 14 edges; `fromRel` symmetrises and drops loops (there are none) |
| D10 cStar, image | `![0,0,1,0,0,5,0,8,0]`, `![0,0,1,0,0,8,0,5,0]` | S015/S016 critical losers | OK: both of size 14, both have two vertices with more than one pebble (not AS); the stated map 0↔1, 3↔4, 5↔7, 6↔8 (2 fixed) was re-checked to be an automorphism of the 14-edge list and to send cStar to the image (docstring only; no theorem depends on it) |

## Statements (Challenge lines 114-195)

- S1 `G9_connected`, S2 `G9_not_bipartite : ¬ G9.Colorable 2`: Mathlib's `Colorable 2` is the existence of a proper colouring by `Fin 2`, i.e. bipartiteness; its negation is the spec's non-bipartite condition. OK.
- S3 `G9_stack_14` / `G9_clear_14`: for every `c` of size 14, `¬ g-able ↔ c = cStar ∨ c = cStarImage`: the exact size-14 loser characterisation K1/K1c. OK.
- S4 `cStar_not_AS`, `cStarImage_not_AS`. OK.
- S5 `G9_stack_large` / `G9_clear_large`: every configuration of every size ≥ 15 is g-able (K2/K2c with C2). OK.
- S6 `G9_stack_losers` / `G9_clear_losers`: a loser of every size 2..14. OK (Prop. 3 shape).
- S7 `G9_stackNumber : IsStackNumber G9 15`, `G9_clearNumber : IsClearNumber G9 15`. OK.
- S8 `G9_*_AS_threshold`: the least t₀≥2 with every AS configuration of every size ≥ t₀ g-able is 14. Together with S7 this is the failure of ASH* directly (15 ≠ 14). OK.
- S9 `G9_*_Lall : IsGreatest {t ∣ 2 ≤ t ∧ ∃ c, size c = t ∧ ¬ g-able} 14` and `G9_*_LAS : IsGreatest {t ∣ 2 ≤ t ∧ ∃ c, size c = t ∧ IsAlmostStacked c ∧ ¬ g-able} 13`: L_all = 14 > 13 = L_AS, the critical-loser form of S003 Thm 4(ii). The `2 ≤ t` restriction excludes size 0 (never g-able) and size 1 (always g-able), as in the spec. OK.
- S10 `G9_not_ASHStarStack`, `G9_not_ASHStarClear`. OK.
- S11 `not_forall_ASHStarStack : ¬ ∀ n (G : SimpleGraph (Fin n)), 2 ≤ n → G.Connected → ASHStarStack G` and `not_forall_ASHStarClear : ¬ ∀ n G, G.Connected → ¬ G.Colorable 2 → ASHStarClear G`. OK: every finite simple graph is isomorphic to one on some `Fin n` and the property is invariant under isomorphism, so quantifying over `Fin n` is the full universal scope; the extra hypothesis `2 ≤ n` (STACK) only weakens the universal statement and so strengthens its negation; the CLEAR universal has the spec's two hypotheses (connected, non-bipartite) and no other.
- S12 `clearable_stackable` (T1). OK.
- S13 `stackable_above` / `clearable_above`: hypotheses "no isolated vertex" and `card V ≤ t` with `t` winning implies every size ≥ t wins. The spec's Lemma 2 assumes connected, n≥2 and t>n; the Lean hypotheses are implied by those (connected with n≥2 has no isolated vertex; t>n gives card V ≤ t), so the Lean lemma is at least as strong. The proof idea (pigeonhole for sizes s>t≥n) is valid at t=n as well. OK.

## Remarks (no mismatch)

- R1 (vacuity): `ASHStarStack G` is conditional on the existence of the stack number; for a graph with no stack number it holds vacuously. For connected graphs with n≥2 the number exists (S003 Prop. 3 with October Lemma 4.7), so this is the intended statement there; for the refutation it cannot help, because `G9_stackNumber` (resp. `G9_clearNumber`) exhibits the number. Refuting the Lean form is therefore at least as strong as refuting the intended form.
- R2: the Lean statements concern the critical form ASH* (the author-reported intended meaning), not the printed pointwise form; the printed-form counterexamples (P4, bull; S003/S004) are not formalised here (Lean pending for them).
- R3: universal L_all(G) ≤ L_AS(G) is NOT claimed anywhere; only its failure for G9.
- R4: K1 (non-g-ability of cStar) is proved through the certificate (checker + kernel evaluation), not through the S015 human proof.

## Finding F1 (found by Comparator, not by this review; fixed)

Comparator run 1 rejected `clearable_stackable` (and, by the same cause, `stackable_above` and `clearable_above`): in the S017 Challenge these three lemmas re-bound `{V : Type*} [Fintype V] [DecidableEq V]` inside the section that already declares the same `variable`, so their universe parameter was named `u_2` instead of the Solution's `u_1` (sessions/S018/PLAN_AMENDMENT_1.md, evidence/S018/f1_diagnosis.txt). This first draft of the review had passed S12-S13 because the pretty-printed and `pp.all` statements are identical (`#check` renames the universe for display): a universe-name difference is invisible to a human reading of the statement and has no mathematical content. Fixed by deleting the redundant re-binding (three lines of Challenge.lean); the statements S12-S13 are otherwise unchanged and the verdicts above stand for the fixed file. Lesson: only Comparator (or an export-level diff) establishes that the Solution states the Challenge; a human statement review cannot replace it.

## Verdict

LEAN_STATEMENT_COLD_RECHECK_PASS for the fixed Challenge.lean (F1 corrected): no mathematical mismatch between formal/Challenge.lean and the programme's specification; no frozen module changed. Scope: the Challenge statements and definitions only; that the Solution proves them is established separately by the Milestone 2 Comparator run.
