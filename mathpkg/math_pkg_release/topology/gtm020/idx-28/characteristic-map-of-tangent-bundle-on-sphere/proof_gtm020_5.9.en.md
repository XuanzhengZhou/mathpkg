---
role: proof
locale: en
of_concept: characteristic-map-of-tangent-bundle-on-sphere
source_book: gtm020
source_chapter: "5"
source_section: "9"
---

We must prove that $R(-x, e_{n-1})^2 = R(x, e_{n-1})^2$. In the $(e_{n-1}, x)$-plane, let $e_{n-1}$ be represented by $0$ and $x$ by the angle $\theta$ ($0 \leq \theta \leq \pi$). The rotation $R(x, e_{n-1})$ sends $e_{n-1}$ to $x$ by rotating through angle $\theta$ around the axis orthogonal to the $(e_{n-1}, x)$-plane, so $R(x, e_{n-1})^2$ acts in this plane as a rotation by $2\theta$.

Similarly, $R(-x, e_{n-1})$ sends $e_{n-1}$ to $-x$. In the $(e_{n-1}, x)$-plane, $-x$ corresponds to the angle $\theta + \pi$ (or $\theta - \pi$). The rotation $R(-x, e_{n-1})$ thus acts through an angle of $\theta + \pi$ (or equivalently $\pi - \theta$ modulo orientation). Squaring this yields a rotation by $2(\theta + \pi) = 2\theta + 2\pi \equiv 2\theta \pmod{2\pi}$.

Since a rotation in the plane is determined by its angle modulo $2\pi$, we have $R(-x, e_{n-1})^2 = R(x, e_{n-1})^2$ as rotations. This extends to $SO(n)$ because both rotations fix the orthogonal complement of the $(e_{n-1}, x)$-plane.

By Corollary 9.9, $c_n(x) = R(x, e_{n-1})^2$. Therefore $c_n(-x) = R(-x, e_{n-1})^2 = R(x, e_{n-1})^2 = c_n(x)$ for all $x \in S^{n-1}$.
