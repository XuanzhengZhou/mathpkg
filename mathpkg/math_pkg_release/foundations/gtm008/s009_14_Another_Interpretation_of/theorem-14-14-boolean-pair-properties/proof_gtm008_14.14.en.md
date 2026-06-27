---
role: proof
locale: en
of_concept: theorem-14-14-boolean-pair-properties
source_book: gtm008
source_chapter: "14"
source_section: "14. Another Interpretation of V^{(B)}"
---

1. It suffices to prove $[(\forall x)[x = u \lor x = v \leftrightarrow x \in \{u, v\}^{(B)}]] = 1.$

But this follows from the fact that for all $x$, $[x \in \{u, v\}^{(B)}] = [x = u] \lor [x = v]$, which holds by construction since $\{u, v\}^{(B)} = \{\langle u, 1 \rangle, \langle v, 1 \rangle\}$.

2. This follows immediately from 1 with $u = v$.

3. This follows from 1 and 2 applied to the definition of ordered pairs: $\langle u, v \rangle^{(B)} = \{\{u\}^{(B)}, \{u, v\}^{(B)}\}^{(B)}$ and $\langle u, v \rangle = \{\{u\}, \{u, v\}\}$.
