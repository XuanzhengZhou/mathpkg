---
role: proof
locale: en
of_concept: polynomial-congruence-prime-ideal
source_book: gtm077
source_chapter: "II"
source_section: "27"
---
# Proof of Theorem 82: Polynomial Congruences modulo a Prime Ideal

If $\mathfrak{p}$ is a prime ideal in the ring of integers of $K$, then any
polynomial congruence

$$x^m + \alpha_1 x^{m-1} + \cdots + \alpha_{m-1} x + \alpha_m \equiv 0 \pmod{\mathfrak{p}}$$

has at most $m$ solutions modulo $\mathfrak{p}$.

**Proof.** We mimic the proof of Theorem 12 for rational primes, using the
fact that the residue class ring $\mathfrak{o}_K / \mathfrak{p}$ is a finite
field (an integral domain with finitely many elements). In the field
$\mathfrak{o}_K / \mathfrak{p}$, the polynomial

$$\bar{f}(x) = x^m + \bar{\alpha}_1 x^{m-1} + \cdots + \bar{\alpha}_m$$

is a polynomial over a field. If it had more than $m$ roots in the field, then
factoring out the roots successively would produce a factorization where the
degree of the remaining factor becomes negative — an impossibility.

More formally: suppose $\bar{x}_1, \ldots, \bar{x}_{m+1}$ are $m+1$ distinct
roots. Then in the polynomial ring over the field $\mathfrak{o}_K / \mathfrak{p}$,

$$\bar{f}(x) = (x - \bar{x}_1) \bar{g}(x)$$

with $\deg \bar{g} = m - 1$. Evaluating at $\bar{x}_i$ for $i \geq 2$ gives
$(\bar{x}_i - \bar{x}_1) \bar{g}(\bar{x}_i) = 0$ in the field. Since
$\bar{x}_i \neq \bar{x}_1$, the field has no zero divisors, so
$\bar{g}(\bar{x}_i) = 0$. Thus $\bar{g}$ has $m$ roots, contradicting the
induction hypothesis. Hence $\bar{f}$ has at most $m$ roots, and the original
congruence has at most $m$ solutions modulo $\mathfrak{p}$.
