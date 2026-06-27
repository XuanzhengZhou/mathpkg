---
role: proof
locale: en
of_concept: theorem-3-5-cardinality-finite-projective-planes
source_book: gtm006
source_chapter: "3"
source_section: "2. Basic Concepts"
---

Let $\mathcal{P}$ be a finite projective plane.

By Theorem 3.4, all lines have the same number of points. Let $n + 1$ be this common number, where $n$ is a positive integer. By the dual of Theorem 3.4, all points are incident with the same number of lines, which must also be $n + 1$ (since part (b) of Theorem 3.4 provides a bijection between the points of any line and the lines through any point).

To show $n \geq 2$, observe that if $A, B, C, D$ is a quadrangle in $\mathcal{P}$, then the point $X = AB \cap CD$ lies on $AB$ and is distinct from both $A$ and $B$ (since $A$ is not on $CD$ and $C, D$ are not collinear with $A$). Thus the line $AB$ contains at least the three points $A, B, X$, so $n + 1 \geq 3$, giving $n \geq 2$.

Now count the total number of points. Fix a point $P$. Every other point $Q \neq P$ lies on a unique line through $P$ (axiom (i)). There are $n + 1$ lines through $P$, and each such line contains $n$ points distinct from $P$. Hence the total number of points is:
\[
1 + (n + 1) \cdot n = n^2 + n + 1.
\]
By the Principle of Duality (Theorem 3.2), the total number of lines is also $n^2 + n + 1$. $\square$
