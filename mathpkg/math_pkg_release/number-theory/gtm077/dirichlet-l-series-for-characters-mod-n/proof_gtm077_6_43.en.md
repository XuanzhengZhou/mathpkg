---
role: proof
locale: en
of_concept: dirichlet-l-series-for-characters-mod-n
source_book: gtm077
source_chapter: "VI"
source_section: "43"
---
# Proof: Dirichlet $L$-series for Residue Characters

Let $\chi$ be a residue character modulo $m$, i.e., a homomorphism from the multiplicative group of residue classes coprime to $m$ into the group of roots of unity, extended to all integers by setting $\chi(n) = 0$ whenever $(n, m) > 1$.

**Absolute convergence and Euler product for $s > 1$.** The Dirichlet $L$-series is defined by

$$L(s, \chi) = \sum_{n=1}^{\infty} \frac{\chi(n)}{n^s}.$$

Since $|\chi(n)| \leq 1$ for all $n$, we have $|\chi(n)/n^s| \leq 1/n^s$, so the series converges absolutely for $s > 1$.

By the complete multiplicativity $\chi(ab) = \chi(a)\chi(b)$, each Euler factor expands as a geometric series:

$$\frac{1}{1 - \chi(p)p^{-s}} = \sum_{k=0}^{\infty} \frac{\chi(p^k)}{p^{ks}} \qquad (s > 1).$$

Multiplying over all primes $p$ and using absolute convergence to rearrange, we obtain the Euler product:

$$L(s, \chi) = \prod_{p} \frac{1}{1 - \chi(p)p^{-s}} \qquad (s > 1).$$

**Convergence for $s > 0$ (non-principal characters).** If $\chi \neq \chi_1$ (the principal character), then the orthogonality of characters gives, for any complete residue system $R$ modulo $m$:

$$\sum_{a \in R} \chi(a) = 0.$$

For any positive integer $N$, write $N = qm + r$ with $0 \leq r < m$. Then

$$\sum_{n=1}^{N} \chi(n) = \sum_{j=0}^{q-1} \sum_{a=1}^{m} \chi(jm + a) + \sum_{a=1}^{r} \chi(qm + a).$$

Since $\chi(jm + a) = \chi(a)$ (the character depends only on the residue class), each full block of $m$ consecutive integers sums to $\sum_{a=1}^{m} \chi(a) = 0$. The remaining partial block contributes at most $r < m$ terms, each bounded by $1$. Hence

$$\left| \sum_{n=1}^{N} \chi(n) \right| \leq m$$

uniformly for all $N$. The sequence $a_n = 1/n^s$ is monotone decreasing to $0$ for $s > 0$. By summation by parts (Abel's theorem on Dirichlet series), the series $\sum_{n=1}^{\infty} \chi(n)/n^s$ converges for all $s > 0$.

**Logarithmic formulation.** For $s > 0$, define

$$\log \frac{1}{1 - \frac{\chi(p)}{p^s}} = \frac{\chi(p)}{p^s} + \frac{1}{2} \frac{\chi(p^2)}{p^{2s}} + \frac{1}{3} \frac{\chi(p^3)}{p^{3s}} + \cdots = \frac{\chi(p)}{p^s} + \frac{f(s,p)}{p^{2s}},$$

where $|f(s,p)| \leq 1$ for $p \geq 2$, $s \geq 1$. Summing over all primes $p$, the series $\sum_p \frac{\chi(p)}{p^s} + \frac{f(s,p)}{p^{2s}}$ converges for $s > 1$ and represents a branch of $\log L(s, \chi)$.

For the principal character $\chi = \chi_1$, the estimate is sharper:

$$L(s, \chi_1) = \log \frac{1}{s-1} + H(s),$$

where $H(s)$ remains finite for $s \geq 1$. This follows from applying Theorem 126 to the field $k = \mathbb{Q}$, since $\chi_1(p) = 1$ for all but finitely many primes $p$ (those dividing $m$).
