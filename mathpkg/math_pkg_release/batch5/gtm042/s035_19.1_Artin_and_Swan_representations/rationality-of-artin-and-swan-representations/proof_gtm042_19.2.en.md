---
role: proof
locale: en
of_concept: rationality-of-artin-and-swan-representations
source_book: gtm042
source_chapter: "19"
source_section: "19.2 Rationality of the Artin and Swan representations"
---

It is enough to prove (ii); assertion (i) then follows, since $a_G$ is obtained from $sw_G$ by adding to it $u_G$, which is realizable over any field.

For this, we apply prop. 44, taking $p = l$, $K = \mathbb{Q}_l$, $n = g = \operatorname{Card}(G)$, and choosing for $K'$ a sufficiently large finite extension of $\mathbb{Q}_l$. Condition (a) of that proposition is satisfied, cf. 19.1.

To check (b), we use the formula

$$g \cdot sw_G = \sum_{i \geqslant 1} g_i \cdot \operatorname{Ind}_{G_i}^{G}(u_{G_i})$$

given above. By ramification theory, these $G_i$ ($i \geqslant 1$) have orders prime to $l$; it follows that every $A'[G_i]$-module is projective (cf. 15.5), where $A'$ denotes the ring of integers of $K'$. Hence $u_{G_i}$ is afforded by a projective $A'[G_i]$-module (even by a projective $\mathbb{Z}_l[G_i]$-module if we wish), and the corresponding induced $A'[G]$-module is projective as well. Taking the direct sum of these modules (each repeated $g_i$ times), we obtain a projective $A'[G]$-module with character $g \cdot sw_G$. All the conditions of prop. 44 are then satisfied.
