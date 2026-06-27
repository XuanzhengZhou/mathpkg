---
role: proof
locale: en
of_concept: first-category-to-nullset
source_book: gtm002
source_chapter: "13"
source_section: "Transforming Linear Sets into Nullsets"
---

Let $A = \bigcup A_n$, where each $A_n$ is nowhere dense. Let
$$E_{n,k} = \{h \in H : m(h(\bar{A}_n)) < 1/k\}.$$
For any $h \in E_{n,k}$, the bounded closed set $h(\bar{A}_n)$ can be enclosed in an open set $G$ in $\mathbb{R}$ such that $m(G) < 1/k$. There exists a number $\delta > 0$ such that $G$ contains the $\delta$-neighborhood of each point of $h(\bar{A}_n)$. If $\varrho(g, h) < \delta$, then $g(\bar{A}_n) \subset G$, and therefore $g$ belongs to $E_{n,k}$. This shows that $E_{n,k}$ is an open subset of $H$, for all $n$ and $k$.

For any $g \in H$ and $\varepsilon > 0$, divide $I$ into a finite number of closed sub-intervals $I_1, \ldots, I_N$ of length less than $\varepsilon$. In the interior $I_i^0$ of $I_i$, choose a closed interval $J_i \subset I_i^0 - g(\bar{A}_n)$ ($i = 1, \ldots, N$). Let $h_i$ be a piece-wise linear homeomorphism of $I_i$ onto itself that leaves the endpoints fixed and maps $J_i$ onto an interval of length nearly equal to $|I_i|$, compressing the complement of $J_i$ into a set of very small measure. The composition of these $h_i$ defines an automorphism $h \in H$ such that $\varrho(g, h) < \varepsilon$ and $m(h(\bar{A}_n))$ is arbitrarily small; hence $h \in E_{n,k}$ for suitably large $k$. This shows that each $E_{n,k}$ is dense in $H$.

Since $H$ is a $G_\delta$ subset of $C[0,1]$ and therefore topologically complete (by Theorem 12.1), the intersection
$$\bigcap_{n,k} E_{n,k}$$
is a residual set in $H$. For any $h$ in this intersection, $m(h(\bar{A}_n)) < 1/k$ for all $n, k$, so $m(h(\bar{A}_n)) = 0$ for every $n$. Hence $h(A) = \bigcup h(A_n) \subset \bigcup h(\bar{A}_n)$ is a nullset. $\square$
