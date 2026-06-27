---
role: proof
locale: en
of_concept: product-metric-space-compactness
source_book: gtm011
source_chapter: "1"
source_section: "1.18"
---

The proof that $d$ is a metric is left to the reader. Suppose $d(\xi^k, \xi) \to 0$. Since
$$\frac{d_n(x_n^k, x_n)}{1 + d_n(x_n^k, x_n)} \leq 2^n d(\xi^k, \xi)$$
we have that
$$\lim_{k \to \infty} \frac{d_n(x_n^k, x_n)}{1 + d_n(x_n^k, x_n)} = 0.$$

This gives that $x_n^k \to x_n$ for each $n \geq 1$. The proof of the converse is left to the reader.

Now suppose that each $(X_n, d_n)$ is compact. To show that $(X, d)$ is compact it suffices to show that every sequence in $X$ has a convergent subsequence; this is accomplished by the Cantor diagonal process. Given a sequence $\{\xi^k\}$ in $X$, where $\xi^k = \{x_n^k\}_{n=1}^\infty$, compactness of $X_1$ yields a subsequence such that the first coordinates converge. From this, compactness of $X_2$ yields a further subsequence with convergent second coordinates. Continuing inductively and taking the diagonal subsequence produces a sequence converging in every coordinate, hence converging in $(X, d)$.
