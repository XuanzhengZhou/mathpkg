---
role: proof
locale: en
of_concept: atomic-partition-degree-bounds
source_book: gtm054
source_chapter: "Chapter V"
source_section: "Section 30"
---

If each vertex of $\Gamma$ is an element of some atom, then by D7 the atoms form the atomic partition. The graph must contain an edge meeting each of two atoms, each of which lies in the neighborhood of the other. By D10 it follows that $2\alpha \leq \kappa$.

On the other hand, let $x \in A$ where $A$ is an atom. Then $x$ is incident with at most $\alpha - 1$ vertices in $A$ and at most $|N(A)|$ vertices in $V + A$. Since $|N(A)| = \kappa(\Gamma)$, we obtain $\rho(x) \leq \kappa + \alpha - 1$. Since $\kappa \leq \check{\rho}$ (by C4), the bound $2\alpha \leq \rho(x)$ also follows.
