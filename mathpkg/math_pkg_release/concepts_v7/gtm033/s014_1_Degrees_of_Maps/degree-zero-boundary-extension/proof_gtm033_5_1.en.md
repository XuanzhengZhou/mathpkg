---
role: proof
locale: en
of_concept: degree-zero-boundary-extension
source_book: gtm033
source_chapter: "5"
source_section: "1. Degrees of Maps"
---

# Proof of Lemma 1.2 (Degree of a Map Extended from a Boundary is Zero)

Let $\omega, \theta$ be the orientations of $W, N$ respectively. Let $M_1, \ldots, M_m$ be the components of $\partial W$.

Since $y$ is a regular value, $h^{-1}(y)$ is a compact $1$-dimensional submanifold of $W$ whose boundary is $(h|\partial W)^{-1}(y)$. Let $u \in h^{-1}(y)$. Then there is a unique $v \in h^{-1}(y)$, $v \neq u$, and a component arc $K \subset h^{-1}(y)$ such that $\partial K = \{u, v\}$. It suffices to show that $u$ and $v$ are of opposite type for $h|\partial W$.

Let $\nu = TW/TK$, the algebraic normal bundle of $K$ in $W$. Since $y$ is a regular value, $Th$ induces a bundle isomorphism $\Phi: \nu \to N_y$ (over $K$). There are natural identifications $\nu_u = (\partial W)_u$, $\nu_v = (\partial W)_v$.

Since $K$ is an arc, there is a unique orientation $\kappa$ of $\nu$ such that $\kappa_u = (\partial \omega)_u$. By Lemma 1.1, $\kappa_v = -(\partial \omega)_v$.

Suppose $u$ is of positive type (for $h|\partial W$). Then $\Phi_u(\kappa_u) = \theta_y$. Since $\Phi$ is an isomorphism of oriented bundles, this forces $\Phi_v(\kappa_v) = -\theta_y$, which means $v$ is of negative type. Thus the endpoints of every component arc $K \subset h^{-1}(y)$ have opposite types. Consequently, the contributions of $u$ and $v$ to $\deg(h|\partial W, y)$ cancel pairwise. Hence $\deg(h|\partial W, y) = 0$.
