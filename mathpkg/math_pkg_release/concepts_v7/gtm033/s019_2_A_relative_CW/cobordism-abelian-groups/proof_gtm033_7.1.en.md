---
role: proof
locale: en
of_concept: cobordism-abelian-groups
source_book: gtm033
source_chapter: "7"
source_section: "1"
---

# Proof of Theorem 1.1: Cobordism Groups

**Theorem 1.1.** The operation of disjoint union makes $\mathfrak{N}^n$ and $\Omega^n$ into abelian groups.

*Proof.* First of all, diffeomorphic manifolds are cobordant: if $M_0 \approx M_1$ then

$$M_0 \times 0 \cup M_1 \times 1 \approx \partial(M_0 \times I)$$

(taking orientations into account where appropriate). The associative and commutative laws follow easily. The zero element of the group is $[V]$ for any $V$ which is the boundary of some compact manifold $W$. For, taking $M$, $M \times I$ and $W$ disjoint, we have

$$(M \times 0 \cup V) \cup (M \times 1) = \partial(M \times I \cup W).$$

Thus $M \cup V \sim M$. (We could take $V = \emptyset$.) The inverse of $[M]$ is $[M]$; the inverse of $[M, \omega]$ is $[M, -\omega]$, as is seen by looking at $M \times I$.

$\square$
