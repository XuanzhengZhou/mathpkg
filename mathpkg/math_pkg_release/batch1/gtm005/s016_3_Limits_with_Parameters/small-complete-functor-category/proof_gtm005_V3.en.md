---
role: proof
locale: en
of_concept: small-complete-functor-category
source_book: gtm005
source_chapter: "V"
source_section: "3. Limits with Parameters"
---

Let $F : J \rightarrow X^P$ be any functor with $J$ small. For each object $p \in P$, the composite $E_p \circ F : J \rightarrow X$ is a small diagram in $X$. Since $X$ is small-complete, each $E_p \circ F$ has a limit $L_p$ in $X$.

By the pointwise limits theorem (limits in $X^P$ are computed pointwise), the object function $p \mapsto L_p$ extends to a functor $L : P \rightarrow X$ (which is an object of $X^P$), and $L$ together with the pointwise limiting cones assembles into a limit of $F$ in $X^P$. Therefore every small diagram in $X^P$ has a limit, so $X^P$ is small-complete.
