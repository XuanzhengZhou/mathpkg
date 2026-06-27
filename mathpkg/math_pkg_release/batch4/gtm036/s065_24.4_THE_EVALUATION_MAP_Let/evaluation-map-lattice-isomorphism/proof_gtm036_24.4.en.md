---
role: proof
locale: en
of_concept: evaluation-map-lattice-isomorphism
source_book: gtm036
source_chapter: "24"
source_section: "24.4"
---

The evaluation map $e \colon E \to E^{**}$ is defined by $e(x)(f) = f(x)$ for $x \in E$, $f \in E^*$. It is well known that $e$ is a linear isometry for any normed space.

To show that $e$ is a lattice isomorphism, it suffices to prove that $e$ preserves the lattice operations. The key step is to show that $e(x)^+ = e(x^+)$ for every $x \in E$.

For any element $f \in E^*$,
$$
e(x)^+(f) = \sup \{g(x): 0 \leq g \leq f \text{ and } g \in E^*\} = f(x^+) = e(x^+)(f),
$$
where the second equality follows from 23.13 (which characterizes the value of $f(x^+)$ as the supremum of $g(x)$ over all $g \in E^*$ with $0 \leq g \leq f$). Hence $e(x)^+ = e(x^+)$.

From this, for any $x, y \in E$,
$$
e(x \vee y) = e((x - y)^+ + y) = e((x - y)^+) + e(y) = e(x - y)^+ + e(y) = (e(x) - e(y))^+ + e(y) = e(x) \vee e(y),
$$
and similarly $e(x \wedge y) = e(x) \wedge e(y)$.

Since $E$ has a separating dual (as a normed lattice), $e$ is injective. The image $e(E)$ is therefore a sublattice of $E^{**}$ that is lattice-isomorphic to $E$.
