---
role: proof
locale: en
of_concept: proposition-3-4
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. First assume that $f$ is convex; to show that $f'$ is increasing let $a \leq x < y \leq b$ and suppose that $0 < t < 1$. Since $0 < (1-t)x + ty - x = t(y-x)$, the definition of convexity gives that

$$\frac{f((1-t)x + ty) - f(x)}{t(y-x)} \leq \frac{f(y) - f(x)}{y-x}.$$

Letting $t \to 0$ gives that

$$f'(x) \leq \frac{f(y) - f(x)}{y-x}.$$

Similarly, using the fact that $0 > (1-t)x + ty - y = (1-t)(x-y)$ and letting $t \to 1$ gives that

$$f'(y) \geq \frac{f(y) - f(x)}{y-x}.$$

So, combining (3.5) and (3.6), we have that $f'$ is increasing.

Now supposing that $f'$ is increasing and that $x < u < y$, apply the Mean Value Theorem for differentiation to find $r$ and $s$ with $x < r < u < s < y$ such that

$$f''(r) = \frac{f(u) - f(x)}{u-x}$$

and

$$f''(s) = \frac{f(y) - f(u)}{y-u}.$$

Since $f''(r) \leq f''(s)$ this gives that

$$\frac{f(u) - f(x)}{u-x} \leq \frac{f(y) - f(u)}{y-u}$$

whenever $x < u < y$. In particular by letting $u = (1-t)x + ty$ where $0 < t < 1$,

$$\frac{f(u) - f(x)}{t(y-x)} \leq \frac{f(y) - f(u)}{(1-t)(y-x)};$$

and hence

$$(1-t)[f(u) - f(x)] \leq

Suppose $f: G^- \to \mathbb{C}$ is continuous and $f$ is analytic in $G$. If we define $M: [a, b] \to \mathbb{R}$ by

$$M(x) = \sup \{ |f(x+iy)| : -\infty < y < \infty \},$$

and $|f(z)| < B$ for all $z$ in $G$, then log $M(x)$ is a convex function.

Before proving this theorem, note that to say that log $M(x)$ is convex means (Exercise 3) that for $a \leq x < u < y \leq b$,

$$(y-x) \log M(u) \leq (y-u) \log M(x) + (u-x) \log M(y)$$

Taking the exponential of both sides gives

3.8 $$M(u)^{(y-x)} \leq M(x)^{(y-u)} M(y)^{(u-x)}$$

whenever $a \leq x < u < y \leq b$. Also, since log $M(x)$ is convex we have that log $M(x)$ is bounded by max $\{ \log M(a), \log M(b) \}$. That is, for $a \leq x \leq b$

$$M(x) \leq \max \{ M(a), M(b) \}.$$

This gives the following.
