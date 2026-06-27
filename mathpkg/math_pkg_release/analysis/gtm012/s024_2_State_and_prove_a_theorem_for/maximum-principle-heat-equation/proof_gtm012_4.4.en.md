---
role: proof
locale: en
of_concept: maximum-principle-heat-equation
source_book: gtm012
source_chapter: "4"
source_section: "The heat equation: classical solutions; derivation"
---

# Proof of Maximum principle for the heat equation (Theorem 4.1)

**Theorem 4.1 (Maximum Principle).** Let $u(x, t)$ be a continuous real-valued function defined on the rectangle $[0, \pi] \times [0, T]$ (where $T > 0$) and suppose $u$ satisfies the heat equation

$$\frac{\partial}{\partial t} u(x, t) = \left( \frac{\partial}{\partial x} \right)^2 u(x, t), \quad x \in (0, \pi), \quad t \in (0, T].$$

Then the maximum of $u$ on $[0, \pi] \times [0, T]$ is attained on the *parabolic boundary*, i.e., either at $t = 0$, or at $x = 0$, or at $x = \pi$. Equivalently,

$$u(x, t) \leq \max \left\{ \max_{y \in [0, \pi]} u(y, 0), \; \max_{s \in [0, T]} u(0, s), \; \max_{s \in [0, T]} u(\pi, s) \right\}$$

for all $(x, t) \in [0, \pi] \times [0, T]$.

**Proof.**

Let $M$ denote the maximum of $u$ on the parabolic boundary:

$$M = \max \{ u(x, 0) : x \in [0, \pi] \} \cup \{ u(0, t) : t \in [0, T] \} \cup \{ u(\pi, t) : t \in [0, T] \}.$$

We must show that $u(x, t) \leq M$ for all $(x, t)$ in the rectangle. Fix an arbitrary $\varepsilon > 0$ and define

$$v(x, t) = u(x, t) - \varepsilon t, \quad (x, t) \in [0, \pi] \times [0, T].$$

Suppose $v$ attains its maximum on the rectangle at a point $(x_0, t_0)$. We claim that $(x_0, t_0)$ must lie on the parabolic boundary.

Assume, for contradiction, that $x_0 \in (0, \pi)$ and $t_0 \in (0, T]$. Then as a function of $x$, $v(\cdot, t_0)$ has a maximum at $x_0$. Since $v$ is twice differentiable in $x$ (because $u$ satisfies the heat equation), we must have

$$\left( \frac{\partial}{\partial x} \right)^2 v(x_0, t_0) \leq 0.$$

On the other hand, since $u$ satisfies the heat equation,

$$\left( \frac{\partial}{\partial x} \right)^2 v(x_0, t_0) = \left( \frac{\partial}{\partial x} \right)^2 u(x_0, t_0) = \frac{\partial}{\partial t} u(x_0, t_0).$$

Now, at a maximum point $(x_0, t_0)$ with $t_0 \in (0, T]$, the time derivative satisfies

$$\frac{\partial}{\partial t} v(x_0, t_0) \geq 0$$

(if $t_0 < T$, then $\partial v/\partial t = 0$ at the interior maximum; if $t_0 = T$, the maximum on the closed rectangle implies $\partial v/\partial t \geq 0$ at $t = T$ by considering left-hand limits). Then

$$\frac{\partial}{\partial t} u(x_0, t_0) = \frac{\partial}{\partial t} v(x_0, t_0) + \varepsilon \geq \varepsilon > 0.$$

Combining these,

$$\left( \frac{\partial}{\partial x} \right)^2 v(x_0, t_0) = \frac{\partial}{\partial t} u(x_0, t_0) \geq \varepsilon > 0.$$

But this contradicts the fact that $v(\cdot, t_0)$ has a maximum at $x_0$, where the second derivative must be $\leq 0$. Therefore $x_0$ cannot be an interior point; the maximum of $v$ on the rectangle occurs on the parabolic boundary ($t = 0$, $x = 0$, or $x = \pi$).

Thus, for any $(x, t)$ in the rectangle,

$$v(x, t) \leq \max_{\text{parabolic boundary}} v.$$

Since $v = u - \varepsilon t$, we have $v \leq u$ on the parabolic boundary, so

$$v(x, t) \leq M.$$

Consequently,

$$u(x, t) = v(x, t) + \varepsilon t \leq M + \varepsilon T, \quad \text{all } (x, t) \in [0, \pi] \times [0, T].$$

Since $\varepsilon > 0$ was arbitrary, we conclude that $u(x, t) \leq M$ for all $(x, t)$ in the rectangle. $\square$
