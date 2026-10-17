# S018 Milestone 4 - submission preparation (NOT a submission)

M1-M3 passed (sessions/S018/LEAN_ASSURANCE.md, LEAN_COLD_RECHECK.md), so the conditional Milestone 4 was carried out as preparation only. Nothing was submitted, registered, published or sent; no author was contacted.

## formalization.yaml

Draft at formal/formalization.yaml, shaped after the PalomarSubmission template (tests/fixtures/palomar-template-formalization.yaml at d4e41c1d) and PalomarPolicy CONTRIBUTING.md (96b034cc) sections 3.1-3.3: version v0.4; project name/description; classification math.CO, MSC 05C57 and 05C85 (both present in Palomar's taxonomy snapshot); sources in "original" mode (a `type: original-proof` entry plus the two hypothesis papers as `background`); TreeStack Palomar entry as an `independent` related formalization; scope, sorry counts 0, axioms []; automation; fidelity; review; alignment of the two universal negations.

## Owner-action items before any submission (none is executed here)

1. **Repository licence (blocker).** Palomar requires exactly one root licence file whose SPDX identifier equals `project.license`. The repository has no LICENSE file. The owner must choose a licence.
2. **People fields.** `project.authors` and `project.responsible_maintainers` must be humans (Palomar policy, Leiden human-authorship principle); left OWNER_TO_CONFIRM.
3. **Automation disclosure.** Palomar asks for the automated methods and model roles. AGENTS.md rule 12 keeps model/vendor names out of repository files, so `automation.methods[].models`, framework and spend are OWNER_TO_CONFIRM: the owner decides how to reconcile the two.
4. **Result origin.** `original-proof` asserts first presentation; the Phase 2 novelty audit has not been run. Confirm after Phase 2, or switch the origin.
5. **Source authors and endorsement.** Author lists and `author_endorsement` of the two papers are left for the owner (contacting authors needs separate authorisation; the existing correspondence draft reply remains NOT SENT).
6. **Layout.** Recommendation: keep the Lean project at `formal/` (Palomar section 6.1: select `formal` as the project directory and `formal/comparator.json` as the Comparator path; the licence stays at the repository root). Moving it to the root would mix the Lean project with the research archive and the Python/Rust tooling; no benefit identified. Owner decision.
7. **Sandboxed Comparator.** Palomar runs `lake comparator` in bwrap on a 32 GB runner with nanoda and con-ron at its own thread counts; this host could not reproduce that configuration (no bwrap; 16 GB). A hosted Linux run (proposed for S019) would close this gap before submission.

## Gate proposals to the owner (not executed; no phase advanced)

- **Phase 1:** propose PASS for the critical form ASH* (both clauses refuted on G9: computed with multiple checkers, independently cold-rechecked S016/S017, and proved in Lean with Comparator statement match and four accepting kernels), with the universal ASH* recorded as FALSE in both clauses and the printed form FALSE (S003/S004). Open side questions (bipartite STACK, PB family) stay open and do not block it.
- **Phase 2:** authorise the first novelty/prior-art audit of the G9 counterexample (no worldwide priority claim exists yet).
- **Phase 3:** propose PASS once a sandboxed Comparator run with exit 0 (hosted Linux, proposed S019) is recorded, or accept the present local evidence explicitly as sufficient.
