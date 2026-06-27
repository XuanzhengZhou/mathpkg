---
role: proof
locale: en
of_concept: dimension-orthogonal-complement
source_book: gtm054
source_chapter: "2"
source_section: "IIA"
---

Since $\mathcal{A}$ is a subspace, $\mathcal{A} = (\mathcal{A}^{\perp})^{\perp}$. Hence:

$$U \in \mathcal{A} \Leftrightarrow S \cdot U = 0 \quad \text{for all } S \in \mathcal{A}^{\perp}$$
$$\Leftrightarrow |S \cap U| \equiv 0 \text{ (modulo 2)} \quad \text{for all } S \in \mathcal{A}^{\perp}$$
$$\Leftrightarrow |S| \quad \text{is even for all } S \in \mathcal{A}^{\perp}$$

Thus $U \in \mathcal{A}$ if and only if $\mathcal{A}^{\perp} \subseteq \mathcal{E}(U)$. This characterization yields the dimension formula through standard linear algebra arguments relating the dimension of a subspace, its orthogonal complement, and the dimension of the ambient space.
