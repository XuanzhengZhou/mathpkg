---
role: proof
locale: en
of_concept: compact-regular-uniformity-from-diagonal-neighborhoods
source_book: gtm027
source_chapter: "6"
source_section: "Compact Spaces"
---

# Proof of Uniqueness of Uniformity on Compact Regular Spaces (Corollary 6.30)

**Corollary 6.30.** If $(X, \mathcal{J})$ is a compact regular topological space, then the family of all neighborhoods of the diagonal $\Delta$ is a uniformity for $X$ and $\mathcal{J}$ is the uniform topology.

**Proof.** Since $(X, \mathcal{J})$ is compact and regular, it is completely regular. Therefore there exists at least one uniformity $\mathcal{U}$ whose uniform topology is $\mathcal{J}$.

By Theorem 6.29, every neighborhood of the diagonal in $X \times X$ (relative to the product topology of $\mathcal{J}$) is a member of $\mathcal{U}$. Conversely, every member of $\mathcal{U}$ is a neighborhood of the diagonal by definition (since the diagonal is contained in each uniformity member, and the uniformity topology makes each member a neighborhood of $\Delta$ in the product uniformity, which coincides with the product topology by Theorem 6.10). Thus $\mathcal{U}$ is precisely the family of all neighborhoods of $\Delta$.

This shows that the uniformity is uniquely determined by the topology: it must be the family of all neighborhoods of the diagonal. Since there is only one such uniformity, the compact regular topology determines the uniformity uniquely.

Moreover, the family of all neighborhoods of $\Delta$ indeed satisfies the uniformity axioms: the diagonal intersection property is clear; symmetry follows because the inverse of a neighborhood of $\Delta$ is again a neighborhood of $\Delta$; the square-refinement property follows from the fact that for any neighborhood $U$ of $\Delta$, by compactness and continuity of the map $(x,y,z) \mapsto (x,z)$ there is a neighborhood $V$ of $\Delta$ with $V \circ V \subset U$.
