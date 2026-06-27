---
role: proof
locale: en
of_concept: trefoil-knot-group-noncommutative
source_book: gtm047
source_chapter: "16"
source_section: "16"
---

**Proof.** The trefoil is the knot defined by Figure 16.4. From the diagram we read off the relation

$$r_1 = g_1 g_3^{-1} g_2^{-1} g_3 \cong e.$$

The figure is invariant under the permutation $(123): 1 \mapsto 2, 2 \mapsto 3, 3 \mapsto 1$ of the subscripts. This gives the relations

$$r_2 = g_2 g_1^{-1} g_3^{-1} g_1 \cong e,$$
$$r_3 = g_3 g_2^{-1} g_1^{-1} g_2 \cong e.$$

Now let $S_3$ be the symmetric group on three symbols, written in the usual cycle notation as above. We define

$$h(g_1) = (23), \quad h(g_2) = (13), \quad h(g_3) = (12).$$

Extending this to products, we get a homomorphism

$$h: F(g_1, g_2, g_3) \rightarrow S_3.$$

Now

$$h(r_1) = (23)(12)(13)(12) = (1)(2)(3),$$

which is the identity. Similarly $h(r_2)$ and $h(r_3)$ are also the identity. Therefore $h$ induces a homomorphism

$$h^*: F(g_1, g_2, g_3) / N(R) \rightarrow S_3.$$

Obviously $h^*$ is surjective, and $S_3$ is not commutative. Therefore $\pi(\mathbf{R}^3 - K)$ is not commutative. In particular, no two generators commute, since their images do not: $(12)(23) = (132) \neq (123) = (23)(12)$, and so on.
