---
role: proof
locale: en
of_concept: ordinal-characterization-boolean-valued
source_book: gtm008
source_chapter: "13"
source_section: "13. Boolean-Valued Set Theory"
---

($\geq$): For each $\alpha \in On$, $[\![u = \check{\alpha}]\!] = [\![u = \check{\alpha}]\!] \cdot [\![\operatorname{Ord}(\check{\alpha})]\!] \leq [\![\operatorname{Ord}(u)]\!]$ by Corollary 13.7 (the substitution property for the predicate $\operatorname{Ord}$). Therefore $\sum_{\alpha \in On} [\![u = \check{\alpha}]\!] \leq [\![\operatorname{Ord}(u)]\!]$.

($\leq$): To prove $[\![\operatorname{Ord}(u)]\!] \leq \sum_{\alpha \in On} [\![u = \check{\alpha}]\!]$, first note from Theorem 13.17 that for distinct ordinals $\alpha \neq \beta$:
$$[\![x = \check{\alpha}]\!] \cdot [\![x = \check{\beta}]\!] \leq [\![\check{\alpha} = \check{\beta}]\!] = 0.$$

Therefore, for each $x \in V^{(B)}$, the set
$$D_x \triangleq \{ \xi \mid [\![x = \check{\xi}]\!] > 0 \}$$
is a set (the mapping $\xi \mapsto [\![x = \check{\xi}]\!]$ is a one-to-one function on $D_x$, and its values lie in the set $B$). Thus $D = \bigcup_{x \in \mathcal{D}(u)} D_x$ is a set of ordinals. Taking an ordinal $\alpha$ greater than $\sup D$, we obtain:
$$(\forall \beta \geq \alpha)(\forall x \in \mathcal{D}(u))\; [\![x = \check{\beta}]\!] = 0.$$

Consequently, $[\![\check{\alpha} \in u]\!] = \sum_{x \in \mathcal{D}(u)} u(x) \cdot [\![x = \check{\alpha}]\!] = 0$.

Since $V^{(B)}$ is a model of $ZF$ (Theorem 13.12), $[\![\operatorname{Ord}(\check{\alpha})]\!] = 1$ and the ordinal property implies that if $u$ is an ordinal, then either $u \in \check{\alpha}$ or $\check{\alpha} \in u$ or $u = \check{\alpha}$ holds. Since $[\![\check{\alpha} \in u]\!] = 0$, we get $[\![\operatorname{Ord}(u)]\!] \leq [\![u \in \check{\alpha} \vee u = \check{\alpha}]\!]$. By induction on the rank of elements of $\check{\alpha}$, this reduces to $\sum_{\beta < \alpha} [\![u = \check{\beta}]\!] \leq \sum_{\beta \in On} [\![u = \check{\beta}]\!]$.
