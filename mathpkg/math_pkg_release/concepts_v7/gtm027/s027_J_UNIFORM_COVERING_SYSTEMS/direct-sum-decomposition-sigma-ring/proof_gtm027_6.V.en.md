---
role: proof
locale: en
of_concept: direct-sum-decomposition-sigma-ring
source_book: gtm027
source_chapter: "6"
source_section: "V"
---

# Proof: Direct Sum Decomposition of a Boolean $\sigma$-Ring

With notation as above, the $\sigma$-ring $\mathcal{Q}$ is additively the direct sum of $\mathcal{B}$ and the $\sigma$-ideal $\mathcal{Q} \cap \mathcal{M}$ (the meager members of $\mathcal{Q}$).

By part (b), each $A \in \mathcal{Q}$ has a unique representative $B \in \mathcal{B}$ such that $A \Delta B \in \mathcal{M}$. But $A \Delta B \in \mathcal{Q}$ (since $\mathcal{Q}$ is closed under symmetric difference), so $A \Delta B \in \mathcal{Q} \cap \mathcal{M}$.

Thus we have the decomposition

$$A = B \Delta (A \Delta B)$$

where $B \in \mathcal{B}$ and $A \Delta B \in \mathcal{Q} \cap \mathcal{M}$. Since $\mathcal{M}$ is a $\sigma$-ideal in $\mathcal{Q}$, this decomposition represents $\mathcal{Q}$ as the direct sum:

$$\mathcal{Q} = \mathcal{B} \oplus (\mathcal{Q} \cap \mathcal{M}).$$

Here the ring operations are symmetric difference $\Delta$ (addition) and intersection $\cap$ (multiplication). The direct sum means every element of $\mathcal{Q}$ is uniquely expressible as the symmetric difference of an element of $\mathcal{B}$ and an element of the $\sigma$-ideal.

This provides the representation theorem of type (ii) for arbitrary Boolean $\sigma$-rings: $\mathcal{Q} / (\mathcal{Q} \cap \mathcal{M}) \cong \mathcal{B}$, generalizing the Borel/meager representation for $[0,1]$.
