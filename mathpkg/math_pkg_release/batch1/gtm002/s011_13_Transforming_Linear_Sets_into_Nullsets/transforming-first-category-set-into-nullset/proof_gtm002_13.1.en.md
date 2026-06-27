---
role: proof
locale: en
of_concept: transforming-first-category-set-into-nullset
source_book: gtm002
source_chapter: "13"
source_section: "13"
---

Let $A = \bigcup_{n=1}^{\infty} A_n$ where each $A_n$ is nowhere dense. For each $n$ and $k$, define
$$E_{n,k} = \{h \in H : m(h(\bar{A}_n)) < 1/k\}.$$

We first show that each $E_{n,k}$ is open in $H$. Fix $h \in E_{n,k}$. Since $m(h(\bar{A}_n)) < 1/k$ and $h(\bar{A}_n)$ is a bounded closed set, it can be enclosed in an open set $G \subset \mathbb{R}$ such that $m(G) < 1/k$. Because $h(\bar{A}_n)$ is compact, there exists $\delta > 0$ such that the $\delta$-neighborhood of every point of $h(\bar{A}_n)$ is contained in $G$. Now if $\varrho(g, h) < \delta$, then for any $x \in \bar{A}_n$ we have $|g(x) - h(x)| < \delta$, so $g(x)$ lies in the $\delta$-neighborhood of $h(x)$, hence in $G$. Thus $g(\bar{A}_n) \subset G$, implying $m(g(\bar{A}_n)) \leq m(G) < 1/k$, so $g \in E_{n,k}$. This proves $E_{n,k}$ is open.

Next we show each $E_{n,k}$ is dense in $H$. Take any $g \in H$ and $\varepsilon > 0$. Divide $I$ into finitely many closed sub-intervals $I_1, \ldots, I_N$ of length less than $\varepsilon$. In the interior $I_i^\circ$ of each $I_i$, choose a closed interval $J_i \subset I_i^\circ \setminus g(\bar{A}_n)$; this is possible because $g(\bar{A}_n)$ is nowhere dense (being the continuous image of a nowhere dense closed set). Let $h_i$ be a piecewise linear homeomorphism of $I_i$ onto itself that fixes the endpoints of $I_i$ and maps $J_i$ onto an interval of length sufficiently close to $|I_i|$ while stretching the complement $I_i \setminus J_i$ into a very small set. By composing these $h_i$, we obtain a homeomorphism $\tilde{h} \in H$ such that $\varrho(\tilde{h}, \text{id})$ is small and $m(\tilde{h}(g(\bar{A}_n)))$ is arbitrarily small. Then $h = \tilde{h} \circ g$ satisfies $h \in E_{n,k}$ and $\varrho(h, g) < \varepsilon$.

Since $H$ is a $G_\delta$ subset of the complete metric space $C[0,1]$, it is topologically complete (by Theorem 12.1) and hence a Baire space. Each $E_{n,k}$ is open and dense in $H$, so the countable intersection
$$E = \bigcap_{n=1}^{\infty} \bigcap_{k=1}^{\infty} E_{n,k}$$
is a residual subset of $H$.

For any $h \in E$, we have $m(h(\bar{A}_n)) < 1/k$ for all $k$, which forces $m(h(\bar{A}_n)) = 0$ for every $n$. Since $A_n \subset \bar{A}_n$, we have $h(A_n) \subset h(\bar{A}_n)$, so $m(h(A_n)) = 0$. Finally,
$$h(A) = \bigcup_{n=1}^{\infty} h(A_n)$$
is a countable union of nullsets, hence a nullset. $\square$
