---
role: proof
locale: en
of_concept: factor-module-lattice-isomorphism
source_book: gtm013
source_chapter: "1"
source_section: "2"
---

Let $K \leq M$. Define

$$\mathcal{S}(M)/K = \{H \in \mathcal{S}(M) \mid K \leq H\},$$

which is a sublattice of $\mathcal{S}(M)$. For each $H$ in this sublattice, $n_K(H) = H/K$ is a submodule of $M/K$. Since $H \leq H'$ implies $n_K(H) \leq n_K(H')$, the map $n_K$ is order-preserving.

Conversely, if $T$ is a submodule of $M/K$, define

$$n_K^+(T) = \{x \in M \mid x + K \in T\}.$$

Since $0 + K = k + K \in T$ for all $k \in K$, we have $K \leq n_K^+(T)$. Moreover, $n_K^+(T)$ is a submodule of $M$: if $x, y \in n_K^+(T)$ and $a, b \in R$, then $(ax + by) + K = a(x + K) + b(y + K) \in T$.

Now $n_K n_K^+(T) = T$ holds by definition. Also $n_K^+ n_K(H) \geq H$ for all $H \in \mathcal{S}(M)/K$, since if $x \in H$, then $x + K \in H/K = n_K(H)$, so $x \in n_K^+ n_K(H)$. Conversely, if $x \in n_K^+ n_K(H)$, then $x + K = a + K$ for some $a \in H$, and since $K \leq H$, we have $x \in H$. Thus $n_K^+ n_K(H) = H$.

Since $n_K^+$ is also order-preserving, $n_K$ and $n_K^+$ define a lattice isomorphism.
