---
role: proof
locale: en
of_concept: alexandroffs-theorem
source_book: gtm002
source_chapter: "12"
source_section: "The Theorem of Alexandroff"
---

Let $X$ be a non-empty $G_{\delta}$ subset of a complete metric space $(Y, \varrho)$, say $X = \bigcap_{i=1}^{\infty} G_i$, where each $G_i$ is open in $Y$. Put $F_i = Y \setminus G_i$ and let

$$d(x, F_i) = \inf \{\, \varrho(x, y) : y \in F_i \,\}.$$

We may assume that each of the sets $F_i$ is non-empty. Then $d(x, F_i)$ is a real-valued continuous function on $Y$, and it is positive on $X$. Define the functions

$$f_i(x) = \frac{1}{d(x, F_i)} \qquad (i = 1, 2, \ldots).$$

These functions $f_i$ satisfy the hypotheses of Lemma 12.2. For suppose that $\{x_n\}$ is a Cauchy sequence of points of $X$, and that for each $i$ the sequence $\{f_i(x_n)\}$ is bounded. Then $x_n$ converges in $Y$ to some point $y$, since $Y$ is complete. The point $y$ cannot belong to any $F_i$, because if $y \in F_i$ then

$$f_i(x_n) = \frac{1}{d(x_n, F_i)} \geq \frac{1}{\varrho(x_n, y)}$$

would be unbounded. Hence $y \in G_i$ for every $i$; that is, $y \in X$. The sequence $\{x_n\}$ is therefore convergent in the subspace $X$. Consequently, by Lemma 12.2, $X$ can be remetrized so as to be complete.
