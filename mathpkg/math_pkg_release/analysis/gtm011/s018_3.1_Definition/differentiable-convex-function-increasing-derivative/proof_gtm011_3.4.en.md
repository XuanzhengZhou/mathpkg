---
role: proof
locale: en
of_concept: differentiable-convex-function-increasing-derivative
source_book: gtm011
source_chapter: "3"
source_section: "3.4"
---

First assume that $f$ is convex; to show that $f'$ is increasing let $a \leq x < y \leq b$ and suppose that $0 < t < 1$. Since $0 < (1-t)x + ty - x = t(y-x)$, the definition of convexity gives that

$$\frac{f((1-t)x + ty) - f(x)}{t(y-x)} \leq \frac{f(y) - f(x)}{y-x}.$$

Letting $t \to 0$ gives that

$$f'(x) \leq \frac{f(y) - f(x)}{y-x}.$$

Similarly, using the fact that $0 > (1-t)x + ty - y = (1-t)(x-y)$ and letting $t \to 1$ gives that

$$f'(y) \geq \frac{f(y) - f(x)}{y-x}.$$

Combining these two inequalities, we have that $f'$ is increasing.

Now supposing that $f'$ is increasing and that $x < u < y$, apply the Mean Value Theorem for differentiation to find $r$ and $s$ with $x < r < u < s < y$ such that

$$f'(r) = \frac{f(u) - f(x)}{u-x}$$

and

$$f'(s) = \frac{f(y) - f(u)}{y-u}.$$

Since $f'$ is increasing and $r < s$, we have $f'(r) \leq f'(s)$, which gives

$$\frac{f(u) - f(x)}{u-x} \leq \frac{f(y) - f(u)}{y-u}$$

whenever $x < u < y$. In particular, letting $u = (1-t)x + ty$ where $0 < t < 1$,

$$\frac{f(u) - f(x)}{t(y-x)} \leq \frac{f(y) - f(u)}{(1-t)(y-x)}.$$

Multiplying both sides by $t(1-t)(y-x)$ yields

$$(1-t)[f(u) - f(x)] \leq t[f(y) - f(u)].$$

Expanding and rearranging,

$$f(u) \leq f(x) + t[f(y) - f(x)] = tf(y) + (1-t)f(x).$$

Substituting $u = (1-t)x + ty$ gives the convexity inequality. Hence $f$ is convex.
