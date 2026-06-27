---
role: proof
locale: en
of_concept: regular-open-in-dense-subspace
source_book: gtm008
source_chapter: "22"
source_section: "22. The Completion of a Boolean Algebra"
---

Let $A \subseteq S$ be regular open in $S$. By Theorem 22.1.1, $A^{-S} = A^{-} \cap S$. Then, since $A^{-0} \cap S$ is open in $S$,

$$A^{-0} \cap S \subseteq (A^{-S})^{0S} = A.$$

On the other hand, if $p \in A$, then since $A$ is open in $S$, there exists a neighborhood $N(p)$ such that $N(p) \cap S \subseteq A$. Since $S$ is dense in $X$, $N(p) \subseteq (N(p) \cap S)^{-}$, hence $N(p) \subseteq A^{-}$, so $p \in A^{-0}$. Since $p \in S$, $p \in A^{-0} \cap S$. Thus $A \subseteq A^{-0} \cap S$.
