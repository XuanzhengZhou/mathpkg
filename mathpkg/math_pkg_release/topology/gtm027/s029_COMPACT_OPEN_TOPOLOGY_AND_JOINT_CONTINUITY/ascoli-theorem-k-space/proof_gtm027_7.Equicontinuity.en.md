---
role: proof
locale: en
of_concept: ascoli-theorem-k-space
source_book: gtm027
source_chapter: "7"
source_section: "Compactness and Equicontinuity"
---

# Proof of Theorem 7.18 — Ascoli Theorem for k-Spaces

Let $X$ be a $k$-space which is either Hausdorff or regular, $Y$ a Hausdorff uniform space, and $C$ the family of all continuous functions on $X$ to $Y$ with the topology of uniform convergence on compacta. A subfamily $F \subset C$ is compact iff:

**(Sketch)** The proof is a straightforward application of Theorem 7.6, the results of this section, and the fact that a function on a $k$-space is continuous if and only if it is continuous on each compact subset of $X$.

**(Necessity)** If $F$ is compact in the compact-open topology, conditions (a) and (b) follow as in Theorem 7.17. For (c), the compact-open topology is jointly continuous on compacta (Theorem 7.5). Since $F$ is compact, the compact-open and pointwise topologies coincide on $F$ (as in the proof of Theorem 7.6). The pointwise topology is then jointly continuous, so by Theorem 7.16, $F$ is equicontinuous. The restriction of $F$ to each compact $K \subset X$ preserves equicontinuity, so $F$ is equicontinuous on every compact subset.

**(Sufficiency)** Assume $F$ satisfies (a), (b), (c). By Theorems 7.14 and 7.15, the pointwise closure of $F$ is equicontinuous and the pointwise topology is jointly continuous on it. Since a function on a $k$-space continuous on each compact set is continuous, the pointwise closure lies in $C$. By Theorem 7.6 (applied with the class $C$ of functions continuous on each compactum), $F$ is compact in the compact-open topology.
