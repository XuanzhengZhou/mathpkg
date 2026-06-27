---
role: proof
locale: en
of_concept: termwise-differentiation-of-uniformly-convergent-series
source_book: gtm011
source_chapter: "VII"
source_section: "2"
---

Let $s_n(z) = \sum_{j=1}^{n} f_j(z)$ be the $n$-th partial sum. Each $s_n$ is analytic on $G$. By hypothesis, $s_n \to f$ uniformly on compact subsets of $G$, i.e., in $C(G, \mathbb{C})$. Applying Theorem 2.1 to the sequence $\{s_n\}$, we conclude that $f$ is analytic and that for each $k \geq 1$,

$$s_n^{(k)} \to f^{(k)}$$

uniformly on compact subsets of $G$. But

$$s_n^{(k)}(z) = \sum_{j=1}^{n} f_j^{(k)}(z),$$

so the convergence $s_n^{(k)} \to f^{(k)}$ means precisely that

$$f^{(k)}(z) = \sum_{n=1}^{\infty} f_n^{(k)}(z)$$

with uniform convergence on compact sets.
