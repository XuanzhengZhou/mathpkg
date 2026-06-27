---
role: proof
locale: en
of_concept: sl2r-acts-by-isometries-on-poincare-half-plane
source_book: gtm051
source_chapter: "5"
source_section: "5.1"
---

**Proof of Proposition 5.1.6.**

Let $u + iv = z$ and $(az + b)/(cz + d) = \tilde{z}$. Writing $dz\, d\tilde{z}$ for $du^2 + dv^2$, the line element for $H_r^2$ at $z$ may be written as
$$
ds^2(z) = -\frac{4r^2\, dz\, d\tilde{z}}{(z - \tilde{z})^2},
$$
where $\tilde{z} = u - iv$ denotes the complex conjugate of $z$.

An easy calculation shows that
$$
d\tilde{z} = d\!\left(\frac{az + b}{cz + d}\right) = \frac{dz}{(cz + d)^2},
$$
and it follows that the line element is invariant under the action of $g \in \mathrm{SL}(2, \mathbb{R})$. Consequently, $\mathrm{SL}(2, \mathbb{R})$ acts by isometries on $H_r^2$.

The transitivity of the action on unit tangent vectors follows from the fact that $\mathrm{SL}(2, \mathbb{R})$ contains enough elements to map any orthonormal frame at one point to any orthonormal frame at another. The isotropy subgroup of a point (say $i$) consists of matrices $g \in \mathrm{SL}(2, \mathbb{R})$ satisfying $g i = i$, which are exactly the rotation matrices
$$
\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix},
$$
forming a subgroup isomorphic to $\mathrm{SO}(2)$.
