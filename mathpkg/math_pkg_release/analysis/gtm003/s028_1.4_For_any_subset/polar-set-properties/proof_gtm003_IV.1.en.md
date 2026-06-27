---
role: proof
locale: en
of_concept: polar-set-properties
source_book: gtm003
source_chapter: "IV"
source_section: "1.4"
---

The $\sigma(G, F)$-closedness of $M^\circ$ follows from the definition: $M^\circ = \{ y \in G : \operatorname{Re}\langle x, y \rangle \leq 1 \text{ for all } x \in M \}$ is an intersection of $\sigma(G, F)$-closed half-spaces $\{ y \in G : \operatorname{Re}\langle x, y \rangle \leq 1 \}$ (each being the inverse image of a closed set under the continuous linear functional $y \mapsto \operatorname{Re}\langle x, y \rangle$), hence closed. Convexity follows similarly, as each half-space is convex and intersections of convex sets are convex. Clearly $0 \in M^\circ$ since $\operatorname{Re}\langle x, 0 \rangle = 0 \leq 1$ for all $x \in M$.

If $M$ is circled, then for any $y \in M^\circ$ and any scalar $\lambda$ with $|\lambda| \leq 1$, we have $\operatorname{Re}\langle x, \lambda y \rangle = \operatorname{Re}(\lambda \langle x, y \rangle) \leq |\lambda| \cdot \operatorname{Re}\langle x, y \rangle \leq 1$ for all $x \in M$ (using that $M$ is circled, so $\bar{\lambda}x \in M$ and $\operatorname{Re}\langle \bar{\lambda}x, y \rangle = \operatorname{Re}(\bar{\lambda}\langle x, y \rangle) = \operatorname{Re}\langle x, \lambda y \rangle$), hence $\lambda y \in M^\circ$, so $M^\circ$ is circled.

If $M$ is a subspace of $F$, then for any $y \in M^\circ$ and scalar $\lambda$, we have $\operatorname{Re}\langle x, \lambda y \rangle = \operatorname{Re}(\lambda \langle x, y \rangle)$. Since $M$ is a subspace, for any $x \in M$, $\bar{\lambda}x \in M$, so $\operatorname{Re}\langle \bar{\lambda}x, y \rangle = \operatorname{Re}(\bar{\lambda}\langle x, y \rangle) \leq 1$. Taking supremum over such relations shows $\lambda y \in M^\circ$, so $M^\circ$ is a subspace.
