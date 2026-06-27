---
role: proof
locale: en
of_concept: characteristic-map-of-tangent-bundle-via-reflection
source_book: gtm020
source_chapter: "5"
source_section: "9"
---

We must prove that $R(-x, e_{n-1})^2 = R(x, e_{n-1})^2$. In the $(e_{n-1}, x)$-plane, where $e_{n-1}$ is represented by $0$ and $x$ by $\theta$ (with $0 \leq \theta \leq \pi$), the rotation $R(-x, e_{n-1})$ sends $e_{n-1}$ to $-x$ by rotating through an angle of $\pi - \theta$ (or $\pi + \theta$, depending on orientation). In either case, squaring the rotation yields a rotation by twice that angle: $R(-x, e_{n-1})^2$ acts by $2(\pi - \theta) = 2\pi - 2\theta$ in the $(e_{n-1}, x)$-plane, which equals $-2\theta \equiv 2\theta \pmod{2\pi}$ as a rotation. Meanwhile $R(x, e_{n-1})^2$ acts by $2\theta$. Since a rotation is determined by its action modulo $2\pi$, the two squares coincide.
