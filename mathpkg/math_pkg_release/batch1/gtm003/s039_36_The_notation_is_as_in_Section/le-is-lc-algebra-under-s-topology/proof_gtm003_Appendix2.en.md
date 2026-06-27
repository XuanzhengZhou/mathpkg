---
role: proof
locale: en
of_concept: le-is-lc-algebra-under-s-topology
source_book: gtm003
source_chapter: "Appendix 2"
source_section: "Topological Algebras"
---

The proof proceeds in several steps:

1. $\mathcal{L}(E)$ with the $\mathfrak{S}$-topology is a locally convex space. The invariance of $\mathfrak{S}$ under each $u \in \mathcal{L}(E)$ ensures that the seminorms defining the $\mathfrak{S}$-topology behave well under composition.

2. Separate continuity of multiplication: For fixed $u \in \mathcal{L}(E)$, the map $v \mapsto u \circ v$ is continuous because for each $S \in \mathfrak{S}$, $u(S) \in \mathfrak{S}$ (by invariance), so the seminorm $\sup_{x \in S} p(u(v(x)))$ is controlled by $\sup_{y \in u(S)} p(v(y))$, which is a continuous seminorm. Similarly for right multiplication.

3. For the $\mathfrak{B}$-topology (bounded convergence), if $B$ is bounded in $\mathcal{L}_{\mathfrak{B}}(E)$, then for each bounded $S \subset E$, $\{u(x) : u \in B, x \in S\}$ is bounded in $E$. This implies the $\mathfrak{B}$-hypocontinuity of multiplication on bounded sets.

4. If $E$ is barreled, the Banach-Steinhaus theorem implies that simply bounded sets are equicontinuous, from which left $\mathfrak{B}$-hypocontinuity for the topology of simple convergence follows.

5. If $\mathcal{L}_{\mathfrak{S}}(E)$ is an (F)-space (complete metrizable), separate continuity implies joint continuity by (III, 5.1), a consequence of the closed graph theorem for (F)-spaces.
