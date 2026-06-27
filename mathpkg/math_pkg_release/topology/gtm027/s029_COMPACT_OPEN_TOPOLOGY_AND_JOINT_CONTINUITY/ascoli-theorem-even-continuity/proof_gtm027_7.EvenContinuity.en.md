---
role: proof
locale: en
of_concept: ascoli-theorem-even-continuity
source_book: gtm027
source_chapter: "7"
source_section: "Even Continuity"
---

# Proof of Theorem 7.21 — Ascoli Theorem (Even Continuity Version)

Let $C$ be the family of all continuous functions on a regular locally compact space $X$ to a regular Hausdorff space $Y$, with the compact-open topology. A subset $F \subset C$ is compact iff:

**(Necessity)** If $F$ is compact relative to the compact-open topology:
- (a) $F$ is closed in $C$ (compact subsets of a Hausdorff space are closed).
- (b) For each $x \in X$, the evaluation map $f \mapsto f(x)$ is continuous on $(C, \text{compact-open})$, so $F[x]$ is compact and $F[x]^-$ is compact.
- (c) By Theorem 7.6, since $F$ is compact in the compact-open topology, the pointwise topology on $F$ coincides with the compact-open topology and is jointly continuous. By Theorem 7.20, $F$ is evenly continuous.

**(Sufficiency)** Assume (a), (b), (c). By Theorem 7.19, the pointwise closure $F^-$ of $F$ in $Y^X$ is evenly continuous, and the pointwise topology $\wp$ is jointly continuous on $F^-$. By Theorem 7.6 (applied with the jointly continuous topology $\wp$ on $F^-$), $F^-$ is $\wp$-compact, hence compact in the compact-open topology (since $\wp$ coincides with the compact-open topology on $F^-$). Condition (a) ensures $F$ is closed, hence $F = F^-$ and $F$ is compact.
