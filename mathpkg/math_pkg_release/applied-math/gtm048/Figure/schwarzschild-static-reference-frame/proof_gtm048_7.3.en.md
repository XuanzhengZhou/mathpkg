---
role: proof
locale: en
of_concept: schwarzschild-static-reference-frame
source_book: gtm048
source_chapter: "7"
source_section: "7.3"
---

The proof proceeds in three parts:

**(1) $Z$ is a static, absolute reference frame.** Since $\partial/\partial t$ is a Killing vector field on $N$, the rescaled field $Z = (1 - 2\mu/r)^{-1/2}(\partial/\partial t)$ is a unit timelike vector field. The metric component $g(\partial/\partial t, \partial/\partial t) = -(1 - 2\mu/r)$ on $N$ (where $r > 2\mu$) ensures $g(Z, Z) = -1$. The field $Z$ is static because it is proportional to the hypersurface-orthogonal Killing field $\partial/\partial t$, and it is absolute because the construction uses only geometrically determined quantities ($r$, $t$, and $g$).

**(2) Characterization of the time function.** Let $\hat{t}: N \to \mathbb{R}$ be a time function for $Z$ satisfying $\hat{Z}\hat{t} \to 1$ as $r \to \infty$. Since $Z$ is proportional to $\partial/\partial t$, the condition $\hat{d}\hat{t} = dt|_N$ follows from the asymptotic normalization and the fact that $Z \to \partial/\partial t$ as $r \to \infty$ (because $(1 - 2\mu/r)^{-1/2} \to 1$). Conversely, if $\hat{d}\hat{t} = dt|_N$, then $\hat{Z}\hat{t} = (1 - 2\mu/r)^{-1/2} \to 1$ as $r \to \infty$.

**(3) Observers at rest.** An observer $\gamma$ in $N$ is at rest relative to $Z$ iff its 4-velocity is parallel to $Z$. Since $Z$ is proportional to $\partial/\partial t$, this means $\gamma$ has constant spatial coordinates, i.e., $r \circ \gamma$ is constant.

The geometric interpretation of $t$ and $r$ established here is valid only on $N$ (where $r > 2\mu$), not on the black hole region $B$ (where $r < 2\mu$).
