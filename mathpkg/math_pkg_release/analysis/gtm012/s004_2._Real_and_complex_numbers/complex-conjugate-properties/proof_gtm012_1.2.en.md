---
role: proof
locale: en
of_concept: complex-conjugate-properties
source_book: gtm012
source_chapter: "1"
source_section: "2. Real and complex numbers"
---

# Proof of Properties of Complex Conjugation

Let $z = x + iy$ and $w = u + iv$ be complex numbers with $x, y, u, v \in \mathbb{R}$.

**1. $(z + w)^* = z^* + w^*$:**

$$(z + w)^* = ((x+u) + i(y+v))^* = (x+u) - i(y+v) = (x - iy) + (u - iv) = z^* + w^*.$$

**2. $(zw)^* = z^* w^*$:**

First compute $zw = (x+iy)(u+iv) = (xu - yv) + i(xv + yu)$. Then

$$(zw)^* = (xu - yv) - i(xv + yu).$$

On the other hand,

$$z^* w^* = (x - iy)(u - iv) = (xu - (-y)(-v)) + i(x(-v) + (-y)u) = (xu - yv) - i(xv + yu).$$

Thus $(zw)^* = z^* w^*$.

**3. $(z^*)^* = z$:**

$$(z^*)^* = (x - iy)^* = x + iy = z.$$

**4. $z^* z = x^2 + y^2$:**

$$z^* z = (x - iy)(x + iy) = x^2 - (iy)^2 = x^2 + y^2.$$

Since $x^2 + y^2 \geq 0$, we have $z^* z \geq 0$ with equality if and only if $z = 0$.
