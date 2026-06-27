---
role: proof
locale: en
of_concept: block-decomposition-of-semiperfect-rings
source_book: gtm013
source_chapter: "7"
source_section: "27. Semiperfect Rings"
---

Since $R$ is semiperfect, there exists a complete set $e_1, \ldots, e_n$ of pairwise orthogonal primitive idempotents, so $R = R e_1 \oplus \ldots \oplus R e_n$. Because 1 is a sum of primitive idempotents, $R$ has a block decomposition (7.9). That is, there exist unique orthogonal central idempotents $u_1, \ldots, u_t$ in $R$ such that $1 = u_1 + \cdots + u_t$ and each $u_j R u_j$ is an indecomposable ring. Given any primitive idempotent $e \in R$, $e u_j \neq 0$ for exactly one $j$, and $e u_j \neq 0$ iff $e u_j = e$. Thus a primitive idempotent belongs to exactly one block.

The characterization via common composition factors follows from Exercise (27.9): members of a pair of left modules $M_1, M_2$ over a semiperfect ring have a common composition factor iff there exists a primitive idempotent $e \in R$ that annihilates neither $M_1$ nor $M_2$.
