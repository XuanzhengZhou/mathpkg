---
role: proof
locale: en
of_concept: dirichlet-series-with-residue-characters
source_book: gtm077
source_chapter: "VI"
source_section: "43"
---
# Proof of Theorem 128: Dirichlet Series with Residue Characters

**Theorem.** Let $\chi$ be a residue character modulo $m$. The Dirichlet series

$$L(s, \chi) = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s}$$

converges absolutely for $s > 1$ with Euler product

$$L(s, \chi) = \prod_{p} \left(1 - \frac{\chi(p)}{p^s}\right)^{-1},$$

and converges conditionally for $s > 0$ whenever $\chi$ is not the principal character.

**Proof.**

*Absolute convergence.* For any $n$, $|\chi(n)| \leq 1$ (the value is either $0$ or a root of unity). Thus $|\chi(n)/n^s| \leq n^{-s}$, and comparison with the Riemann zeta function $\zeta(s) = \sum n^{-s}$ gives absolute convergence for all real $s > 1$.

*Euler product.* The character $\chi$ is completely multiplicative: $\chi(ab) = \chi(a)\chi(b)$ for all positive integers $a, b$. For a fixed prime $p$ and $s > 1$, the geometric series expansion gives

$$\left(1 - \frac{\chi(p)}{p^s}\right)^{-1} = \sum_{k=0}^{\infty} \frac{\chi(p^k)}{p^{ks}}.$$

By the fundamental theorem of arithmetic and absolute convergence for $s > 1$, the formal product over all primes rearranges into the series:

$$\prod_{p} \left(1 - \frac{\chi(p)}{p^s}\right)^{-1} = \prod_{p} \sum_{k=0}^{\infty} \frac{\chi(p^k)}{p^{ks}} = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s} = L(s, \chi).$$

The rearrangement is justified because the series converges absolutely for $s > 1$.

*Conditional convergence for $s > 0$ (non-principal case).* Suppose $\chi \neq \chi_1$, the principal character modulo $m$. A basic property of non-principal characters (fundamental to the orthogonality relations) is that the sum over any complete residue system vanishes:

$$\sum_{a=1}^{m} \chi(a) = 0.$$

Consequently, for any integer $N$, writing $N = qm + r$ with $0 \leq r < m$:

$$\left| \sum_{n=1}^{N} \chi(n) \right| = \left| \sum_{k=0}^{q-1} \sum_{a=1}^{m} \chi(km + a) + \sum_{a=1}^{r} \chi(qm + a) \right| = \left| \sum_{a=1}^{r} \chi(qm + a) \right| \leq r \leq m.$$

Thus the partial sums $S_N = \sum_{n=1}^{N} \chi(n)$ are bounded: $|S_N| \leq m$ for all $N$.

For $s > 0$, the sequence $b_n = 1/n^s$ is monotonically decreasing with limit $0$. Applying Abel's summation formula:

$$\sum_{n=1}^{N} \frac{\chi(n)}{n^s} = \frac{S_N}{N^s} + \sum_{n=1}^{N-1} S_n \left(\frac{1}{n^s} - \frac{1}{(n+1)^s}\right).$$

The first term tends to $0$ as $N \to \infty$ (since $|S_N| \leq m$ and $s > 0$). The series on the right converges absolutely because

$$\sum_{n=1}^{\infty} |S_n| \left(\frac{1}{n^s} - \frac{1}{(n+1)^s}\right) \leq m \sum_{n=1}^{\infty} \left(\frac{1}{n^s} - \frac{1}{(n+1)^s}\right) = m \cdot 1 = m,$$

by telescoping (since $1/n^s \to 0$ as $n \to \infty$ for $s > 0$). Therefore $L(s, \chi)$ converges for all $s > 0$ when $\chi \neq \chi_1$.
