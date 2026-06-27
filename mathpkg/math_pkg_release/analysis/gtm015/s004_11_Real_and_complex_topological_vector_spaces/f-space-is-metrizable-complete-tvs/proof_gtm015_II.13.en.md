---
role: proof
locale: en
of_concept: f-space-is-metrizable-complete-tvs
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "13. Spaces of type (F)"
---

# Proof that Space of Type (F) is a Metrizable Complete TVS

**Theorem (13.4).** If $(E, d)$ is a space of type $(F)$ then $E$ is a metrizable complete TVS in the topology derived from $d$.

*Proof.* The metric $d$ is additively invariant:

$$d(x + z, y + z) = d((x + z) - (y + z), \theta) = d(x - y, \theta) = d(x, y).$$

It follows that the topology is compatible with the additive group structure (10.4), therefore $E$ is a metrizable topological group. The definition of a space of type $(F)$ includes the completeness of $(E, d)$ as a metric space, so $E$ is a complete topological group.

It remains to verify the continuity of scalar multiplication. By the definition of type $(F)$, we have:
- (ii) if $\lambda_n \to 0$ in $\mathbb{K}$, then $d(\lambda_n x, \theta) \to 0$ for each $x \in E$,
- (iii) if $d(x_n, \theta) \to 0$, then $d(\lambda x_n, \theta) \to 0$ for each $\lambda \in \mathbb{K}$.

Thus conditions (ii) and (iii) of Lemma (13.3) are satisfied. Applying (13.3), the scalar multiplication is jointly continuous, and $E$ is a TVS. Hence $E$ is a metrizable complete TVS. $\square$
