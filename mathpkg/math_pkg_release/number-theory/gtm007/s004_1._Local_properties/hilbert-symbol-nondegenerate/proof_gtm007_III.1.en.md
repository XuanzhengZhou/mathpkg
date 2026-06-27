---
role: proof
locale: en
of_concept: hilbert-symbol-nondegenerate
source_book: gtm007
source_chapter: "III"
source_section: "§1. Local properties"
---

The bilinearity of the Hilbert symbol is formula v): $(a a', b) = (a, b)(a', b)$, whose proof is deferred to §2.

Nondegeneracy means: if $a \in k^*$ is not a square, there exists $b \in k^*$ such that $(a, b) = -1$. 

Over $k = \mathbf{R}$, this is immediate: if $a < 0$, take $b = -1$ (which is also negative); then $(a, b) = -1$ by Theorem 1.

Over $k = \mathbf{Q}_p$, the nondegeneracy follows from the explicit formulas of Theorem 1 together with the properties of the Legendre symbol (for $p \neq 2$) and the functions $\varepsilon$ and $\omega$ (for $p = 2$). Specifically, for any nonsquare unit $u \in \mathbf{U}$, there exists a unit $v$ such that the Legendre symbol or the $\varepsilon/\omega$ invariants produce a factor of $-1$.

Thus the Hilbert symbol defines a perfect pairing on the $\mathbf{F}_2$-vector space $k^*/k^{*2}$.
