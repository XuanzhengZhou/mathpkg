---
role: proof
locale: en
of_concept: smooth-function-expansion-lemma
source_book: gtm014
source_chapter: "I"
source_section: "§6. Morse Theory"
---

Fix $x$ in $U$ and let $\phi(t) = f(a + t(x - a))$. This is well-defined for $t$ in $[0,1]$ by convexity. Then

$$f(x) - f(a) = \phi(1) - \phi(0) = \int_0^1 \frac{d\phi}{dt} dt$$

and

$$\frac{d\phi}{dt}(t) = \sum_{i=1}^{n} \frac{\partial f}{\partial x_i}(a + t(x - a))(x_i - a_i)$$

by the chain rule. Define

$$g_i(x) = \int_0^1 \frac{\partial f}{\partial x_i}(a + t(x - a)) dt.$$

Since $f$ is smooth, the partial derivatives are smooth, and differentiation under the integral sign shows each $g_i$ is smooth. By construction,

$$f(x) = f(a) + \sum_{i=1}^{n} g_i(x)(x_i - a_i).$$

Evaluating at $x = a$ gives $g_i(a) = \int_0^1 \frac{\partial f}{\partial x_i}(a) dt = \frac{\partial f}{\partial x_i}(a)$.
