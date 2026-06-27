---
role: proof
locale: en
of_concept: dimension-cardinality-invariant
source_book: gtm036
source_chapter: "1"
source_section: "1"
---

The proof is in two parts. First, suppose there is a finite Hamel base $B$ for $E$, and $A$ is an arbitrary linearly independent set. Set up a one-by-one replacement process: a member $x_1$ of $A$ is a linear combination of members of $B$, so some member of $B$ is a linear combination of $x_1$ and the other members of $B$. Hence $x_1$ together with $B$ with one member deleted is a Hamel base. Continue: at the $r$-th stage, $x_r \in A$ is a linear combination of $x_1, \dots, x_{r-1}$ and the non-deleted members of $B$, but $x_r$ is not a linear combination of $x_1, \dots, x_{r-1}$ alone. Therefore one of the remaining members of $B$ can be replaced by $x_r$ to yield a Hamel base. This process continues until $A$ is exhausted (so $|A| \leq |B|$) or all members of $B$ are deleted, in which case every vector is a linear combination of the selected members of $A$, so $A$ has no remaining members.

For infinite bases: let $B$ and $C$ be two infinite Hamel bases. For each $x \in B$, let $F(x)$ be the finite subset of $C$ such that $x$ is a linear combination with non-zero coefficients of the members of $F(x)$. Since finite linear combinations of $\bigcup\{F(x) : x \in B\}$ include every member of $B$ and therefore every member of $E$, we have $C = \bigcup\{F(x) : x \in B\}$. Let $k(A)$ denote the cardinal number of $A$. Then $k(C) \leq k(B) \cdot \aleph_0 = k(B)$. By symmetry, $k(B) \leq k(C)$, so $k(B) = k(C)$.
