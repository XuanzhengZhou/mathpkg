---
role: proof
locale: en
of_concept: stationary-flow-conditional-extremum
source_book: gtm060
source_chapter: "Appendix 2"
source_section: "Section 47"
---

This result is a direct application of Arnold's general theorem on stationary motions of Lie groups with right-invariant metrics (Theorems 7 and 9 from earlier in the appendix).

The configuration space is the group $G = \operatorname{SDiff}(D)$ of volume-preserving diffeomorphisms. The Lie algebra $\mathfrak{g}$ consists of divergence-free vector fields on $D$. The kinetic energy
$$H(v) = \frac{1}{2} \int_D \langle v, v \rangle \, d\mu$$
defines a right-invariant Riemannian metric on $G$.

By the general theory, the coadjoint action of $G$ on $\mathfrak{g}^*$ partitions the dual Lie algebra into coadjoint orbits. Under the identification $\mathfrak{g}^* \cong \mathfrak{g}$ given by the metric, the coadjoint orbits correspond precisely to the sets of isovorticial vector fields (fields that can be carried to each other by volume-preserving diffeomorphisms).

Euler's equation $\dot{v} = -B(v, v)$ on $\mathfrak{g}$ is the geodesic equation for the right-invariant metric. A stationary flow satisfies $\dot{v} = 0$, i.e., $B(v, v) = 0$.

Arnold's theorem states that a vector $v \in \mathfrak{g}$ is a critical point of the kinetic energy restricted to its coadjoint orbit if and only if $B(v, v) = 0$, i.e., if and only if $v$ corresponds to a stationary flow. Therefore, stationary flows are precisely the conditional extrema (critical points) of the kinetic energy on the manifold of isovorticial fields.
