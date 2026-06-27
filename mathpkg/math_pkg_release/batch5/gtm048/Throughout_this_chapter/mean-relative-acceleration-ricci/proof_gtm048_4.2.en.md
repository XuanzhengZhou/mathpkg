---
role: proof
locale: en
of_concept: mean-relative-acceleration-ricci
source_book: gtm048
source_chapter: "4"
source_section: "4.2"
---

Let $N$ be a 3-dimensional spacelike submanifold through $z$ such that the given $Z$ is orthogonal to $N$ at $z$. Let $Z$ be a unit vector field defined on $N$ such that $Zz = Z$ and $Zy$ is orthogonal to $N$ at $y$ for all $y \in N$. Define a map $\phi: N \times (-\varepsilon, \varepsilon) \to M$ by $\phi(y, t) = \gamma t$, where $\gamma$ is the geodesic issuing from $y$ with $\gamma 0 = y$ and $\gamma_* 0 = Zy$.

$\phi$ is a $C^\infty$ map by virtue of the $C^\infty$ dependence of solutions of ordinary differential equations on their initial conditions. At $(z, 0)$, $\phi_*$ is the identity on $N_z$ and carries $(d/dt)$ onto $Z$. Thus $\phi_*$ is nonsingular at $(z, 0)$. By the inverse function theorem, $\phi$ is a diffeomorphism in a neighborhood of $(z, 0)$. We may assume $N$ and $\varepsilon$ to be so small that $\phi$ is a diffeomorphism on $N \times (-\varepsilon, \varepsilon)$ itself.

Let $Q = \phi_*(d/dt)$. Then $Q$ is a geodesic reference frame in $\operatorname{image} \phi$, and $Q|N = Z$. Let $\alpha$ be the mean relative-acceleration of $Q$. By the definition of mean relative-acceleration and the geometric properties of the Ricci tensor:

$$\operatorname{Ric}(Z, Z) = -3(\alpha z),$$

as desired. Thus the mean relative-acceleration equals $-\frac{1}{3} \operatorname{Ric}(Q, Q)$.
