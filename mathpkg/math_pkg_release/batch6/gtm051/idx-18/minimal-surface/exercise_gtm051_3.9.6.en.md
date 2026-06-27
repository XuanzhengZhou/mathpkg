---
role: exercise
locale: en
chapter: "3"
section: "3.9"
exercise_number: 6
---

**3.9.6 Minimal surfaces.** A surface $f: U \to \mathbb{R}^3$ is called a **minimal surface** if $H(u) \equiv 0$. The reason for this name is the fact that these are precisely the surfaces for which the first variation of area vanishes.

Consider a family $f^\epsilon(u) = f(u) + \epsilon a(u)n(u)$ of surfaces neighboring $f$. Here $\epsilon$ lies in an interval containing $0$ and $a: U \to \mathbb{R}$ is a smooth function. For sufficiently small $\epsilon$, $f^\epsilon$ is a regular surface and we may define its first fundamental form.

(a) Show that up to terms of second order and higher in $\epsilon$,
$$g_{ik}^\epsilon = g_{ik} - 2\epsilon a h_{ik}.$$

(b) Show that the area element $g^\epsilon = \det(g_{ik}^\epsilon)$ satisfies
$$g^\epsilon = g(1 - \epsilon \cdot 4aH).$$

(c) Conclude that
$$\left. \frac{\partial \sqrt{g^\epsilon}}{\partial \epsilon} \right|_{\epsilon=0} = -2aH\sqrt{g}.$$

(d) Prove that the only way this can equal zero for all functions $a$ (with compact support) is for $H$ to be identically zero.

(e) Using standard techniques of advanced calculus (differentiation under the integral sign and the divergence theorem), show that a surface is minimal ($H \equiv 0$) if and only if given any variation $f^\epsilon(u) = f(u) + \epsilon a(u)n(u)$ of $f$, the area function
$$A(\epsilon) = \int_U \sqrt{g^\epsilon} \, du^1 du^2$$
has a critical point at $\epsilon = 0$.
