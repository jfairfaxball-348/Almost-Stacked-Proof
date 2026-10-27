# Provenance for the Palomar submission

## Two histories in one public GitHub repository

The self-contained Palomar submission is an **orphan Git history** in
`jfairfaxball-348/Almost-Stacked-Proof`, originally submitted as commit
[`34363e5222136c54b08e0c5550e2d49b9f23f5fd`](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/commit/34363e5222136c54b08e0c5550e2d49b9f23f5fd).
It contains the Lean project, not the large research archive. The research,
computations, independent re-checks, generator, and build-assurance records
exist in the **separate main-line Git history of the same repository**.
They are pinned here to immutable research commit
[`5f0900c17995362155bff0e8aecd7fa67e0d8363`](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/commit/5f0900c17995362155bff0e8aecd7fa67e0d8363).
A link to the repository homepage or the current `main` branch alone
would not identify them.

The snapshot was packaged in session S019. The S019 record explicitly
documents copying the formal Lean sources byte-for-byte and independently
checking the fresh-clone snapshot. See the frozen records below. The
orphan snapshot and research commit need not have an ancestor relationship.

## Frozen record index (all links pinned to the research commit)

| Subject | Immutable record |
| --- | --- |
| Initial nine-vertex STACK counterexample and exact checks (S015) | [research/S015_G9_COUNTEREXAMPLE.md](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/5f0900c17995362155bff0e8aecd7fa67e0d8363/research/S015_G9_COUNTEREXAMPLE.md) |
| CLEAR extension, exact recurrences and computations (S016) | [research/S016_CLEAR.md](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/5f0900c17995362155bff0e8aecd7fa67e0d8363/research/S016_CLEAR.md) |
| Independent STACK cold re-check (S016) | [sessions/S016/GATE1_AUDIT.md](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/5f0900c17995362155bff0e8aecd7fa67e0d8363/sessions/S016/GATE1_AUDIT.md) |
| Independent CLEAR cold re-check (S017) | [sessions/S017/CLEAR_RECHECK.md](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/5f0900c17995362155bff0e8aecd7fa67e0d8363/sessions/S017/CLEAR_RECHECK.md) |
| Untrusted Lean certificate-data generator (S017) | [tools/s017_gen_layers.py](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/5f0900c17995362155bff0e8aecd7fa67e0d8363/tools/s017_gen_layers.py) |
| Lean statement/specification cold re-check (S018) | [sessions/S018/LEAN_COLD_RECHECK.md](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/5f0900c17995362155bff0e8aecd7fa67e0d8363/sessions/S018/LEAN_COLD_RECHECK.md) |
| Formal proof and external-kernel assurance (S018) | [sessions/S018/LEAN_ASSURANCE.md](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/5f0900c17995362155bff0e8aecd7fa67e0d8363/sessions/S018/LEAN_ASSURANCE.md) |
| Snapshot construction, exact build and verification (S019) | [sessions/S019/PACKAGING.md](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/5f0900c17995362155bff0e8aecd7fa67e0d8363/sessions/S019/PACKAGING.md) |
| S019 handoff and explicit original snapshot commit | [sessions/S019/CLOSEOUT.md](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/5f0900c17995362155bff0e8aecd7fa67e0d8363/sessions/S019/CLOSEOUT.md) |
| Fresh-clone comparator output | [evidence/S019/comparator_fresh.txt](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/5f0900c17995362155bff0e8aecd7fa67e0d8363/evidence/S019/comparator_fresh.txt) |
| Fresh-clone additional proof-checker outcomes | [evidence/S019/kernels_fresh.txt](https://github.com/jfairfaxball-348/Almost-Stacked-Proof/blob/5f0900c17995362155bff0e8aecd7fa67e0d8363/evidence/S019/kernels_fresh.txt) |

The research files were written at different stages: a historical S015 or
S016 status such as LEAN_PENDING reports the state *at that time*, not the
later S019 state. Similarly, the generator creates untrusted data; the
formal checker verifies its correctness independently by Lean kernel
evaluation. The snapshot itself contains `Challenge.lean`,
`Solution.lean`, `AlmostStacked/`, and `comparator.json`.

## Claim scope and limitations

- Mathematical claim: on G9 (graph6 `HCQTaXi`), the critical forms of the
  STACK and CLEAR Almost Stacked Hypotheses fail; the submitted Lean
  statements are the ones checked by Palomar.
- Evidence of computation and independent *agent/tool* re-checks is
  documented above. This is not a claim that independent human referees
  checked the result. No human peer review is claimed.
- A separate worldwide novelty/prior-art audit was not performed (waived
  by the owner). No worldwide priority claim is made.
- The additional proof check `con-leche` remained inconclusive after
  hitting the recorded memory cap; the other specific successful replays
  are reported accurately in the S019 records.
- This provenance-only correction does not change Lean source code,
  theorem statements, certificate data, toolchain, or comparator settings.
