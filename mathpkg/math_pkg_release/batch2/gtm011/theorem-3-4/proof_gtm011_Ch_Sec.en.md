---
role: proof
locale: en
of_concept: theorem-3-4
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Suppose that $\varphi$ is subharmonic and $G_1$ and $u_1$ are as in the statement of the theorem. Then $\varphi - u_1$ is clearly subharmonic and must satisfy the Maximum Principle.

Now suppose $\varphi$ is continuous and has the stated property; let $\bar{B}(a, r) \subset G$. According to Corollary 2.10 there is a continuous function $u: \bar{B}(a, r) \to \mathbb{R}$ which is harmonic in $B(a; r)$ and $u(z) = \varphi(z)$ for $|z - a| = r$. By hypothesis, $\varphi - u$ satisfies the Maximum Principle. But $(\varphi - u)(z) \equiv 0$ for $|z - a| = r$. So $\varphi \leq u$ and

$$\varphi(a) \leq u(a) = \frac{1}{2\pi} \int_0^{2\pi} u(a + re^{i\theta}) d
