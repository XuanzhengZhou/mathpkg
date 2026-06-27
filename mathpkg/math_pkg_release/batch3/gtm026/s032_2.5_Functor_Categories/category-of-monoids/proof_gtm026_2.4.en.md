---
role: proof
locale: en
of_concept: category-of-monoids
source_book: gtm026
source_chapter: "2"
source_section: "2.4"
---

Given a monoidal category $(\mathcal{K}, \otimes, I, a, b, c)$, the objects are monoids $(K, m, e)$ in $\mathcal{K}$. The morphisms are monoid homomorphisms $f: (K, m, e) \to (K', m', e')$, i.e., $\mathcal{K}$-morphisms $f: K \to K'$ satisfying $m' \cdot (f \otimes f) = f \cdot m$ and $f \cdot e = e'$. Composition is inherited from $\mathcal{K}$: the composite of two monoid homomorphisms is again a monoid homomorphism because
$$
m'' \cdot ((g \cdot f) \otimes (g \cdot f)) = m'' \cdot (g \otimes g) \cdot (f \otimes f) = g \cdot m' \cdot (f \otimes f) = g \cdot f \cdot m,
$$
and $(g \cdot f) \cdot e = g \cdot e' = e''$. The identity $\mathrm{id}_K$ on any monoid $(K, m, e)$ is a monoid homomorphism since $m \cdot (\mathrm{id}_K \otimes \mathrm{id}_K) = m$ and $\mathrm{id}_K \cdot e = e$. Associativity of composition and the identity laws follow directly from $\mathcal{K}$.
