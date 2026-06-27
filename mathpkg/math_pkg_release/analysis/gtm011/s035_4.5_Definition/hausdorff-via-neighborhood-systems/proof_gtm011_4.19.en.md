---
role: proof
locale: en
of_concept: hausdorff-via-neighborhood-systems
source_book: gtm011
source_chapter: "4"
source_section: "4.19"
---

Suppose $(X, \mathcal{T})$ is Hausdorff. Let $x$ and $y$ be distinct points in $X$. Then there exist disjoint open sets $U, V \in \mathcal{T}$ with $x \in U$ and $y \in V$. By the definition of the induced topology (Proposition 4.17), since $U$ is open and $x \in U$, there exists $U' \in \mathcal{N}_x$ such that $U' \subset U$. Similarly, there exists $V' \in \mathcal{N}_y$ such that $V' \subset V$. Since $U \cap V = \emptyset$, we have $U' \cap V' = \emptyset$.

Conversely, suppose the neighborhood condition holds. Let $x$ and $y$ be distinct points. By hypothesis, there exist $U \in \mathcal{N}_x$ and $V \in \mathcal{N}_y$ with $U \cap V = \emptyset$. Define

$$U^* = \{z \in X : \text{there exists } W \in \mathcal{N}_z \text{ with } W \subset U\},$$
$$V^* = \{z \in X : \text{there exists } W \in \mathcal{N}_z \text{ with } W \subset V\}.$$

Then $U^*$ and $V^*$ are open in the induced topology (by Proposition 4.17), $x \in U^*$, $y \in V^*$, and $U^* \cap V^* = \emptyset$ (since any point in the intersection would yield a neighborhood contained in both $U$ and $V$, contradicting $U \cap V = \emptyset$). Thus $(X, \mathcal{T})$ is Hausdorff.
