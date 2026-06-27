---
role: proof
locale: en
of_concept: lebesgues-covering-lemma
source_book: gtm011
source_chapter: "II"
source_section: "4"
---

The proof is by contradiction; suppose that $\mathcal{G}$ is an open cover of $X$ and no such $\epsilon > 0$ can be found. In particular, for every integer $n$ there is a point $x_n$ in $X$ such that $B(x_n; 1/n)$ is not contained in any set $G$ in $\mathcal{G}$. Since $X$ is sequentially compact there is a point $x_0$ in $X$ and a subsequence $\{x_{n_k}\}$ such that $x_0 = \lim x_{n_k}$. Let $G_0 \in \mathcal{G}$ such that $x_0 \in G_0$ and choose $\epsilon > 0$ such that $B(x_0; \epsilon) \subset G_0$. Now let $N$ be such that $d(x_0, x_{n_k}) < \epsilon/2$ for all $n_k \geq N$. Let $n_k$ be any integer larger than both $N$ and $2/\epsilon$, and let $y \in B(x_{n_k}; 1/n_k)$. Then $d(x_0, y) \leq d(x_0, x_{n_k}) + d(x_{n_k}, y) < \epsilon/2 + 1/n_k < \epsilon$. That is, $B(x_{n_k}; 1/n_k) \subset B(x_0; \epsilon) \subset G_0$, contradicting the choice of $x_{n_k}$.
