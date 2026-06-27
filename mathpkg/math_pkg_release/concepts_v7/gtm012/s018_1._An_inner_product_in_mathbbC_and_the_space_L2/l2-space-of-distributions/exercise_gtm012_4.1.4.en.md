---
role: exercise
locale: en
chapter: "4. Hilbert Spaces and Fourier Series"
section: "§1. An inner product in ℂ, and the space L²"
exercise_number: 4
---

# Exercise 4

Suppose $f: [0, 2\pi] \to \mathbb{R}$ is such that

$$f(x) = 1, \quad x \in [a, b),$$
$$f(x) = 0, \quad x \notin [a, b).$$

Define

$$F(v) = \frac{1}{2\pi} \int_0^{2\pi} f(x) v(x) \, dx = \frac{1}{2\pi} \int_a^b v(x) \, dx, \quad v \in \mathcal{P}.$$

Show that $F \in \mathbf{L}^2$.

*Hint.* Approximate $f$ by continuous periodic functions (e.g., piecewise linear approximations) and show the corresponding sequence is $\|\cdot\|$-Cauchy.
