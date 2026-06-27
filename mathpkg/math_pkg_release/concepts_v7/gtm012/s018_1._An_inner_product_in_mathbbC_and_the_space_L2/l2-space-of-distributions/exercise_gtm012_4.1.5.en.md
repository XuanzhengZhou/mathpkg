---
role: exercise
locale: en
chapter: "4. Hilbert Spaces and Fourier Series"
section: "§1. An inner product in ℂ, and the space L²"
exercise_number: 5
---

# Exercise 5

Suppose $f: [0, 2\pi] \to \mathbb{C}$ is constant on each subinterval $[x_{i-1}, x_i)$, where

$$0 = x_0 < x_1 < \cdots < x_n = 2\pi.$$

Define

$$F(v) = \frac{1}{2\pi} \int_0^{2\pi} f(x) v(x) \, dx.$$

Show that $F \in \mathbf{L}^2$.

*Hint.* This is a step function. Approximate it by continuous periodic functions using a mollification or piecewise linear interpolation, and show that the resulting sequence is $\|\cdot\|$-Cauchy.
