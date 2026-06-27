---
role: proof
locale: en
of_concept: finite-set-not-equivalent-to-proper-subset
source_book: gtm027
source_chapter: "Appendix"
source_section: "The Classification Axiom Scheme"
---

# Proof of Finite Sets Not Equivalent to Proper Subsets

PROOF It is sufficient to consider the case where $x$ is an integer. Suppose $y \subset x$, $y \neq x$, $P(y) = x$, and $x \in \omega$. Then $x \neq 0$ and hence $x = u + 1$ for some integer $u$. Because $y \neq x$ there is a subset of $u$ which is equivalent to $y$ and hence $P(y) \leq u$. But $P(y) = x = u + 1$, and this contradicts the fact that each integer is a cardinal number.

The property of theorem 172, that a finite set is equivalent to no proper subset, actually characterizes

is a 1-1 function $f$ on $x + 1$ such that $f(y) \in u$ for $y$ in $x$ and $f(x) \in x \sim u$. Hence $P(x + 1) \leq P(x)$.

The principal remaining theorem depends on an order which will be assigned to the cartesian product $R \times R$. An intuitive description of this order may be instructive. It is to be a well ordering, and on $\omega \times \omega$ it is to have the property that the class of all predecessors of a member $(x,y)$ of $\omega \times \omega$ is finite (a generalization of this fact is the key to the usefulness of the order).

Picture $\omega \times \omega$ as a subset of the Euclidean plane and divide $\omega \times \omega$ into classes, putting in the same class pairs $(x,y)$ and $(u,v)$ such that the maximum of $x$ and $y$ is identical with the maximum of $u$ and $v$. Each class then consists of two sides of a square, and the ordering is arranged so that points on smaller squares precede points on large squares. For points on the sides of the same square the ordering proceeds along the upper edge and to the right, up to but not including the corner point, and then along the right-hand edge upward, ending with the corner point.

If $x$ and $y$ are ordinals, the larger of them is $x \cup y$. This motivates the following definition.
