---
role: proof
locale: en
of_concept: gauss-map-via-bundle-morphism
source_book: gtm020
source_chapter: "3. Vector Bundles"
source_section: "5"
---

The first statement is clear: if $(u, f): \xi^k \rightarrow \gamma_k^m$ is a vector bundle morphism that is an isomorphism on each fibre, then composing with the canonical projection $q: E(\gamma_k^m) \rightarrow F^m$ gives a map $q u: E(\xi^k) \rightarrow F^m$ which is a linear monomorphism on each fibre, hence a Gauss map.

For the converse, suppose $g: E(\xi^k) \rightarrow F^m$ is a Gauss map. For each $b \in B$, the restriction of $g$ to the fibre $p^{-1}(b)$ is a linear monomorphism onto a $k$-dimensional subspace of $F^m$. Define
$$f(b) = g(p^{-1}(b)) \in G_k(F^m),$$
the point in the Grassmannian corresponding to this $k$-dimensional subspace. Define
$$u(x) = (f(p(x)), g(x)) \in E(\gamma_k^m)$$
for $x \in E(\xi^k)$. Then $q u(x) = q(f(p(x)), g(x)) = g(x)$, so $q u = g$. The continuity of $f$ follows by considering local coordinates of $\xi$, and from this the continuity of $u$ follows. Thus $(u, f)$ is the required vector bundle morphism.
