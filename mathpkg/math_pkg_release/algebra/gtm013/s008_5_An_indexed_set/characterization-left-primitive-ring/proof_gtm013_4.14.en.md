---
role: proof
locale: en
of_concept: characterization-left-primitive-ring
source_book: gtm013
source_chapter: "4"
source_section: "14"
---

By Schur's Lemma (13.3), $D = \operatorname{End}({}_R T)$ is a division ring, whence $T_D$ is a $D$-vector space. Since ${}_R T$ is faithful and simple, the ring homomorphism $\lambda: R \to \operatorname{End}(T_D) = \operatorname{BiEnd}({}_R T)$ is injective and the Density Theorem (14.3) establishes that its image is dense in $\operatorname{End}(T_D)$. For the final statement, suppose $x_1, \ldots, x_n \in T$ are $D$-linearly independent and $y_1, \ldots, y_n \in T$. Then there is a linear transformation $b \in \operatorname{End}(T_D)$ such that $b(x_i) = y_i$ $(i = 1, \ldots, n)$. Now apply (14.3).

Conversely, if $D$ is a division ring and ${}_R T_D$ satisfies the density condition, then ${}_R T$ is faithful by hypothesis and simple (for any non-zero $x \in T$, $\{x\}$ is $D$-linearly independent so $Rx = T$ by the condition). Hence $R$ is left primitive. $\square$
