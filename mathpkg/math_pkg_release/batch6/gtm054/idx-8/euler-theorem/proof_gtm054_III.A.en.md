---
role: proof
locale: en
of_concept: euler-theorem
source_book: gtm054
source_chapter: "III"
source_section: "A"
---

Let $\Gamma = (V, f, E)$ be a multigraph.

By IIA8, $E \in \mathcal{X}(\Gamma)$ (the cycle space) if and only if $\mathcal{X}^{\perp}(\Gamma)$ is even. The condition that $\mathcal{X}^{\perp}(\Gamma)$ is even means precisely that each vertex has even valence (by definition of the orthogonal complement of the cycle space).

If $\Gamma$ is connected and $E$ is a cycle (i.e., $E \in \mathcal{X}(\Gamma)$), then by Proposition A10, since $\Gamma_E = \Gamma$ is connected and $E \in \mathcal{L}(\Gamma) \setminus \{\varnothing\}$, the submultigraph $\Gamma_E = \Gamma$ is a circuit. This circuit uses every edge exactly once (since its edge set is $E$), so it is an Euler circuit.

Conversely, if $\Gamma$ has an Euler circuit, it is necessarily connected. Moreover, the set $E$ of all edges of $\Gamma$ is precisely the edge set of the Euler circuit, which is a cycle. Hence $E \in \mathcal{X}(\Gamma)$, and by IIA8 each vertex has even valence.
