---
role: proof
locale: en
of_concept: pid-is-gaussian
source_book: gtm030
source_chapter: "II"
source_section: "4"
---

First, we prove $A'$. Let $(a_1) \subseteq (a_2) \subseteq (a_3) \subseteq \cdots$ be an ascending chain of principal ideals. The union $\bigcup (a_i)$ is an ideal, hence principal: $\bigcup (a_i) = (d)$. Then $d \in (a_n)$ for some $n$, so $(d) \subseteq (a_n)$. But $(a_n) \subseteq (a_{n+k}) \subseteq (d)$ for all $k$, so the chain stabilizes at $(a_n)$. Thus no infinite properly ascending chain exists.

Next, let $a, b \in \mathfrak{A}$. The ideal $(a) + (b) = \{ax + by \mid x, y \in \mathfrak{A}\}$ is principal: $(a) + (b) = (d)$. Since $(d) \supseteq (a)$, $d \mid a$, and similarly $d \mid b$. If $e \mid a$ and $e \mid b$, then $(e) \supseteq (a)$ and $(e) \supseteq (b)$, so $(e) \supseteq (a)+(b) = (d)$, hence $e \mid d$. Thus $d$ is a GCD of $a$ and $b$. Therefore condition C holds.

Since both A' and C hold, by Theorem 1 the domain is Gaussian.
