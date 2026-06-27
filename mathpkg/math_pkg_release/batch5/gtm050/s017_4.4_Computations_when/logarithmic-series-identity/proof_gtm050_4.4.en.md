---
role: proof
locale: en
of_concept: logarithmic-series-identity
source_book: gtm050
source_chapter: "4"
source_section: "4.4"
---

**Proof by summation by parts (Abel summation).** Define the partial sums of the geometric series:

$$
S(0) = 0, \qquad S(n) = S(n-1) + x^n = \frac{x(1 - x^n)}{1 - x} \quad \text{for } n \geqslant 1.
$$

Note that for $|x| \leqslant 1$, $x \neq 1$, the sequence $S(n)$ is bounded. Indeed,

$$
|S(n)| = \left| \frac{x(1 - x^n)}{1 - x} \right| \leqslant \frac{2}{|1 - x|}.
$$

Now apply summation by parts (the discrete analog of integration by parts). For any sequences $(a_n)$ and $(b_n)$,

$$
\sum_{n=1}^{N} a_n b_n = S(N) b_N - \sum_{n=1}^{N-1} S(n) (b_{n+1} - b_n).
$$

Set $a_n = x^n$ and $b_n = 1/n$. Then $S(n) = \sum_{k=1}^{n} x^k$, and

$$
\sum_{n=1}^{N} \frac{x^n}{n} = \frac{S(N)}{N} + \sum_{n=1}^{N-1} S(n) \left( \frac{1}{n} - \frac{1}{n+1} \right) = \frac{S(N)}{N} + \sum_{n=1}^{N-1} \frac{S(n)}{n(n+1)}.
$$

Since $S(n)$ is bounded by $M = 2/|1-x|$, we have $|S(N)/N| \leqslant M/N \to 0$ as $N \to \infty$. Moreover,

$$
\sum_{n=1}^{\infty} \left| \frac{S(n)}{n(n+1)} \right| \leqslant M \sum_{n=1}^{\infty} \frac{1}{n(n+1)} = M < \infty,
$$

so the series $\sum_{n=1}^{\infty} \frac{S(n)}{n(n+1)}$ converges absolutely. Hence $\sum_{n=1}^{\infty} \frac{x^n}{n}$ converges for all $|x| \leqslant 1$, $x \neq 1$.

To identify the sum, consider $f(x) = \sum_{n=1}^{\infty} x^n/n$ as a power series. For $|x| < 1$, termwise differentiation gives $f'(x) = \sum_{n=1}^{\infty} x^{n-1} = \frac{1}{1-x}$. Integrating from $0$ to $x$ with $f(0) = 0$ yields $f(x) = -\log(1-x) = \log\frac{1}{1-x}$. By Abel's theorem on power series continuity at the boundary, the identity extends to all $|x| \leqslant 1$, $x \neq 1$, where the series converges conditionally on $|x| = 1$ (except at $x = 1$, where it diverges).
