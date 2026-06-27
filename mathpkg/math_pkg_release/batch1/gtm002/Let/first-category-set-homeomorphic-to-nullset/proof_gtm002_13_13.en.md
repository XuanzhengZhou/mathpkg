---
role: proof
locale: en
of_concept: first-category-set-homeomorphic-to-nullset
source_book: gtm002
source_chapter: "13"
source_section: "13"
---

Let $A = \bigcup A_n$, where each $A_n$ is nowhere dense. Let
$$E_{n,k} = \{h \in H : m(h(\bar{A}_n)) < 1/k\}.$$

For any $h \in E_{n,k}$, the bounded closed set $h(\bar{A}_n)$ can be enclosed in an open set $G$ in $\mathbb{R}$ such that $m(G) < 1/k$. There exists a number $\delta > 0$ such that $G$ contains the $\delta$-neighborhood of each point of $h(\bar{A}_n)$. If $\varrho(g, h) < \delta$, then $g(\bar{A}_n) \subset G$, and therefore $g \in E_{n,k}$. This shows that $E_{n,k}$ is an open subset of $H$, for all $n$ and $k$.

To show $E_{n,k}$ is dense, take any $g \in H$ and $\varepsilon > 0$. Divide $I$ into a finite number of closed sub-intervals $I_1, \ldots, I_N$ of length less than $\varepsilon$. In the interior of each $I_i$, choose a closed interval $J_i$ disjoint from $g(\bar{A}_n)$ (possible since $\bar{A}_n$ is nowhere dense). Let $h_i$ be a piecewise linear homeomorphism of $I_i$ onto itself that fixes endpoints and maps $J_i$ onto an interval of length close to $|I_i|$, compressing the complement. Then $h = \bigcup h_i$ composed with $g$ satisfies $\varrho(h, g) < \varepsilon$ and $h \in E_{n,k}$.

Thus each $E_{n,k}$ is open and dense in $H$. The intersection $\bigcap_{n,k} E_{n,k}$ is residual in $H$, and any $h$ in this intersection satisfies $m(h(A)) \leq m(\bigcup_n h(\bar{A}_n)) \leq \sum_n 1/k_n \to 0$ for a suitable choice of $k_n$.
