---
role: exercise
locale: en
chapter: "X"
section: "5"
exercise_number: 3
---

This exercise gives a proof of the Riemann Mapping Theorem where it is assumed that if $G$ is a simply connected region, $G \neq \mathbb{C}$, then Green's Functions exist.

(a) Let $\gamma$ be a differentiable closed curve. If $f: \partial G \to \mathbb{R}$ is continuous and $g(z, a) = g_a(z)$ is the Green's Function on $G$ with singularity at $a$, show that

$$h(a) = \int_{\gamma} f(z) \frac{\partial g}{\partial n}(z, a) \, ds$$

is a formula for the solution of the Dirichlet Problem with boundary values $f$; where $\frac{\partial g}{\partial n}$ is the derivative of $g$ in the direction of the outward normal to $\gamma$ and $ds$ indicates that the integral is with respect to arc length. (Note: these concepts are not discussed in this book but the formula is sufficiently interesting so as to merit presentation.)

(Hint: Apply Green's formula

$$\iint_{\Omega} [u \Delta v - v \Delta u] \, dx \, dy = \int_{\partial\Omega} \left[ u \frac{\partial v}{\partial n} - v \frac{\partial u}{\partial n} \right] \, ds$$

with $\Omega = G - \{z: |z-a| \leq \delta\}$, $\delta < d(a, \{\gamma\})$, $u = h$, $v = g_a(z) = g(z, a)$.)

(b) Show that if $G = \{z: |z| < 1\}$ then (5.5) reduces to equation (2.5).
