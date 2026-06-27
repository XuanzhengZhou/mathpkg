---
role: proof
locale: en
of_concept: alexandroff-theorem
source_book: gtm002
source_chapter: "12"
source_section: "The Theorem of Alexandroff"
---

Let $X$ be a non-empty $G_{\delta}$ subset of a complete metric space $(Y, \varrho)$, say $X = \bigcap_{i=1}^{\infty} G_i$, where each $G_i$ is open in $Y$. Put $F_i = Y \setminus G_i$ and let

$$d(x, F_i) = \inf\{\varrho(x, y) : y \in F_i\}.$$

We may assume that each of the sets $F_i$ is non-empty (if some $F_i$ is empty, then $G_i = Y$ and that term may be omitted from the intersection). Then $d(x, F_i)$ is a real-valued continuous function on $Y$, positive on $X$. Define

$$f_i(x) = \frac{1}{d(x, F_i)} \qquad (i = 1, 2, \ldots).$$

We verify that the functions $f_i$ satisfy the hypotheses of Lemma 12.2. Suppose that $\{x_n\}$ is a Cauchy sequence of points of $X$ (with respect to the metric $\varrho$ restricted to $X$), and that for each $i$ the sequence $\{f_i(x_n)\}$ is bounded. Since $Y$ is complete, the sequence $\{x_n\}$ converges in $Y$ to some point $y \in Y$.

The point $y$ cannot belong to any $F_i$, because if $y \in F_i$ then $\varrho(x_n, y) \to 0$ would imply $d(x_n, F_i) \to 0$, and consequently $f_i(x_n) = 1/d(x_n, F_i)$ would be unbounded, contradicting the hypothesis. Hence $y \in G_i$ for every $i$; that is, $y \in X$. The sequence $\{x_n\}$ is therefore convergent in the subspace $X$.

Consequently, the hypotheses of Lemma 12.2 are satisfied, and therefore $X$ can be remetrized so as to be complete. $\square$
