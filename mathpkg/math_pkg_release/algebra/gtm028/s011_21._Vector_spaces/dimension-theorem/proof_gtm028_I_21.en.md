---
role: proof
locale: en
of_concept: dimension-theorem
source_book: gtm028
source_chapter: "I"
source_section: "21"
---

Let $V$ admit a finite basis $B = \{x_1, \ldots, x_n\}$ of $n$ elements and let $B'$ be any other basis of $V$. We show that $B'$ also has $n$ elements.

Since $B$ generates $V$, every element of $B'$ is a linear combination of elements of $B$. By repeated application of the exchange property $(S_5)$, we can replace elements of $B$ by elements of $B'$ one by one while maintaining a basis. More precisely: by Theorem 21, since $B'$ is free, we can take $L = B'$ and $S = B$ (a finite generating set) to obtain a subset $B'' \subseteq B$ such that $B' \cup B''$ is a basis and $B' \cap B'' = \emptyset$. But $B'$ is already a basis, hence $B' \cup B'' = B'$ and $B'' = \emptyset$. By the maximality argument in the proof of Theorem 21, this implies $|B'| \geq |B| = n$.

Symmetrically, applying Theorem 21 with $L = B$ and $S = B'$, we obtain $|B| \geq |B'|$. Therefore $|B'| = |B| = n$.
