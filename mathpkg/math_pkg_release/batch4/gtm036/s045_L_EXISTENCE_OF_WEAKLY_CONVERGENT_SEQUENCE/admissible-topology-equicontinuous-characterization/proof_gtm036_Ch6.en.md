---
role: proof
locale: en
of_concept: admissible-topology-equicontinuous-characterization
source_book: gtm036
source_chapter: "Chapter 6: Admissible Topologies"
source_section: ""
---

Let $\mathcal{T}$ be a locally convex topology on $E$ with dual $E^*$. By definition of $E^*$, each $f \in E^*$ is $\mathcal{T}$-continuous, so $\mathcal{T}$ is admissible relative to the natural pairing $\langle E, E^* \rangle$.

By the bipolar theorem (Theorem 8.21 or its consequence in Theorem 16.4), every $\mathcal{T}$-neighborhood $U$ of $0$ satisfies $U = U^{\circ\circ}$ where the outer polar is taken in $E^*$. Thus the polars $U^\circ$ are $\sigma(E^*, E)$-bounded and equicontinuous subsets of $E^*$.

Conversely, the topology of uniform convergence on $\mathcal{T}$-equicontinuous subsets of $E^*$ has as a local subbase the polars of such sets. By the Alaoglu-Bourbaki theorem, $\mathcal{T}$-equicontinuous sets are relatively weak* compact, hence $w(E^*, E)$-bounded. Their polars are $\mathcal{T}$-neighborhoods of $0$ (again by the bipolar theorem). Therefore the topology of uniform convergence on $\mathcal{T}$-equicontinuous sets coincides with $\mathcal{T}$.

Equivalently, the family of polars of all $\mathcal{T}$-neighborhoods of $0$ (which are precisely the $\mathcal{T}$-equicontinuous subsets of $E^*$) determines $\mathcal{T}$ by the bipolar theorem.
