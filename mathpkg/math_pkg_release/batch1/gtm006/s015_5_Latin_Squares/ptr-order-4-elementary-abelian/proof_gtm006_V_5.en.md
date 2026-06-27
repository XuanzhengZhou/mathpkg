---
role: proof
locale: en
of_concept: ptr-order-4-elementary-abelian
source_book: gtm006
source_chapter: "V"
source_section: "5"
---

**Proof.**

Let $(R, T)$ be a PTR of order $4$. By Exercise 5.6, the only loops of order $4$ are the two groups: $\mathbb{Z}_4$ and $\mathbb{Z}_2 \times \mathbb{Z}_2$. The additive loop $(R, +)$ defined by $a + b = T(1, a, b)$ is a loop of order $4$, so it must be one of these two groups.

By Exercise 5.7, the Latin square corresponding to the addition table of $(\mathbb{Z}_4, +)$ admits no orthogonal mate. However, by Lemma 5.7 and the construction from a PTR, the $n-1 = 3$ squares $\{x\}$ for $x \neq 0$ must be a complete set of MOLS, and in particular, the square defined by $T(x,i,j)$ for a fixed $x$ must have an orthogonal mate.

If $(R, +)$ were isomorphic to $\mathbb{Z}_4$, then the addition table would be the matrix from Exercise 5.7, which would preclude the existence of orthogonal Latin squares, contradicting the PTR construction. Therefore $(R, +)$ cannot be $\mathbb{Z}_4$, and must be the elementary abelian group $\mathbb{Z}_2 \times \mathbb{Z}_2$.
