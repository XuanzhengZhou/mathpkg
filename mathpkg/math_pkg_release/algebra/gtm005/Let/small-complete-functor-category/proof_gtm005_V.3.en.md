---
role: proof
locale: en
of_concept: small-complete-functor-category
source_book: gtm005
source_chapter: "V"
source_section: "3. Limits with Parameters"
---

**Proof.** If $X$ is small-complete, then for any small index category $J$ and any functor $S : J \rightarrow X^P$, we need to construct a limit. For each $p \in P$, consider the evaluated functor $E_p S : J \rightarrow X$. Since $X$ is small-complete, each $E_p S$ has a limit $\operatorname{Lim}(E_p S)$ in $X$. By the pointwise limits theorem, these assemble into a functor $p \mapsto \operatorname{Lim}(E_p S)$ and yield a limit $\operatorname{Lim} S$ in $X^P$ satisfying $E_p(\operatorname{Lim} S) = \operatorname{Lim}(E_p S)$. Thus every small diagram in $X^P$ has a limit, so $X^P$ is small-complete. $\square$
