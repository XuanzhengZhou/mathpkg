---
role: proof
locale: en
of_concept: ascoli-theorem-equicontinuity
source_book: gtm027
source_chapter: "7"
source_section: "Compactness and Equicontinuity"
---

# Proof of Theorem 7.17 — Ascoli Theorem (Equicontinuity Version)

Let $C$ be the family of all continuous functions on a regular locally compact space $X$ to a Hausdorff uniform space $Y$, with the topology of uniform convergence on compacta. A subfamily $F \subset C$ is compact iff:

**(Necessity)** If $F$ is compact, then (a) $F$ is closed in $C$ (since $C$ is Hausdorff). (b) For each $x \in X$, the evaluation map $e_x$ is continuous, so $F[x] = e_x[F]$ is compact, hence $F[x]^-$ is compact. (c) By Theorem 7.11, the compact-open topology on $C$ equals the topology of uniform convergence on compacta, and by Theorem 7.5 this topology is jointly continuous on compacta. Since $X$ is locally compact, joint continuity on compacta equals joint continuity (Corollary 7.5). Thus the topology on $F$ is jointly continuous, and by Theorem 7.16, $F$ is equicontinuous.

**(Sufficiency)** Assume (a) $F$ is closed in $C$, (b) $F[x]^-$ is compact for each $x \in X$, and (c) $F$ is equicontinuous. By Theorem 7.14, the pointwise closure $\overline{F}$ (in $Y^X$) is equicontinuous. By Theorem 7.15, the pointwise topology $\wp$ on $\overline{F}$ is jointly continuous, hence jointly continuous on compacta. By Theorem 7.6, $\overline{F}$ is $\wp$-compact. Since $\wp$ equals the compact-open topology on $\overline{F}$ (Theorems 7.5, 7.11), $\overline{F}$ is compact in the compact-open topology. Since $F$ is closed in $C$ and $C$ has the compact-open topology, $F$ is compact.
