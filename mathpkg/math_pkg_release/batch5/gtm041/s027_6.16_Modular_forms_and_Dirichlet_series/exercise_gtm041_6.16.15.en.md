---
role: exercise
locale: en
chapter: "6"
section: "6.16"
exercise_number: 15
---

This exercise outlines Riemann's derivation of the functional equation
$$\pi^{-s/2} \Gamma\!\left(\frac{s}{2}\right) \zeta(s) = \pi^{(s-1)/2} \Gamma\!\left(\frac{1-s}{2}\right) \zeta(1-s)$$
from the functional equation (see Exercise 4.1)
$$\vartheta\!\left(\frac{-1}{\tau}\right) = (-i\tau)^{1/2} \vartheta(\tau)$$
satisfied by Jacobi's theta function
$$\vartheta(\tau) = 1 + 2 \sum_{n=1}^{\infty} e^{\pi i n^2 \tau}.$$

(a) If $\sigma > 1$ prove that
$$\pi^{-s/2} \Gamma\!\left(\frac{s}{2}\right) n^{-s} = \int_{0}^{\infty} e^{-\pi n^2 x} x^{s/2-1} \, dx$$
and use this to derive the representation
$$\pi^{-s/2} \Gamma\!\left(\frac{s}{2}\right) \zeta(s) = \int_{0}^{\infty} \psi(x) x^{s/2-1} \, dx,$$
where $2\psi(x) = \vartheta(x) - 1$.

(b) Use (a) and the theta functional equation to obtain the representation
$$\pi^{-s/2} \Gamma\!\left(\frac{s}{2}\right) \zeta(s) = \frac{1}{s(s-1)} + \int_{1}^{\infty} \left(x^{s/2-1} + x^{(1-s)/2-1}\right) \psi(x) \, dx$$
for $\sigma > 1$.

(c) Show that the equation in (b) gives the analytic continuation of $\zeta(s)$ beyond the line $\sigma = 1$ and that it also implies the functional equation for $\zeta(s)$.
