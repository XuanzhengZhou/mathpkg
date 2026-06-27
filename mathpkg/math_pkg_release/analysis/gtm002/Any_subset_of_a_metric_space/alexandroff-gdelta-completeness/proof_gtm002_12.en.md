---
role: proof
locale: en
of_concept: alexandroff-gdelta-completeness
source_book: gtm002
source_chapter: "12"
source_section: "The Theorem of Alexandroff"
---

Let $X$ be a non-empty $G_\delta$ subset of a complete metric space $(Y, \varrho)$, say $X = \bigcap_{i=1}^{\infty} G_i$, with each $G_i$ open in $Y$. Put $F_i = Y \setminus G_i$ and define

$$d(x, F_i) = \inf \{ \varrho(x, y) : y \in F_i \}.$$

We may assume that each of the sets $F_i$ is non-empty. Then $d(x, F_i)$ is a real-valued continuous function on $Y$, positive on $X$. Define

$$f_i(x) = \frac{1}{d(x, F_i)} \qquad (i = 1, 2, \ldots).$$

The functions $f_i$ satisfy the hypotheses of Lemma 12.2. For suppose that $\{x_n\}$ is a Cauchy sequence of points of $X$ (in the $\sigma$-metric constructed in Lemma 12.2), and that for each $i$ the sequence $\{f_i(x_n)\}$ is bounded. Then $\{x_n\}$ is also a Cauchy sequence in $(Y, \varrho)$ since $\varrho(x, y) \leq \sigma(x, y)$. By completeness of $Y$, the sequence $x_n$ converges in $Y$ to some point $y$.

The point $y$ cannot belong to any $F_i$: if $y \in F_i$, then $\varrho(x_n, y) \to 0$, so $d(x_n, F_i) \leq \varrho(x_n, y) \to 0$, which would imply $f_i(x_n) = 1/d(x_n, F_i) \to \infty$, contradicting the boundedness of $\{f_i(x_n)\}$. Hence $y \notin F_i$ for every $i$, so $y \in G_i$ for every $i$. That is, $y \in X = \bigcap G_i$.

Therefore the sequence $\{x_n\}$ is convergent in the subspace $X$. By Lemma 12.2, $X$ can be remetrized so as to be complete. $\square$
