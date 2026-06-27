---
role: proof
locale: en
of_concept: bijection-forms-representatives
source_book: gtm041
source_chapter: ""
source_section: "Quadratic Forms and the Modular Group"
---

Given a quadratic form $Q(x, y) = ax^2 + bxy + cy^2$ with $d = 4ac - b^2 > 0$, $a > 0$, $c > 0$, consider the quadratic polynomial $f(z) = az^2 + bz + c$. Its roots are
$$\tau = \frac{-b + i\sqrt{d}}{2a}, \quad \overline{\tau} = \frac{-b - i\sqrt{d}}{2a}.$$

Since $d > 0$ and $a > 0$, we have $\text{Im}(\tau) = \frac{\sqrt{d}}{2a} > 0$, so $\tau$ lies in the upper half-plane. Conversely, given $\tau$ with $\text{Im}(\tau) > 0$ and fixed $d > 0$, we can recover the coefficients:
$$a = \frac{\sqrt{d}}{2\,\text{Im}(\tau)}, \quad b = -2a\,\text{Re}(\tau), \quad c = \frac{b^2 + d}{4a} = a|\tau|^2.$$

The conditions $a > 0$ and $c > 0$ are satisfied. This gives a bijection between forms with fixed discriminant $d$ and representatives $\tau$ in the upper half-plane.
