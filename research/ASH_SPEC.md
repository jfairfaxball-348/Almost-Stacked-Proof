# ASH source-indexed working specification (S002)

**Source gate distinction:** The October paper arXiv:2610.09650v1 is **ABSTRACT_INSPECTED ONLY**, dated October 7/8 2026 (23 pp); direct original PDF and HTML inaccessible during S002. Therefore its internal numbering, full quantifiers and tree estimator equations have **not** been verified. Do not promote this document into an October transcribed specification.

**Authoritative inspected formulation:** Csernák–Soukup, *Stacking and clearing in graph pebbling*, arXiv:2604.22341v1, PDF page 3 (definitions), page 20 **Hypothesis 9.1**, pages 21–26 (Theorems 9.4–9.7, 10.1). Finite connected G; natural-number pebble configuration c; legal u→v moves subtract two at u and add one at adjacent v; exact total ∑c=t. Stackable means some reachable configuration has singleton support, with an *unspecified* survivor location. Clearable means some reachable configuration has exactly one pebble. Almost stacked iff some v0 has all c(u)≤1 for u≠v0.

**Hypothesis 9.1(1), paraphrase faithful to read text:** For every finite connected G, stack(G) equals the *least* integer t≥2 such that every almost-stacked configuration of exact mass t is stackable. Stack(G) itself is the least t≥2 for which **every** configuration of mass t is stackable.

**Hypothesis 9.1(2), paraphrase faithful to read text:** For every finite connected **non-bipartite** G, clear(G) equals the least integer t≥2 such that every almost-stacked configuration of exact mass t is clearable. Clear(G) itself quantifies **all** configurations of exact mass t. The bipartite class is EXCLUDED from this second quantifier.

**Boundaries:** For K1 stacking is 2 under t≥2; its tree estim is 1 and the TreeStack theorem accordingly assumes |V|≥2. K1 is bipartite and not in clearing. Empty graphs absent. Configuration t=0 and t=1 are not threshold candidates even if terminal property trivial. A move *strictly* reduces mass, so stacking is not the same as preserving total t at a vertex. No claims for multigraphs or loops beyond original finite-graph convention; computational campaign uses simple undirected graphs only.

**Earlier tree formula independently inspected (April PDF p.26):**
`sigma_T(r)=1+sum_{v=r or deg(v)>1} deg(v)*2^dist(r,v)`;
`leaf_T(r)=#{v ≠ r : deg(v)=1}`;
`estim(T)=max_r (sigma_T(r)+leaf_T(r))`.
Exact match to inspected TreeStack/Estimator.lean, for |V(T)|≥2. The September 25 arXiv:2609.31811 and TreeStack Lean theorem `stack_eq_estim_of_two_le_card` supply independent prior result. The October abstract's conditional tree claim is not the universal ASH statement.

**Source convention for cycles:** Almost-stacked C_(2n) stackability at t=2^(n+1)-1 and C_(2n+1) clearability at t=3*2^n-2 are SOURCE_STATED; obtaining unrestricted equalities requires ASH (April Theorems 9.6–9.7). Never present them as unconditional universal consequences.

Pending: independently open the actual October full text; record exact version/date, its hypothesis label, full logical prerequisites, estimator and corrected edge cases. If changed from April, update all mirrors before an October theorem/counterexample certification.
