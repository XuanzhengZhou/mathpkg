---
role: proof
locale: en
of_concept: projective-topology-as-projective-limit
source_book: gtm036
source_chapter: "Appendix"
source_section: "D"
---

Assume $N = \bigcap_{t \in A} g_t^{-1}(0) = \{0\}$. For each $t \in A$, let $H_t = g_t[F] \subseteq F_t$ be the image of $F$ under $g_t$, equipped with the subspace topology inherited from $F_t$. The map $g_t: F \to H_t$ is surjective by definition and continuous with respect to the projective topology on $F$.

Consider the diagonal map
$$\Phi: F \to \prod_{t \in A} H_t, \qquad \Phi(x) = (g_t(x))_{t \in A}.$$
Each coordinate map $\pi_t \circ \Phi = g_t$ is continuous, so $\Phi$ is continuous into the product. Moreover, since $N = \{0\}$, the map $\Phi$ is injective: if $\Phi(x) = \Phi(y)$, then $g_t(x) = g_t(y)$ for all $t$, so $x - y \in N = \{0\}$ and $x = y$.

The projective topology on $F$ is the weakest topology making every $g_t$ continuous, which is precisely the initial topology induced by $\Phi$. Because $N = \{0\}$, $\Phi$ is a topological embedding of $F$ into $\prod_t H_t$. The image $\Phi[F]$ is exactly the projective limit $\varprojlim H_t$ (with the bonding maps induced by the original relations among the $g_t$ when $A$ is directed), and by property (b) this limit carries the natural topology — the relativization of the product.

Hence $F$ is homeomorphic and linearly isomorphic to $\varprojlim \, g_t[F]$, equipped with the natural projective limit topology.
