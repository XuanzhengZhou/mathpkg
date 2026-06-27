---
role: proof
locale: en
of_concept: reduction-to-primitive-pythagorean-triple
source_book: gtm050
source_chapter: "1"
source_section: "1.3 How to find Pythagorean triples"
---

Let $(x, y, z)$ be a Pythagorean triple, so $x^2 + y^2 = z^2$ with $x, y, z$ positive integers. Let $d = \gcd(x, y, z)$ and set $x' = x/d$, $y' = y/d$, $z' = z/d$.

Dividing the Pythagorean equation by $d^2$ yields
$$\frac{x^2}{d^2} + \frac{y^2}{d^2} = \frac{z^2}{d^2},$$
which is exactly $(x')^2 + (y')^2 = (z')^2$. Thus $(x', y', z')$ is again a Pythagorean triple.

By construction, $\gcd(x', y', z') = 1$, so $(x', y', z')$ is a primitive Pythagorean triple. This shows that every Pythagorean triple can be reduced to a primitive one by dividing by the greatest common divisor.

Conversely, if $(x', y', z')$ is a primitive Pythagorean triple and $n$ is any positive integer, then multiplying by $n$ gives $(nx', ny', nz')$, which satisfies $(nx')^2 + (ny')^2 = n^2(x'^2 + y'^2) = n^2 z'^2 = (nz')^2$, so $(nx', ny', nz')$ is also a Pythagorean triple. Hence every non-primitive Pythagorean triple is an integer multiple of a primitive one.
