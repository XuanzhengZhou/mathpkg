---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Let $E$ be a vector space over $\mathbb{K}$ and $A$ a convex subset of $E$. The following elementary properties govern the behavior of faces of $A$:

1. **$A$ is a face of itself.** This is immediate from the definition: if $\langle u, v \rangle \subset A$ and $\langle u, v \rangle \cap A \neq \varnothing$, then trivially $\langle u, v \rangle \subset A$.

2. **Arbitrary intersections of faces are faces.** If $(F_i)_{i \in I}$ is a family of faces of $A$ with nonempty intersection, then $F = \bigcap_{i \in I} F_i$ is also a face of $A$. Indeed, $F$ is convex (as an intersection of convex sets) and if $\langle u, v \rangle \subset A$ meets $F$, then it meets each $F_i$, so by the face property $\langle u, v \rangle \subset F_i$ for all $i$, hence $\langle u, v \rangle \subset F$.

3. **Transitivity: a face of a face is a face.** If $F$ is a face of $A$ and $G$ is a face of $F$, then $G$ is a face of $A$. This follows because $\langle u, v \rangle \subset A$ meeting $G$ implies (since $G \subset F$) that the segment meets $F$, so $\langle u, v \rangle \subset F$; then since $G$ is a face of $F$, $\langle u, v \rangle \subset G$.

These properties, particularly (2), are essential for the Zorn's lemma argument in the Krein-Mil'man theorem: the intersection of a chain of closed faces of a compact convex set is nonempty (by compactness) and, by (2), remains a face, providing the upper bound needed.
