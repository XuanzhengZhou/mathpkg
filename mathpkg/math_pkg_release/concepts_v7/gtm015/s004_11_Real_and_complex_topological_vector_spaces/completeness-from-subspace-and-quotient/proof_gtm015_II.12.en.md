---
role: proof
locale: en
of_concept: completeness-from-subspace-and-quotient
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "12. Metrizable complete TVS"
---

# Proof of Completeness from Complete Subspace and Quotient

**Theorem (12.2).** Suppose $E$ is a metrizable TVS, and $M$ is a closed linear subspace of $E$ such that $M$ and $E/M$ are complete TVS, in the relative topology and the quotient topology, respectively. Then $E$ is a complete TVS.

*Proof.* The TVS $M$ and $E/M$ are of course metrizable (cf. 6.4); the completeness of $E$ is an immediate application of (9.2). The theorem cited (9.2) states that if a metrizable topological group $G$ has a closed normal subgroup $H$ such that $H$ and $G/H$ are complete, then $G$ is complete. Applying this to the additive topological group $(E, +)$ with the closed subgroup $M$ (which is normal since the group is abelian), and noting that $M$ and $E/M$ are complete as topological groups, we conclude that $(E, +)$ is complete, hence $E$ is a complete TVS. $\square$
