---
role: proof
locale: en
of_concept: dirichlet-l-series
source_book: gtm077
source_chapter: "VI"
source_section: "43"
---
# Proof of Theorem 128: Dirichlet $L$-Series

**Theorem 128.** If $\chi(n)$ denotes a residue character of $n$ mod $m$, then the Dirichlet series

$$L(s, \chi) = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s}$$

is absolutely convergent for $s > 1$ and as long as $s > 1$ we have the product representation

$$L(s, \chi) = \prod_{p} \frac{1}{1 - \frac{\chi(p)}{p^s}},$$

in which $p$ runs through all positive rational primes. If moreover, $\chi$ is not the principal character, then the infinite series for $L(s, \chi)$ is convergent even for $s > 0$.

**Proof.**

**(i) Absolute convergence for $s > 1$ and product representation.** The coefficients $\chi(n)$ satisfy $|\chi(n)| \leq 1$, since $\chi(n)$ is either a root of unity, or, in case $(n, m) > 1$, equal to $0$. Hence

$$\left|\frac{\chi(n)}{n^s}\right| \leq \frac{1}{n^s},$$

and the series $\sum_{n=1}^{\infty} \frac{\chi(n)}{n^s}$ is absolutely convergent for $s > 1$ by comparison with the Riemann zeta series.

The multiplicative property of characters,

$$\chi(ab) = \chi(a)\chi(b)$$

for all pairs of positive integers $a, b$, implies that for each prime $p$:

$$\frac{1}{1 - \frac{\chi(p)}{p^s}} = 1 + \frac{\chi(p)}{p^s} + \frac{\chi(p^2)}{p^{2s}} + \cdots$$

By absolute convergence, multiplying these factors over all primes $p$ (in the sense of an absolutely convergent infinite product) yields the Euler product representation:

$$L(s, \chi) = \prod_{p} \frac{1}{1 - \frac{\chi(p)}{p^s}}.$$

This is entirely analogous to the proof of the Euler product for the Dedekind zeta-function in Theorem 124.

**(ii) Convergence for $s > 0$ when $\chi$ is not the principal character.** If $\chi \neq \chi_1$ (where $\chi_1$ is the principal character mod $m$), then by the fundamental property of characters,

$$\sum_{n \in R} \chi(n) = 0$$

for any complete system $R$ of residues mod $m$. Let $x$ be a positive integer and write $x = y \cdot m + r$ with integers $y \geq 0$ and $0 \leq r < m$. Then

$$\left| \sum_{n=1}^{x} \chi(n) \right| = \left| \sum_{q=0}^{y-1} \sum_{j=1}^{m} \chi(qm + j) + \sum_{j=1}^{r} \chi(ym + j) \right| \leq r \leq m,$$

since each complete block $\sum_{j=1}^{m} \chi(qm + j) = \sum_{j=1}^{m} \chi(j) = 0$. Thus the partial sums $\left|\sum_{n=1}^{x} \chi(n)\right|$ are bounded uniformly by $m$.

For $s > 0$, the terms $\frac{1}{n^s}$ decrease monotonically to $0$. By the Dirichlet convergence test (summation by parts / Abel's lemma), the series $\sum_{n=1}^{\infty} \frac{\chi(n)}{n^s}$ converges (conditionally) for all $s > 0$ when $\chi$ is not the principal character.
