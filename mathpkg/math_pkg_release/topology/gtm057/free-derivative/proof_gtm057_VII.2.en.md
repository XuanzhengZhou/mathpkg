---
role: proof
locale: en
of_concept: free-derivative
source_book: gtm057
source_chapter: "VII"
source_section: "2"
---
Uniqueness follows because the values are specified on a generating set of $F$. For existence, define $\Lambda_j: W(A) \to JF$ inductively on the semigroup of words $W(A)$:
$$\Lambda_j 1 = 0,$$
$$\Lambda_j(a_i^n) = \delta_{ij} \frac{x_i^n - 1}{x_i - 1},$$
$$\Lambda_j(ab) = \Lambda_j a + \theta a \cdot \Lambda_j b.$$
One verifies that equivalent words have equal images, so $\partial/\partial x_j$ is well-defined on $F$ by $(\partial/\partial x_j)\theta a = \Lambda_j a$. Extension to $JF$ is by linearity.
