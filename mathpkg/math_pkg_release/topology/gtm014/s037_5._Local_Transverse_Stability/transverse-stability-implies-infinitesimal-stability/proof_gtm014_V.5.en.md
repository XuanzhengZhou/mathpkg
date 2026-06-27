---
role: proof
locale: en
of_concept: transverse-stability-implies-infinitesimal-stability
source_book: gtm014
source_chapter: "V"
source_section: "5. Local Transverse Stability"
---

Assume that $f$ is locally transverse stable at $p$. By Corollary 1.3 it is sufficient to show that $f$ satisfies the conditions of infinitesimal stability to order $m$. In particular, we need to show that if $\tau$ is in $J^m(f^*TY)_p$, then there exists a deformation $F_t$ of $f$ and a vector field $\zeta$ on $X$ such that the $m$-jet version of the infinitesimal condition is satisfied.

The proof splits into two cases: namely, whether or not $\sigma$ is a diagonal element. Suppose $\sigma = (\sigma_1, \ldots, \sigma_s)$ is a diagonal element. Recall from Proposition 6.1 the diffeomorphism $T: U \times V \times \mathring{\mathcal{O}}_\sigma \to J^k(U, V)$. This is extended to an immersion by taking products over the $s$ source points: define $\tilde{T}: U_1 \times \cdots \times U_s \times V \times \mathring{\mathcal{O}}_\sigma \times \cdots \times \mathring{\mathcal{O}}_\sigma \to J^k(U_1, V) \times \cdots \times J^k(U_s, V) \subset J^k(X, Y)$ by

$$\tilde{T}(x_1, \ldots, x_s, y, \tau_1, \ldots, \tau_s) = (T(x_1, y, \tau_1), \ldots, T(x_s, y, \tau_s)).$$

One defines $\mathcal{D}_\sigma^s(U_1, \ldots, U_s, V)$ as the connected component of $\sigma$ in $\mathcal{D}_\sigma^s \cap (J^k(U_1, V) \times \cdots \times J^k(U_s, V))$. By arguments similar to those in Proposition 5.1, $\operatorname{Im} \tilde{T} = \mathcal{D}_\sigma^s(U_1, \ldots, U_s, V)$. The map $\tilde{T}$ provides coordinates on the orbit, and the transversality condition translates into the surjectivity of the map $(d\gamma_2) \oplus (d\gamma_1)$ onto the tangent space of the orbit, which is precisely the infinitesimal stability condition.
