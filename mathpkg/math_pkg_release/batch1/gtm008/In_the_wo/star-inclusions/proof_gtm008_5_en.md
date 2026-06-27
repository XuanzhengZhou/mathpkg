---
role: proof
locale: en
of_concept: star-inclusions
source_book: gtm008
source_chapter: "5"
source_section: "Partial Order Structures and Topological Spaces"
---

**Proof.** 
1. Let $a \in G_1$. Then $[a] \subseteq G_1$, so $N(a) \subseteq G_1^*$, hence $[a] \subseteq G_1^{*\Delta}$ (since $G_1^*$ is an open subset of $\mathcal{F}$). Therefore $a \in G_1^{*\Delta}$.

2. Let $F \in G_2$. Then $(\exists a \in F)[N(a) \subseteq G_2]$. Hence $(\exists a \in F)[[a] \subseteq G_2^\Delta]$, and thus $(\exists a \in F)[N(a) \subseteq G_2^{\Delta*}]$ (since $G_2^\Delta$ is an open subset of $P$). Therefore $F \in G_2^{\Delta*}$. $\square$
