---
role: proof
locale: en
of_concept: metric-splits-exact-sequence
source_book: gtm020
source_chapter: "9"
source_section: "9.6"
---

Let $\beta$ be a riemannian or hermitian metric on $\eta$. For each fibre $\eta_b = p^{-1}(b)$ over $b \in B$, the restriction $\beta_b$ is an inner product on the vector space $\eta_b$. Since $u$ is a $B$-monomorphism, the image $u(\xi_b)$ is a vector subspace of $\eta_b$ for each $b \in B$.

Define the orthogonal complement of $u(\xi_b)$ in $\eta_b$ by
$$u(\xi_b)^\perp = \{ y \in \eta_b \mid \beta_b(u(x), y) = 0 \text{ for all } x \in \xi_b \}.$$

Because $\beta_b$ is an inner product and $u$ is injective on fibres, we have the orthogonal direct sum decomposition
$$\eta_b = u(\xi_b) \oplus u(\xi_b)^\perp$$
for each $b \in B$. Since $v$ is a $B$-epimorphism and $\ker v = \operatorname{im} u$, the map $v$ induces an isomorphism
$$v|_{u(\xi_b)^\perp}: u(\xi_b)^\perp \xrightarrow{\cong} \zeta_b.$$

Let $s: \zeta \to \eta$ be the inverse of this isomorphism on each fibre, i.e., for $z \in \zeta_b$, define $s(z)$ to be the unique element of $u(\xi_b)^\perp$ such that $v(s(z)) = z$. By construction, $s$ is a $B$-morphism and $v \circ s = \operatorname{id}_\zeta$.

Now define the $B$-morphism $w: \xi \oplus \zeta \to \eta$ by
$$w(x, z) = u(x) + s(z)$$
for $x \in \xi_b$ and $z \in \zeta_b$ (where $+$ denotes addition in the vector space $\eta_b$). By the orthogonal decomposition, $w$ is well-defined and is a $B$-morphism.

The commutativity of the diagram follows directly:
- $w \circ i = u$: for $x \in \xi_b$, $w(i(x)) = w(x, 0) = u(x) + s(0) = u(x)$.
- $v \circ w = j$: for $(x, z) \in \xi_b \times \zeta_b$, $v(w(x,z)) = v(u(x) + s(z)) = v(u(x)) + v(s(z)) = 0 + z = z = j(x,z)$,
since $v \circ u = 0$ (by exactness) and $v \circ s = \operatorname{id}_\zeta$.

Thus $w$ splits the short exact sequence.
