---
role: proof
locale: en
of_concept: mobius-fixed-points
source_book: gtm011
source_chapter: "3"
source_section: "3.5"
---

Let $S(z) = \frac{az+b}{cz+d}$ with $ad-bc \neq 0$. A fixed point satisfies $S(z) = z$, i.e.,

$$\frac{az+b}{cz+d} = z \implies az + b = cz^2 + dz \implies cz^2 + (d-a)z - b = 0.$$

If $c \neq 0$, this is a quadratic equation in $\mathbb{C}$, which has at most two solutions (counting multiplicity) unless all coefficients vanish. All coefficients vanish only when $c = 0$, $b = 0$, and $d = a$, which implies $S(z) = \frac{az}{a} = z$, the identity.

If $c = 0$, the equation becomes $(d-a)z - b = 0$. If $d \neq a$, there is exactly one fixed point $z = b/(d-a)$. If $d = a$, then $b = 0$ gives the identity; otherwise $b \neq 0$ yields no finite fixed points. In the latter case $\infty$ is the only fixed point (since $c = 0$ implies $S(\infty) = \infty$).

Hence a non-identity Mobius transformation has at most two fixed points in $\mathbb{C}_\infty$.
