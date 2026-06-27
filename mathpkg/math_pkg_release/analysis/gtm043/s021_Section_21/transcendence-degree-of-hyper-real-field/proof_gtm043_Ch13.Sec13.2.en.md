---
role: proof
locale: en
of_concept: transcendence-degree-of-hyper-real-field
source_book: gtm043
source_chapter: "13"
source_section: "13.2"
---
Let $M$ be a hyper-real maximal ideal in $C(X)$. Choose $u = M(s)$ where $s \geq 1$ and $u$ is infinitely large.

Let $\{r_j\}_{j \in J}$ be a Hamel basis for $\mathbb{R}$ over $\mathbb{Q}$, so $|J| = \mathfrak{c}$. Consider the family $\{u^{r_j} : j \in J\}$.

Suppose a nontrivial polynomial relation holds:
$$\sum_{k=1}^m a_k u^{s_k} = 0,$$
where $s_k = n_{k1} r_1 + \cdots + n_{kq} r_q$ with each $n_{kj} \in \mathbb{Q}$. By $\mathbb{Q}$-linear independence of the $r_j$, the exponents $s_k$ are distinct. They are positive, so each $u^{s_k}$ is infinitely large.

Let $s_l = \max_k s_k$. Factoring $u^{s_l}$:
$$u^{s_l}\left(a_l + \sum_{k \neq l} a_k u^{s_k - s_l}\right) = 0.$$
For $k \neq l$, $s_k - s_l < 0$, so $u^{s_k - s_l}$ is infinitesimal. Thus the sum in parentheses differs infinitesimally from $a_l \neq 0$, a contradiction.

Hence $\{u^{r_j}\}$ is algebraically independent over $\mathbb{R}$. The transcendence degree is at least $\mathfrak{c}$.