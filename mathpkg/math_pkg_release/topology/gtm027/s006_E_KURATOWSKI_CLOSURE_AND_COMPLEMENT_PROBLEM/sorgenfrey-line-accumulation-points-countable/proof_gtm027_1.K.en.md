---
role: proof
locale: en
of_concept: sorgenfrey-line-accumulation-points-countable
source_book: gtm027
source_chapter: "1"
source_section: "K"
---

# Proof on Accumulation Points from the Right in the Sorgenfrey Line

**Theorem.** If $A$ is a set of real numbers, then the set of all points of $A$ which are not accumulation points from the right is countable. More generally, the set of points of $A$ which are not accumulation points from both the right and the left is countable.

*Proof.* Recall: a point $x$ is a $\mathfrak{J}$-accumulation point of $A$ (accumulation point from the right) if every basic neighborhood $[x, x+\varepsilon)$ intersects $A \setminus \{x\}$.

Let $C = \{x \in A : x \text{ is not a right accumulation point of } A\}$. For each $x \in C$, there exists $\varepsilon_x > 0$ such that $[x, x+\varepsilon_x) \cap (A \setminus \{x\}) = \emptyset$.

Consider the collection of intervals $\{[x, x+\varepsilon_x) : x \in C\}$. These intervals are pairwise disjoint: if $x < y$ and the intervals overlapped, then $y \in [x, x+\varepsilon_x)$, which would put $y$ in $A \setminus \{x\}$, contradicting the defining property of $\varepsilon_x$.

A family of pairwise disjoint intervals in $\mathbb{R}$, each of positive length, can be at most countable (each interval contains a rational number, and the rationals are countable). Therefore $C$ is countable.

For the more general statement: the set of points that fail to be accumulation points from the right or fail to be accumulation points from the left is the union of two countable sets, hence countable. (The left-hand version follows by symmetry, considering the space with the reverse order.) $\square$
