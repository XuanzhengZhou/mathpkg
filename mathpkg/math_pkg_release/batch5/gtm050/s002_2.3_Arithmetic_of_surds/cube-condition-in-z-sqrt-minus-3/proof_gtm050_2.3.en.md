---
role: proof
locale: en
of_concept: cube-condition-in-z-sqrt-minus-3
source_book: gtm050
source_chapter: "2"
source_section: "2.3"
---

**Euler's attempted proof (fallacious).** Euler argued as follows: if $p^2 + 3q^2$ is a cube, then factoring in $\mathbb{Z}[\sqrt{-3}]$ gives

$$
p^2 + 3q^2 = (p + q\sqrt{-3})(p - q\sqrt{-3}) = \text{cube}.
$$

Assuming unique factorization holds in $\mathbb{Z}[\sqrt{-3}]$, and noting that $p + q\sqrt{-3}$ and $p - q\sqrt{-3}$ are relatively prime (when $\gcd(p, q) = 1$ and $p \not\equiv q \pmod{2}$), each factor must itself be a cube up to a unit. Since the only units in $\mathbb{Z}[\sqrt{-3}]$ are $\pm 1$, both of which are cubes ($1 = 1^3$, $-1 = (-1)^3$), it follows that

$$
p + q\sqrt{-3} = (a + b\sqrt{-3})^3
$$

for some integers $a, b$. Expanding the right-hand side yields

$$
(a + b\sqrt{-3})^3 = a^3 + 3a^2 b\sqrt{-3} + 3a b^2(-3) + b^3(-3)\sqrt{-3} = (a^3 - 9ab^2) + (3a^2b - 3b^3)\sqrt{-3}.
$$

Equating real and imaginary parts gives the parametrization $p = a^3 - 9ab^2$, $q = 3a^2b - 3b^3$.

**Why the proof fails.** The ring $\mathbb{Z}[\sqrt{-3}]$ does not enjoy unique factorization. For example, $4 = 2 \cdot 2 = (1 + \sqrt{-3})(1 - \sqrt{-3})$ gives two essentially distinct factorizations of $4$. The failure of unique factorization invalidates the step where each factor is asserted to be a cube. To salvage the argument, one must pass to the larger ring $\mathbb{Z}[\omega]$ where $\omega = e^{2\pi i/3} = \frac{-1 + \sqrt{-3}}{2}$ is a primitive cube root of unity; this ring does have unique factorization and Euler's conclusion is in fact correct, though his justification was incomplete.
