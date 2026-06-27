---
role: proof
locale: en
of_concept: harmonic-functions-real-parts-holomorphic
source_book: gtm012
source_chapter: "5"
source_section: "6. Laplace's equation and the Dirichlet problem"
---

# Proof of Harmonic Functions as Real Parts of Holomorphic Functions

**Theorem 6.2.** If $u$ is harmonic in a neighborhood of $(x_0, y_0)$, then $u$ is the real part of a function which is holomorphic (i.e., has a power series expansion) in a disc

$$|x + iy - z_0| < \varepsilon$$

where $z_0 = x_0 + iy_0$.

*Proof.* Suppose first that $(x_0, y_0) = (0, 0)$ and that the set in which $u$ is defined contains the closed disc $x^2 + y^2 \leq 1$. Let

$$g(\theta) = u(\cos \theta, \sin \theta), \quad \theta \in \mathbb{R}.$$

Then $u$ is the unique solution of the Dirichlet problem in the unit disc with $g$ as value on the boundary. If $(b_n)_{n=1}^{\infty}$ are the Fourier coefficients of $g$, then we know that in polar coordinates $u$ is given by

$$\sum_{-\infty}^{\infty} r^{|n|} b_n \exp (in\theta).$$

Since $u$ is real, $g$ is real. Therefore $b_n = \overline{b_{-n}}$ and the series is

$$b_0 + 2 \operatorname{Re} \left( \sum_{1}^{\infty} r^n b_n \exp (in\theta) \right).$$

Let $f$ be defined by

$$f(z) = \sum_{0}^{\infty} a_n z^n$$

where

$$a_0 = b_0; \quad a_n = 2b_n, \quad n > 0.$$

Then

$$u(x, y) = \operatorname{Re} \left( \sum_{0}^{\infty} a_n (re^{i\theta})^n \right) = \operatorname{Re} \left( f(re^{i\theta}) \right)$$

$$= \operatorname{Re} \left( f(x + iy) \right), \quad x^2 + y^2 < 1.$$

In the general case, assume that $u$ is defined on a set containing the closed disc of radius $\varepsilon$ centered at $(x_0, y_0)$, and let

$$u_1(x, y) = u(x_0 + \varepsilon x, y_0 + \varepsilon y).$$

Then $u_1$ is harmonic in a set containing the unit disc, so

$$u_1 = \operatorname{Re} f_1$$

where $f_1$ is holomorphic in the unit disc. Setting $f(z) = f_1((z - z_0)/\varepsilon)$ completes the proof. $\square$
