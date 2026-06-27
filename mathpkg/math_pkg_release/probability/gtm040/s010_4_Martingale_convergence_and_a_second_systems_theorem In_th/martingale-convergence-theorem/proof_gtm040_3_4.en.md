---
role: proof
locale: en
of_concept: martingale-convergence-theorem
source_book: gtm040
source_chapter: "3"
source_section: "4"
---

Failure of almost-everywhere convergence means that there exists a set of points $\omega$ of positive measure for which the sequence diverges. At least one of two things must happen. Either $f_n(\omega)$ for each fixed $\omega$ in a set of positive measure oscillates infinitely often above and below rationals $r(\omega)$ and $s(\omega)$, or the sequence diverges to $\pm\infty$ on a set of positive measure.

**(1)** Suppose $\liminf |f_n(\omega)| = +\infty$ on a set $E$ of positive measure $m$. Then for every $N$, there exists $n$ such that $|f_n(\omega)| \geq N$ on a subset of $E$ of measure at least $m/2$. Hence $M[|f_n|] \geq N \cdot m/2$, contradicting the uniform bound $M[|f_n|] \leq K$ for all $n$ as $N \to \infty$. Thus this case is impossible.

**(2)** Suppose $f_n(\omega)$ oscillates infinitely often above and below rationals $r(\omega)$ and $s(\omega)$ on a set of positive measure $m$. Order the set of all pairs of rationals (which is a denumerable set) and call the $k$-th pair $q_k$. Consider the denumerable family of sets $A_k$ defined by

$$A_k = \{\omega \mid f_n(\omega) \text{ oscillates infinitely often above and below the rationals of the pair } q_k\}.$$

It is possible for more than one set to have the same point in it, but every point $\omega$ for which $f_n(\omega)$ oscillates infinitely often is in some $A_k$. Therefore,

$$\sum \mu(A_k) \geq \mu\!\left(\bigcup A_k\right) = m > 0$$

and there must exist a $t$ for which $\mu(A_t) > 0$. That is, for every $\omega$ in a set $A_t$ of positive measure, $f_n(\omega)$ oscillates infinitely often above and below fixed rationals $r$ and $s$ with $r < s$. Let $\beta_n(\omega)$ be the number of upcrossings of $[r, s]$ by $f_0(\omega), \ldots, f_n(\omega)$. By Proposition 3-11,

$$M[\beta_n] \leq \frac{M[|f_n|] + |r|}{s - r} \leq \frac{K + |r|}{s - r} = c \quad \text{for every } n.$$

Furthermore, the $\beta_n$ are non-negative and increasing with $n$ to a function $\beta$, so that $M[\beta] = \lim M[\beta_n] \leq c$ by the Monotone Convergence Theorem. But on $A_t$, $\beta(\omega) = +\infty$ since the sequence oscillates infinitely often. Since $\mu(A_t) > 0$, this implies $M[\beta] = +\infty$, contradicting $M[\beta] \leq c$.

Both possible modes of divergence lead to contradictions. Therefore the set of points where the sequence does not converge has measure zero, and $\lim_{n \to \infty} f_n(\omega)$ exists and is finite almost everywhere.
