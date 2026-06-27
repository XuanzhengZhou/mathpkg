---
role: proof
locale: en
of_concept: annihilator-sums-intersections
source_book: gtm013
source_chapter: "1"
source_section: "2"
---

(1) Since $K_\beta \leq \sum_{\alpha} K_\alpha$ for each $\beta$, applying Proposition 2.15(1) (order-reversal) yields $l_R(\sum_\alpha K_\alpha) \subseteq l_R(K_\beta)$ for each $\beta$, hence $l_R(\sum_\alpha K_\alpha) \subseteq \bigcap_\alpha l_R(K_\alpha)$. Conversely, if $r \in \bigcap_\alpha l_R(K_\alpha)$, then $r$ annihilates each $K_\alpha$, hence annihilates every finite sum of elements from the $K_\alpha$, i.e., annihilates the sum $\sum_\alpha K_\alpha$. Thus $r \in l_R(\sum_\alpha K_\alpha)$. The second identity is proved dually.

(2) By Proposition 2.15(1), $l_R(\bigcap_\alpha K_\alpha)$ contains each $l_R(K_\alpha)$ (since $\bigcap_\alpha K_\alpha \subseteq K_\beta$ implies $l_R(K_\beta) \subseteq l_R(\bigcap_\alpha K_\alpha)$). Therefore the sum $\sum_\alpha l_R(K_\alpha)$ is contained in $l_R(\bigcap_\alpha K_\alpha)$. The second inclusion is dual.
