---
role: introduce
locale: en
content_hash: ""
written_against: ""
---

Let $E$ be a locally convex, separated topological vector space over $\mathbb{K}$, and let $A$ be a nonempty, compact, convex subset of $E$. If $H$ is any closed $\mathbb{R}$-hyperplane tangent to $A$, then $H$ contains at least one extremal point of $A$.

This is a fundamental existence theorem. The existence of such tangent hyperplanes $H$ is guaranteed by the Hahn-Banach separation theorem (33.13, 30.11), so the theorem asserts that extremal points always exist in compact convex subsets of locally convex spaces.

**Proof outline (Kelley's Zorn argument).** Let $\mathcal{F}$ be the family of all closed faces $F$ of $A$ such that $F \subset H$. This family is nonempty because $H \cap A \in \mathcal{F}$ (Proposition 36.6: a tangent hyperplane intersection is a face). Order $\mathcal{F}$ by reverse inclusion: $F_1 \leq F_2$ iff $F_1 \supset F_2$.

For any chain $(F_\iota)_{\iota \in I}$ in $\mathcal{F}$, the intersection $F = \bigcap_\iota F_\iota$ is nonempty by the compactness of $A$, closed, and a face of $A$ (36.5). Thus $F \in \mathcal{F}$ and is an upper bound for the chain. By Zorn's lemma, $\mathcal{F}$ possesses a maximal element, i.e., a minimal closed face $F_0 \subset H$.

Suppose $F_0$ contains two distinct points $x \neq y$. By the Hahn-Banach theorem, there exists a continuous linear form separating them, leading to a closed hyperplane $H'$ tangent to $F_0$. Then $H' \cap F_0$ is a proper closed face of $F_0$, contradicting the minimality of $F_0$. Hence $F_0$ is a singleton $\{a\}$, and $a$ is an extremal point of $A$ lying in $H$.

This theorem is a key step toward the full Krein-Mil'man theorem (36.9), which states that every compact convex set in a locally convex separated TVS is the closed convex hull of its extremal points.
