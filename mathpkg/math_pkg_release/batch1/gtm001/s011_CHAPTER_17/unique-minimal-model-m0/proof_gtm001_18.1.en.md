---
role: proof
locale: en
of_concept: unique-minimal-model-m0
source_book: gtm001
source_chapter: "18"
source_section: "18.1"
---

From Mostowski's theorem (Theorem 12.8), every standard model is $\in$-isomorphic to a standard transitive model. Therefore the existence of a set that is a standard model of ZF implies the existence of a set that is a standard transitive model of ZF.

If $\alpha$ is the smallest ordinal not contained in such a model, then $\alpha$ is the class of ordinals for that model. Let $\alpha_0$ be the smallest such ordinal, witnessed by a standard transitive model $N_0$. Since $N_0$ is a model of ZF, define

$$M_0 = L^{N_0} = \{x \mid (\exists \alpha \in N_0) [x = F' \alpha]\} = \{F' \alpha \mid \alpha < \alpha_0\}.$$

Then $M_0$ is a model of ZF + $V = L$. If $N$ is any standard transitive model of ZF, then $N$ is closed under the fundamental operations, and since $\alpha_0 \subseteq N$, it follows that $M_0 \subseteq N$. This establishes $M_0$ as the unique minimal model. Countability follows from the Lowenheim-Skolem theorem.
