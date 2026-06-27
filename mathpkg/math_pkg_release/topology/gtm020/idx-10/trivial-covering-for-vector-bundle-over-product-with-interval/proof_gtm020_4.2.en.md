---
role: proof
locale: en
of_concept: trivial-covering-for-vector-bundle-over-product-with-interval
source_book: gtm020
source_chapter: "4"
source_section: "4.2"
---

For each $b \in B$ and $t \in I$, there exist an open neighborhood $U(t)$ of $b$ in $B$ and an open neighborhood $V(t)$ of $t$ in $[0,1]$ such that $\xi|_{U(t) \times V(t)}$ is trivial. This follows from the local triviality of the vector bundle $\xi$ over $B \times I$: each point $(b,t) \in B \times I$ has a product neighborhood on which $\xi$ is trivial.

By the compactness of $[0,1]$, there exist a finite sequence of numbers $0 = t_0 < t_1 < \cdots < t_n = 1$ and open neighborhoods $U(i)$ of $b$ in $B$ such that $\xi|_{U(i) \times [t_{i-1}, t_i]}$ is trivial for $1 \leq i \leq n$.

Let $U = \bigcap_{i=1}^{n} U(i)$, which is an open neighborhood of $b$ in $B$. Then $\xi|_{U \times [t_{i-1}, t_i]}$ is trivial for each $i$. Using a clutching argument (or by induction on $i$), these local trivializations can be glued together to obtain a trivialization of $\xi|_{U \times I}$. Thus, each $b \in B$ has an open neighborhood $U$ such that $\xi|_{U \times I}$ is trivial, yielding the desired open covering $\{U_i\}_{i \in I}$ of $B$.
