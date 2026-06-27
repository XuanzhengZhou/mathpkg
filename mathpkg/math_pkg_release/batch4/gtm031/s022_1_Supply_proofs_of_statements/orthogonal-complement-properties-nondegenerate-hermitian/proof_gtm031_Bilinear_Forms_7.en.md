---
role: proof
locale: en
of_concept: orthogonal-complement-properties-nondegenerate-hermitian
source_book: gtm031
source_chapter: "Bilinear Forms"
source_section: "7"
---

From the general theory of bilinear forms, we know that for a non-degenerate bilinear form, the mapping $\mathfrak{S} \mapsto j(\mathfrak{S})$ (which coincides with $\mathfrak{S}^{\perp}$ for a hermitian scalar product) is an anti-automorphism of the lattice of subspaces onto itself. This establishes property (3): the mapping $\mathfrak{S} \mapsto \mathfrak{S}^{\perp}$ is bijective between subspaces and reverses inclusions ($\mathfrak{S}_1 \subseteq \mathfrak{S}_2$ implies $\mathfrak{S}_2^{\perp} \subseteq \mathfrak{S}_1^{\perp}$).

For property (1): from the general theory, we have the dimension formula $\dim \mathfrak{S}^{\perp} = n - \dim \mathfrak{S}$. This follows from the fact that the map $v \mapsto g(\cdot, v)$ from $\mathfrak{R}$ to the dual space $\mathfrak{R}^*$ is injective (by non-degeneracy) and hence an isomorphism when $\dim \mathfrak{R} < \infty$. Under this isomorphism, $\mathfrak{S}^{\perp}$ corresponds to the annihilator of $\mathfrak{S}$ in $\mathfrak{R}^*$, which has dimension $n - \dim \mathfrak{S}$.

For property (2): from (1), we compute
$$\dim \mathfrak{S}^{\perp\perp} = n - \dim \mathfrak{S}^{\perp} = n - (n - \dim \mathfrak{S}) = \dim \mathfrak{S}.$$

It is clear from the definition that $\mathfrak{S} \subseteq \mathfrak{S}^{\perp\perp}$: if $u \in \mathfrak{S}$, then for any $v \in \mathfrak{S}^{\perp}$ we have $g(u, v) = 0$, so $u \in (\mathfrak{S}^{\perp})^{\perp} = \mathfrak{S}^{\perp\perp}$. Since $\mathfrak{S} \subseteq \mathfrak{S}^{\perp\perp}$ and they have the same finite dimension, we conclude $\mathfrak{S}^{\perp\perp} = \mathfrak{S}$. Thus the mapping $\mathfrak{S} \mapsto \mathfrak{S}^{\perp}$ is involutorial.
