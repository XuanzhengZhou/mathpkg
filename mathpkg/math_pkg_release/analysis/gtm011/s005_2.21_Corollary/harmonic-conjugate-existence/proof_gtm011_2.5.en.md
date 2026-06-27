---
role: proof
locale: en
of_concept: harmonic-conjugate-existence
source_book: gtm011
source_chapter: "2"
source_section: "5"
---

Let $G = B(0; R)$ with $0 < R \leq \infty$, and let $u : G \to \mathbb{R}$ be harmonic. We construct a harmonic function $v$ such that $u$ and $v$ satisfy the Cauchy-Riemann equations. Define

$$v(x, y) = \int_0^y u_x(x, t) \, dt + \varphi(x)$$

and determine $\varphi$ so that $v_x = -u_y$. Differentiating both sides with respect to $x$ gives

$$v_x(x, y) = \int_0^y u_{xx}(x, t) \, dt + \varphi'(x).$$

Since $u$ is harmonic, $u_{xx} = -u_{yy}$, so

$$v_x(x, y) = -\int_0^y u_{yy}(x, t) \, dt + \varphi'(x) = -[u_y(x, y) - u_y(x, 0)] + \varphi'(x)$$
$$= -u_y(x, y) + u_y(x, 0) + \varphi'(x).$$

For $v_x = -u_y$ to hold, we need $\varphi'(x) = -u_y(x, 0)$. Therefore we set

$$\varphi(x) = -\int_0^x u_y(s, 0) \, ds.$$

With this choice, $u$ and $v$ satisfy the Cauchy-Riemann equations and $v$ is a harmonic conjugate of $u$. By the sufficiency of the Cauchy-Riemann equations (with continuous second partials), $f = u + iv$ is analytic on $G$.
