---
role: proof
locale: en
of_concept: smooth-first-order-taylor
source_book: gtm014
source_chapter: "6"
source_section: "6. Morse Theory"
---

Fix $x \in U$ and let $\phi(t) = f(a + t(x - a))$. This is well-defined for $t \in [0,1]$ by convexity of $U$. Then
$$f(x) - f(a) = \phi(1) - \phi(0) = \int_0^1 \frac{d\phi}{dt} \, dt$$
and by the chain rule,
$$\frac{d\phi}{dt}(t) = \sum_{i=1}^{n} \frac{\partial f}{\partial x_i}(a + t(x - a))(x_i - a_i).$$
Let
$$g_i(x) = \int_0^1 \frac{\partial f}{\partial x_i}(a + t(x - a)) \, dt.$$
Then $f(x) = f(a) + \sum_{i=1}^{n} g_i(x)(x_i - a_i)$, and evaluating at $x = a$ gives $g_i(a) = \frac{\partial f}{\partial x_i}(a)$. Smoothness of the $g_i$ follows from smoothness of $f$ and differentiation under the integral.
