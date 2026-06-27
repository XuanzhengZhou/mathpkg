---
role: proof
locale: en
of_concept: alexandroff-gdelta-remetrization
source_book: gtm002
source_chapter: "12"
source_section: "12"
---

Let $X$ be a non-empty $G_{\delta}$ subset of a complete metric space $(Y, \varrho)$, say $X = \bigcap_{i=1}^{\infty} G_i$ where each $G_i$ is open in $Y$. Put $F_i = Y \setminus G_i$ and define the distance function

$$d(x, F_i) = \inf \{ \varrho(x, y) : y \in F_i \}.$$

We may assume that each of the sets $F_i$ is non-empty. Then $d(x, F_i)$ is a real-valued continuous function on $Y$, and it is positive precisely on $G_i$. In particular, $d(x, F_i) > 0$ for all $x \in X$.

Define the functions $f_i(x) = 1 / d(x, F_i)$ for $i = 1, 2, \ldots$. Each $f_i$ is continuous on $X$ (in fact on each $G_i$). We claim that these functions satisfy the hypotheses of Lemma 12.2.

Suppose that $\{x_n\}$ is a Cauchy sequence of points of $X$ with respect to some metric on $X$, and that for each $i$ the numerical sequence $\{f_i(x_n)\}$ is bounded. Since $Y$ is complete and the original metric $\varrho$ restricted to $X$ is at least as coarse (any Cauchy sequence in $X$ relative to a compatible metric that makes the $f_i$ uniformly continuous will also be Cauchy relative to $\varrho$ after applying Lemma 12.2's construction), the sequence $\{x_n\}$ converges in $Y$ to some point $y \in Y$.

The point $y$ cannot belong to any $F_i$, for if $y \in F_i$, then $d(x_n, F_i) \leq \varrho(x_n, y) \to 0$, and consequently $f_i(x_n) = 1/d(x_n, F_i)$ would be unbounded, contradicting the hypothesis that each $\{f_i(x_n)\}$ is bounded. Hence $y \notin F_i$ for every $i$, which means $y \in G_i$ for every $i$. Therefore $y \in \bigcap_{i=1}^{\infty} G_i = X$.

Thus the sequence $\{x_n\}$ converges in the subspace $X$. Consequently, by Lemma 12.2, $X$ can be remetrized so as to be complete.
