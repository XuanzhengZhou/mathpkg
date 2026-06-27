---
role: proof
locale: en
of_concept: ordinal-characterization-boolean-valued
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

First, $[\![u = \check{\alpha}]\!] = [\![u = \check{\alpha}]\!] \cdot [\![\text{Ord}(\check{\alpha})]\!] \leq [\![\text{Ord}(u)]\!]$ by Corollary 13.7. Summing over $\alpha \in On$ gives $\sum_{\alpha \in On} [\![u = \check{\alpha}]\!] \leq [\![\text{Ord}(u)]\!]$.

For the reverse inequality, note by Theorem 13.17 that for $\alpha \neq \beta$, $[\![u = \check{\alpha}]\!] \cdot [\![u = \check{\beta}]\!] \leq [\![\check{\alpha} = \check{\beta}]\!] = 0$. Therefore the map $\xi \mapsto [\![u = \check{\xi}]\!]$ is injective on $D_u = \{\xi \mid [\![u = \check{\xi}]\!] > 0\}$, and since the values range over the set $B$, $D_u$ is a set. Let $D = \bigcup_{x \in \mathcal{D}(u)} D_x$ be a set, and take $\alpha$ greater than $\sup D$. Then $(\forall \beta \geq \alpha)(\forall x \in \mathcal{D}(u)) [\![x = \check{\beta}]\!] = 0$, so $[\![\check{\alpha} \in u]\!] = 0$. Since $V^{(B)}$ models $ZF$, $[\![\text{Ord}(u)]\!] \leq [\![u \subseteq \check{\alpha}]\!]$, which implies $[\![\text{Ord}(u)]\!] \leq \sum_{\beta < \alpha} [\![u = \check{\beta}]\!] \leq \sum_{\beta \in On} [\![u = \check{\beta}]\!]$.
