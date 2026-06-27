---
role: proof
locale: en
of_concept: closure-of-normed-lattice-in-bidual
source_book: gtm036
source_chapter: "24"
source_section: "24.4"
---

Identify $E$ with its image $e(E) \subseteq E^{**}$ under the evaluation map. By 23.14, the lattice operations $(f, g) \mapsto f \vee g$ and $(f, g) \mapsto f \wedge g$ are continuous on $E^{**}$ with respect to the norm topology.

Let $x, y \in E^-$. Then there exist sequences $(x_n), (y_n)$ in $E$ such that $x_n \to x$ and $y_n \to y$ in norm. By continuity of the lattice operations,
$$
x_n \vee y_n \to x \vee y, \qquad x_n \wedge y_n \to x \wedge y.
$$
Since $x_n \vee y_n$ and $x_n \wedge y_n$ belong to $E$ (as $E$ is a lattice), their limits $x \vee y$ and $x \wedge y$ belong to the closure $E^-$.

Thus $E^-$ is closed under the lattice operations and, being a closed subspace of the Banach lattice $E^{**}$, is itself a Banach lattice. Since $E$ is dense in $E^-$ by construction, $E^-$ is a Banach lattice completion of the normed lattice $E$.
