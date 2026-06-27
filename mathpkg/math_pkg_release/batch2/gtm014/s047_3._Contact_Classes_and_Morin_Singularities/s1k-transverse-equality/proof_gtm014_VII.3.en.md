---
role: proof
locale: en
of_concept: s1k-transverse-equality
source_book: gtm014
source_chapter: "VII"
source_section: "3. Contact Classes and Morin Singularities"
---

We need only prove this locally. Let $p$ be in $S_{1_k}(f)$. By choosing coordinates on $X$ based at $p$ and on $Y$ based at $f(p)$, we may assume that $p = f(p) = 0$ and that $f(x_1, \ldots, x_n) = (h(x), x_2, \ldots, x_n)$ where $\partial^s h / \partial x_1^s(0) = 0$ for $s \leq k$. In these coordinates, $S_{1_k}(f)$ is given by the equations $\partial h / \partial x_1 = \cdots = \partial^k h / \partial x_1^k = 0$.

We proceed by induction. In case $k = 1$, $S_1(f) = S_{1_1}(f)$ since both are given by $\partial h / \partial x_1 = 0$. The transversality hypothesis guarantees that $S_1(f)$ is a submanifold. Now assume inductively that $S_{1_k}^{k-1}(f) = S_{1_{k-1}}(f)$ and that this set is a submanifold. Let $q \in S_{1_{k-1}}(f)$. Then $q \in S_{1_k}^{k-1}(f)$ iff $\partial / \partial x_1|_q \in T_q S_{1_{k-1}}(f)$, since $\operatorname{Ker} d(f|_{S_{1_{k-1}}(f)})_q = \operatorname{Ker} (df)_q \cap T_q S_{1_{k-1}}(f)$ and $\operatorname{Ker} (df)_q = \langle \partial / \partial x_1|_q \rangle$. The transversality condition ensures this condition is equivalent to the vanishing of $\partial^k h / \partial x_1^k(q)$, establishing the equality.
