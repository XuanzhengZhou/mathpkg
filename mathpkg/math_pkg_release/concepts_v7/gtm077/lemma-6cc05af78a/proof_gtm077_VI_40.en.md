---
role: proof
locale: en
of_concept: lemma-6cc05af78a
source_book: gtm077
source_chapter: "VI"
source_section: "40"
---
# Proof of Lemma (a): Convergence of the Riemann Zeta Function

**Lemma (a).** The series $\sum_{n=1}^{\infty} \frac{1}{n^s}$ converges for $s > 1$, and represents a continuous function of $s$, the so-called Riemann zeta-function $\zeta(s)$. Moreover

$$\lim_{s \to 1} (s - 1)\zeta(s) = 1.$$

*Proof.* It follows from the definition of the definite integral that for $n > 1$,

$$\int_{n}^{n+1} \frac{dx}{x^s} < \frac{1}{n^s} < \int_{n-1}^{n} \frac{dx}{x^s} \quad (n > 1).$$

This inequality holds because the function $x \mapsto 1/x^s$ is strictly decreasing for $s > 0$. On the interval $[n, n+1]$ the function attains its minimum at the right endpoint and its maximum at the left endpoint, giving the lower bound; similarly on $[n-1, n]$ the function attains its maximum at the left endpoint, giving the upper bound.

Summing over $n = 2, 3, \ldots, N$ and adding the $n = 1$ term, we obtain:

$$\int_{1}^{N+1} \frac{dx}{x^s} < \sum_{n=1}^{N} \frac{1}{n^s} < 1 + \int_{1}^{N} \frac{dx}{x^s}.$$

Taking the limit as $N \to \infty$, we have:

$$\int_{1}^{\infty} \frac{dx}{x^s} \leq \zeta(s) \leq 1 + \int_{1}^{\infty} \frac{dx}{x^s}.$$

For $s > 1$, the improper integral converges:

$$\int_{1}^{\infty} \frac{dx}{x^s} = \frac{1}{s - 1}.$$

Hence the series converges for $s > 1$. Since each term $1/n^s$ is a positive continuous function of $s$, the series represents a continuous function $\zeta(s)$ for $s > 1$ (the convergence is uniform on compact subsets of $(1, \infty)$).

From the bounds we obtain:

$$\frac{1}{s - 1} < \zeta(s) < 1 + \frac{1}{s - 1},$$

and multiplying by $(s - 1)$:

$$1 < (s - 1)\zeta(s) < s.$$

Taking the limit as $s \to 1^+$ yields:

$$\lim_{s \to 1} (s - 1)\zeta(s) = 1.$$

as claimed. $\square$
