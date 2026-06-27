---
role: proof
locale: en
of_concept: change-of-order-of-integration
source_book: gtm012
source_chapter: "1"
source_section: "7. Functions of two variables"
---

# Proof of Theorem 7.2: Change of Order of Integration (Rectangle)

**Theorem 7.2.** Suppose $f$ is a continuous complex-valued function on the rectangle

$$A = \{(x, y) \mid a \leq x \leq b,\; c \leq y \leq d\}.$$

Then the functions

$$g(x) = \int_c^d f(x, t) \, dt, \qquad h(y) = \int_a^b f(s, y) \, ds$$

are continuous, and

$$\int_a^b g(x) \, dx = \int_c^d h(y) \, dy.$$

Equivalently,

$$\int_a^b \left( \int_c^d f(x, y) \, dy \right) dx = \int_c^d \left( \int_a^b f(x, y) \, dx \right) dy.$$

**Proof.** The preceding remarks show that $g$ and $h$ are not only continuous but differentiable. More generally, the functions

$$\int_c^y f(s, t) \, dt, \qquad \int_a^x f(s, t) \, ds$$

are continuous functions of $s$ and of $t$ respectively. Define

$$F_1(x, y) = \int_a^x \left\{ \int_c^y f(s, t) \, dt \right\} ds,$$

$$F_2(x, y) = \int_c^y \left\{ \int_a^x f(s, t) \, ds \right\} dt.$$

We want to show that $F_1(b, d) = F_2(b, d)$. The remarks preceding this theorem (on differentiation under the integral sign) show that

$$D_2 F_1(x, y) = \int_a^x f(s, y) \, ds = D_2 F_2(x, y).$$

Therefore, $F_2 - F_1$ is constant along each vertical line segment in the rectangle $A$. Indeed, for each fixed $x$, the function $y \mapsto F_2(x, y) - F_1(x, y)$ has zero derivative, hence is constant in $y$.

Similarly,

$$D_1 F_1(x, y) = \int_c^y f(x, t) \, dt = D_1 F_2(x, y).$$

Therefore, $F_2 - F_1$ is constant along each horizontal line segment.

Since $F_1(a, c) = F_2(a, c) = 0$, we conclude that $F_1(x, y) \equiv F_2(x, y)$ for all $(x, y)$ in the rectangle. In particular, $F_1(b, d) = F_2(b, d)$, which is precisely the desired equality of the iterated integrals. $\square$
