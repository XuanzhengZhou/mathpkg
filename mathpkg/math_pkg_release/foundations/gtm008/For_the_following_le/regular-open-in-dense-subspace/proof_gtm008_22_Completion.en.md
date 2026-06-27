---
role: proof
locale: en
of_concept: regular-open-in-dense-subspace
source_book: gtm008
source_chapter: "22"
source_section: "The Completion of a Boolean Algebra"
---

Let $A \subseteq S$ be regular open in $S$. By Theorem 22.1(1), $A^{-S} = A^{-} \cap S$. Since $A^{-0} \cap S$ is open in $S$, and $A$ is regular open in $S$ (i.e., $A = (A^{-S})^{0S}$), we have

$$A^{-0} \cap S \subseteq (A^{-S})^{0S} = A.$$

On the other hand, if $p \in A$, then since $A$ is open in $S$, there exists an open neighborhood $N(p)$ in $X$ such that $N(p) \cap S \subseteq A$. Since $S$ is dense in $X$, $N(p) \subseteq (N(p) \cap S)^{-} \subseteq A^{-}$, hence $p \in A^{-0}$. Therefore $p \in A^{-0} \cap S$, giving $A \subseteq A^{-0} \cap S$.

Both inclusions yield $A = A^{-0} \cap S$.
