---
role: proof
locale: en
of_concept: compact-hausdorff-topology-coincidence
source_book: gtm027
source_chapter: "7"
source_section: "Compact Open Topology and Joint Continuity"
---

# Proof of Corollary — Compact Hausdorff Range Forces Topology Coincidence

Let $\mathcal{J}$ be a topology for $F$ which is jointly continuous on compacta. By Theorem 7.5, $\mathcal{J} \supset \mathcal{C} \supset \wp$, where $\mathcal{C}$ is the compact-open topology and $\wp$ is the pointwise topology.

If $(F, \mathcal{J})$ is compact and the range space $Y$ is Hausdorff, then $(F, \wp)$ is also Hausdorff (as a subspace of the product of Hausdorff spaces). A continuous bijection from a compact space to a Hausdorff space is a homeomorphism. The identity map $\mathrm{id} : (F, \mathcal{J}) \to (F, \wp)$ is continuous (since $\mathcal{J} \supset \wp$). Since $(F, \mathcal{J})$ is compact and $(F, \wp)$ is Hausdorff, this map is closed and hence a homeomorphism. Therefore $\mathcal{J} = \wp$. Combined with $\mathcal{J} \supset \mathcal{C} \supset \wp$, we obtain $\mathcal{J} = \mathcal{C} = \wp$.

In particular, if $(F, \mathcal{C})$ is compact and $Y$ is Hausdorff, then $\mathcal{C} = \wp$ on $F$.
