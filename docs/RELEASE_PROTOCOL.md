# Release chain: proof to Palomar to arXiv

1. **Mathematics:** claim exact graph/configuration model, unconditional proof or finite counterexample with independent verification. Proof dependencies closed. State uncertainty honestly.
2. **First novelty check:** check closest literature after a candidate result, before major formalisation. Record nearest theorem/equivalence, not just topic matches.
3. **Lean:** pin current supported version and mathlib; compile proof with no `sorry`, `admit` or unjustified axioms; run explicit kernel/independent replay and verify actual CI.
4. **Final comprehensive novelty:** check the final exact theorem and proof against primary public sources afresh; classify priority with bounded uncertainty.
5. **Palomar:** only on explicit owner approval; consult current registry requirements rather than blindly copying another project's `formalization.yaml`; freeze immutable commit, comparator/challenge/provenance, run full official preflight, then submit and independently verify registry ID/version. Palomar registration is not peer review.
6. **arXiv:** create standalone paper, source bundle, bib, exact theorem/assumptions, related TreeStack credit, machine-checkable and computational evidence with limitations. Independently build and inspect PDF and source; owner authorisation required before upload. Then record arXiv ID/version and eventual journal option.

**Stop on failed gate.** The user has specified the sequence: proof -> first novelty -> Lean -> final novelty -> Palomar -> arXiv. Do not prematurely write a public solved-problem claim.
