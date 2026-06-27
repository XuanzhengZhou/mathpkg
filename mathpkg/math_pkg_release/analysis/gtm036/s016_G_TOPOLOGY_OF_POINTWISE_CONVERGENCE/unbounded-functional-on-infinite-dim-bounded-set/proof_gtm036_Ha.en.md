---
role: proof
locale: en
of_concept: unbounded-functional-on-infinite-dim-bounded-set
source_book: gtm036
source_chapter: "H"
source_section: "H(a)"
---

Let $A$ be a bounded set in $E$ that is contained in no finite-dimensional subspace. Since $A$ is not contained in any finite-dimensional subspace, we can select a sequence $\{a_n\} \subset A$ of linearly independent vectors. Let $L = \operatorname{span}\{a_n : n \in \mathbb{N}\}$.

Define a linear functional $f$ on $L$ by setting $f(a_n) = n$ for each $n$ and extending linearly. Since $\{a_n\}$ are linearly independent, this defines $f$ consistently on $L$. Extend $f$ to a linear functional on all of $E$ (using a Hamel basis or the Hahn-Banach theorem if $E$ is locally convex; more generally, any linear map on a subspace extends to the whole space via a Hamel basis).

Then $|f(a_n)| = n$ for all $n$, while $a_n \in A$. Since $n \to \infty$, $f$ is not bounded on $A$.

For the existence of such a set $A$ in an infinite-dimensional pseudo-metrizable space: the space contains an infinite linearly independent set. Any bounded neighborhood $U$ of $0$ contains a balanced, absorbing neighborhood. Take an infinite linearly independent subset $\{x_n\}$ scaled to lie in $U$; this set is bounded (contained in $U$) but lies in no finite-dimensional subspace.
