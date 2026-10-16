# ACTIVE S01490: a finite certificate for the unbounded AS tail

This is a scoped universal tool toward a genuine counterexample search, not
a proof or disproof of ASH*. Known occupied+3 reduction is credited to the
primary sources and earlier programme work. STACK only; no CLEAR campaign.

**Proposition90.** Let G be finite connected simple, n>=2, and T>=n+1.
The following are equivalent:

1. EVERY AS input of EACH exact mass T,T+1,T+2 stacks.
2. EVERY AS input of EVERY mass at least T stacks, equivalently L_AS<T.

Proof.2 implies1. Suppose instead an AS loser d has mass M>=T. Since M>n,
it has exactly one heavy s, with d_s>=M-(n-1). If M>=T+3, then d_s>=5.
Choose a true neighbor w of s, guaranteed by connectedness/n>=2. The three
legal moves s->w,s->w,w->s remove exactly3 at s and restore all other counts,
including any original singleton at w. Thus d reaches d-3e_s, which must lose
or prefixing its win would win d. It remains AS. Repeat until mass is in
T,T+1,T+2. Its source count is still>=T-(n-1)>=2, so no zero-source bit or
vanished heavy is silently identified. This contradicts1. QED.

Each exact layer t>=T consists uniquely of (t-|U|)e_s+1_U, with s in V and
U subset V minus{s}. There are n*2^(n-1) distinct inputs per layer, source
count>=2. Literal full-input positive histories for ALL three layers give
a finite complete upper certificate for the UNBOUNDED AS domain, covering
3n*2^(n-1) inputs with unrestricted roots. One AS-winning layer is insufficient;
the separately refuted printed formulation already demonstrates that.

A fully certified general loser c of mass T>=n+1 plus complete independently
checked winning certificates for these three AS layers therefore gives
L_all>=T>L_AS, a genuine mathematical disproof of universal ASH*-STACK.
Repository certification still requires labeled adjacency, exact threshold,
fresh independent negative/AS audits, and later separately gated kernel/cold
work. Partial screens and failed move sequences prove nothing of this kind.

This is an explicit application of known+3 semigroup closure, not a claimed
new general periodicity theorem. It makes direct counterexample screening
cheaper and exact: one AS loser in these layers rejects a proposed mass-T
counterexample, while absence requires completing every positive case.
