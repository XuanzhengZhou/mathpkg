---
role: proof
locale: en
of_concept: theorem-5-2
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Define $f: \partial G \to \mathbb{R}$ by $f(z) = \log |z - a|$, and let $u: G^- \to \mathbb{R}$ be the unique continuous function which is harmonic on $G$ and such that $u(z) = f(z)$ for $z$ in $\partial G$. Then $g_a(z) = u(z) - \log |z - a|$ is easily seen to be the Green's Function.

This section will close with one last result which says that Green's Functions are conformal invariants.

5.3

where $h(z) = \log |A_1 + A_2(z-a) + \ldots|$ is harmonic near $z = a$ since $A_1 \neq 0$.

Suppose that $\gamma_x(w) = \Delta(w) - \log|w - \alpha|$ where $\Delta$ is a harmonic function on $\Omega$. Using (5.4)

$$\varphi(z) = \Delta(f(z)) - \log|f(z) - \alpha|$$

$$= [\Delta(f(z)) - h(z)] - \log|z - a|.$$

Since $\Delta \circ f - h$ is harmonic near $z = a$, $\varphi(z) + \log|z - a|$ is harmonic near $z = a$.

Exercises

1. (a) Let $G$ be a simply connected region, let $a \in G$, and let $f: G \rightarrow D = \{z: |z| < 1\}$ be a one-one analytic function such that $f(G) = D$ and $f(a) = 0$. Show that the Green's Function on $G$ with singularity at $a$ is $g_a(z) = -\log|f(z)|$.

(b) Find the Green's Functions for each of the following regions:

(i) $G = \mathbb{C} - (\infty, 0]$; (ii) $G = \{z: \text{Re } z > 0\}$; (iii) $G = \{z: 0 < \text{Im } z < 2\pi\}$.

2. Let $g_a$ be the Green's Function on a region $G$ with singularity at $z = a$. Prove that if $\psi$ is a positive superharmonic function on $G - \{a\}$ with $\liminf [\psi(z) + \log|z - a|] > -\infty$, then $g_a(z) \leq \psi(z)$ for $z \neq a$.

3. This exercise gives a proof of the Riemann Mapping Theorem where it is assumed that if $G$ is a simply connected region, $G \neq \mathbb{C}$, then:

(i) $\mathbb{C}_\

tiable closed curve. If $f: \partial G \to \mathbb{R}$ is continuous and $g(z, a) = g_a(z)$ is the Green's Function on $G$ with singularity at $a$, show that

$$h(a) = \int_{\gamma} f(z) \frac{\partial g}{\partial n}(z, a) \, ds$$

is a formula for the solution of the Dirichlet Problem with boundary values $f$; where $\frac{\partial g}{\partial n}$ is the derivative of $g$ in the direction of the outward normal to $\gamma$ and $ds$ indicates that the integral is with respect to arc length. (Note: these concepts are not discussed in this book but the formula is sufficiently interesting so as to merit presentation.) (Hint: Apply Green's formula

$$\iint_{\Omega} [u \Delta v - v \Delta u] \, dx \, dy = \int_{\delta \Omega} \left[ u \frac{\partial v}{\partial n} - v \frac{\partial u}{\partial n} \right] \, ds$$

with $\Omega = G - \{z: |z-a| \leq \delta\}$, $\delta < d(a, \{\gamma\})$, $u = h$, $v = g_a(z) = g(z, a)$.)

(b) Show that if $G = \{z: |z| < 1\}$ then (5.5) reduces to equation (2.5).

Chapter XI

Entire Functions

To begin this chapter, let us recall the Weierstrass Factorization Theorem for entire functions (VII. 5.14). Let $f$ be an entire function with a zero of multiplicity $m \geq 0$ at $z = 0$; let $\{a_n\}$ the zeros of $f$, $a_n \neq 0$, arranged so that a zero of mult
