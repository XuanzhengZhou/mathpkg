---
role: proof
locale: en
of_concept: pi-cross-exp-injective-diffeomorphism
source_book: gtm051
source_chapter: "5"
source_section: "5.2"
---

First translate the claim into a statement for a local coordinate system $(U, g)$. Let $u_0 \in U$ be a representative of $p_0$. The map $\pi \times \exp: B_\epsilon U_0 \rightarrow U \times U$ exists and is differentiable by (5.2.2).

Using the inverse function theorem (0.5.1), it will suffice to show that the differential of $\pi \times \exp$ is injective at $(u_0, 0)$. Toward that end, consider the curve $(u_0 + t X_0, t X)$ in $B_\epsilon U_0$. This curve passes through $(u_0, 0)$ when $t = 0$. Its image in $M \times M$ under $\pi \times \exp$ is

$$t \mapsto (\pi(u_0 + t X_0, t X), \exp_{(u_0 + t X_0)}(t X)).$$

In the notation of (5.2.2), this curve represents a geodesic of length $|X| < \rho$ joining two nearby points. The differential injectivity at $(u_0, 0)$ follows because the tangent to this curve at $t = 0$ is $(X_0, X)$, and if $(X_0, X) \neq (0, 0)$ then its image under the differential is nonzero --- the map separates the base-point direction from the geodesic direction.

Thus the differential of $\pi \times \exp$ is injective at $(u_0, 0)$. By the inverse function theorem, $\pi \times \exp$ is a local diffeomorphism at $(u_0, 0)$, which means it is an injective diffeomorphism from $B_\epsilon M_0$ onto an open subset of $M \times M$ for sufficiently small $\epsilon > 0$.
