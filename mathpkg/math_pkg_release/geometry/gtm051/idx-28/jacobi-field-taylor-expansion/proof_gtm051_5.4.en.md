---
role: proof
locale: en
of_concept: jacobi-field-taylor-expansion
source_book: gtm051
source_chapter: "5"
source_section: "5.4"
---

The Jacobi field $Y(t) = y(t)e_2(t)$ satisfies the Jacobi differential equation

$$\ddot{y} + K \circ c(t) \cdot y(t) = 0.$$

Since $y(0) = 0$ and $\dot{y}(0) = 1$, we compute the Taylor coefficients. From the initial conditions, $y(0) = 0$ gives the constant term as $0$, and $\dot{y}(0) = 1$ gives the coefficient of $t$ as $1$. The differential equation at $t = 0$ yields $\ddot{y}(0) = -K \circ c(0) \cdot y(0) = 0$, so the $t^2$ term vanishes. Differentiating the differential equation,

$$\dddot{y}(t) + \frac{d}{dt}(K \circ c(t)) \cdot y(t) + K \circ c(t) \cdot \dot{y}(t) = 0,$$

so $\dddot{y}(0) = -K \circ c(0) \cdot \dot{y}(0) = -K \circ c(0)$. Hence the Taylor expansion is

$$y(t) = y(0) + \dot{y}(0)t + \frac{\ddot{y}(0)}{2}t^2 + \frac{\dddot{y}(0)}{6}t^3 + \dots = t - K \circ c(0) \cdot \frac{t^3}{6} + \dots.$$
