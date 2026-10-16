# S016 plan - Gate 1 cold re-check of G9 (STACK), then Gate 2 critical ASH*-CLEAR

2026-10-16. Fresh owner invocation (OWNER_INVOCATION.txt, complete accessible text normalized UTF-8 LF, no transport-byte identity claimed): "run next session". This selects exactly S016 under the owner-revised handoff authoritative/NEXT_SESSION_PROMPT.md (sha256 dc5873f87931edc0a879631679c8afd7c3d6dc333bb6b2ce49d2fb36339991bd = authoritative/handoffs/S016_OWNER_REVISED_2026-10-16.md), archived byte-identically as AUTHORISED_PROMPT.md. No S017, Lean, registration, publication, Palomar or author contact.

Entry pin: live origin/main 334941329b77412e2ca3f6cb75ef23ade7760e35, tree 0fc574565c48af006dde88210794b0f6bfa90561, ordered parents e21ea9d480b60a033638b0f6389db457df4a5d02 (S015 merge) and 09744ce9a226575cb1d5d5aa7d75947822a31958 (S016 handoff revision, PR #19). Session branch session/S016-g9-recheck-and-clear.

Environment: Windows 11 host, Intel i7-11800H (16 logical CPUs), 15.7 GiB RAM; Python 3.12.10; rustc/cargo 1.97.1 (msvc target); Node 24.18.0; MSVC Build Tools 14.44 cl.exe; xz 5.8.3. No nauty on this host.

## Gate 1 - independent cold re-check of the G9 STACK counterexample (mandatory first milestone)

Claims under test (research/S015_G9_COUNTEREXAMPLE.md): on G9 = graph6 HCQTaXi with edge list 0-3,0-5,0-6,1-4,1-7,1-8,2-6,2-8,3-5,3-6,4-7,4-8,5-7,6-8:
K1 c*=(0,0,1,0,0,5,0,8,0) and its image are the only non-stackable configurations of mass 14, neither AS;
K2 every configuration of mass 15 is stackable;
K3 every AS configuration of mass 14 is stackable;
K4 every layer 2..14 has a non-stackable configuration (counts 36,128,383,930,1862,2887,3280,2510,1301,473,124,21,2).

G1.1 Definitions. Re-derive from research/ASH_SPEC.md, S003 reconciliation (October Lemma 4.7, S003 Thm 4) and SRC-0010: moves, stackable (exactly one occupied vertex), AS, exact-layer threshold with t>=2, monotonicity above n, and check that the G9 failure holds under (a) the critical form "L_AS=L_all" and (b) the "least t0 with every AS of every size >=t0 stackable" form, with stack computed as the exact-layer least t>=2.

G1.2 Human proof. Line-by-line audit of S015_G9_COUNTEREXAMPLE.md section 5 and its dependencies 111-113 (and the credited cancellation 47). Every padded-tree case is re-derived in writing; any gap is recorded, not silently patched.

G1.3 NEW independent checker (preregistered here, written after this plan is hashed): tools/s016_g9_reverse.rs, Rust, built with rustc -O. Different language AND different algorithm from all S015 tools: it never tests forward moves for a loser condition. It enumerates the set W of stackable configurations of mass <=16 as the backward closure of all single piles k*e_v (1<=k<=16, all 9 v) under reverse moves (c -> c - e_v + 2e_u for an edge uv with c_v>=1), restricted to mass <=16. Correctness: every forward move lowers mass by exactly one, so a configuration of mass m<=16 is stackable iff it lies on a backward chain from a single pile of mass <=m, i.e. iff it lies in W. Configurations are encoded as 9 base-17 digits in a u64 and indexed with a hash set; each mass layer is enumerated independently by an odometer (no reuse of S015 enumeration code) to compute complements. Outputs: per-mass total/loser/AS-loser counts for masses 1..16, every loser of masses 13..16 listed, a SHA256 of the canonical loser list, and verdicts for K1-K4. Graph: decoded from the string HCQTaXi by an independent graph6 decoder inside the same Rust file and asserted equal to the edge list above; automorphism check of the stated map. A second fresh Gate-1 check: tools/s016_g9_forward.mjs (Node), a plain memoised forward DFS from c* and its image computing the full reachable set and confirming no single pile; and a forward winning-sequence search for every AS configuration of mass 14 and every configuration of mass 15 (each found sequence replayed by an independent legality replayer inside the script).
Caps: each process <=8 GiB, <=2 h wall. A cap is UNKNOWN; UNKNOWN at Gate 1 suspends the counterexample status pending diagnosis.

G1.4 Replay of every S015 certificate checker and digest comparison: python tools/s015_cert_check.py on G9_certificate.json; tools/s015_cert_full15_check.py on G9_mass15_all_winning.txt.xz; tools/s015_cert_brute.py 16 (re-run, compare its output with evidence/S015/counterexample/brute_truth_table.json byte-for-byte or by content where line endings differ); tools/s015_validate.py on G9 (compare with python_layer_validator.txt); tools/s015_author_check.py if the authors' public code is present locally (else recorded NOT_AVAILABLE); s015_layers_v3.cpp and s015_check_v2.c rebuilt with MSVC cl and re-run on G9 if they compile unchanged (else recorded NOT_REBUILT with the compiler message; no source edits to S015 tools). Every file listed in evidence/S015/HASHES.md is re-hashed and compared.

Outcome rule (from the handoff, binding): all checks agree => record STACK refutation COLD_RECHECK_PASS (LEAN_PENDING; propose Phase 3 Lean authorization to the owner) and proceed to Gate 2. Any discrepancy => stop CLEAR work, suspend the counterexample status, diagnose definitively, and make that the session's work.

## Gate 2 - critical ASH*-CLEAR (only if Gate 1 passes)

Definitions (ASH_SPEC): G connected non-bipartite; c clearable iff legal moves reach total mass exactly 1; clear(G) least t>=2 with every configuration of size t clearable; L_all^CLEAR, L_AS^CLEAR largest masses of a non-clearable configuration / AS non-clearable configuration; critical ASH*-CLEAR(G) iff L_AS^CLEAR(G)=L_all^CLEAR(G).

G2.1 Lemmas re-stated and proved for CLEAR in research/S016_CLEAR.md before any CLEAR computation: candidate completeness for the loser-layer recursion, termination above n, monotonicity, and "ASH*-CLEAR iff the top losing layer contains an AS configuration".

G2.2-G2.4 Computations (cheapest test on G9/CAM90/PB family; complete non-bipartite order-8 then order-9 atlases with two independently written tools, compared with frozen S003/S004 order-7 CLEAR data; symbolic follow-up). Each requires a separate hashed PLAN_AMENDMENT before it runs, fixing graph class, caps, tools and digests. Graph generation without nauty on this host must be justified in that amendment (e.g. frozen S015 graph6 lists evidence/S015/cam82/graphs_8.g6 and cam83/graphs_9.g6.xz, whose counts were cross-checked in S015).

## Closeout

Per AGENTS.md: one atomic authored session commit, ordinary PR, non-force merge if permitted; synchronise state/spec/catalogues/ledgers/registry/manifests; complete FUTURE S017 handoff; propose (not execute) Phase 3 Lean authorization if Gate 1 passes. Phase 1 stays IN_PROGRESS unless both clauses are resolved.
